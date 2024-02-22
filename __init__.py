import evdev
from evdev import InputDevice, ecodes
from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
from ovos_utils.log import LOG
from ovos_bus_client.message import Message
import time
from ovos_bus_client.apis.ocp import OCPInterface
from ovos_plugin_common_play.ocp import MediaType, PlaybackType


class NumericKeySkill(OVOSSkill):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def initialize(self):
        # Initialize the OCP audio service with the bus
        self.audio = OCPInterface(self.bus)
        self.keyboard_device = InputDevice("/dev/input/event6")  # Use `python -m evdev.evtest` to get the event number
        self.menu1 = "https://i.ibb.co/RYZjzY7/menu1.jpg"
        self.menu2 = "https://i.ibb.co/FKrHHTp/menu2.jpg"
        self.menu2a = "https://i.ibb.co/mh8zWpB/Scherm-2.jpg"
        self.menu3 = "https://i.ibb.co/ZS5DHrn/menu-1-alternatief.jpg"
        self.url = "https://icecast.omroep.nl/radio1-bb-mp3"
        self.radio1 = [
        {
                "media_type": MediaType.RADIO,
                "uri": self.url,
                "playback": PlaybackType.AUDIO,
                "image": "https://is5-ssl.mzstatic.com/image/thumb/Purple126/v4/7b/b1/b5/7bb1b5c6-5dae-a362-d4b0-1e31c12d084c/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/512x512bb.jpg",
                "bg_image": "https://cms-assets.nporadio.nl/npoRadio1/archief/_videoThumbnail/2365104/18_aa_NPO_Radio_1_logo_2014.svg.jpg",
                "skill_icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/NPO_Radio_1_logo_2014.svg/1200px-NPO_Radio_1_logo_2014.svg.png",
                "author": "Radio 1 live",
                "title" : " ",
                "length": 0
            }
        ]


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


    def welcome(self):
        self.gui.show_image(self.menu1, fill="PreserveAspectCrop", override_idle=True, override_animations=False)
        self.bus.emit(Message("ovos.phal.plugin.homeassistant.set.light.brightness", data = {"device": "moodlight", "brightness": 1000}))
        self.bus.emit(Message("ovos.phal.plugin.homeassistant.set.light.color", data = {"device": "moodlight", "color": "yellow"}))
        self.speak("Welkom bij de Visio Voice Assistent.")
        self.speak("Kies 1 voor weer, 2 voor de tijd of 3 voor nieuws. Kies 0 voor meer.")
        self.listen_for_keyboard(self)

    def listen_for_keyboard(self, message):
        for event in self.keyboard_device.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.code == ecodes.KEY_KP0 and event.value == 1:
                    LOG.info("Numeric key 0 pressed")
                    self.handle_numeric_key_press(0)
                elif event.code == ecodes.KEY_KP1 and event.value == 1:
                    LOG.info("Numeric key 1 pressed")
                    self.handle_numeric_key_press(1)
                elif event.code == ecodes.KEY_KP2 and event.value == 1:
                    LOG.info("Numeric key 2 pressed")
                    self.handle_numeric_key_press(2)
                elif event.code == ecodes.KEY_KP3 and event.value == 1:
                    LOG.info("Numeric key 3 pressed")
                    self.handle_numeric_key_press(3)
                elif event.code == ecodes.KEY_KP4 and event.value == 1:
                    LOG.info("Numeric key 4 pressed")
                    self.handle_numeric_key_press(4)
                elif event.code == ecodes.KEY_KP5 and event.value == 1:
                    LOG.info("Numeric key 5 pressed")
                    self.handle_numeric_key_press(5)
                elif event.code == ecodes.KEY_KP6 and event.value == 1:
                    LOG.info("Numeric key 6 pressed")
                    self.handle_numeric_key_press(6)
                elif event.code == ecodes.KEY_KP7 and event.value == 1:
                    LOG.info("Numeric key 7 pressed")
                    self.handle_numeric_key_press(7)
                elif event.code == ecodes.KEY_KP8 and event.value == 1:
                    LOG.info("Numeric key 8 pressed")
                    self.handle_numeric_key_press(8)
                elif event.code == ecodes.KEY_KP9 and event.value == 1:
                    LOG.info("Numeric key 9 pressed")
                    self.handle_numeric_key_press(9)


    def handle_numeric_key_press(self, key_code):
        self.speak(f"U koos voor {key_code}")
        if key_code == 1:
            self.speak("weer")
            self.emit_utterance("weer")
        elif key_code == 2:
            self.speak("tijd")
            self.emit_utterance("tijd")
        elif key_code == 3:
            self.speak("nieuws")
            self.emit_utterance("nieuws")
        elif key_code == 4:
            self.speak("huisradio de Vlasborch")
            self.emit_utterance("praat met huisradio de Vlasborch")
        elif key_code == 5:
            self.speak("YouTube")
            self.emit_utterance("speel YouTube")
        elif key_code == 6:
            self.speak("Spel")
            self.emit_utterance("ronja en de piraten")
        elif key_code == 7:
            self.speak("Radio 1")
            self.audio.play(self.radio1)



        elif key_code == 8:
            self.speak("Nog te maken")
       #     self.emit_utterance("")
        elif key_code == 9:
            self.speak("Nog te maken")
       #     self.emit_utterance("")
        elif key_code == 0:
            self.speak("meer opties")
            self.gui.show_image(self.menu1, fill="PreserveAspectCrop", override_idle=True, override_animations=False)
            self.gui.show_image(self.menu2a, fill="PreserveAspectCrop", override_idle=True, override_animations=False)
            self.speak("Kies 4 voor huisradio, 5 voor YouTube of 6 voor spel.")

    def emit_utterance(self, utterance):
        intent_message = Message("recognizer_loop:utterance", data={
            "utterances": [utterance]
        })
        self.bus.emit(intent_message)

    def shutdown(self):
        pass
