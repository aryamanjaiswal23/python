from questions import Questions

prompt=[
    "which one is a color: \n a. red \n b. wer \n c. wsdf",
    "which one is an actor: \n a. you\n b.you \nc. not you",
    "which one is a cat sound:\n a. purr\n b. meow\n c. bark"
]
qu=[
    Questions(prompt[0],"a"),Questions(prompt[1],"c"),Questions(prompt[2],"c")
]
def run_test(questions):
    score=0
    for q in questions:
        ans=input(q.prompt +"\nYour answer:")
        if ans==q.answer: score+=1

    print("your score:" +str(score) +"/ "+str(len(questions)))
    
run_test(qu)