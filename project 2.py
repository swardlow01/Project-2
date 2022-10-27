#sarahwardlow
import time
import random
out = []
element = ""

def prt_list(list):
    for x in list:
        print(x, flush=True)
        if len(x) < 70:
            time.sleep(3)
        else:
            time.sleep(4)

def prt_single(sentence, num):
    print(sentence, flush=True)
    time.sleep(num)

#introduction
def intro():
    global element
    element = random.choice(["Math", "English", "Science", "History"])
    story = [
        "Hi! My name is Alex!",
        "I have just started my first year of college.", f"I need help finding my {element} class.",
        "I have just stepped out of my dorm's lobby.\n"
    ]
    prt_list(story)

#firstchoice
def choose_1():
    act = [
    "Enter 1 to go left outside the dorm.",
    "Enter 2 to go right outside the dorm.\n"
    ]
    prt_list(act)
    response = str(input("Which way should I go?\n"))
    return response
#ifleft
def go_left():
    choice1 = [
        "I start to walk left.",
        "As I start walking, I notice I am heading the route to the dining hall.\n"
    ]
    choice2 = [
        "I think I'm going to go left.",
        "I'm already going to be late, I might as well have a nice breakfast.\n"]
    if "message" in out:
        prt_list(choice2)
    else:
        prt_list(choice1)
    response1 = str(input("Would you like to (3) stop and have breakfast or (4) go to class?\n"))
    return response1


#ifalexgoesleft
def breakfast():
    response1 = go_left()
    if response1 == "3":
        choice3 = [
        "I begin my journey to the dining hall for a nice breakfast.",
        "As I make my way inside the dining hall, I see one of my friends from my first class.",
        "I sit down and ask her if she is planning on going to class.",
        "She says 'No, I got an email this morning it was cancelled.'",
        "'That would've been nice to know!' I respond.",
        "Guess I should start checking my email!",
        "Now I can enjoy a nice breakfast!\n"
        ]
        choice4 = [
        "I begin my journey to the dining hall for a nice breakfast.",
        "As I make my way inside the dining hall, I see one of my friends from my first class.",
        "I swipe my student ID card, and then make my way to her table.",
        "I sit down and ask her if she is planning on going to class.",
        f"I say 'no', and I tell her that our {element} class has been cancelled today.",
        "She told me she had already seen the email!",
        "Now I can enjoy a nice breakfast!\n"]
        if "message" in out:
            prt_list(choice4)
            play_again()
        else:
            prt_list(choice3)
            play_again()
    elif response1 == "4":
        choice6 = [
        "I am sprinting in the opposite direction, trying to make up for lost time.",
        "I finally make it inside the building, and my class is on the third floor.",
        "I climb up all three flights of stairs.",
        "I finally arrive at my classroom and take a seat.",
        "I look up at the board, where there is a message.",
        "The message reads, 'I sent an email. Class is cancelled. See you tomorrow.'\n",
        "I make my way back to my dorm.\n"
        ]
        if "message" in out:
            prt_single("I know class is cancelled, why do we wanna go back? Try again!", 2)
        else:
            prt_list(choice6)
            out.append("message")
            choose_1
    else:
        prt_single("Make a decision, quick!", 2)
        breakfast()

#ifalexgoesright
def go_right():
    prt_single("I think I will go right.\n", 2)
    choice5 = [
    "That was the correct choice!",
    f"I finally make it inside the {element} building.",
    "My class is on the third floor.",
    "I climb up all three flights of stairs.",
    "I finally arrive at my classroom.",
    "I take a seat and look up at the board, where there is a message.",
    "The message reads, 'I sent an email. Class is cancelled. See you tomorrow.'",
    "I make my way back to my dorm.\n"
    ]
    if "message" in out:
        prt_single(
        f"I already know that my {element} class is cancelled, why go that direction again? Try again!", 1
        )
        prt_single("I walk back out of the empty classroom.\n", 2)
    else:
        prt_list(choice5)
        out.append("message")


def game():
    response = choose_1()
    if response == "1":
        breakfast()
    elif response == "2":
        go_right()
    else:
        game()
    game()


def word_game():
    intro()
    game()
    play_again()

def play_again():
    global out
    prt_single("Would you like to play again?", 2)
    response2 = str(input("Please enter 'yes' for yes and 'no' for no. \n").lower())
    if response2 == "yes":
        out = []
        word_game()
    elif response2 == "no":
        exit()
    else:
        play_again()


word_game()
