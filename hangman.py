#hangman game

import random

def random_word():
    words=["python","java","cpp","html","ruby","react"]
    return random.choice(words)       #random.choice() is used here to give a element

def display(n):      # To display the hangman diagram
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           
           
           
           
           
        """
    ]
    return stages[n]

def printlst(lst):                    #To print all element of the list seperately insted of printing as list
    for i in range(len(lst)):
        print(lst[i], end=" ")
    print("\n")



def game():         #Main function
    word=random_word()  #Generate random word from the list
    size=len(word)
    res_list=["_"]*size    #initializing the resultant list
    chance=6   #life
    print(f"---You have {chance} lives left---")
    while(chance>0):
        print(display(chance))
        printlst(res_list)
        user_ip=input("Guess a Character: ").lower()    #to avoid error we are turning input to lower case
        if(user_ip not in word):   #if the input is not in word then user has guessed incorrectly so life is lost
            chance-=1  
            print("Wrong!!!... the letter is not present in the word")
            print(f"---You have {chance} lives left---")
        else:
            print("Correct!!!... You have chosen correct letter")
            print(f"---you have {chance} lives left---")
            pos=word.index(user_ip)    #To find the position of the user guessed in the random word
            res_list[pos]=user_ip      #Changing the already present _ to the letter correctly guessed by user in respective index
            if('_' in res_list):       #If _ present then still he hasn't completed
                ct=res_list.count('_')
                print(f"Still {ct} more to go....")
            else:                      #If _ not present then he has completed his guessing part
                print("...............Congratulations...............")
                print("!!!  You have correctly guessed the word  !!!")
                break
    else:     #If he has lost the game else loop runs as it doesn't got terminated by break statement so it means user has lost
        print("!!!  You have lost the game. Better luck next time  !!!")
        print(display(chance))
                

                
#main
print("-------------HANGMAN GAME-------------------")
game()