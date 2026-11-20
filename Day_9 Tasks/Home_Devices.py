class WiFiDevice:
    def connect_wifi(self, network):
        print(f"Connected to WiFi network: {network}")

class VoiceAssistant:
    def voice_command(self, command):
        print(f"Executing voice command: '{command}'")

# Inherits capabilities from both parent classes
class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def __init__(self, device_name):
        self.device_name = device_name

    def status(self):
        print(f"{self.device_name} is online and ready.")

speaker = SmartSpeaker("Echo Dot")
speaker.connect_wifi("Home_5G")
speaker.voice_command("Play morning news")
speaker.status()