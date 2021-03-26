'''
Gra w zgadywanie liczb.
Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
1. Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
2. Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", po czym wrócić do pkt. 1
3. Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "To small!", po czym wrócić do pkt. 1.
4. Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "To big!", po czym wrócić do pkt. 1.
5. Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", po czym zakończyć działanie programu.
'''

from random import randint
def los():
    los = int(randint(1, 100))
    print(los)
    while True:
        try:
            liczba = input("Chose number: ")
            liczba = float(liczba)
        except:
            print("It's not a number!")
            continue
        if liczba == los:
            return "You win!"
            break
        elif liczba < los:
            print("To small!")
        else:
            print("To big!")

print(los())