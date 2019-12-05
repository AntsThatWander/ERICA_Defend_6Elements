import pygame

#초기화
pygame.init()
width, height = 1400, 1030
screen = pygame.display.set_mode((width, height))

#이미지를 가져온다
player = pygame.image.load("resources/my_resources/player_ready_Red.png")
ball_room = pygame.image.load("resources/my_resources/magic_room.png")
card_room = pygame.image.load("resources/my_resources/card_room.png")
pave_road = pygame.image.load("resources/my_resources/pave_road.png")
ground = pygame.image.load("resources/my_resources/ground.png")
tent = pygame.image.load("resources/my_resources/tent.png")
tent_road = pygame.image.load("resources/my_resources/tent_road.png")
castle = pygame.image.load("resources/my_resources/castle_wall.png")

#플레이어 이동 리스트
keys = [False, False]
playpos = [220, 310]
#플레이어 색깔 리스트
color = [False, False, False, False, False, False]

#화면 띄우기
while True:
    #화면을 깨끗하게 한다.
    screen.fill((255,255,255)) #RGB

    #모든 요소들을 다시 그린다.
    #blit은 다시 그리기
    for x in range(5):
            screen.blit(tent_road,(0,(x+1)*140-110))
            screen.blit(tent,(0,(x+1)*140-110))
            screen.blit(pave_road,(300,(x+1)*140-110))
            screen.blit(ground,(300,(x+1)*140+20))
    screen.blit(castle, (200,30))
    screen.blit(ball_room, (0,730))
    screen.blit(card_room, (300,730))
    screen.blit(player, playpos)
   

    #화면을 다시 그린다.
    pygame.display.flip() 

    #게임 종료.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_w or pygame.K_UP):
                keys[0] = True
            elif event.key == (pygame.K_s or pygame.K_DOWN):
                keys[1] = True
        if event.type == pygame.KEYUP:
            if event.key == (pygame.K_w or pygame.K_UP):
                keys[0] = False
            elif event.key == (pygame.K_s or pygame.K_DOWN):
                keys[1] = False
    #플레이어 이동
    if keys[0] and playpos[1]>30:
        playpos[1] = playpos[1] - 140
    elif keys[1] and playpos[1]<590:
        playpos[1] = playpos[1] + 140
