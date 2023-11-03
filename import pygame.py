import pygame
W,H=10,20
TILE=45
GAME_RES=W*TILE,H*TILE
FPS=60
run=1
pygame.init()
win=pygame.display.set_mode(GAME_RES)
pygame.display.set_caption("Tetris") 
clock=pygame.time.Clock()
grid=[pygame.Rect(x*TILE,y*TILE,TILE,TILE) for x in range(W) for y in range(H)]

while run:
    win.fill((150,150,150))
    
    
    
    
    
    [pygame.draw.rect(win,(0,0,0),i_rect,1) for i_rect in grid]
    
    
    
    
    
    pygame.display.flip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0