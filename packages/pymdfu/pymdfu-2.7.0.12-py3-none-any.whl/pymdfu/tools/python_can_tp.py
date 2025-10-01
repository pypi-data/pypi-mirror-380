"""Generic tool for CAN ISO-TP based on python-can and can-isotp"""
import textwrap
import copy
import pprint
import isotp
import can
from pymdfu.tools import ToolArgumentParser, ToolConfigurationError
from pymdfu.transport import TransportError
from pymdfu.tools.python_can import PythonCanTool
from pymdfu.utils import parse_int_or_hex

ISOTP_DEFAULT_CONFIG = {
    "stmin": 0,
    "blocksize": 0,
    "tx_data_length": 8,
    "tx_data_min_length": None,
    "rx_flowcontrol_timeout": 1000,
    "rx_consecutive_frame_timeout": 1000,
    "tx_padding": None,
    "wftmax": 3,
    "max_frame_size": 4095,
    "can_fd": False,
    "bitrate_switch": False
}

class PythonCanTpTool(PythonCanTool):
    """Generic Python CAN TP Tool"""
    TX_DATA_MIN_LENGTH_VALUES = [1,2,3,4,5,7,8,12,16,20,24,32,48,64]
    STMIN_MAX_VALUE = 0xF9
    def __init__(self, tool_args):
        super().__init__(tool_args)
        self.logger.debug("Reading CAN ISO-TP configuration file %s", self.args.can_tp_config)
        self.isotp_config = self.load_isotp_config(self.args.can_tp_config)
        self._init_isotp_stack()

    def _init_can_stack(self):
        """Dummy to defer stack init from parent class to this class.
        """

    def _init_isotp_stack(self):
        """CAN ISO-TP stack initialization
        """
        txt = pprint.pformat(self.can_config)
        self.logger.debug("CAN configuration: \n%s", txt)
        txt = pprint.pformat(self.isotp_config)
        self.logger.debug("CAN ISO-TP configuration: \n%s ", txt)
        if self.extended_id:
            # 29-bit extended ID
            filters = [
                {"can_id": self.mdfu_host_id, "can_mask": 0x1FFFFFFF, "extended": True},
            ]
            isotp_addressing_mode = isotp.AddressingMode.Normal_11bits
        else:
            filters = [
                {"can_id": self.mdfu_host_id, "can_mask": 0x7FF, "extended": False},
            ]
            isotp_addressing_mode = isotp.AddressingMode.Normal_11bits
        self.bus = can.Bus(can_filters=filters, **self.can_config)

        addr = isotp.Address(isotp_addressing_mode, rxid=self.mdfu_host_id, txid=self.mdfu_client_id)
        self.isotp_config["blocking_send"] = True
        self.transport = isotp.CanStack(self.bus,
                                        address=addr,
                                        error_handler=self.my_error_handler,
                                        params=self.isotp_config)

    def my_error_handler(self, error):
        """CAN ISO-TP error handler

        :param error: Exception object
        :type error: isotp.IsoTpError
        """
        # Called from a different thread, needs to be thread safe
        self.logger.warning('IsoTp error happened : %s - %s', error.__class__.__name__, str(error))

    @classmethod
    def _validate_isotp_config(cls, config: dict):
        """Validate ISO-TP configuration

        Ensures that ISO-TP parameters are valid and in correct format.
        Converts parameter string literals to integers where needed.

        :param config: ISO-TP configuration
        :type config: dict
        :return: Validated ISO-TP configuration
        :rtype: dict
        :raises ToolConfigurationError: If parameter validation fails
        """
        isotp_config = {}
        try:
            for key, value in config.items():
                if key in ISOTP_DEFAULT_CONFIG:
                    if key == "stmin":
                        val = int(value)
                        if val > cls.STMIN_MAX_VALUE:
                            raise ValueError("ISO-TP parameter stmin is outside its allowed range")
                    elif key == "tx_data_min_length":
                        val = int(value)
                        if val not in cls.TX_DATA_MIN_LENGTH_VALUES:
                            raise ValueError("ISO-TP parameter tx_data_min_length must be one of "
                                             f"{cls.TX_DATA_MIN_LENGTH_VALUES}")
                    elif key in ["can_fd", "bitrate_switch"]:
                        if isinstance(value, str):
                            val = bool(value.lower() == "true")
                        else:
                            val = value
                    else:
                        val = int(value)
                    isotp_config[key] = val
                else:
                    raise ValueError(f"Unknown ISO-TP parameter {key}")
        except ValueError as exc:
            raise ToolConfigurationError(str(exc)) from exc
        return isotp_config

    @classmethod
    def load_isotp_config(cls, path : str) -> dict:
        """Load CAN ISO-TP configuration from a file

        :param path: Path to configuration file
        :type path: str
        :return: Dictionary with configuration parameters
        :rtype: dict
        """
        isotp_config = copy.deepcopy(ISOTP_DEFAULT_CONFIG)
        try:
            parsed_isotp_config = cls.load_config(path)
            # flatten if we have the config in an isotp subsection
            if "isotp" in parsed_isotp_config:
                parsed_isotp_config = parsed_isotp_config["isotp"]
            validated_config = cls._validate_isotp_config(parsed_isotp_config)
            # Update default config with values from user configuration
            isotp_config.update(validated_config)
        except ToolConfigurationError as exc:
            raise ToolConfigurationError(f"Reading of CAN ISO-TP configuration failed with: {exc}") from exc
        return isotp_config

    @classmethod
    def _parse_args(cls, tool_args):
        parser_common = ToolArgumentParser()
        parser_common.add_argument("--can-config",
            type=cls._validate_path,
            dest="can_config",
            default=None,
            required=True
        )
        parser_common.add_argument("--can-tp-config",
            type=cls._validate_path,
            dest="can_tp_config",
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
        return args

    @classmethod
    def usage_help(cls):
        return ("--can-config <file path> --host-id <host-id> --client-id <client-id> "
            "--can-tp-config <file path> [--can-context <context>]")

    @classmethod
    def tool_help(cls):
        return "Python CAN ISO-TP Tool"

    @classmethod
    def parameter_help(cls):
        return textwrap.dedent("""\
        Python CAN tool options:
            --can-config <file path>
                            Path to CAN configuration file. This file specifies the parameters for
                            the specific CAN bus interface and must follow the rules in the
                            python-can documentation.
            --can-tp-config <file-path>
                            Path to CAN ISO-TP configuration file.
            --can-context <context>
                            Selects a context (section) in the configuration file for the CAN configuration.
                            - If not specified, the default 'can' context is used
                            - If 'can' context is not present the configuration is assumed to be without
                              any context, so parameters that are outside a context will be used.
            --client-id <id>
                            MDFU CAN client arbitration ID as integer or hexadecimal value.
            --host-id <id>
                            MDFU CAN host arbitration ID as integer or hexadecimal value.

        """)

    def list_connected(self):
        self.logger.info("Not supported")

    def open(self):
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
            raise TransportError("Timeout while receiving ISO-TP frame")
        return msg

class PythonCanTpClientTool(PythonCanTpTool):
    """Python CAN ISO-TP MDFU client tool
    """
    def _init_isotp_stack(self):
        """CAN ISO-TP transport initialization

        :param can_config: Python CAN configuration
        :type isotp_config: dict
        :param isotp_config: ISO-TP stack configuration
        :type isotp_config: dict
        """
        filters = [
            {"can_id": self.mdfu_client_id, "can_mask": 0x7FF, "extended": False},
        ]
        self.bus = can.Bus(can_filters=filters, **self.can_config)

        addr = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=self.mdfu_client_id, txid=self.mdfu_host_id)
        self.isotp_config["blocking_send"] = True
        self.transport = isotp.CanStack(self.bus,
                                        address=addr,
                                        error_handler=self.my_error_handler,
                                        params=self.isotp_config)
if __name__ == "__main__":
    print(PythonCanTpTool.usage_help())
    print(PythonCanTpTool.tool_help())
    print(PythonCanTpTool.parameter_help())
