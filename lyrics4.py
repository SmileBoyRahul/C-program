import time
import sys

def print_lyrics():
    lyrics = [
        "Jara si duriyaan bhi",
        "Nahin tumse gawaara",
        "Haa, Aise pyaar hamko",
        "Nahin hoga dubaara",
        "Jahaan tum..",
        "Miloge..",
        "Jaana vahi tak hai",
        "Hasi hai...",
        "Nami hai..",
        "Jo hai tumhi tak hai...",
        "Badhne do, chahte ye",
        "Thoda aur, Thoda aur",
        "Thoda aur...",
        "Chale aao, Paas mere",
        "Thoda aur, Thoda aur",
        "thoda aur...",
    ]

    delays = [
        0.3, 0.3, 0.3, 0.3, 0.2, 0.2, 0.3, 0.2,
        0.2, 0.4, 0.2, 0.3, 0.5, 0.3, 0.4, 0.5,
    ]

    print(" THODA AUR : \n")
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