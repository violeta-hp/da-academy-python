import random 
number=[]
attemps=0
def Make_num():
	for i in range(4):
	    x= random.randrange(0,9)
	    number.append(x)
	if len(number)> len(set(number)):
            number.clear()
            Make_num()

def Play_game():
    global attemps
    attemps += 1
    caliente= 0
    frio = 0
    print(number)
    choice = input('Please enter a 4 digit number')
    guess= [] #local array because we want to make it like the array above in num 
    for i in range (4):
        guess.append(int(choice[i]))
    for i in range (4):
        for j in range(4):
            if(guess[i]== number[j]):
                for x in range(4): 
                    if(guess[x]== number[x]:
                        frio += 1
     print('Frio:',frio)
     print('Caliente:',caliente)
     if(frio==4):
           print('You won after', attempts, 'attempts!')
     if (frio!=4):
   	 PlayGame()

print(number)