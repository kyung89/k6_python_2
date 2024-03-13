# https://www.pygame.org/docs/tut/newbieguide.html [한글번역 사용하기]

# 우리의 목표는 p.347
import sys
import pygame
 
import settings
from util import init, create_bullet, handle_key_event, update_bullets, render

screen, clock, image, screen_rect, ship_rect, bullets = init()

while True: # while 은 계속 돈다
    # Process player inputs.
    for event in pygame.event.get(): # 01. 키보드, 마우스 이벤트
        if event.type == pygame.QUIT: # x 누르면 닫히도록 구현하였음
            pygame.quit()
            sys.exit() # raise SystemExit 대신 사용해봄! import sys 필요
            #raise SystemExit
        elif event.type == pygame.KEYDOWN:
            handle_key_event(ship_rect, bullets, event)

    # Do logical updates here. # 02. update 위치
    # ...

    screen.fill("gray")  # Fill the display with a solid color: 화면을 보라색으로 채웠음! default 는 까만색임!

    # Render the graphics here. # 03. 그림 그리기
    # ...
   
    new_bullets = update_bullets(screen_rect, bullets)
    
    render(screen, image, ship_rect, new_bullets)

    pygame.display.flip()  # 04. Refresh on-screen display # 새로 그리고, 뒤집기
    clock.tick(settings.FRAME_PER_SECOND)         # wait until next frame (at 60 FPS) # 그림을 60장 그린다