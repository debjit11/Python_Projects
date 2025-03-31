def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")
    
def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")
    
def mul(a,b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")
    
def div(a,b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")
    
    
    
    
while True:
        print("A.Addition")
        print("S.Subtraction")
        print("M.Multiplication")
        print("D.Divition")
        
        
        choice = input(" what you want to chose: ")
        if choice == "a" or choice == "A":
            print("Addition")
            
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            
            add(a, b)
        elif choice == "s" or choice == "S":
            print("Subtraction")
            
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            
            sub(a, b)
        elif choice == "m" or choice == "M":
            print("Multiplication")
            
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            
            mul(a, b)
        elif choice == "d" or choice == "D":
            print("Divition")
            
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            
            div(a, b)
        
        elif choice == "e" or choice == "E":
            print("Exit the progam")
            
        else:
            print("Only use number")
            break
