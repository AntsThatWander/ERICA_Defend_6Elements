import pygame
#초기화
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#이미지를 가져온다
player = pygame.image.load("resources/images/dude.png")
player_stick = pygame.image.load("resources/images/player1.png")


#화면 띄우기
while True:
    #화면을 깨끗하게 한다.
    screen.fill((0,0,0)) #RGB

    #모든 요소들을 다시 그린다.
    
    screen.blit(player, (100,100)) #blit은 다시 그리기
    screen.blit(player_stick, (100,200))

    #화면을 다시 그린다.
    pygame.display.flip() 

    #게임 종료.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
