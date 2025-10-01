
"""MDFU client"""
import threading
import time
from logging import getLogger
from collections import deque
from packaging.version import Version
from .mdfu import MdfuCmd, MdfuCmdPacket, MdfuStatusPacket, MdfuStatus,\
                    MdfuCmdNotSupportedError, ClientInfo, ImageState,\
                    CmdNotExecutedCause
from .transport import TransportError

# pylint: disable=too-many-instance-attributes
class MdfuClient(threading.Thread):
    """MDFU client

    This class can be used to simulate a MDFU client
    """
    DEFAULT_CLIENT_INFO = {
        "version" : Version("1.2.0"),
        "buffer_count" : 1,
        "buffer_size" : 512,
        "default_timeout" : 10, # (float) seconds
        "timeouts" : {},
        "inter_transaction_delay" : 0 # (float) seconds
    }
    """Client read timeout

    The client thread must poll for new incoming data and this cannot be blocking or
    the thread cannot exit when the client is shut down. The READ_TIMEOUT defines
    how long the client is allowed to block during a read. The timeout is defined
    as float in seconds.
    """
    READ_TIMEOUT = 2
    def __init__(self, transport, client_info=None, response_delays=None):
        """MDFU client class initialization

        :param transport: Transport object
        :type transport: Transport
        :param client_info: Client information, optional, defaults to None.
        When not defined the default values from DEFAULT_CLIENT_INFO are used.

        :type client_info: ClientInfo, optional
        :param response_delays: Delays for command responses, defaults to None which
        implicitly sets all delays to zero, so a response will be returned immediately.
        Delays are defined in a dictionary with values from MdfuCmd as keys and delays
        in seconds as float.
        :type response_delays: dict
        """
        self.queue = deque()
        self.sequence_number = 0
        self.last_sequence_number = 0
        self.last_response = None
        self.logger = getLogger("pymdfu.MdfuClient")
        self.resend = False
        self.transport = transport
        if client_info:
            self.client_info = client_info
        else:
            self.client_info = ClientInfo(**self.DEFAULT_CLIENT_INFO)
        if response_delays is not None:
            self.response_delays = response_delays
        else:
            self.response_delays = {}
        self.stop_event = threading.Event()
        super().__init__(name="MDFU client")

    def stop(self):
        """Stop MDFU client
        """
        # Send event to stop the thread
        self.logger.debug("Shutting down MDFU client")
        self.stop_event.set()
        # Wait for thread to end
        self.join()
        self.logger.debug("MDFU client shutdown finished")

    def get_command(self):
        """Read a MDFU command from transport layer

        For detected transport errors a response message is added to the response queue.

        :return: MDFU command or None
        :rtype: MdfuCommand | None
        """
        data = None
        try:
            # We must have a timeout set here to not block or otherwise the client thread will never be able
            # to finish
            data = self.transport.read(timeout=self.READ_TIMEOUT)
        except TimeoutError:
            pass
        except TransportError as exc:
            if "timeout" not in str(exc).lower():
                self.logger.debug("Transport error: %s", exc)
                status_packet = MdfuStatusPacket(self.sequence_number,
                                    MdfuStatus.COMMAND_NOT_EXECUTED.value,
                                    data=bytes(CmdNotExecutedCause.TRANSPORT_INTEGRITY_CHECK_ERROR.value),
                                    resend=True)
                self.last_response = status_packet
                self.queue.appendleft(status_packet)
        return data

    def decode_command_packet(self, data):
        """Decode Mdfu command packet

        :param data: Data to decode
        :type data: bytes | bytearray
        :return: Mdfu command object or None if errors are detected
        :rtype: MdfuCmd | None
        """
        try:
            cmd_packet = MdfuCmdPacket.from_binary(data)
        except ValueError:
            self.logger.warning("MDFU client got an invalid packet: 0x%x\n", data.hex())
            status_packet = MdfuStatusPacket(self.sequence_number,
                                            MdfuStatus.COMMAND_NOT_EXECUTED.value,
                                            resend=True)
            self.last_response = status_packet
            self.queue.appendleft(status_packet)
            cmd_packet = None
        except MdfuCmdNotSupportedError:
            status_packet = MdfuStatusPacket(self.sequence_number, MdfuStatus.COMMAND_NOT_SUPPORTED.value)
            self.last_response = status_packet
            self.queue.appendleft(status_packet)
            cmd_packet = None
        return cmd_packet

    def handle_mdfu_command(self, packet: MdfuCmd):
        """Validate and execute MDFU command

        :param packet: MDFU command
        :type packet: MdfuCmd
        """
        # Execute command with valid sequence number or sync bit set
        if packet.sync or (self.sequence_number == packet.sequence_number):
            status_packet = self._execute_command(packet)
            self.last_response = status_packet
            self.queue.appendleft(status_packet)
            if packet.sync:
                self.sequence_number = packet.sequence_number
                self.last_sequence_number = self.sequence_number
            self._increment_sequence_number()

        # command has been executed already, resend last response
        elif self.last_sequence_number == packet.sequence_number:
            self.queue.appendleft(self.last_response)

        # Invalid sequence number. Do not execute and ask for next expected sequence number packet
        else:
            self.logger.warning("Wrong sequence number, expected " \
                                "%d but got %d", self.sequence_number, packet.sequence_number)
            status_packet = MdfuStatusPacket(self.sequence_number,\
                            MdfuStatus.COMMAND_NOT_EXECUTED.value,
                            int(CmdNotExecutedCause.SEQUENCE_NUMBER_INVALID.value).to_bytes(1, "little"),
                            resend=True)
            self.last_response = status_packet
            self.queue.appendleft(status_packet)

    def run(self):
        self.transport.open()
        while True:
            # Thread termination upon stop event
            if self.stop_event.is_set():
                break

            data = self.get_command()
            if data:
                packet = self.decode_command_packet(data)
                if packet is None:
                    continue
                self.logger.debug("MDFU Client got a packet\n%s\n", packet)

                self.handle_mdfu_command(packet)

            if len(self.queue):
                response =self.queue.pop()
                self.logger.debug("Mdfu client sending response:\n%s\n", response)
                self.transport.write(response.to_binary())
        self.transport.close()
        self.queue.clear()
        self.sequence_number = 0

    def _execute_command(self, packet: MdfuCmdPacket):
        """Execute MDFU command

        :param packet: MDFU command packet
        :type packet: MdfuCmdPacket
        :return: MDFU status packet
        :rtype: MdfuStatusPacket
        """
        if packet.command == MdfuCmd.GET_CLIENT_INFO.value:
            status_packet = self.cmd_get_client_info(packet)
        elif packet.command == MdfuCmd.WRITE_CHUNK.value:
            status_packet = self.cmd_write_chunk(packet)
        elif packet.command == MdfuCmd.START_TRANSFER.value:
            status_packet = self.cmd_start_transfer(packet)
        elif packet.command == MdfuCmd.END_TRANSFER.value:
            status_packet = self.cmd_end_transfer(packet)
        elif packet.command == MdfuCmd.GET_IMAGE_STATE.value:
            status_packet = self.cmd_get_image_state(packet)
        else:
            self.logger.error("Command not supported %s", packet.command)
            status_packet = MdfuStatusPacket(packet.sequence_number, MdfuStatus.COMMAND_NOT_SUPPORTED.value)
        return status_packet

    def _increment_sequence_number(self):
        """Increment the sequence number
        """
        self.sequence_number = (self.sequence_number + 1) & 0x1f

    def cmd_get_client_info(self, packet):
        """Handle Get Client Info command

        :param packet: MDFU command packet
        :type packet: MdfuCmdPacket
        """
        if MdfuCmd.GET_CLIENT_INFO in self.response_delays:
            time.sleep(self.response_delays[MdfuCmd.GET_CLIENT_INFO])
        status_packet = MdfuStatusPacket(packet.sequence_number, MdfuStatus.SUCCESS.value, self.client_info.to_bytes())
        return status_packet

    def cmd_start_transfer(self, packet):
        """Handle Start Transfer command

        :param packet: MDFU command packet
        :type packet: MdfuCmdPacket
        """
        if MdfuCmd.START_TRANSFER in self.response_delays:
            time.sleep(self.response_delays[MdfuCmd.START_TRANSFER])
        status_packet = MdfuStatusPacket(packet.sequence_number, MdfuStatus.SUCCESS.value)
        return status_packet

    def cmd_write_chunk(self, packet):
        """Handle Write Chunk command

        :param packet: MDFU command packet
        :type packet: MdfuCmdPacket
        """
        if MdfuCmd.WRITE_CHUNK in self.response_delays:
            time.sleep(self.response_delays[MdfuCmd.WRITE_CHUNK])
        status_packet = MdfuStatusPacket(packet.sequence_number, MdfuStatus.SUCCESS.value)
        return status_packet

    def cmd_get_image_state(self, packet):
        """Handle Get image state command

        :param packet: MDFU command packet
        :type packet: MdfuCmdPacket
        """
        if MdfuCmd.GET_IMAGE_STATE in self.response_delays:
            time.sleep(self.response_delays[MdfuCmd.GET_IMAGE_STATE])
        status_packet = MdfuStatusPacket(packet.sequence_number, MdfuStatus.SUCCESS.value,
                                         bytes([ImageState.VALID.value]))
        return status_packet

    def cmd_end_transfer(self, packet):
        """Handle End Transfer command

        :param packet: MDFU command packet
        :type packet: MdfuCmdPacket
        """
        if MdfuCmd.END_TRANSFER in self.response_delays:
            time.sleep(self.response_delays[MdfuCmd.END_TRANSFER])
        status_packet = MdfuStatusPacket(packet.sequence_number, MdfuStatus.SUCCESS.value)
        return status_packet


if __name__ == "__main__":
    from .mac import MacFactory
    from .mdfu import Mdfu
    from .transport.uart_transport import UartTransport
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.root.setLevel(logging.DEBUG)
    upgrade_image = bytes(512 * [0xff])

    mac_host, mac_client = MacFactory.get_bytes_based_mac()
    transport_client = UartTransport(mac=mac_client)
    client = MdfuClient(transport_client)

    transport_host = UartTransport(mac=mac_host)
    host = Mdfu(transport_host)

    client.start()
    host.run_upgrade(upgrade_image)
    client.stop()
