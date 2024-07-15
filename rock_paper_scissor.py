from tkinter import *
from PIL import Image, ImageTk
from random import randint
import time
from tkinter import messagebox

# main window
root = Tk()
root.geometry("1080x500")
root.title("Rock Scissor Paper")
root.configure(background="#0ABDE3")

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.jpeg"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.jpeg"))
# pimg = Image.open("paper-user.jpeg")
# paimg=pimg.resize(500,500)
# paper_img=ImageTk.PhotoImage(paimg)
scissor_img = ImageTk.PhotoImage(Image.open("scissor-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.jpeg"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.jpeg"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.jpeg"))
water_img = ImageTk.PhotoImage(Image.open("water.jpeg"))
img=Image.open("life.png")
rimg=img.resize((50, 50))
life_img = ImageTk.PhotoImage(rimg)

# insert picture
user_label = Label(root, image=scissor_img, bg="#0ABDE3")
comp_label = Label(root, image=scissor_img_comp, bg="#0ABDE3")
life_label = Label(root, image=life_img, bg="#0ABDE3", width=50, height=50)
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)
#life_label.grid(row=2, column=4)


# scores
playerScore = Label(root, text=0, font=100, bg="#0ABDE3", fg="#154360")
computerScore = Label(root, text=0, font=100, bg="#0ABDE3", fg="#154360")
lifeScore = Label(root, text=0, font=100, bg="#0ABDE3", fg="#154360")
lifecount = Label(root, text=0, font=100, bg="#0ABDE3", fg="#154360")
level = Label(root, text=1, font=100, bg="#0ABDE3", fg="#154360")
turn = Label(root, text=0, font=100, bg="#0ABDE3", fg="#154360")
#turn.grid(row=2,column=2)
timeExpired = Label(root, text=0)
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)
#lifeScore.grid(row=3, column=4)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="#0ABDE3", fg="#154360")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#0ABDE3", fg="#154360")
level_indicator = Label(root, font=50, bg="#0ABDE3", fg="#154360")
turn_indicator = Label(root, font=50, bg="#0ABDE3", fg="#154360")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#0ABDE3", fg="#154360")
msg.grid(row=3, column=2)
msg2 = Label(root, font=50, bg="#0ABDE3", fg="#154360")

#isTimeExpired
def getInput():
    timeExpired["text"]=str(1)
    

# update message

def updateMessage(x):
    msg['text'] = x
def updateMessage2(x):
    msg2['text'] = x
    msg2.grid(row=4, column=2)

#Time
secondString = StringVar()
secondString.set("10")
secondTextbox = Entry(root, width=3, font=("Calibri", 20, ""),bg="#0ABDE3", textvariable=secondString)
secondTextbox.grid(row=1,column=2)
# update life score

def updateLifeScore():
    score = int(lifeScore["text"])
    score += 1  
    lifeScore["text"] = str(score)
    if score==2:
        sc = int(lifecount["text"])
        sc += 1
        lifecount["text"] = str(sc)
        life_label.grid(row=2, column=4)
        lifecount.grid(row=3, column=4)
        water.grid(row=5, column=4)
        lifeScore["text"] = str(0)
        
        
        
# reset life score
def resetLifeScore():
    lifeScore["text"] = str(0)

# remove life
def removeLife():
    lifecount["text"] = str(0)
    life_label.grid_remove()
    lifecount.grid_remove()
    water.grid_remove()
    
# reduce life score
def reduceLife():
    sc = int(lifecount["text"])
    if sc>1:
        sc -= 1  
        lifecount["text"] = str(sc)
    else:
       removeLife()

