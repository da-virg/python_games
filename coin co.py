import pgzrun

from random import randint

WIDTH = 600
HEIGHT = 600
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 200, 200

coin = Actor("coin")
coin.pos = 100, 100

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("orange")
        screen.draw.text("final score: " + str(score), color="black", topleft=(10, 10), fontsize=60)
    
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        fox.x = fox.x - 4
    elif keyboard.right:
        fox.x = fox.x + 4
    elif keyboard.up:
        fox.y = fox.y - 4
    elif keyboard.down:
        fox.y = fox.y + 4

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()
        
clock.schedule(time_up, 15.0)
place_coin()

pgzrun.go()
