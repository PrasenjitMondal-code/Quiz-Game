



print(" \n                                          Well Come TO Quiz Game \n ")




name=input("Enter Your Name : ")
age=int(input("\nEnter Your Age : "))
gender=input("\nGender (Female/Male) :  ").lower()



why=input("\nWhy would you like to join this quiz ? : ")





import random


choises=["\okhe! that's a common resson","achha...bujhlam","hmm...I Got Your Point but it's quite abnormal. is not it ", "Okhe! Okhe! i undestand", "Really... It's Ture ","Whatever never mind"]

computer= random.choice(choises) 

print(computer +" "+ name )
print("\nLet's Start The Quiz\n")
score =0




while True:


    quiz_1=input("\nWho Is The Father Of Computer Science ? :  ")


    if quiz_1!=("charles babbage").lower():
        print("Incorrect")

    else:
        print("Correct")
        score +=1




    quiz_2=input("\nFull Form Of AI ? : ")

    if quiz_2!=("Artificial Intelligence").lower():
        print("Incorrect")
    else:
        print("Correct")
        score +=1



    quiz_4=input("\nScientific Name Of Computer  ? :  ")

    if quiz_4!=("sillico sapiens").lower():
        print("Incorrect")
    else:
        print("Correct")
        score +=2




    quiz_5=input("\nIn Which type of computer data are represented as discrete signsl  ? :  ")

    if quiz_5!=("digital computer").lower():
        print("Incorrect")
    else:
        print("Correct")
        score +=1

    print("\nYou Have Got "+ str(score) + " Question Correct out of 5")

    print("\nYou Have Got "+str((score/6)*100)+ " % " +" out of 100 % ")



    play_again=input("\nDo You Want To Play Again : ")

    if play_again!=("yes").lower():
        break

print("\nGood Bye! Have a nice day")
        