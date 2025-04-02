def main():
    print("This is Doller to Ruppe converter..")
    print("")
    
    dollars = eval(input("Enter the Doller amount: "))
    
    ruppe = convert_to_ruppe(dollars)
    
    print(f"This is {ruppe} ruppe")
    
convert_to_ruppe = lambda dollars: dollars*85.66

main()
 
 