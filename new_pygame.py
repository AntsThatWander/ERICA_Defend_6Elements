import pygame

#초기화
pygame.init()
width, height = 1400, 1030
screen = pygame.display.set_mode((width, height))

#이미지를 가져온다
player_stick = pygame.image.load("resources/my_resources/player_ready_Red.png")
ball_room = pygame.image.load("resources/my_resources/magic_room.png")
card_room = pygame.image.load("resources/my_resources/card_room.png")
pave_road = pygame.image.load("resources/my_resources/pave_road.png")
ground = pygame.image.load("resources/my_resources/ground.png")
tent = pygame.image.load("resources/my_resources/tent.png")
tent_road = pygame.image.load("resources/my_resources/tent_road.png")
castle = pygame.image.load("resources/my_resources/castle_wall.png")

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
    screen.blit(player_stick, (220,310))
   

    #화면을 다시 그린다.
    pygame.display.flip() 

    #게임 종료.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
