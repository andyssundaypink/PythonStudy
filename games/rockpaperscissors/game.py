import random
import pygame
from pygame.locals import *
from button import Button, ButtonText

# initialize pygame
pygame.init()
# Define the dimensions of screen object
screen = pygame.display.set_mode((680, 480))
# Give the screen a caption
pygame.display.set_caption("Rock Paper Scissors Game")

# Define the font and text colours
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.SysFont('Arial', 32)

# Instantiate all the button objects
rock_button = Button("resources/rock.png", "rock", (50, 50), (200, 100))
paper_button = Button("resources/paper.png", "paper", (50,50), (300, 100))
scissors_button = Button("resources/scissors.png", "scissors",  (50,50), (400, 100))
reset_button = ButtonText("Reset", (380, 350), "Arial", 32, green, blue)
buttons = [rock_button, paper_button, scissors_button, reset_button]

# Initializes all images needed and scale it
rock = pygame.image.load("resources/rock.png")
rock = pygame.transform.scale(rock, (50, 50))
paper = pygame.image.load("resources/paper.png")
paper = pygame.transform.scale(paper, (50, 50))
scissors = pygame.image.load("resources/scissors.png")
scissors = pygame.transform.scale(scissors, (50, 50))

# Initializes all texts needed
text = font.render('Please choose Rock, Paper, or Scissors', 0, green)
text1 = font.render("You", True, green, blue)
text2 = font.render("VS", True, green, blue)
text3 = font.render("Computer", True, green, blue)

choices = ["rock", "paper", "scissors"]
computer = ""
player_score = 0
cpu_score = 0
player = ""
cpu_changed = False


def show_chosen_image():
    if player == "rock":
        screen.blit(rock, (220, 280))
    elif player == "paper":
        screen.blit(paper, (220, 280))
    elif player == "scissors":
        screen.blit(scissors, (220, 280))
    if computer == "rock":
        screen.blit(rock, (400, 280))
    elif computer == "paper":
        screen.blit(paper, (400, 280))
    elif computer == "scissors":
        screen.blit(scissors, (400, 280))


def show_score():
    player_score_text = font.render(str(player_score), True, green, blue)
    screen.blit(player_score_text, (220, 220))
    cpu_score_text = font.render(str(cpu_score), True, green, blue)
    screen.blit(cpu_score_text, (420, 220))


# Our game loop
while 1:
    # Clear the screen before drawing it again
    screen.fill(0)
    # Define where the buttons and texts will appear on the screen
    # Use blit to draw them on the screen surface
    for button in buttons:
        button.draw(screen)
    screen.blit(text, (50, 50))
    screen.blit(text1, (200, 180))
    screen.blit(text2, (300, 180))
    screen.blit(text3, (380, 180))

    show_chosen_image()
    show_score()

    # Update the display using flip
    pygame.display.flip()

    # for loop through the event queue
    for event in pygame.event.get():
        # register the event to buttons
        for button in buttons:
            button.event_handler(event)

        if getattr(rock_button, 'chosen'):
            player = 'rock'
            cpu_changed = True
        elif getattr(paper_button, 'chosen'):
            player = 'paper'
            cpu_changed = True
        elif getattr(scissors_button, 'chosen'):
            player = 'scissors'
            cpu_changed = True
        elif getattr(reset_button, 'chosen'):
            player = ''
            computer = ''
            cpu_changed = False
            player_score = 0
            cpu_score = 0
        else:
            cpu_changed = False

        # Check for the Quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and cpu_changed:
                computer = random.choice(choices)
                if player == computer:
                    player_state = "Draw"
                elif player == "rock":
                    if computer == "paper":
                        player_state = "Lose"
                        cpu_score += 1
                    elif computer == "scissors":
                        player_state = "Win"
                        player_score += 1
                elif player == "paper":
                    if computer == "scissors":
                        player_state = "Lose"
                        cpu_score += 1
                    elif computer == "rock":
                        player_state = "Win"
                        player_score += 1
                elif player == "scissors":
                    if computer == "rock":
                        player_state = "Lose"
                        cpu_score += 1
                    elif computer == "paper":
                        player_state = "Win"
                        player_score += 1


