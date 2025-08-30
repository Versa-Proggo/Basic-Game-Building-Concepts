import pygame,random
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=640,480
display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My first game screen")
rect_width,rect_height=120,80
pygame_rect=pygame.Rect(0,0,rect_width,rect_height)
pygame_rect.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
rect_speed=5
rect_color=(255,0,0)
font=pygame.font.Font(None,36)
text=font.render("Move with WASD – Touch walls for color change!",True,(0,0,0))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT-40))
def random_color():return(random.randint(0,255),random.randint(0,255),random.randint(0,255))
bg_color=(255,255,255)
def game_loop():
    global rect_color,bg_color
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:running=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:pygame_rect.x-=rect_speed
        if keys[pygame.K_d]:pygame_rect.x+=rect_speed
        if keys[pygame.K_w]:pygame_rect.y-=rect_speed
        if keys[pygame.K_s]:pygame_rect.y+=rect_speed
        if pygame_rect.left<=0:
            pygame_rect.left=0
            rect_color=(0,0,255)
            bg_color=random_color()
        if pygame_rect.right>=SCREEN_WIDTH:
            pygame_rect.right=SCREEN_WIDTH
            rect_color=(255,255,0)
            bg_color=random_color()
        if pygame_rect.top<=0:
            pygame_rect.top=0
            rect_color=(255,0,0)
            bg_color=random_color()
        if pygame_rect.bottom>=SCREEN_HEIGHT:
            pygame_rect.bottom=SCREEN_HEIGHT
            rect_color=(0,255,0)
            bg_color=random_color()
        display_surface.fill(bg_color)
        pygame.draw.rect(display_surface,rect_color,pygame_rect)
        display_surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__=="__main__":game_loop()
