#CONTACT BOOK
contacts = []
def add_con(name,CON_NUM,add):
    contacts.append({'name':name,'con_num':CON_NUM,'add':add})
    print(f"CONTACT DETAILS OF {name} IS ADDED.")

def view_con():
    print(f"YOU HAVE TOTAL {len(contacts)} CONTACTS")
    for index, contact in enumerate(contacts, start = 1):
        print(f"{index}.{contact['name']}")

def del_con(con_index):
    print(f"CONTACT DETAILS OF {contacts[con_index-1]['name']} IS DELETED.")
    contacts.pop(con_index-1)

def search_con(con_index):
    print(f"DETAILS OF CONTACT AT INDEX {con_index} IS:")
    print(contacts[con_index-1]['name']+"\n"+contacts[con_index-1]['con_num']+"\n"+contacts[con_index-1]['add'])                   
def update_name(con_index,name):
    contacts[con_index-1].update({'name':name})
def update_con(con_index,contact):
    contacts[con_index-1].update({'con_num':contact})
def update_add(con_index, add):
    contacts[con_index-1].update({'add':add})
print("===================WELCOME TO YOUR CONTACT BOOK.=================")
while(True):
    print("PRESS 1 TO CONTINUE.")
    print("PRESS 0 TO EXIT.")
    try:
        choice = int(input("ENTER YOUR CHOICE:"))
    except ValueError as e:
        print(e+"please enter valid value.")    
    if choice == 0:
        print("=============THANKS FOR VISITING YOUR CONTACT BOOK=============")
        break
    else:
        print("PRESS 'A' TO ADD CONTACTS.")
        print("PRESS 'D' TO DELETE CONTACTS.")
        print("PRESS 'V' TO VIEW CONTACTS.")
        print("PRESS 'U' TO UPDATE CONTACTS.")
        print("PRESS 'S' TO SEARCH CONTACTS.")
        task = input("ENTER THE TASK YOU WANT TO PERFORM:")
        if task.lower() == 'a':
            name = input("ENTER THE NAME:")
            while(True):
                CON_NUM = input(f"ENTER {name}'S CONTACT NUMBER:")
                if len(CON_NUM) == 10:
                    break
                else:
                    print("PLEASE ENTER A VALID NUMBER.")    
                    continue
            add = input(f"ENTER THE ADDRESS OF {name}:")
            add_con(name,CON_NUM,add)
        elif task.lower()== 'v':
            view_con()
        elif task.lower()== 'd':
            con_index = int(input("ENTER THE INDEX OF CONTACT YOU WANT TO DELETE:"))
            del_con(con_index)
        elif task.lower()== 's':
            index = int(input("ENTER THE INDEX OF CONTACT YOU WANT TO SEARCH:"))
            search_con(index)
        elif task.lower()=='u':
            value = int(input("ENTER WHOSE CONTACT YOU WANT TO UPDATE:"))
            update_status = input("ENTER WHAT YOU WANT TO UPDATE(name,contact number ,address):")
            if update_status.lower() == 'name':
                NAME = input("ENTER THE NEW NAME")
                update_name(value, NAME)
            elif update_status.lower()== 'contact number':
                connum = input("ENTER THE NEW CONTACT NUMBER:")
                update_con(value,connum)   
            if update_status.lower()== 'address':
                address = input("ENTER THE NEW address:")
                update_add(value,address)