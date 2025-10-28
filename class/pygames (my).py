import pygame
pygame.init()
CS16 = 1220
CS2 = 1800
PUBG = 2890

windows =pygame.display.set_mode((CS2, CS16))
pygame.display.set_caption("shablon")
lkh = pygame.time.Clock()
gtrer = (20)
kyygu = (30)
gfh =(58)


run =True

while run:
    lkh.tick(PUBG)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                gtrer -= gfh
            if i.key == pygame.K_d:
                gtrer += gfh
            if i.key == pygame.K_w:
                kyygu -= gfh
            if i.key == pygame.K_s:
                kyygu += gfh
    windows.fill("#acf321")
    pygame.draw.rect(windows, (152,231,190), (gtrer,kyygu,40,50))
    pygame.display.flip()
pygame.quit()