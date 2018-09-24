#program na zaliczenie
#zgadywanie słowa wybranego przez komputer

import random

WORDS = ("komputer", "sokowirówka", "automat", "stevejobs")

word = random.choice(WORDS)

correct = word

liczbal = len(correct)

proba = 1


# let's play a game

print("\t///TEST AREA///", correct, "\n\n\n")

print("Witaj w grze w której spróbujesz zgadnąć słowo, które ja wybieram")
print("Podam Ci ile liter ma to słowo, a Ty będziesz zgadywał, co to za litery")
print("A później spróbujesz zgadnąć hasło.")
print("Zaczynajmy!")
print("\nLiczba liter w zgadywaniem słowie to: ", liczbal, "liter")
litera = input("A teraz spróbuj zgadnąć literę znajdującą się w tym słowie: ")


liczbaliter = len(litera)

while litera != "" and liczbaliter < 2:

    if litera in correct and proba < 5:
        print("TAK", proba)
        litera = input("A teraz spróbuj zgadnąć literę znajdującą się w tym słowie: ")
        liczbaliter = len(litera)
        proba += 1
    if litera not in correct and proba < 5:
        print("NIE", proba)
        litera = input("A teraz spróbuj zgadnąć literę znajdującą się w tym słowie: ")
        liczbaliter = len(litera)
        proba += 1
    elif proba == 5:
        if litera in correct:
            print("TAK")
        if litera not in correct:
            print("NIE")
        break

else:
    print("Oszukujesz, więc teraz zgaduj od razu :)))")

#druga pętla

zgaduj = input("Ostateczna próba, zgaduj słowo! Twoja odpowiedź to: ")

while zgaduj != correct and zgaduj !="":
    print("źle, jeszcze raz!")
    zgaduj = input("Ostateczna próba, zgaduj słowo! Twoja odpowiedź to: ")
if zgaduj == correct:
    print("GRATULACJE ZGADŁEŚ!!! ---===KONIEC===---")


input("\n\n\nTo koniec programu na zaliczenie. Dziękuję!")

