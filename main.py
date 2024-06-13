import pygame
import datetime

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("rolex")
pygame.display.set_icon(pygame.image.load("Без названия.png"))

white = (255, 255, 255)
body_image = pygame.image.load('body.png')
left_hand_image = pygame.image.load('2_hand.png')
right_hand_image = pygame.image.load('1_hand.png')


clock_radius = 200


left_hand_offset = (45, -15)
right_hand_offset = (-45, -15)

def blit_rotate_center(surf, image, center, offset, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    new_rect = new_rect.move(offset)
    surf.blit(rotated_image, new_rect.topleft)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    now = datetime.datetime.now()
    second = now.second
    minute = now.minute

    screen.fill(white)

    center_x, center_y = width // 2, height // 2

    body_rect = body_image.get_rect(center=(center_x, center_y))
    screen.blit(body_image, body_rect.topleft)

    sec_a = -second * 6  
    min_a = -minute * 6 

    blit_rotate_center(screen, left_hand_image, (center_x, center_y), left_hand_offset, sec_a)
    blit_rotate_center(screen, right_hand_image, (center_x, center_y), right_hand_offset, min_a)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
