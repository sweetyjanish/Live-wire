import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Rolling Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize player scores
player1_score = 0
player2_score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Roll the dice
                die_roll = random.randint(1, 6)

                # Update player scores
                if player1_score < 100:
                    player1_score += die_roll
                elif player2_score < 100:
                    player2_score += die_roll

    # Draw scores on the screen
    font = pygame.font.Font(None, 36)
    text1 = font.render(f"Player 1 Score: {player1_score}", True, BLACK)
    text2 = font.render(f"Player 2 Score: {player2_score}", True, BLACK)

    screen.fill(WHITE)
    screen.blit(text1, (50, 50))
    screen.blit(text2, (50, 100))
    pygame.display.flip()

    # Check for a winner
    if player1_score >= 100 or player2_score >= 100:
        winner = "Player 1" if player1_score >= 100 else "Player 2"
        print(f"{winner} wins!")
        running = False

pygame.quit()