#a few questions with 4 options and increment the score for eah answer being right have a game reset and end buttons.

#this code is not suitable for tkinter(refer gpt)
import tkinter
from tkinter import Tk
from tkinter import *
from tkinter.font import families


correct_answers=0
questions=10

def quiz():
    global correct_answers
    global questions
    label_result.config("Question 1:\n")
    print("What planet is known as the Red Planet?")
    mars=1
    jupyter=2
    pluto=3
    venus=4
    user_choice=input("Enter\n 1. for mars,\n 2. for jupiter \n3.for pluto and \n4. for venus")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==1:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {mars}")

    print("Ouestion 2:\n")
    print(" What is the process by which plants make their food using sunlight called?")
    chrolopyhll=1
    fertiliser=2
    botany=3
    photosynthesis=4
    user_choice=input("Enter\n 1. for chrolophyll,\n 2. for fertiliser \n3.for botany and \n4. for photosysnthesis")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==4:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {photosynthesis}")

    print("Ouestion3:\n")
    print("What gas do humans exhale that plants use for photosynthesis?")
    sulphurdioxide=1
    carbondioxide=2
    nitrogen=3
    sulphur=4
    user_choice=input("Enter\n 1. for suplhurdioxide,\n 2. for carbondioxide \n3.for nitrogen and \n4. for sulphur")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==2:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {carbondioxide}")


    print("Ouestion4:\n")
    print("What is the largest organ in the human body?")
    liver=1
    kidney=2
    skin=3
    intestine=4
    user_choice=input("Enter\n 1. for liver,\n 2. for kidney \n3.for skin and \n4. for intestine")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==3:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {skin}")

    print("Ouestion5:\n")
    print("Who was the first President of the United States?")
    GeorgeWashington=1
    BarackObama=2
    RonaldReagan=3
    JimmyCarter=4
    user_choice=input("Enter\n 1. for GeorgeWashington,\n 2. for BarackObama \n3.for RonaldReagan and \n4. for JimmyCarter")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==1:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {GeorgeWashington}")

    print("Ouestion6:\n")
    print("What is the largest ocean on Earth?")
    PacificOcean=1
    AtlanticOcean=2
    IndianOcean=3
    ArcticOcean=4
    user_choice=input("Enter\n 1. for Pacific-Ocean,\n 2. for Atlantic-Ocean \n3.for Indian-Ocean and \n4. for Arctic-Ocean")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==1:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {PacificOcean}")

    print("Ouestion7:\n")
    print("What is the capital city of France?")
    Moscow=1
    London=2
    Paris=3
    Berlin=4
    user_choice=input("Enter\n 1. Moscow,\n 2. for London \n3.for Paris and \n4. for Berlin")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==3:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {Paris}")

    print("Ouestion8:\n")
    print("What is the longest river in the world?")
    amazonriver=1
    nile=2
    mississipi=3
    niger=4
    user_choice=input("Enter\n 1. amazon-river,\n 2. for nile \n3.for mississipi and \n4. for niger")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==2:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {nile}")

    print("Ouestion10:\n")
    print("What is the tallest mountain in the world?")
    Rakaposhi=1
    Mounteverest=2
    Gonggar=3
    BroadPeak=4
    user_choice=input("Enter\n 1. Rakaposhi,\n 2. for Mount-everest \n3.for Makalu and \n4. for Broad-Peak")
    users_choice=int(user_choice)
    print(users_choice)
    if users_choice==2:
        print("Your answwer was right")
        correct_answers+=1
    else:
        print(f"You chose the wrong option, the correct answer was {Mounteverest}")
        

    print(f"You got {correct_answers} answers right out of  {questions}.")

def restart_game():
    global correct_answers, questions
    correct_answers=0
    questions=0
    label_score.config(text=f"Score-->{correct_answers}")
    label_result.config(text="Game Reset! Let's play again")
    entry_answer.delete(0, 'end')

root=Tk()
root.title("QUIZ GAME!")
root.attributes("-fullscreen")
root.configure(bg="navy")

label_title=Label(root, text="QUIZ GAME!")
label_result=Label(root, font=("Beige"), pady=30)
label_score=Label(root, text="Correct Answers: ", font=("Comic Sans MS", 14), pady=20, bg="beige")
entry_answer=Entry(root, font=("helvetica", 16), width=10, justify="center")
    
button_reset=Button(root, text="Reset Game", font=("#D3D3D3", 14), justify="center", command=restart_game)

button_exit=Button(root, text="Exit Game", font=("helvetica, 14"), justify="center",command=root.destroy)

label_title.pack()
label_result.pack(pady=20)
label_score.pack(pady=10)
entry_answer.pack(padx=40, pady=40)
# button_guess.pack(pady=10)
button_reset.pack(side="left", padx=20, pady=20)
button_exit.pack(side="right", padx=20, pady=20)

root,mainloop()











