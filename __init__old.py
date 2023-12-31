import evdev
from evdev import InputDevice, ecodes
from select import select
from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
from ovos_utils.log import LOG


class NumericKeySkill(OVOSSkill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyboard = InputDevice('/dev/input/event7') 


    def runtime_requirements(self):
        return RuntimeRequirements(
            internet_before_load=False,
            network_before_load=False,
            gui_before_load=False,
            requires_internet=False,
            requires_network=False,
            requires_gui=False,
            no_internet_fallback=True,
            no_network_fallback=True,
            no_gui_fallback=True,
        )


    @intent_handler('shortcuts.intent')
    
    def listen_for_keyboard_events(self):
        try:
            while True:
                r, _, _ = select([self.keyboard], [], [], 0.1)  # Use 0.1 second as the timeout to poll
                if r:
                    for event in self.keyboard.read():
                        if event.type == ecodes.EV_KEY:
                            key_code = event.code
                            key_value = event.value

                            if key_value == 1:  # Key pressed (KP0-KP9)
                                if key_code >= ecodes.KEY_KP0 and key_code <= ecodes.KEY_KP9:
                                    digit = key_code - ecodes.KEY_KP0  # Get the pressed digit
                                    self.handle_numeric_key(digit)
        except Exception as e:
            self.log.error(f"Error reading keyboard input: {str(e)}")

    def handle_numeric_key(self, digit):
        # Perform specific actions based on the pressed digit
        if digit == 0:
            self.speak("You pressed 0")
            LOG.info("0 pressed")
            # Add your action for 0 here
        elif digit == 1:
            self.speak("You pressed 1")
            LOG.info("1 pressed")
            # Add your action for 1 here
        # Repeat for digits 2 to 9

    def stop(self):
        pass

    def run(self):
        self.listen_for_keyboard_events()

