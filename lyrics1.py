import time
import sys

def print_lyrics():
    lyrics = [
        "Maaji saasu tujhi mother",
        "Maaji hona re humsafar",
        "I like your beauty",
        "I like your fashion",
        "Tuja var thamu ne maari nazar",
        "Ek number",
        "Tujhi kamar",
        "Haaye chaal shaaky shaky",
        "Haaye kitti sundar",
        "Tujha dimple",
        "Je paaije take it take it",
        "Ek number",
        "Tujhi kamar",
        "Haaye chaal shaaky shaky",
        "Haaye kitti sundar",
        "Tujha dimple",
        "Je paaije take it take it",
    ]

    delays = [
        0.3, 0.3, 0.3, 0.3, 0.3, 0.5, 0.5, 0.3,
        0.5, 0.5, 0.3, 0.5, 0.5, 0.3, 0.5, 0.5
    ]

    print(" Shaky Shaky : \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics()    