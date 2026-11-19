'''12. Smart Home Devices (Multiple Inheritance) 
A smart home device may have both WiFi connectivity and Voice control features. 
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that 
inherits from both using multiple inheritance. '''

class WifiDevice():
    def wifi(self):
        print("Wifi coonectivity is available")
class VoiceAssistant():
    def voice(self):
        print("voice assistant is available")
class SmartSpeaker(WifiDevice , VoiceAssistant):
    def display(self):
        print("Smart speaker Features:")
        self.wifi()
        self.voice()
obj=SmartSpeaker()
obj.display()
