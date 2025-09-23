print("----CONTACT BOOK----\n")

contact_book=[]
information=[]

while True:

    def add():
        name=input("Enter the Store name : ")
        contact=input("Enter the contact number : ")
        email=input("Enter the E-mail : ")
        address=input("Enter the Address : ")
        information=[name,contact,email,address]
        contact_book.append(information)

        print("contact successfully added!")

        return contact_book,information
    
    def view(contact_book):
        
        if(contact_book==[]):
            
            print("THE CONTACT BOOK IS EMPTY!")
        else:
            print("\nNAME | CONTACT NUMBER | E-MAIL | ADDRESS")
            print("----------------------------------------")
            for i in range (len(contact_book)):
                print(i+1,*contact_book[i], sep=" | ")

    def search(contact_book):
        z=False
        if(contact_book==[]):
            print("THE CONTACT BOOK IS EMPTY!")
        else:
            l=1
            u=len(contact_book)

            sear=int(input("Do you want to search the contact by\n1. Name \n2.Number\n"))

            if sear==1:
                n=(input("Enter the name you want to search : "))

                for i in range(len(contact_book)):
                    if (contact_book[i][0]==n):
                        x=contact_book[i]
                        print("Search Successfull!\n")
                        print(*x,sep=" | ")
                        z=True
                if(z==False):
                    print("No Contact Found")

            elif sear==2:
                c=input("Enter the number you want to search : ")
                for i in range(len(contact_book)):
                    if (contact_book[i][1]==c):
                        y=contact_book[i]
                        print("Search Successfull!\n")
                        print(*y,sep=" | ")

    def update(contact_book):
        if(contact_book==[]):
            print("THE CONTACT BOOK IS EMPTY!")
        else:
            ser=int(input("Enter the serial no. of the contact you want to update : "))

            print("What do you want to update?")
            print("1. Name\n 2.Contact number\n 3.E-mail\n 4.Address\n")
            ch=int(input())
            if(ch==1):
                updated_name=input("Enter the updated name : ")
                contact_book[ser-1][0]=updated_name
            if(ch==2):
                updated_contact=input("Enter the updated contact number : ")
                contact_book[ser-1][0]=updated_contact
            if(ch==3):
                updated_email=input("Enter the updated E-mail : ")
                contact_book[ser-1][0]=updated_email
            if(ch==4):
                updated_address=input("Enter the updated Address : ")
                contact_book[ser-1][0]=updated_address

            print("Contact updated succcessfully!")

    def delete(contact_book):
        if(contact_book==[]):
            print("THE CONTACT BOOK IS EMPTY!")
        else:
            delt=int(input("Enter the serial no. of the contact you want to delete : "))
            del(contact_book[delt-1])
            print("\nContact deleted succcessfully!")

    print("1. Add contact")
    print("2. View contactlist")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")

    choice=int(input("\nEnter your choice : "))
    if choice==1:
        add()
    elif choice==2:
        view(contact_book)
    elif choice==3:
        search(contact_book)
    elif choice==4:
        update(contact_book)
    elif choice==5:
        delete(contact_book)
    else:
        print("INVALID CHOICE!")


    repeat=input("\nDo you want to perform another opertaion? (y/n) : ")
    if repeat=='y':
        continue
    else:
        break