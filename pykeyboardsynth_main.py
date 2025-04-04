import pygame
import numpy as np
import sys
import pygame.locals

def generate_beep(frequency, sample_rate=44100, duration=1.0):
    # generate a sine wave
    sine_wave = (32767 * np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate)).astype(np.int16)

    # Duplicate for both channels (left and right)
    stereo_wave = np.column_stack((sine_wave, sine_wave))

    # create a Sound object from the generated stereo sine wave
    beep = pygame.mixer.Sound(array=stereo_wave)

    return beep

# Dictionary mapping keys to frequencies
key_to_frequency = {
    'q': 261.63,  # C4
    '2': 277.18,  # C#4/Db4
    'w': 293.66,  # D4
    '3': 311.13,  # D#4/Eb4
    'e': 329.63,  # E4
    'r': 349.23,  # F4
    '5': 369.99,  # F#4/Gb4
    't': 392.00,  # G4
    '6': 415.30,  # G#4/Ab4
    'y': 440.00,  # A4
    '7': 466.16,  # A#4/Bb4
    'u': 493.88,  # B4
    'i': 523.25,  # C5
    '9': 554.37,  # C#5/Db5
    'o': 587.33,  # D5
    '0': 622.25,  # D#5/Eb5
    'p': 659.26,  # E5
    'a': 698.46,  # F5
    'z': 739.99,  # F#5/Gb5
    's': 783.99,  # G5
    'x': 830.61,  # G#5/Ab5
    'd': 880.00,  # A5
    'c': 932.33,  # A#5/Bb5
    'f': 987.77,  # B5
    'g': 1046.50, # C6
    'h': 1108.73, # C#6/Db6
    'j': 1174.66, # D6
    'k': 1244.51, # D#6/Eb6
    'l': 1318.51  # E6
}

# Dictionary to store currently playing sounds
playing_sounds = {}

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
fadeout_time = 1000  # 1 second fadeout

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check if the key pressed is in the key_to_frequency dictionary
            if event.unicode in key_to_frequency:
                # Stop any previous sound associated with this key
                if event.unicode in playing_sounds:
                    playing_sounds[event.unicode].stop()
                    del playing_sounds[event.unicode]

                # Create a new sound and play it
                frequency = key_to_frequency[event.unicode]
                sound = generate_beep(frequency)
                sound.play(-1)  # Play sound indefinitely with -1
                playing_sounds[event.unicode] = sound
        elif event.type == pygame.KEYUP:
            # Check if the released key had a sound playing
            if event.unicode in playing_sounds:
                sound = playing_sounds[event.unicode]
                sound.fadeout(fadeout_time)  # Fadeout the sound over the specified time
                del playing_sounds[event.unicode]  # Remove the sound from the dictionary


# Quit Pygame
pygame.quit()
sys.exit()
