import time
import sys

def print_lyrics():
    lyrics = [
        "Teri aankhon se hui yaariyaan",
        "Chalte chalte yuhin",
        "Teri ankhon ne meri ankho se",
        "Aap biti kahin",
        "Teri ankhon ke pichhe pichhe ham",
        "Pagle se chal pade",
        "Teri ankhey ab dil ke chakkar me",
        "Kuchh bhi na sunti hai",
        "Dil ye dhokha dhadi kar dega",
        "Socha na tha",
        "Itni ye gadbadi kar dega",
        "Socha na tha",
        "Aisi mushkil khadi kar dega",
        "Socha na tha...",
    ]

    delays = [
        0.3, 1.0, 0.3, 1.0, 0.3, 1.0, 0.3, 1.0, 0.3, 0.5, 0.3, 0.6, 0.5,
    ]

    print(" Dhokha Dhadi : \n")
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