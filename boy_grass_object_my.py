from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
        pass

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x = random.randint(0, 700)
        self.image = load_image('run_animation.png')
        self.frame = random.randint(0, 7)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90)
        pass

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8
        pass

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width //2, frame_height //2)

class ball21x21:
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = 599
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= 5
        if self.y < 55:
            self.y = 55

    def draw(self):
        self.image.draw(self.x, self.y)
        pass


#class ball41x41:
    pass



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



def reset_world():
    global running

    running = True

    global world

    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for _ in range(11)]    # Grass 도장을 이용해서 grass 객체 생성
    world += team

    zombie = Zombie()
    world.append(zombie)

    small_ball = [ball21x21() for _ in range(10)]
    world += small_ball

    #big_ball = [ball41x41() for _ in range(10)]
    #world += big_ball

def update_world():
    for game_object in world:
        game_object.update()

    pass

def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()
    pass


open_canvas()
reset_world()
while running:
    handle_events()
    #게임 로직 실행
    update_world()
    #게임 랜더링
    render_world()
    delay(0.05)

close_canvas()