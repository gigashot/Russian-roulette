import pygame
import random
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT =  600

# Colors
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (150, 0, 0)
GREEN = (0, 100, 0)

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Russian Roulette")

# Fonts
font_small = pygame.font.SysFont(None, 35)
font_medium = pygame.font.SysFont(None, 55)
font_large = pygame.font.SysFont(None, 75)

def draw_text(text, font, color, surface, x, y):
    # text object == vykreslený text
    textobj = font.render(text, True, color)
    # text rectangle == creates a rectangle around the text
    textrect = textobj.get_rect()
    # center of the rectangle
    textrect.center = (x, y)
    # draw text on the surface
    surface.blit(textobj, textrect)

# Load sound
bang_sound = pygame.mixer.Sound("assets/gunshot.mp3")
click_sound = pygame.mixer.Sound("assets/empty-gun-click.mp3")
spin_sound = pygame.mixer.Sound("assets/revolver-spin.mp3")
ring_sound = pygame.mixer.Sound("assets/ear-ringing-sound.mp3")
pygame.mixer.music.load("assets/background-music.mp3")

# Load images
background_image = pygame.image.load("assets/bar1.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load n scale revolver
revolver_image = pygame.image.load("assets/revolver.png")
revolver_image = pygame.transform.scale(revolver_image, (600, 600))

# Flash image
flash_image = pygame.image.load("assets/flash.png")
flash_image = pygame.transform.scale(flash_image, (600, 600))

# Load n scale spin animation
spin_frames = [
    pygame.transform.scale(pygame.image.load(f"assets/spin_{i}.png"), (600, 600))
    for i in range(1, 8)
]

#explanation - pygame.display.flip() - updates the screen

def menu():
    pygame.mixer.music.play(-1)
    screen.fill(BLACK)
    draw_text("Russian Roulette", font_large, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3.5)
    draw_text("Remember. . . You can not win. . . or can you?", font_small, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5)
    draw_text("Warning: LOUD SOUNDS!", font_small, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text("click anywhere to continue", font_small, GREEN, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2)
    pygame.display.flip() # updates the whole screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

def animate_spin():
    for frame in spin_frames:
        screen.blit(background_image, (0, 0)) # .blit - draws background on top of everything
        screen.blit(frame, (300, 0)) # draws frame on top of background
        pygame.display.flip() # updates the whole screen
        pygame.time.delay(100)


def animate_trigger(): 
    screen.blit(background_image, (0, 0)) # same principle as above
    screen.blit(flash_image, (300, 0))
    pygame.display.flip() # updates the whole screen
    pygame.time.delay(200)
    pygame.display.flip()

def main():
    running = True
    score = 0
    cylinder = [0, 0, 0, 0, 0, 1]
    random.shuffle(cylinder) # shuffles the cylinder

    # buttons
    spin_button = pygame.Rect(250, 500, 200, 50)
    trigger_button = pygame.Rect(750, 500, 200, 50) 

    while running:
        
        screen.blit(background_image, (0, 0)) # .blit - draws revolver on top of background, aka the same as above
        screen.blit(revolver_image, (300, 0)) # same here
        
        
        pygame.draw.rect(screen, GREEN, spin_button) # draws the button
        pygame.draw.rect(screen, RED, trigger_button) # same here

        draw_text("Spin", font_medium, BLACK, screen, spin_button.centerx, spin_button.centery) # adds(draws) text on the button
        draw_text("Fire", font_medium, BLACK, screen, trigger_button.centerx, trigger_button.centery) # same here
        draw_text(f"Score: {score}", font_small, GREEN, screen, SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10) # display score in top left corner

        pygame.display.flip() # updates the whole screen
        if score == 18:
            pygame.mixer.music.stop()
            screen.fill(WHITE)
            draw_text("You Win?", font_large, GREEN, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
            draw_text("After unbelivable odds, you are still alive.", font_medium, GREEN, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            draw_text("You have decided to stop and go home", font_medium, GREEN, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text("leave this for another time...", font_small, GREEN, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.2)
            #win_music.play()
            pygame.display.flip() # updates the whole screen
            pygame.time.wait(10000)
            running = False
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if spin_button.collidepoint(event.pos):
                    spin_sound.play()
                    animate_spin()
                    cylinder = [0, 0, 0, 0, 0, 1]
                    random.shuffle(cylinder)
                elif trigger_button.collidepoint(event.pos):
                    if cylinder.pop() == 1:
                        pygame.mixer.music.stop()
                        animate_trigger()
                        bang_sound.play()
                        ring_sound.play()
                        screen.fill(WHITE)
                        draw_text("Death comes alas", font_large, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                        pygame.display.flip() # updates the whole screen
                        pygame.time.wait(5000)
                        running = False
                        pygame.quit()
                    else:
                        click_sound.play()
                        score += 1

if __name__ == "__main__":
    menu()