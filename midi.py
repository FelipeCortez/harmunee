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

    def play(self, midi_note):
        note_on = [0x90, midi_note, 112] # channel 1, middle C, velocity 112
        note_off = [0x80, midi_note, 0]
        self.midiout.send_message(note_on)
        self.midiout.send_message(note_off)
