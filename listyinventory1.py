#Inwentarz bohatera 3.0
#pobawmy się w listy!

#utwórz listę zawierającą pewne elemnty i wyświetl jej zawartość
#za pomocą pętli for
inventory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]
for item in inventory:
    print(item)

#wyświetl długość listy
print("Twój dobytek zawiera", len(inventory), "elementy-ów.")

#sprawdź czy element należy do listy za pomocą operatora in
if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę.")

#wyświetl jeden element wskazany przez indeks
index = int(input("\nWprowadź indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje się", inventory[index])

#wyświetl wycinek
start = int(input("\nWprowadź indeks wyznaczający początek wycinka: "))
finish = int(input("Wprowadź indeks wyznaczający koniec wycinka: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

#dokonaj konektacji dwóch list
chest = ["złoto", "klejnoty"]
print("Znajdujesz skrzynię, która zawiera:")
print(chest)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print("Twój aktualny inwentarz to:")
print(inventory)

#przypisz poptrzez indeks
print("Wymieniasz swój miecz na kuszę.")
inventory[0] = "kusza"
print("Twój aktualny inwentarz to:")
print(inventory)

input("\n\nAby koniec to Enter")
