from caesar import caesar

# your code is here!
START_1 = True
while START_1:
    operation = input("type 'e' to encrypt, type 'd' to decrypt: ")
    if operation == "g":
        print("invalid option")
        break
    text = input("type your text: ")
    shift = int(input("type the shift number: "))
    if operation == "e":
        print(f"your e message is {caesar(text, shift, operation)}")
    
        decision = input("do you want to continue? (y/n): ")
        START_1 = False
        if decision == "y":
            START_1 = True
    elif operation == "d":
        print(f"your d message is {caesar(text, shift, operation)}")
        decision = input("do you want to continue? (y/n): ")
        START_1 = False
        if decision == "y":
            START_1 = True
    



    



