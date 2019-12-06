import pygame
import images

#초기화
pygame.init()
width, height = 1280, 960
screen = pygame.display.set_mode((width, height))

#플레이어 이동 리스트
keys = [False, False]
playpos = [220, 310]
#플레이어 색깔 리스트
color = [True, False, False, False, False, False]
#
acc = [0,0]
#화살
arrows = []

#화면 띄우기
while True:
    #화면을 깨끗하게 한다.
    screen.fill((255,255,255)) #RGB
    
    #모든 요소들을 다시 그린다.#blit은 다시 그리기
    for x in range(5):
            screen.blit(images.tent_road,(0,(x+1)*140-110))
            screen.blit(images.tent,(0,(x+1)*140-110))
            screen.blit(images.pave_road,(300,(x+1)*140-110))
    screen.blit(images.castle, (200,30))
    screen.blit(images.ball_room, (0,730))
    screen.blit(images.card_room, (300,730))
    screen.blit(images.player, playpos)
    screen.blit(images.zombie,(400,30))
    screen.blit(images.zombie_barrier,(300,30))
    screen.blit(images.nighthorror,(500,30))
    screen.blit(images.ling,(600,30))
    screen.blit(images.crawler,(700,30))
    screen.blit(images.sting,(800,80))
    screen.blit(images.cannon,(900,30))
    screen.blit(images.ball,(900,40))
    screen.blit(images.black,(500,310))
    screen.blit(images.seer,(1200,30))
    #screen.blit(images.final,(600,30))
    screen.blit(images.card_Red, (400,745))
   

    #화면을 다시 그린다.
    pygame.display.flip() 

    #게임 이벤트
    for event in pygame.event.get(): 
        #게임 종료
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        #이동 관련 입력
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or  event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_s or  event.key == pygame.K_DOWN:
                keys[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or  event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_s or  event.key == pygame.K_DOWN:
                keys[1] = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     position = pygame.mouse.get_pos()
        #     acc[1] = acc[1] + 1
        #     arrows.append()
    #플레이어 이동
    if keys[0] and playpos[1]>30:
        playpos[1] = playpos[1] - 140
    elif keys[1] and playpos[1]<590:
        playpos[1] = playpos[1] + 140
