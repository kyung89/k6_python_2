# https://www.pygame.org/docs/tut/newbieguide.html [한글번역 사용하기]

# 우리의 목표는 p.347
import sys
import pygame

pygame.init()

# setting.py 로 따로 관리하는 방법도 있다
FRAME_PER_SECOND = 60
IMG_SRC = 'images_ch12/ship.bmp'
SHIP_SPEED = 5
WIDTH = 1280
HEIGHT = 720

# util 로 주요 기능들을 함수로 정의해 관리할 수 있다

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
image = pygame.image.load(IMG_SRC)
image_rect = image.get_rect()
image_left = screen.get_width() / 2 - image_rect.width / 2
image_top = screen.get_height() - image_rect.height
rect = pygame.Rect((image_left, image_top), (400, 400)) # left, top, width, height
#rect = pygame.Rect(0 ,0, 1280, 720)
#rect = screen.get_rect()
#rect = image.get_rect()

bullets = []
BULLET_COLOR = (255, 0, 0)
def create_bullet(image_rect):
    bullet = pygame.Rect(0, 0, 5, 50)
    bullet.midtop = image_rect.midtop
    bullet.top -= image_rect.height
    return bullet

while True: # while 은 계속 돈다
    # Process player inputs.
    for event in pygame.event.get(): # 01. 키보드, 마우스 이벤트
        if event.type == pygame.QUIT: # x 누르면 닫히도록 구현하였음
            pygame.quit()
            sys.exit() # raise SystemExit 대신 사용해봄! import sys 필요
            #raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.left -= SHIP_SPEED
            elif event.key == pygame.K_RIGHT:
                rect.left += SHIP_SPEED
            elif event.key == pygame.K_UP:
                rect.top -= SHIP_SPEED
            elif event.key == pygame.K_DOWN:
                if rect.top + image.get_height() < screen.get_height(): # 화면 바깥으로 가지 않도록 처리!
                    rect.top += SHIP_SPEED
            elif event.key == pygame.K_SPACE:
                bullets.append(create_bullet(image_rect))

    # Do logical updates here. # 02. update 위치
    # ...

    screen.fill("gray")  # Fill the display with a solid color: 화면을 보라색으로 채웠음! default 는 까만색임!

    # Render the graphics here. # 03. 그림 그리기
    # ...
    screen.blit(image, rect)

    my_bullets = []
    for bullet in bullets:
        bullet.top -= 1
        pygame.draw.rect(screen, BULLET_COLOR, bullet)


    pygame.display.flip()  # 04. Refresh on-screen display # 새로 그리고, 뒤집기
    clock.tick(FRAME_PER_SECOND)         # wait until next frame (at 60 FPS) # 그림을 60장 그린다