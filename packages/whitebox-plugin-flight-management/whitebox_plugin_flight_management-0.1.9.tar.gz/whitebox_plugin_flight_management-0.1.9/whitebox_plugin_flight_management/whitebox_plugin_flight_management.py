from whitebox import Plugin
from .handlers import FlightStartHandler, FlightEndHandler


class WhiteboxPluginFlightManagement(Plugin):
    name = "Flight Management"

    provides_capabilities = [
        "flight-management",
    ]
    slot_component_map = {
        "flight-management.trigger-button": "TriggerButton",
    }
    exposed_component_map = {
        "flight-management": {
            "trigger-button": "TriggerButton",
        }
    }

    plugin_event_map = {
        "flight.start": FlightStartHandler,
        "flight.end": FlightEndHandler,
    }

    state_store_map = {
        "inputs": "stores/inputs",
        "flight.mission-control": "stores/mission_control",
    }

    plugin_url_map = {
        "flight.flight-session-list": "whitebox_plugin_flight_management:flight-session-list",
    }

    def get_plugin_classes_map(self):
        from .services import FlightService

        return {
            "flight.FlightService": FlightService,
        }


plugin_class = WhiteboxPluginFlightManagement
