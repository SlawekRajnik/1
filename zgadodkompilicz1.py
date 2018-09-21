#program na zaliczenie
#zgadywanie słowa wybranego przez komputer

import random

WORDS = ("komputer", "sokowirówka", "automat", "stevejobs")

word = random.choice(WORDS)

correct = word

liczbal = len(correct)

# let's play a game

print("\t///TEST AREA///", correct, "\n\n\n")

print("Witaj w grze w której spróbujesz zgadnąć słowo, które ja wybieram")
print("Podam Ci ile liter ma to słowo, a Ty będziesz zgadywał, co to za litery")
print("A później spróbujesz zgadnąć hasło.")
print("Zaczynajmy!")
print("\nLiczba liter w zgadywaniem słowie to: ", liczbal, "liter")
litera = input("A teraz spróbuj zgadnąć literę znajdującą się w tym słowie: ")

#sprawdź czy użytkownik nie oszukuje
oszust = len(litera)

while oszust == 1 and proba == 5:
    for letter in correct:
        
    


input("To koniec programu na zaliczenie. Dziękuję!")

