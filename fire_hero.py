import pygame,sys
pygame.init()
SC_W,SC_H=450,900
win=pygame.display.set_mode((SC_W,SC_H))
pygame.display.set_caption("Fire Hero") 
clock=pygame.time.Clock()
pygame.mouse.set_visible(False)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((100,100))
        self.image.fill((255,255,255))
        self.rect=self.image.get_rect(center=(SC_W/2,SC_H/2))
    def update(self):
        self.rect.center=pygame.mouse.get_pos()
        

player=Player()
player_group=pygame.sprite.Group()
player_group.add(player)
run=1
while run:

    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0
            pygame.quit()
            sys.exit()

    win.fill((30,30,30))
    player_group.draw(win)
    player_group.update()
    pygame.display.flip()
    clock.tick(30)