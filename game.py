import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Russian Roulette")

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 55)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Load sounds
bang_sound = pygame.mixer.Sound('assets/gunshot.mp3')
click_sound = pygame.mixer.Sound('assets/empty-gun-click.mp3')
spin_sound = pygame.mixer.Sound('assets/revolver-spin.mp3')
ring_sound = pygame.mixer.Sound('assets/ear-ringing-sound.mp3')

# Load images
background_image = pygame.image.load('assets/bar.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and scale revolver image
revolver_image = pygame.image.load('assets/revolver.png')
revolver_image = pygame.transform.scale(revolver_image, (600, 600))  # 200 * 3 = 600

# Load and scale animation frames
spin_frames = [
    pygame.transform.scale(pygame.image.load(f'assets/spin_{i}.png'), (600, 600))  # 200 * 3 = 600
    for i in range(1, 8)
]

# Load and scale trigger effect
flash_image = pygame.image.load('assets/flash.png')
flash_image = pygame.transform.scale(flash_image, (600, 600))  # 200 * 3 = 600

def animate_spin():
    for frame in spin_frames:
        screen.blit(background_image, (0, 0))  # Draw the background first
        screen.blit(frame, (300, 0))  # Adjusted position to fit the larger image
        pygame.display.flip()
        pygame.time.delay(100)  # Adjust delay for animation speed

def animate_trigger():
    screen.blit(background_image, (0, 0))  # Draw the background first
    screen.blit(flash_image, (300, 0))  # Adjusted position to fit the larger image
    pygame.display.flip()
    pygame.time.delay(200)  # Adjust delay for animation duration
    screen.blit(background_image, (0, 0))  # Redraw the background
    screen.blit(revolver_image, (300, 0))  # Adjusted position to fit the larger image
    pygame.display.flip()

def main():
    running = True
    score = 0
    cylinder = [0, 0, 0, 0, 0, 1]  # One bullet in the cylinder
    random.shuffle(cylinder)  # Randomize the cylinder

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if spin_button.collidepoint(event.pos):
                    # Spin the cylinder
                    spin_sound.play()
                    animate_spin()
                    cylinder = [0, 0, 0, 0, 0, 1]
                    random.shuffle(cylinder)
                elif trigger_button.collidepoint(event.pos):
                    # Pull the trigger
                    if cylinder.pop() == 1:
                        animate_trigger()
                        bang_sound.play()
                        ring_sound.play()
                        
                        draw_text('Game Over', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        running = False
                    else:
                        click_sound.play()
                        screen.blit(background_image, (0, 0))  # Draw the background first
                        screen.blit(revolver_image, (300, 0))  # Adjusted position to fit the larger image
                        score += 1
                        draw_text(f'Score: {score}', font, GREEN, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.wait(1000)

        screen.blit(background_image, (0, 0))  # background

        # show revolver
        screen.blit(revolver_image, (300, 0))

        # Button positions and sizes
        spin_button = pygame.Rect(250, 500, 200, 50)
        trigger_button = pygame.Rect(750, 500, 200, 50)

        # Drawing buttons
        pygame.draw.rect(screen, GREEN, spin_button)
        pygame.draw.rect(screen, RED, trigger_button)
        draw_text('Spin', font, BLACK, screen, spin_button.centerx, spin_button.centery)
        draw_text('Trigger', font, BLACK, screen, trigger_button.centerx, trigger_button.centery)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
