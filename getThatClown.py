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