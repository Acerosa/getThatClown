import pygame
import random

# Initialize pygame
pygame.init()

# Set screen
windowWidth = 945
windowHeight = 600
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Get that Clown")

# Set FPS and clock
fps = 60
clock = pygame.time.Clock()

# Set game values
playerStartingLives = 5
clownStartingVelocity = 5
clownAcceleration = 1

# Set colours
blue = (1, 175, 209)
yellow = (248, 231, 28)

# Load fonts
font = pygame.font.Font("getThatClownAssets/Franxurter.ttf", 32)

# Load sound effects and music
clickSound = pygame.mixer.Sound("getThatClownAssets/clickSound.wav")
missSound = pygame.mixer.Sound("getThatClownAssets/missSound.wav")
pygame.mixer.music.load("getThatClownAssets/ctcBackgroundMusic.wav")

# Load images
backgroundImage = pygame.image.load("getThatClownAssets/background.png")
clownImage = pygame.image.load("getThatClownAssets/clown.png")

# GAME FUNCTIONALITY
def increaseScore():
    """Increases the player's score"""
    global score
    score += 1

def updateClownVelocity():
    """Increases the velocity of the clown"""
    global clownVelocity
    clownVelocity += clownAcceleration

def decreasePlayerLives():
    """Decreases the player's lives"""
    global playerLives
    playerLives -= 1




def updateScreen():
    """Updates the display"""
    screen.blit(backgroundImage, (0, 0))
    screen.blit(titleText, (50, 10))
    screen.blit(scoreText, (windowWidth - 200, 10))
    screen.blit(livesText, (windowWidth - 200, 50))
    screen.blit(clownImage, clownRect)
    pygame.display.update()

# Set initial game state
score = 0
playerLives = playerStartingLives
clownRect = clownImage.get_rect(center=(windowWidth // 2, windowHeight // 2))
clownDx = random.choice([-1, 1])
clownDy = random.choice([-1, 1])
clownVelocity = clownStartingVelocity

# Set initial HUD text
titleText = font.render("Get that Clown", True, blue)
scoreText = font.render("Score: " + str(score), True, yellow)
livesText = font.render("Lives: " + str(playerLives), True, yellow)

# The main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    updateScreen()
    pygame.display.update()
    clock.tick(fps)

# End the game
pygame.quit()