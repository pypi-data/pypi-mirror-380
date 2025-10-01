# Import necessary types and helpers from Python's standard library.
from collections.abc import Callable
from typing import Any, Optional

# Import constants used for state management and event listening.
from homeassistant.const import MATCH_ALL, STATE_OFF, STATE_ON, STATE_UNKNOWN
from homeassistant.core import Event, callback

# Import custom modules from this integration.
from ...api import TISApi  # The main API for communicating with TIS devices.
from ...Protocols.udp.ProtocolHandler import (
    TISProtocolHandler,
    TISPacket,
)  # TIS protocol specifics.


class BaseTISSwitch:
    """Base class for TIS switches, providing common functionality."""

    def __init__(
        self,
        tis_api: TISApi,
        *,
        channel_number: int,
        device_id: list[int],
        gateway: str,
        is_protected: bool = False,
        **kwargs: Any,
    ) -> None:
        """Initialize the base switch attributes."""
        super().__init__(**kwargs)

        self.api = tis_api
        self._state = STATE_UNKNOWN

        # Store device-specific information.
        self.device_id = device_id
        self.gateway = gateway
        self.channel_number = int(channel_number)
        self.is_protected = is_protected
        self._listener: Optional[Callable] = (
            None  # To hold the event listener unsubscribe function.
        )

        # This avoids rebuilding the byte arrays every time a command is sent.
        self.on_packet: TISPacket = TISProtocolHandler.generate_control_on_packet(self)
        self.off_packet: TISPacket = TISProtocolHandler.generate_control_off_packet(
            self
        )
        self.update_packet: TISPacket = (
            TISProtocolHandler.generate_control_update_packet(self)
        )

    async def async_added_to_hass(self) -> None:
        """Run when the entity is added to Home Assistant. Subscribe to events."""

        # Define a callback function to handle incoming TIS events.
        @callback
        def _handle_event(event: Event) -> None:
            """Handle incoming TIS events from the event bus and update the switch's state."""

            # Check if the event is intended for this specific device.
            # The event_type is used here as a filter for the device_id.
            if event.event_type == str(self.device_id):
                feedback_type = event.data.get("feedback_type")

                # --- Handle different types of feedback from the device ---

                # A direct response to a control command.
                if feedback_type == "control_response":
                    channel_value = event.data["additional_bytes"][2]
                    channel_number = event.data["channel_number"]
                    # Ensure the response is for this specific channel.
                    if int(channel_number) == self.channel_number:
                        # A value of 100 typically means ON (100% brightness/power).
                        self._state = (
                            STATE_ON if int(channel_value) == 100 else STATE_OFF
                        )
                        self._attr_is_on = self._state == STATE_ON

                # A response to a general status update request.
                elif feedback_type == "update_response":
                    additional_bytes = event.data["additional_bytes"]
                    # The status of each channel is in an array; get this channel's status.
                    channel_status = int(additional_bytes[self.channel_number])
                    self._state = STATE_ON if channel_status > 0 else STATE_OFF
                    self._attr_is_on = self._state == STATE_ON

                # The device has been reported as offline.
                elif feedback_type == "offline_device":
                    self._state = STATE_UNKNOWN
                    self._attr_is_on = None

                # Tell Home Assistant to update the state in the frontend.
                self.schedule_update_ha_state()

        # Subscribe the handler to all events on the Home Assistant event bus.
        # The filtering happens inside _handle_event.
        self._listener = self.hass.bus.async_listen(MATCH_ALL, _handle_event)

        # Request the current state of the switch from the device upon startup.
        await self.api.protocol.sender.send_packet(self.update_packet)

    async def async_will_remove_from_hass(self) -> None:
        """Run when the entity is about to be removed. Unsubscribe from events."""
        # Clean up the event listener to prevent memory leaks.
        if callable(self._listener):
            try:
                self._listener()
            finally:
                self._listener = None

    async def turn_switch_on(self, **kwargs: Any) -> None:
        """Turn the switch on by sending the on_packet."""
        # Send the pre-generated 'on' packet and wait for an acknowledgement (ack).
        return await self.api.protocol.sender.send_packet_with_ack(self.on_packet)

    async def turn_switch_off(self, **kwargs: Any) -> None:
        """Turn the switch off by sending the off_packet."""
        # Send the pre-generated 'off' packet and wait for an acknowledgement (ack).
        return await self.api.protocol.sender.send_packet_with_ack(self.off_packet)
