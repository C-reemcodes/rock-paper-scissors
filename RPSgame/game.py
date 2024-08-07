import tkinter
import random
import tkinter.messagebox as mb
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title('Game')
root.geometry('695x425')

player_score = 0
computer_score = 0
rounds_played = 0
wins=0

def score(user_choice):
    global rounds_played
    global player_score
    global computer_score
    global wins
    chances = ('rock', 'paper', 'scissors')
    computer_choice = random.choice(chances)
    
    if user_choice == computer_choice:
        pass
    elif user_choice == 'rock' and computer_choice == 'scissors':
        player_score = player_score +1
        wins+=1
    elif user_choice == 'paper' and computer_choice == 'rock':
        player_score = player_score +1
        wins+=1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        player_score = player_score +1
        wins+=1
    else:
        computer_score = computer_score +1
        wins-=1
        
    rounds_played = rounds_played + 1

    pscore.config(text=f'Your score: {player_score}')
    cscore.config(text=f'Computer score: {computer_score}')
    rounds_label.config(text=f'rounds left: {3-rounds_played}')
    player_image_handler(user_choice)
    computer_image_handler(computer_choice)

    if rounds_played % 3 == 0:
        player_score = computer_score = rounds_played = 0
        pscore.config(text='Your score: 0')
        cscore.config(text='Computer score: 0')
        rounds_label.config(text='rounds left : 3')
        player_image_handler(bg_image)
        computer_image_handler(bg_image)
        call()


def call():
    string = ''
    if wins < 0:
        string = 'You lost.'
    elif wins == 0:
        string = "It's a tie."
    else:
        string = 'You won!'
    play = mb.askquestion('Exit Application', f'{string}\nDo you want to play again?')
    if play == 'yes':
        mb.showinfo('Return', "Let's play another round!")
    else:
        root.destroy()

def player_image_handler(player_choice):
    if player_choice == 'rock':
        player_image.config(image=rock_image)
    elif player_choice == 'paper':
        player_image.config(image=paper_image)
    elif player_choice == 'scissors':
        player_image.config(image=scissors_image)
    else:
        player_image.config(image=bg_image)

def computer_image_handler(computer_choice):
    if computer_choice == 'rock':
        computer_image.config(image=rock_image)
    elif computer_choice == 'paper':
        computer_image.config(image=paper_image)
    elif computer_choice == 'scissors':
        computer_image.config(image=scissors_image)
    else:
        computer_image.config(image=bg_image)

frame1= tkinter.Frame(root, height=450, width= 600, bg='lightskyblue3')
frame1.grid(row=0, column=0, pady=1, padx=0)

bg_image = tkinter.PhotoImage(file='images/background.png')

og_rock= Image.open('images/rock.png')
resized_rock = og_rock.resize((200,200))
rock_image = ImageTk.PhotoImage(resized_rock)


og_paper = Image.open('images/paper.png')
resized_paper =og_paper.resize((200,200))
paper_image = ImageTk.PhotoImage(resized_paper)

og_scissors = Image.open('images/scissors.png')
resized_scissors = og_scissors.resize((200,200))
scissors_image = ImageTk.PhotoImage(resized_scissors)

player_image = tkinter.Label(frame1, image=bg_image, relief='sunken')
player_image.grid(row=4, pady=10, padx=10, sticky=tkinter.W)
computer_image = tkinter.Label(frame1, image=bg_image, relief='sunken')
computer_image.grid(row=4, pady=10, padx=10, sticky=tkinter.E)


topbar = tkinter.Label(frame1, text='ROCK PAPER SCISSORS', bg='lightskyblue3',font=('Helvetica',18,'bold'))
topbar.grid(row=1, sticky=tkinter.N,pady=10, padx=200)

label0= tkinter.Label(frame1, text="LET'S PLAY", font=('Helvetica',16,'bold'), bg='lightskyblue3')
label0.grid(row=0, sticky=tkinter.N)

pscore = tkinter.Label(frame1, text='Your score: 0',font=('Helvetica',12,'bold'),fg='green', bg='lightskyblue3')
pscore.grid(row=2, sticky=tkinter.W, pady=10)

cscore = tkinter.Label(frame1, text='Computer score: 0',font=('Helvetica',12,'bold'),fg='red', bg='lightskyblue3')
cscore.grid(row=2, sticky=tkinter.E, pady=10)

rounds_label = tkinter.Label(frame1, text='rounds left : 3',font=('Helvetica',12,'bold'),fg='blue', bg='lightskyblue3')
rounds_label.grid(row=2, sticky=tkinter.N)


rockbutton = tkinter.Button(frame1, text='rock', command = lambda: score('rock'), bg='gray',width=10, font=('Helvetica',10,'bold'))
rockbutton.grid(row=3, pady=10, padx=10, sticky=tkinter.W)

paperbutton = tkinter.Button(frame1, text='paper', command= lambda: score('paper'),bg='snow',width=10, font=('Helvetica',10,'bold'))
paperbutton.grid(row=3, pady=10, sticky=tkinter.N)

scissorsbutton = tkinter.Button(frame1, text='scissors', command= lambda: score('scissors'),bg='darkorange', width=10, font=('Helvetica',10,'bold'))
scissorsbutton.grid(row=3, pady=10, padx=10, sticky=tkinter.E)


root.mainloop()