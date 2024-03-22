user_name= input("Enter name : ")
menu= "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice= input(">>>").upper()
while choice!="Q":
    if choice=="H":
        print(f"Hello {user_name}")
    elif choice=="G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid message")
    print(menu)
    choice=input(">>>").upper()
print("Finished.")