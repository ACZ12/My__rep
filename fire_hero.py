import pygame
import sys
import random



pygame.init()
SC_W, SC_H = 450, 900
win = pygame.display.set_mode((SC_W, SC_H))
pygame.display.set_caption("Fire Hero")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.draw.line(win,(255,255,255),(0,SC_H),(SC_W,SC_H))

run = True
game = True
block_appearance_delay = 2000
block_appearance_time = 0
current_block = None
score=0

allitasok==["Bipi a cserkészet megalapítója."]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(SC_W / 2, SC_H / 2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def create_block(self):
        return Block(random.randint(0, SC_W), -30)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y -= 5
        if self.rect.y <= -100:
            self.kill()

class Block(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.y += 2
        
            

text_font=pygame.font.SysFont(None,30)

def text(text,font,text_col,x,y):
    img=font.render(text,True,text_col)
    win.blit(img,(x,y))

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
bullet_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    while game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet_group.add(player.create_bullet())

        current_time = pygame.time.get_ticks()

        if current_time - block_appearance_time >= block_appearance_delay:
            current_block = player.create_block()
            block_group.add(current_block)
            block_appearance_time = current_time

        

        collisions = pygame.sprite.groupcollide(bullet_group, block_group, True, True)
        collisions2 = pygame.sprite.groupcollide(block_group, player_group, True, True)

        if collisions:
            score+=1

        if collisions2:
            game=False

        for block in block_group:
            if block.rect.y >= SC_H:
                game = False
                block.kill()

        win.fill((30, 30, 30))
        block_group.draw(win)
        bullet_group.draw(win)
        player_group.draw(win)

        player_group.update()
        bullet_group.update()
        block_group.update()

        pygame.display.flip()
        clock.tick(120)

    text(f"Your score : {score}",text_font,(0,240,255),150,500)
    pygame.display.flip()

pygame.quit()
sys.exit()
