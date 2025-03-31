Quize = {
    "question1": {
        "question":"What is the capital odf India?",
        "answer":"Delhi"
        
    },
    "question2": {
        "question":"What is the capital of West Bangal?",
        "answer":"Kolkata"
        
    },
    "question3": {
        "question":"Who is the PM imn India?",
        "answer":"Modi"
        
    },
    "question4": {
        "question":"Who is the founder of OpenAi?",
        "answer":"Altman"
        
    },
    "question5": {
        "question":"Who is Debjit Das?",
        "answer":"Coder"
        
    },
    
   
}

score = 0

for key ,value in Quize.items(): 
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value["answer"].lower():
        print("Currect:)")
        score = score + 1
        print("Your score is: " + str(score))
        
    else:
        print("Wrong!!")
        print("The answer is: " + value["answer"])
        print("Your score is: " + str(score))
        
        
print(f"You got {str(score)} out of 5 question currectly:)")
print(f"Your persentage is: {str(int(score/5*100))} % ")


        
    