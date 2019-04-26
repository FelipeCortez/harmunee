import time
import rtmidi

class MidiPlayer():
    def __init__(self):
        self.midiout = rtmidi.MidiOut()

        if self.midiout.get_ports():
            self.midiout.open_port(0)
        else:
            self.midiout.open_virtual_port("outport")

    def __del__(self):
        del self.midiout

    def noteon(self, midi_note):
        self.midiout.send_message([0x90, midi_note, 112])

    def noteoff(self, midi_note):
        self.midiout.send_message([0x80, midi_note, 0])
