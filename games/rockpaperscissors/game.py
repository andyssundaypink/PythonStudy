import random
import pygame
from button import Button, ButtonText

pygame.init()
width = 680
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock Paper Scissors Game")

rock_button = Button("resources/rock.png", "rock", (50, 50), (200, 100))
paper_button = Button("resources/paper.png", "paper", (50,50), (300, 100))
scissors_button = Button("resources/scissors.png", "scissors",  (50,50), (400, 100))

rock = pygame.image.load("resources/rock.png")
rock = pygame.transform.scale(rock, (50, 50))
paper = pygame.image.load("resources/paper.png")
paper = pygame.transform.scale(paper, (50, 50))
scissors = pygame.image.load("resources/scissors.png")
scissors = pygame.transform.scale(scissors, (50, 50))

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.SysFont('Arial', 32)
text = font.render('Please choose Rock, Paper, or Scissors', 0, green)

choices = ["rock", "paper", "scissors"]
computer = ""
player_score = 0
cpu_score = 0
player = ""
cpu_changed = False

while 1:
    screen.fill(0)
    rock_button.draw(screen)
    paper_button.draw(screen)
    scissors_button.draw(screen)
    screen.blit(text, (50, 50))
    text1 = font.render("You", True, green, blue)
    screen.blit(text1, (200, 180))
    text5 = font.render("VS", True, green, blue)
    screen.blit(text5, (300, 180))
    text3 = font.render("Computer", True, green, blue)
    screen.blit(text3, (380, 180))

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

    text6 = font.render(str(player_score), True, green, blue)
    screen.blit(text6, (220, 220))
    text7 = font.render(str(cpu_score), True, green, blue)
    screen.blit(text7, (420, 220))

    reset_button = ButtonText("Reset", (360, 350), "Arial", 32, green, blue)
    reset_button.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        rock_button.event_handler(event)
        paper_button.event_handler(event)
        scissors_button.event_handler(event)
        reset_button.event_handler(event)
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


