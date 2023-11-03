import pygame
screen=pygame.display.set_mode([360,600])
background=pygame.image.load("kol.png")
spaceship=pygame.image.load("posa.png")
keep_alive=True
clock=pygame.time.Clock()
bullet=pygame.image.load("zelst.png")
bullet_y=500
fired=False
planets=["sel.png","tenkes.png","stav.png"]
p_idx=0
planet=pygame.image.load(planets[p_idx])
planet_x=140
move_direction="right"

while keep_alive:
    screen.blit(background,[0,0])
    screen.blit(spaceship,[160,500])
    pygame.event.get()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]==True:
        fired=True
    if fired is True:
        bullet_y-=5
        if bullet_y==80:
            fired=False
            bullet_y=500
    if move_direction=="right":
        planet_x+=5
        if planet_x==300:
            move_direction="left"
    else: 
        planet_x-=5
        if planet_x==0:
            move_direction="right"
    screen.blit(planet,[planet_x,50])
    screen.blit(bullet,[180,bullet_y])
    if bullet_y<=80 and planet_x<180 and planet_x>120:
        p_idx+=1
        if p_idx>len(planets):
            planet=pygame.image.load(planets[p_idx])
            planet_x=10
        else:
            print("YOU WIN!")
            keep_alive=False
    
    pygame.display.update()
    clock.tick(60)
