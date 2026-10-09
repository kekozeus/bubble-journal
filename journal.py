from datetime import date

entries = [] #se crea una lista para las entries del journal
while True: #repetir el menu
    print("=== Welcome to Bubble Journal ===")
    print("What would you like to do?")
    print("1. Write a new entry")
    print("2. View all entries")
    print("3. Search entries by date")
    print("4. Exit")
    option = input("Write your option here: ")

    if option == "1":
        entry_date = input("Write the date(YYYY-MM-DD): ")
        entry_date = date.fromisoformat(entry_date)
        title = input("Type in the title of this entry: ")
        mood = input("How are you feeling today?: ")
        journal_entry = input("Start writing your entry: ")
        print("Entry saved!")
        entries.append((entry_date, title, mood, journal_entry)) # se usa la funcion append para guardar datos dentro de la lista, entre () para que se guarden distintas variables al mismo tiempo, esto se llama "tupla"
        
    elif option == "2":
        if not entries:
             print("You don't have any entries yet.")
        else:
            for entry in entries: #se utiliza un loop de iteracion para imprimir cada elemento por separado
                    print("=====================")
                    print(entry[0]) #fecha
                    print(entry[1]) #titulo
                    print("=====================")
                    print("Mood of today:", entry[2]) #mood
                    print("Your entry:", entry[3]) #content
    elif option == "3":
        search_date  = input("Type in the date you want to search for: ")
        search_date  = date.fromisoformat(search_date)

        found = False

        for entry in entries:
            if entry [0] == search_date: 
                print("=====================")
                print(entry[0]) #fecha
                print(entry[1]) #titulo
                print("=====================")
                print("Mood of today:", entry[2]) #mood
                print("Your entry:", entry[3]) #content
                found = True

        if not found:
             print("No records found.")

    elif option == "4":
         break
    else:
         print("Invalid option. Try again.")

