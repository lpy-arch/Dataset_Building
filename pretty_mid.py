import pretty_midi

midi_data = pretty_midi.PrettyMIDI('./music_examples/X Japan - Endless Rain.mid')
print(midi_data.instruments[-2].program)