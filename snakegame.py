import pygame
import random
import time

pygame.init()
clock=pygame.time.Clock()

display_width=400
display_height=600

set_window=pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption("Snake Game")

yellow=(255,255,0)
black=(0,0,0)
red=(213,50,80)
green=(0,255,0)
blue=(50,153,213)

snake_block=10
snake_speed=15
snake_pos=[]
def snake(snake_block, snake_pos):
    for x in snake_pos:
        pygame.draw.rect(set_window, yellow, [x[0], x[1], snake_block, snake_block])

#main function
def snakegame():
    game_over=False
    game_end=False
    x1=display_width/2
    y1=display_height/2

    x1_change=0
    y1_change=0

    snake_pos=[]
    length_of_snake=1

    mouse_x=round(random.randrange(0, display_width-snake_block)/10)*10
    mouse_y=round(random.randrange(0, display_height-snake_block)/10)*10

    while not game_over:
        while game_end==True:
            set_window.fill(blue)
            font_style=pygame.font.SysFont("commicsansms",20)
            messege=font_style.render("Replay? Press R", True, red)
            set_window.blit(messege,[display_width/6, display_height/3])

            score=length_of_snake-1
            score_font=pygame.font.SysFont("comicsansms", 35)
            value=score_font.render("Score: "+ str(score),True, green)
            set_window.blit(value, [display_width/3, display_height/5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        snakegame()
                if event.type==pygame.QUIT:
                    game_over=True
                    game_end=False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change= -snake_block
                    y1=0
                elif event.type==pygame.K_RIGHT:
                    x1_change= snake_block
                    y1=0
                elif event.type==pygame.K_UP:
                    y1_change= -snake_block
                    x1=0
                elif event.type==pygame.K_DOWN:
                    y1_change= snake_block
                    x1=0
        if x1>=display_width or x1<0  or y1>=display_height or y1<0:
            game_end=True
        x1+=x1_change
        y1+=y1_change
        set_window.fill(black)
        pygame.draw.rect(set_window, green, [mouse_x,mouse_y,snake_block, snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_pos.append(snake_head)

        if len(snake_pos)>length_of_snake:
            del snake_pos[0]
        for x in snake_pos[:-1]:
            if x==snake_head:
                game_end=True
        snake(snake_block, snake_pos)
        pygame.display.update()
        if x1==mouse_x and y1==mouse_y:
            mouse_x = round(random.randrange(0, display_width - snake_block) / 10) * 10
            mouse_y = round(random.randrange(0, display_height - snake_block) / 10) * 10
            length_of_snake+=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
snakegame()