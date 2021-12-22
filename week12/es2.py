#gestione dati
#struttura dati:: record

def printMenu():
    print("*** gestione rubrica ***")
    print("  1. print contacts")
    print("  2. search contact ")
    print("  3. new contact")
    print("  4. remove contact")
    print("  5. exit")
    print("command: ")
    return
def readContacts(f_name):
    f_dict = {}
    fp = open(f_name, "r")
    for line in fp:
        line = line.split(":")
        f_dict[line[0]] = line[1:]
    fp.close()
    return f_dict

def printContacts(f_dict):
    for key, value in f_dict.items():
        print(key, value)
    return

def main():
    rubrica = {}
    rubrica = readContacts("contacts.txt")
    # gestione menu
    op = -1
    while op != "5":
        printMenu()
        op = input()
        if op == "1":
            printContacts(rubrica)
            #print
        elif op == "2":
            #search
            name = input("Name to search: ")
            if name in rubrica:
                print(rubrica[name])
            else:
                print("contact does not exist")
        elif op == "3":
            #new
            print(3)
            name = input(" - New name: ")
            if name not in rubrica:
                cell = input(" - New Cell: ")
                addr = input(" - New Address: ")
                # ricerca id max -> ricerca valore massimo tra i valori di un dict @home
                id = "99999"
                rubrica[name] = [id, cell, addr]
        elif op == "4":
            #del
            name = input(" Name to delete: ")
            if name in rubrica:
                rubrica.pop(name)
            else:
                print(name, "not in book")
        elif op == "5":
            #exit
            print(5)
            fp = open("contacts.txt", "w")
            for key, value in rubrica.items():
                line=""
                line += key+":"
                line += value[0]+":"
                line += value[1]+":"
                line += value[2]
            fp.close()
        else:
            print("invalid command")
    return

main()