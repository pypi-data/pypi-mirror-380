import pygame, random, sys

CONFIG = {
    "width": 600,
    "height": 400,
    "cell_size": 20,
    "snake_speed": 5,
    "colors": {
        "background": (0, 0, 0),
        "snake": (0, 200, 0),
        "food": (200, 0, 0),
        "text": (255, 255, 255)
    }
}

WIDTH, HEIGHT = CONFIG["width"], CONFIG["height"]
CELL_SIZE = CONFIG["cell_size"]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("d1snake")
clock = pygame.time.Clock()

snake = [(100,100),(80,100),(60,100)]
direction = (CELL_SIZE,0)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))

def draw_snake(s):
    for segment in s:
        pygame.draw.rect(screen, CONFIG["colors"]["snake"], (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(pos):
    pygame.draw.rect(screen, CONFIG["colors"]["food"], (*pos, CELL_SIZE, CELL_SIZE))

def game_over():
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over", True, CONFIG["colors"]["text"])
    rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def run():
    global direction, food, snake
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_s and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_a and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_d and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        new_head = (snake[0][0]+direction[0], snake[0][1]+direction[1])
        snake.insert(0, new_head)

        if (new_head[0]<0 or new_head[0]>=WIDTH or
            new_head[1]<0 or new_head[1]>=HEIGHT or
            new_head in snake[1:]):
            game_over()

        if new_head == food:
            food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        else:
            snake.pop()

        screen.fill(CONFIG["colors"]["background"])
        draw_snake(snake)
        draw_food(food)
        pygame.display.flip()
        clock.tick(CONFIG["snake_speed"])
