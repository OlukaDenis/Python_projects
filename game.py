import random
import simplegui


COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""

def choice_to_number(choice):
    game_dict = {"Rock": 0, "Paper": 1, "Scissors": 2}
    return game_dict[choice]

def number_to_choice(number):
    game_dict = {0: "Rock", 1: "Paper", 2: "Scissors"}
    return game_dict[number]

def random_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])
def choice_result(human_choice, computer_choice):
    global COMPUTER_SCORE
    global HUMAN_SCORE
    
    human_number = choice_to_number(hunan_choice)
    computer_number = choice_to_number(computer_choice)

    if(human_number - computer_number) % 3 == 1:
        COMPUTER_SCORE += 1
        print("Computer wins")
    elif (human_number == computer_number):
        print("Draw")
    else:
        HUMAN_SCORE += 1
        print("Human wins")

#Code fo GUI
#Handler for mouse click on rock
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = "Rock"
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

#Handler for mouse click on paper
def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = "Paper"
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

#Handler for mouse click on scissors
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = "Scissors"
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
        
#Handler to draw on canvas
def draw(canvas):
    try:
        #Draw choices
        canvas.draw_text("You: " +human_choice, [10,40], 48, "Green")
        canvas.draw_text("Computer: " +computer_choice, [10,80], 48, "Red")

        #Draw scores
        canvas.draw_text("Human Score: " +str(HUMAN_SCORE), [10,150], 30, "Green")
        canvas.draw_text("Computer Score: " +str(COMPUTER_SCORE), [10,190], 30, "Red")
    except TypeError:
        pass

#Create a frame and assign callbacks to event handlers
def play_game():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    #start frame animation
    frame.start()

play_game()









        
