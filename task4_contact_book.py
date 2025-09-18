print("----CONTACT BOOK----\n")

list1=[]
list2=[]

while True:

    def add():
        name=input("Enter the Store name : ")
        contact=input("Enter the contact number : ")
        email=input("Enter the E-mail : ")
        address=input("Enter the Address : ")
        list2=[name,contact,email,address]
        list1.append(list2)

        print("contact successfully added!")

        return list1,list2
    
    def view(list1):
        print("NAME | CONTACT NUMBER | E-MAIL | ADDRESS")
        for i in range (len(list1)):
            print(list1[i])

    def search(list1,list2):
        l=1
        u=len(list1)

        sear=int(input("Do you want to search the contact by\n1. Name \n2.Number\n"))

        if sear==1:
            n=(input("Enter the name you want to search : "))
            for i in range(len(list1)):
                a=list1[i][0]
                for j in range(len(n)):
                    if n[j]==a[j]:
                        c=list1[i]
            print(c)

        elif sear==2:
            c=input("Enter the number you want to search : ")
            for i in range(len(list1)):
                if c==list2[1]:
                    print(list1[i])

    def update(list1):
        ser=int(input("Enter the serial no. of the contact you want to update : "))

        print("What do you want to update?")
        print("1. Name\n 2.Contact number\n 3.E-mail\n 4.Address\n")
        ch=int(input())
        if(ch==1):
            updated_name=input("Enter the updated name : ")
            list1[ser-1][0]=updated_name
        if(ch==2):
            updated_contact=input("Enter the updated contact number : ")
            list1[ser-1][0]=updated_contact
        if(ch==3):
            updated_email=input("Enter the updated E-mail : ")
            list1[ser-1][0]=updated_email
        if(ch==4):
            updated_address=input("Enter the updated Address : ")
            list1[ser-1][0]=updated_address

        print("Contact updated succcessfully!")

    def delete(list1):
        delt=int(input("Enter the serial no. of the contact you want to delete"))
        print("\nContact deleted succcessfully!")
        
        if delt==1:
            for i in range(1,len(list1)):
                print(list1[i])
        elif delt==len(list1):
            for i in range(1,len(list1)):
                print(list1[i])
        else:
            for i in range(delt,len(list1)):
                list1[i]=list1[i+1]

            for i in range(len(list1)):
                print(list1[i])

    print("1. Add contact")
    print("2. View contactlist")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")

    choice=int(input("\nEnter your choice : "))
    if choice==1:
        add()
    elif choice==2:
        view(list1)
    elif choice==3:
        search(list1,list2)
    elif choice==4:
        update(list1)
    elif choice==5:
        delete(list1)
    else:
        print("INVALID CHOICE!")


    repeat=input("\nDo you want to perform another opertaion? (y/n) : ")
    if repeat=='y':
        continue
    else:
        break
    
    