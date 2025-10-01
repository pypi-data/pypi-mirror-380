"""Generic CAN tool for adapters supported in python-can"""
import logging
import textwrap
from pathlib import Path
import configparser
import pprint
try:
    # When Python 3.11 becomes the minimum supported version for this tool
    # we can remove the tomli fallback solution here since this version
    # will have tomllib in its standard library.
    import tomllib as toml_reader #pylint: disable=import-error
except ModuleNotFoundError:
    import tomli as toml_reader #pylint: disable=import-error
import can
from pymdfu.tools import Tool, ToolArgumentParser, ToolConfigurationError
from pymdfu.transport import Transport, TransportError
from pymdfu.utils import parse_int_or_hex

# pylint: disable=too-many-instance-attributes
class PythonCanTool(Tool, Transport):
    """Generic CAN Tool"""
    def __init__(self, tool_args):
        self.logger = logging.getLogger(__name__)
        self.args = self._parse_args(tool_args)
        self.logger.debug("Reading CAN configuration file %s context %s", self.args.can_config, self.args.can_context)
        self.can_config = self.load_can_config(self.args.can_config, self.args.can_context)

        self.extended_id = self.args.extended_id
        self.mdfu_client_id = self.args.client_id
        self.mdfu_host_id = self.args.host_id
        self._init_can_stack()

    def _init_can_stack(self):
        """CAN stack initialization

        :param can_config: CAN configuration
        :type can_config: dict
        """
        txt = pprint.pformat(self.can_config)
        self.logger.debug("CAN configuration: \n%s", txt)
        if self.extended_id:
            # 29-bit extended ID
            filters = [
                {"can_id": self.mdfu_host_id, "can_mask": 0x1FFFFFFF, "extended": True},
            ]
        else:
            filters = [
                {"can_id": self.mdfu_host_id, "can_mask": 0x7FF, "extended": False},
            ]
        self.bus = can.Bus(can_filters=filters, **self.can_config)
        # TODO When a new CAN transport has been defined we can hook it up here
        self.transport = None
        raise NotImplementedError("Generic CAN tool needs a transport implementation")

    @classmethod
    def load_can_config(cls, path, context=None):
        """Load CAN configuration

        :param path: Path to configuration file
        :type path: str
        :return: CAN configuration
        :rtype: dict
        """
        config = cls.load_config(path, context)
        # extract CAN configuration if there is a can section
        if context is None and "can" in config:
            config = config["can"]
        return config

    @staticmethod
    def load_config(path, context=None):
        """Load configuration from file

        The file can be in TOML or INI format. The type of file is derived from the postfix,
        .toml -> TOML file and all other postfixes -> INI file.

        :param path: Path to the configuration file
        :type path: str
        :param context: Context to load from the file (file section to load), defaults to None,\
        meaning load all sections and add them to the dictionary.
        :type context: str, optional
        :return: Configuration
        :rtype: dict
        :raises: KeyError when a context was not present in the configuration file
        """
        path = Path(path)
        try:
            if path.suffix.lower() == ".toml":
                with open(path, 'rb') as file:
                    config = toml_reader.load(file)
            else:
                config = configparser.ConfigParser()
                config.read(path)
                # This converts the ConfigParser into a dictionary where each section will inherit
                # from the default section
                config = {section: dict(config.items(section)) for section in config.sections()}
        except (toml_reader.TOMLDecodeError, configparser.Error) as exc:
            raise ToolConfigurationError(exc) from exc

        try:
            if context is not None:
                final_config = config[context]
            else:
                final_config = config
        except KeyError as exc:
            raise ToolConfigurationError(f"Section '{context}' not found in configuration file {path}") from exc

        return final_config

    @staticmethod
    def _validate_path(path):
        try:
            file_path = Path(path)
            if not file_path.exists():
                raise ToolConfigurationError(f"Configuration file {file_path.absolute()} not found")
        except TypeError as exc:
            raise ToolConfigurationError(f"Invalid path :{exc}") from exc
        return path

    @classmethod
    def _parse_args(cls, tool_args):
        parser_common = ToolArgumentParser()
        parser_common.add_argument("--can-config",
            type=str,
            dest="can_config",
            default=None,
            required=True
        )
        parser_common.add_argument("--can-context",
            type=str,
            dest="can_context",
            default=None,
            required=False
        )
        parser_common.add_argument("--client-id",
            dest="client_id",
            type=parse_int_or_hex,
            required=True
        )
        parser_common.add_argument("--host-id",
            dest="host_id",
            type=parse_int_or_hex,
            required=True
        )
        parser_common.add_argument(
            "--extended-id",
            action="store_true",
            default=False,
            help="Enable extended ID mode"
        )
        args = parser_common.parse_args(tool_args)
        if args.config is not None:
            file_path = Path(args.config)
            if not file_path.exists():
                raise ToolConfigurationError(f"CAN configuration file {file_path.absolute()} not found")
        return args

    @classmethod
    def usage_help(cls):
        return "--can-config <file path> --host-id <host-id> --client-id <client-id> [--can-context <context>]"

    @classmethod
    def tool_help(cls):
        return "Python CAN Tools"

    @classmethod
    def parameter_help(cls):
        return textwrap.dedent("""\
        Python CAN tool options:
            --can-config <file path>
                            Path to configuration file. This file specifies the parameters for
                            the specific interface and must follow the rules in the
                            python-can documentation.
            --can-context <context>
                            Selects a configuration in the configuration file.
            --client-id <id>
                            MDFU CAN client arbitration id.
            --host-id <id>
                            MDFU CAN host arbitration id.

        """)

    def list_connected(self):
        self.logger.info("Not supported")

    def open(self):
        self.logger.debug("PythonCanTool opened")
        self.transport.start()

    def close(self):
        self.transport.stop()
        self.bus.shutdown()

    @property
    def mac(self):
        """MAC layer

        :return: MAC layer used in the transport layer
        :rtype: Mac
        """
        return None

    def write(self, data):
        self.transport.send(data, send_timeout=2)

    def read(self, timeout=None):
        msg = self.transport.recv(block=True, timeout=timeout)
        if msg is None:
            raise TransportError("Timeout while receiving ISOTP frame")
        return msg

class PythonCanClientTool(PythonCanTool):
    """Python CAN MDFU client Tool
    """
    def _init_can_stack(self):
        """CAN stack initialization
        :param can_config: Python CAN configuration
        :type isotp_config: dict
        :param isotp_config: ISO TP stack configuration
        :type isotp_config: dict
        """
        filters = [
            {"can_id": self.mdfu_client_id, "can_mask": 0x7FF, "extended": False},
        ]
        self.bus = can.Bus(can_filters=filters, **self.can_config)

        raise NotImplementedError("No transports are currently implemented for CAN")

if __name__ == "__main__":
    print(PythonCanTool.usage_help())
    print(PythonCanTool.tool_help())
    print(PythonCanTool.parameter_help())
