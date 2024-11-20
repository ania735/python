from os import system
owoce=["Banana","Lemon","Apple"]
while True:
    print("MENU")
    Menu="""
        1.Wyświetl liste owoców.
        2.Dodaj owoc do listy owoców.
        3.Odejmij owoc z listy owoców.
        4.Wyświetl liste owoców w kolejności alfabetycznej.
        5.Koniec programu"""
    print(Menu)

    menu=str(input("Podaj nr menu: "))

    if menu.isalpha():
        print("Wprowadziłeś nieprawidłową cyfrę: ")
        print("Wprowadź cyfrę od 1-5:")
        
    elif menu =="1":
        
        system("cls")
        print("Lista owoców")
        for i in range(len(owoce)):
            print(str(i+1)+".",(owoce[i]))

    elif menu =="2":
        system("cls")
        owoc_dodany=str(input("Podaj nazwę owocu który chcesz dodać do listy owoców: ")).capitalize().strip()
        if owoc_dodany.isdigit():
            print("Wprowadziłeś nieprawidłową nazwę owocu: ")
            print("Wprowadź prwidłową nazwę:")
        else:
            print("Dodaj owoc do listy owoców: ")
            owoce.append(owoc_dodany) 
            print("Dodany owoc",owoc_dodany)
            for i in range(len(owoce)):
                print(str(i+1)+".",(owoce[i]))
    elif menu == "3":
        system("cls")
        owoc_odjenty = str(input("Podaj nazwę owocu(pisaną dużą literą), którą chcesz odjąć z listy: "))
        if owoc_odjenty.isdigit():
            print("Podałeś złą nazwę owocu:")
        elif owoc_odjenty not in owoce:
                print("Ten owoc nie znajduje się na liście owoców:")
        else:
            if owoc_odjenty in owoce:
                print("Odejmij owoc z listy: ")
                owoce.remove(owoc_odjenty)
                print("Aktualna lista po usunięciu owoca:")
                for i in range(len(owoce)):
                    print(str(i+1)+".",(owoce[i]))
    elif menu == "4":
        print("Lista w kolejności alfabetycznej:")
        owoce.sort()
        for i in range(len(owoce)):
            print(str(i+1)+".",(owoce[i]))
                    
    elif menu == "5":
        print("wyjście z programu:")
        break
    input("Naciśnij enter, aby kontynuować:")            
