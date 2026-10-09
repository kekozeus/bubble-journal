from datetime import date
import json
import os

path_to_check = "entries.json" #revisar si el archivo existe donde se guardaran las entradas
if os.path.exists(path_to_check):
    with open(path_to_check, "r", encoding="utf-8") as file:
        entries = json.load(file) #leer el JSON file
else:
    entries = [] #se crea una lista para las entries del journal
    #creacion de un ARCHIVO para verificar JSON
    with open(path_to_check, "w", encoding="utf-8") as file:
        json.dump(entries, file, indent=4, sort_keys=True) #funcion para crear y guardar el JSON file

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
        entry_date = date.fromisoformat(entry_date) #cambiar el date type de texto a date
        title = input("Type in the title of this entry: ")
        mood = input("How are you feeling today?: ")
        journal_entry = input("Start writing your entry: ")

        new_entry = { #guardamos el archivo con datos JSON
             "date": entry_date.isoformat(),
             "title": title,
             "mood": mood,
             "entry": journal_entry
        }

        entries.append(new_entry) #se guarda el JSON en el [] entries con el diccionario new_entry
        
        with open(path_to_check, "w", encoding="utf-8") as file:
            json.dump(entries, file, indent=4, ensure_ascii=False) #guardar la lista con json.dump
        print("Entry saved!")

        #entries.append((entry_date, title, mood, journal_entry)) # se usa la funcion append para guardar datos dentro de la lista, entre () para que se guarden distintas variables al mismo tiempo, esto se llama "tupla"
        
    elif option == "2":
        if not entries:
             print("You don't have any entries yet.")
        else:
            for entry in entries: #se utiliza un loop de iteracion para imprimir cada elemento por separado
                    print("=====================")
                    print("Date:", entry["date"]) #el elemento entre [] pertenece a las claves del diccionario JSON
                    print("Title:", entry["title"])
                    print("=====================")
                    print("Mood of today:", entry["mood"])
                    print("Your entry:", entry["entry"])
    elif option == "3":
        search_date  = input("Type in the date you want to search for: ")

        found = False

        for entry in entries: 
            if entry["date"] == search_date:
                print("=====================")
                print("Date:", entry["date"])
                print("Title:", entry["title"])
                print("=====================")
                print("Mood of today:", entry["mood"])
                print("Your entry:", entry["entry"])
                found = True

        if not found:
             print("No records found.")

    elif option == "4":
         break
    else:
         print("Invalid option. Try again.")

