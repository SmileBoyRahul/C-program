import time
import sys

def print_lyrics():
    lyrics = [
        "Palkein jhapakta hai aasmaan..",
        "Lakhon faristo ki hai tu jaan..",
        "Woh puchhte hai",
        "Rehti kahan....",
        "Meri baahon me rehti unko bata..",
        "Palkein jhapakta hai aasmaan..",
        "Usne bhi tujhsa dekha kahan..",
        "Hain raunakein vaha tu hai jahan",
        "Meri baahon me rehna",
        "Yahi hai dua",
        "Tu agar meri",
        "Ye hawaayein teri",
        "Tu agar meri",
        "Saari rahein teri",
        "Tu agar meri",
        "Main hoon tera...",
    ]

    delays = [
        0.6, 0.6, 0.3, 0.5, 0.6, 0.6, 0.6, 0.3,
        0.6, 0.4, 0.6, 0.4, 0.6, 0.4, 0.6, 0.5
    ]

    print(" Gehra Hua : \n")
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
            time.sleep(1.0)

print_lyrics()    