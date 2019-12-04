import pygame
#초기화
pygame.init()
width, height = 1200, 900
screen = pygame.display.set_mode((width, height))

#이미지를 가져온다
player = pygame.image.load("resources/images/dude.png")
player_stick = pygame.image.load("resources/Black_lord.png")
red = pygame.image.load("resources/my_resources/Test_Red.png")


#화면 띄우기
while True:
    #화면을 깨끗하게 한다.
    screen.fill((255,255,255)) #RGB

    #모든 요소들을 다시 그린다.
    
    screen.blit(player, (0,100)) #blit은 다시 그리기
    screen.blit(player_stick, (100,300))
    screen.blit(red, (0,600))

    #화면을 다시 그린다.
    pygame.display.flip() 

    #게임 종료.
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
