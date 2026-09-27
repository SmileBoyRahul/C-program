import time
import sys

def print_lyrics():
    lyrics = [
        "Main ab kyu hosh mein aata nahi",
        "Sukoon ye dil kyu paata nahi",
        "Kyu todu khud se jo they wadey,",
        "Ke ab ye ishq nibhaana nahi",
        "Main modu tumse jo ye chehra",
        "Dobara nazar milana nahi",
        "Ye duniya jaane mera dard",
        "Tujhe ye nazar kyu aata nahi?",
    ]

    delays = [
        0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8,
    ]

    print(" pal pal : \n")
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