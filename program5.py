def pro():
    a1= int(input("Enter the first number:"))
    a2=int(input("Enter the seond number:"))
    choice = input("Enter the arthematic choice (a) for addition\n (s) for subustraction \n (m) for multiplication \n (d) for division:")
    if choice == 'a':
        print(f"Addition {a1+a2}")
    elif choice == 's':
        print(f"Substraction {a1-a2}")
    elif choice == 'm':
        print(f"Multiplication {a1*a2}")
    elif choice == 'd':
        if a2 == 0:
            print("Zero cant be divided")
        print(f"Division {a1/a2}")
    else :
        print("The invalid choice!!!!")

a = pro()
print(a)