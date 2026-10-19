midi_note=int(input("Enter a MIDI note [0, 127]: "))
music_note_value=midi_note%12
musical_note=""
match music_note_value:
    case 0:
        musical_note="C"
    case 1:
        musical_note = "C#"
    case 2:
        musical_note = "D"
    case 3:
        musical_note = "D#"
    case 4:
        musical_note = "E"
    case 5:
        musical_note = "F"
    case 6:
        musical_note = "F#"
    case 7:
        musical_note = "G"
    case 8:
        musical_note = "G#"
    case 9:
        musical_note = "A"
    case 10:
        musical_note = "A#"
    case 11:
        musical_note = "B"

exp=( (midi_note - 69) / 12)

freq=440*2**exp

print(f"MIDI Note {midi_note} is {freq:.2f} Hz which is a {musical_note}")