from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ")

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file = open("key.key","rb")  #rb = Opens the key file in binary read mode
    key = file.read()
    file.close()
    return key
key = load_key() + master_pwd.encode()
fer = Fernet(key)
def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:",user,"| Password:",fer.decrypt(passw.encode()).decode())

def add():
    name = input("Enter Account Name: ")
    pwd = input(" Enter Password: ")
    
    with open("password.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")
    print("Password add successfully") 
while True:
    mode = input("Would you like to add password or view existing ones(view/add), press p to quit? ").lower()
    if mode == "p":
        break
    elif mode == "view":
        view()
    elif mode == "add" or "yes" :
        add()
    else:
        print("Invalid mode.")
        continue
        

