import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont(None, 40)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Sample sentences for typing
SENTENCES = ["Ayomide wipes down the countertops diligently.",
"Ayomide polishes the silverware with care.",
"Ayomide disinfects the bathroom surfaces thoroughly.",
"Ayomide irons the clothes neatly.",
"Ayomide arranges the books on the shelves methodically.",
"Ayomide waters the plants tenderly.",
"Ayomide cleans the mirrors streak-free.",
"Ayomide changes the bed linens efficiently.",
"Ayomide sorts the recycling conscientiously.",
"Ayomide empties the trash bins regularly.",
"Ayomide straightens the furniture meticulously.",
"Ayomide dusts the lampshades delicately.",
"Ayomide organizes the shoe rack systematically.",
"Ayomide buffs the wooden floors to a shine.",
"Ayomide de-clutters the hallway diligently.",
"Ayomide cleans the stove grates thoroughly.",
"Ayomide sweeps the patio with precision.",
"Ayomide vacuums the rugs meticulously.",
"Ayomide scrubs the bathtub thoroughly.",
"Ayomide folds the towels neatly.",
"Ayomide mops the tiled floors with care.",
"Ayomide tidies up the children's toys conscientiously.",
"Ayomide organizes the spice cabinet systematically.",
"Ayomide dusts the ceiling fan blades gently.",
"Ayomide wipes down the refrigerator shelves diligently.",
"Ayomide vacuums under the furniture car.",
    "Ayomide mops the kitchen cheerfully.",
]

# Game variables
sentence = random.choice(SENTENCES)
user_input = ""
time_start = None
time_end = None
typing_speed = 0

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                if user_input == sentence:
                    time_end = pygame.time.get_ticks()
                    time_elapsed = (time_end - time_start) / 1000
                    words_typed = len(user_input.split())
                    typing_speed = words_typed / (time_elapsed / 60)
                    print(f"Your typing speed: {typing_speed} words per minute")
                    sentence = random.choice(SENTENCES)
                    user_input = ""
                    time_start = None  # Reset timer
                else:
                    print("Incorrect! Try again.")
                    time_start = pygame.time.get_ticks()  
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                if time_start is None:
                    time_start = pygame.time.get_ticks()  
                user_input += event.unicode

    
    sentence_surface = FONT.render(sentence, True, WHITE)
    sentence_rect = sentence_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(sentence_surface, sentence_rect)

    
    input_surface = FONT.render(user_input, True, WHITE)
    input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(input_surface, input_rect)

    
    speed_surface = FONT.render(f"Typing Speed: {typing_speed:.2f} words per minute", True, WHITE)
    speed_rect = speed_surface.get_rect(midtop=(WIDTH // 2, HEIGHT - 100))
    screen.blit(speed_surface, speed_rect)

    # 
    if time_start is not None and time_end is None:
        time_elapsed = (pygame.time.get_ticks() - time_start) / 1000
        timer_surface = FONT.render(f"Time: {time_elapsed:.2f} seconds", True, WHITE)
        timer_rect = timer_surface.get_rect(midbottom=(WIDTH // 2, HEIGHT - 50))
        screen.blit(timer_surface, timer_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
