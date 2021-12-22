#gestione rubrica
#struttura dati :: lista di dict

def printMenu():

    print("******gestione rubrica******")
    print("1.print contact")
    print("2.search contact")
    print("3.new contact")
    print("4.remove contact")
    print("5.exit")
    print("command: ")

    return

def readContacts(f_name):
    fp=open(f_name,"r")
    f_list=[]
    for line in fp:
        line=line.split(":")
        contact={}
        contact["name"] = line[0]
        contact["id"]=line[1]
        contact["cell"] = line[2]
        contact["addr"] = line[3]
        f_list.append(contact)
    fp.close()
    return f_list

def printContacts(f_list):

    for item in f_list:
        for key,val in item.items():
            print(key,"--->",val)
    #for val in item.values():
    #   print(val)

    return

def searchContact(f_list,f_name):
    pos=-1
    for i,item in enumerate(f_list):
        if item["name"] == f_name: #i alternativa: f f_name in item.values()
            pos=i
    return pos


def addContact(f_list):
    name=input("- new name: ")
    pos= searchContact(f_list,name)
    if pos == -1:
        #ask info
        cell=input("- new cell: ")
        addr=input("- new address: ")
        #search max id
        max_id=-1
        for item in f_list:
            if int(item["id"])> max_id:
                max_id=int(item["id"])
        id=max_id+1
        contact={}
        contact["name"]=name
        contact["id"]=str(id)
        contact["cell"]=cell
        contact["addr"]=addr
        f_list.append(contact)
    else:
        print("contact already extisting")
    return

def save(f_name,f_list):
    fp=open(f_name,"w")
    for item in f_list:
        line=""
        line += item["name"]+":"
        line += item["id"]+":"
        line += item["cell"]+":"
        line += item["addr"]
        fp.write(line)

    fp.close()

    return f_list

def main():
    book=[]
    book=readContacts("contacts.txt")
    #gestione menu'
    op=-1
    while op != "5":
        printMenu()
        op=input()
        if op == "1":
            printContacts(book)
            #print
        elif op=="2":
            name=input("Name to search: ")
            pos=searchContact(book,name) #pos <-- indice contatto cercato
            if pos != -1:
                print(book[pos])
            #search

        elif op=="3":
            #new
            addContact(book)

        elif op== "4":
            #del
            name=input("name to delete: ")
            pos=searchContact(book,name)
            if pos != -1:
                book.pop(pos)
            else:
                print("no contact ",name)

        elif op== "5":
            #exit
            save("contacts.txt", book)
        else:
            print("invalid command")
    return

main()