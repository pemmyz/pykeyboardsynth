# pykeyboardsynth

- This project predates [js_keyboardsynth](https://github.com/pemmyz/js_keyboardsynth) , which is originally based on same idea from this project.
- For all the latest features and fixes please check [js_keyboardsynth](https://github.com/pemmyz/js_keyboardsynth)

# 🎹 Pygame Keyboard Synth

This is a simple virtual synthesizer built with **Pygame** and **NumPy**. It maps your keyboard keys to musical notes and plays sine wave tones when keys are pressed.

## 🔊 Features

- Press keys to play notes from C4 to E6
- Polyphonic: Play multiple notes at once
- Smooth fadeout on key release
- Uses NumPy to generate real-time sine wave audio

## ⌨️ Keyboard Mapping

| Key | Note  | Frequency (Hz) |
|-----|-------|----------------|
| q   | C4    | 261.63         |
| 2   | C#4   | 277.18         |
| w   | D4    | 293.66         |
| 3   | D#4   | 311.13         |
| e   | E4    | 329.63         |
| r   | F4    | 349.23         |
| 5   | F#4   | 369.99         |
| t   | G4    | 392.00         |
| 6   | G#4   | 415.30         |
| y   | A4    | 440.00         |
| 7   | A#4   | 466.16         |
| u   | B4    | 493.88         |
| i   | C5    | 523.25         |
| 9   | C#5   | 554.37         |
| o   | D5    | 587.33         |
| 0   | D#5   | 622.25         |
| p   | E5    | 659.26         |
| a   | F5    | 698.46         |
| z   | F#5   | 739.99         |
| s   | G5    | 783.99         |
| x   | G#5   | 830.61         |
| d   | A5    | 880.00         |
| c   | A#5   | 932.33         |
| f   | B5    | 987.77         |
| g   | C6    | 1046.50        |
| h   | C#6   | 1108.73        |
| j   | D6    | 1174.66        |
| k   | D#6   | 1244.51        |
| l   | E6    | 1318.51        |

## 🛠️ Requirements

- Python 3.x
- Pygame
- NumPy

