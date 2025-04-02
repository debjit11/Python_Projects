from PyDictionary import PyDictionary

dictionary = PyDictionary()
while True:
    word = input("enter your word: ")
    
    if word == "":
        break
    print(dictionary.meaning(word))
#-----------------------------------------------------------------
def main():
    words = {
        "human":"insan",
        "girl":"ladki",
        "boy":"ladka"
    }
    
    word = input("Enter the word: ")
    
    if word in words:
        print(f"the meaning of {word} is: {words[word]}")
        
main()
