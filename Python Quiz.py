print("Welcome to python quiz game")
score=0
print("Which organization maintains and owns the copyright of the “Laws of Cricket”, a code for the cricket game?")
print("1. International Cricket Council\n2. Marylebone Cricket Club\n3. Yorkshire Cricket Club\nD] Mason Cricket Club")
ans=int(input("Your choice-enter option number : "))
if(ans==2):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("How many significant subsidiaries of Google parent company Alphabet have?")
print("1.1\n2.2\n3.3\n4.4")
ans=int(input("Your choice-enter option number : "))
if(ans==4):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Which of the following sons of Dhritarashtra survived after the Kurushetra war?")
print("1.Yuyutsu\n2.Duryodhana\n3.Vikarna\n4.Dushasana")
ans=int(input("Your choice-enter option number : "))
if(ans==1):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Your score is : ",score," out of 3")