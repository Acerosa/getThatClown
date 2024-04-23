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

def inputHandler():
    """Handles user input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickHandler(event.pos)
    return True


def clickHandler(pos):
    """Handles mouse click events"""
    if gameOver:
        restartGame()
    else:
        mouseX, mouseY = pos
        if clownRect.collidepoint(mouseX, mouseY):
            clickSound.play()
            increaseScore()
            updateClownVelocity()
        else:
            missSound.play()
            decreasePlayerLives()


def increaseScore():
    """Increases the player's score"""
    global score
    score += 1
    updateScoreText()


def updateLivesText():
    """Updates the player lives HUD text"""
    global livesText
    livesText = font.render("Lives: " + str(playerLives), True, yellow)


def updateScoreText():
    """Updates the score HUD text"""
    global scoreText, livesText
    scoreText = font.render("Score: " + str(score), True, yellow)


def updateClownVelocity():
    """Increases the velocity of the clown"""
    global clownVelocity
    clownVelocity += clownAcceleration


def decreasePlayerLives():
    """Decreases the player's lives"""
    global playerLives
    playerLives -= 1
    updateLivesText()
    if playerLives == 0:
        gameOverScreen()


def moveClown():
    """Moves the clown and handles collision with screen edges"""
    global clownRect, clownDx, clownDy
    clownRect.x += clownDx * clownVelocity
    clownRect.y += clownDy * clownVelocity

    if clownRect.left <= 0 or clownRect.right >= windowWidth:
        clownDx = -1 * clownDx
    if clownRect.top <= 0 or clownRect.bottom >= windowHeight:
        clownDy = -1 * clownDy


def updateScreen():
    """Updates the display"""
    screen.blit(backgroundImage, (0, 0))
    screen.blit(titleText, (50, 10))
    screen.blit(scoreText, (windowWidth - 200, 10))
    screen.blit(livesText, (windowWidth - 200, 50))
    screen.blit(clownImage, clownRect)
    if gameOver:
        screen.blit(gameOverText, gameOverRect)
        screen.blit(continueText, continueRect)

    pygame.display.update()


def restartGame():
    """Restarts the game"""
    global score, playerLives, gameOver
    score = 0
    playerLives = playerStartingLives
    clownRect.center = (windowWidth // 2, windowHeight // 2)
    clownVelocity = clownStartingVelocity
    clownDx = random.choice([-1, 1])
    clownDy = random.choice([-1, 1])
    gameOver = False


def gameOverScreen():
    """Displays the game over screen"""
    global gameOver
    gameOver = True


# Set initial game state
score = 0
playerLives = playerStartingLives
clownRect = clownImage.get_rect(center=(windowWidth // 2, windowHeight // 2))
clownDx = random.choice([-1, 1])
clownDy = random.choice([-1, 1])
clownVelocity = clownStartingVelocity
gameOver = False

# Set initial HUD text
titleText = font.render("Get that Clown", True, blue)
scoreText = font.render("Score: " + str(score), True, yellow)
livesText = font.render("Lives: " + str(playerLives), True, yellow)

gameOverText = font.render("GAME OVER", True, blue, yellow)
continueText = font.render("Click anywhere to play again", True, yellow, blue)

gameOverRect = gameOverText.get_rect(center=(windowWidth // 2, windowHeight // 2))
continueRect = continueText.get_rect(center=(windowWidth // 2, windowHeight // 2 + 64))

# The main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    running = inputHandler()
    if not gameOver:
        moveClown()
    updateScreen()
    clock.tick(fps)

# End the game
pygame.quit()