def runTimer():
    # try:
    #     totalSeconds = int(secondString.get())
    # except:
    #     print("Error")
    totalSeconds = int(secondString.get())
    while(totalSeconds > -1):
        tx=int(timeExpired["text"])
        if tx==1:
            timeExpired["text"]=str(0)
            break
        secondString.set("{0:2d}".format(totalSeconds))

        ### Update the interface
        root.update()
        time.sleep(1)
        ### Let the user know if the timer has expired
        if(totalSeconds == 0):
            #messagebox.showinfo("", "Your time has expired!")
            # updateMessage("Time expired")
            # updateMessage2("Game over")
            level["text"]=str(1)
            updateMessage("Game over!Your time has expired!")
            turn["text"]=str(0)
            #startTurn(0)
            # time.sleep(1)
            # root.destroy()
            # time.sleep(5)
            # root.destroy()
            updateMessage2("Try again from the first level")
            removeLife()
            #getInput()
            level["text"]=str(1)
            playerScore["text"]=str(0)
            computerScore["text"]=str(0)
            secondString.set("{0:2d}".format(10))
            resetLifeScore()
            startLevel(1)
            runTimer()
            # water.grid_remove()
            # rock.grid_remove()
            # paper.grid_remove()
            # scissor.grid_remove()
        totalSeconds -= 1


# start level
def startLevel(lb):
    level_indicator['text']="Level "+str(lb)
    level_indicator.grid(row=0, column=2)
    secondString.set("{0:2d}".format(11-lb))
    
startLevel(1)
# update user score

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
    
# update computer score

def updateCompScore():
    score = int(computerScore["text"])
    score += 1  
    computerScore["text"] = str(score)


        
# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!")
        resetLifeScore()
    elif player == "water":
        if computer == "paper":
            updateMessage("You Win")
            updateUserScore()
            reduceLife()
        else:
            updateMessage("Its a tie!")
            reduceLife()
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
            resetLifeScore()
        else:
            updateMessage("You Win")
            updateUserScore()
            updateLifeScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
            resetLifeScore()
        else:
            updateMessage("You Win")
            updateUserScore()
            updateLifeScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
            resetLifeScore()
        else:
            updateMessage("You Win")
            updateUserScore()
            updateLifeScore()

    else:
        pass
    


# update choices
choices = ["rock", "paper", "scissor"]
def updateChoice(x):
    getInput()
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    elif x == "water":
        user_label.configure(image=water_img)
    else:
        user_label.configure(image=scissor_img)
    
    checkWin(x, compChoice)
    t=int(turn["text"])
    lv=int(level["text"])
    t=t+1
    turn["text"]=str(t)
    if t==5:
        turn["text"]=str(0)
        lv=int(level["text"])
        lv += 1
        level["text"]=str(lv)
        ps=int(playerScore["text"])
        cs=int(computerScore["text"])
        resetLifeScore()
        if ps<cs:
            #time.sleep(1)
            updateMessage("Game over!You loose the level!")
            turn["text"]=str(0)
            # time.sleep(5)
            # root.destroy()
            updateMessage2("Try again from the first level")
            removeLife()
            getInput()
            level["text"]=str(1)
            playerScore["text"]=str(0)
            computerScore["text"]=str(0)
            secondString.set("{0:2d}".format(10))
            startLevel(1)
            runTimer()
            # water.grid_remove()
            # rock.grid_remove()
            # paper.grid_remove()
            # scissor.grid_remove()
        else:
            if lv==11:             
                updateMessage("You won the Game!")
                updateMessage2("Start from the first level")
                removeLife()
                getInput()
                level["text"]=str(1)
                playerScore["text"]=str(0)
                computerScore["text"]=str(0)
                secondString.set("{0:2d}".format(10))
                startLevel(1)
                runTimer()
            else:
                #time.sleep(2)
                updateMessage("You won the level!")
                updateMessage2("Welcome to the next level")
                playerScore["text"]=str(0)
                computerScore["text"]=str(0)
                startLevel(lv)
    else:
        updateMessage2("")
    secondString.set("{0:2d}".format(11-lv))
    timeExpired["text"]=str(0)
    runTimer()

# buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock"))
rock.grid(row=5,column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper"))
paper.grid(row=5, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#9b59b6", fg="white", command=lambda: updateChoice("scissor"))
scissor.grid(row=5, column=3)
water = Button(root, width=20, height=2, text="WATER",
                 bg="green", fg="white", command=lambda: updateChoice("water"))
runTimer()
root.mainloop()