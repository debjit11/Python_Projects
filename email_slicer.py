def main():
    print(" Welcome To Email Slicer...")
    print("")
    
    email_inp = input(" Enter your email: ")
    
    (username , domain) = email_inp.split("@")
    (domain,extension) = domain.split(".")
    
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extention: {extension}")
    
while True:
    main()