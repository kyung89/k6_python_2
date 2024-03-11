import pygame
import settings

def init():
    pygame.init()
    screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
    clock = pygame.time.Clock()
    image = pygame.image.load(settings.IMG_SRC)

    screen_rect = screen.get_rect()
    ship_rect = image.get_rect()
    ship_rect.midbottom = screen_rect.midbottom
    bullets = []
    return screen,clock,image,screen_rect,ship_rect,bullets

def create_bullet(ship_rect):
    bullet = pygame.Rect(0, 0, 5, 50)
    bullet.midtop = ship_rect.midtop
    bullet.top -= ship_rect.height
    return bullet

def handle_key_event(ship_rect, bullets, event):
    if event.key == pygame.K_LEFT:
        ship_rect.left -= settings.SHIP_SPEED
    elif event.key == pygame.K_RIGHT:
        ship_rect.left += settings.SHIP_SPEED
    elif event.key == pygame.K_SPACE:
        b = create_bullet(ship_rect)
        bullets.append(b)
        
def update_bullets(screen_rect, bullets):
    new_bullets = []
    for bullet in bullets:
        if screen_rect.top < bullet.top:
            bullet.top -= 1
            new_bullets.append(bullet)
    return new_bullets
    
def render(screen, image, ship_rect, new_bullets):
    screen.blit(image, ship_rect)
    for bullet in new_bullets:
        pygame.draw.rect(screen, settings.BULLET_COLOR, bullet)