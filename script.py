import pygame
from random import randint

# CONSTANTS ------------------------------------------
FPS = 60
WIDTH = 800
HEIGHT = 600
GAME_SPEED = 4     
DISPLAY_COLOR = (230, 230, 250)
DINO_COLOR = 'yellow'
CACTUS_COLOR = 'green'



# INIT PYGAME ------------------------------------------
pygame.init()

# DISPLAY ------------------------------------------
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Run DINO!')
pygame.display.set_icon(pygame.image.load('Dino/dino.png'))

def update_dispalay():
   pygame.display.update()
   display.fill(DISPLAY_COLOR)
   

def set_fps():
   pygame.time.Clock().tick(FPS)





# DINO  ------------------------------------------
user_width = 60
user_height = 100
user_x = WIDTH // 3
user_y = HEIGHT - user_height - 100
jump_counter = 30

# draw dino
def draw_dino():
   pygame.draw.rect(display, DINO_COLOR, (user_x, user_y, user_width, user_height))
   pygame.draw.rect(display, (255, 165, 0), (user_x, user_y, user_width, user_height), 3)

# jump animation
is_make_jump = False

def is_jump():
   global is_make_jump

   keys = pygame.key.get_pressed()
   if keys[pygame.K_SPACE]:
      is_make_jump = True
   if is_make_jump:
      jump()


def jump():
   global is_make_jump, user_y, jump_counter

   if jump_counter >= -30:
      user_y -= jump_counter / 2.5
      jump_counter -= 1
   else:
      jump_counter = 30
      is_make_jump = False




# CACTUS ------------------------------------------
class Cactus:
   def __init__(self, x, y, width, height, speed):
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.speed = speed
   
   def move_cactus(self) -> bool:
      if self.x >= -self.width:
         pygame.draw.rect(display, CACTUS_COLOR, (self.x, self.y, self.width, self.height))
         pygame.draw.rect(display, (0, 128, 0), (self.x, self.y, self.width, self.height), 3)
         self.x -= self.speed
         return True
      else:
         self.x = WIDTH + 50 + randint(-30, 60)
         return False
      
   def return_cactus(self, radius):
      self.x = radius


cactus_arr = []

def create_cactuses_arr(array):
   array.append(Cactus(WIDTH + 50, HEIGHT - 50 - 100, randint(20, 60), 50, GAME_SPEED))
   array.append(Cactus(WIDTH + 300, HEIGHT - 70 - 100, randint(20, 60), 70, GAME_SPEED))
   array.append(Cactus(WIDTH + 600, HEIGHT - 37 - 100, randint(20, 60), 37, GAME_SPEED))



def find_radius(array):

   maximum = max(array[0].x, array[1].x, array[2].x)
   choise = randint(0, 5)

   if maximum < WIDTH:
      radius = WIDTH
      if radius - maximum < 50:
         radius += 50
   else:
      radius = maximum

   if choise == 0:
      radius += randint(10, 15)
   else:
      radius += randint(200, 350)

   return radius



def drow_cactus_arr(array):
   for cactus in cactus_arr:
      check = cactus.move_cactus()
      if not check:
         radius = find_radius(array)
         cactus.return_cactus(radius)

   




# RUN GAME FUNC ------------------------------------------
def run_game():
   game = True

   create_cactuses_arr(cactus_arr)

   while game:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            game = False
            pygame.quit()

      update_dispalay()
      set_fps()

      draw_dino()
      is_jump()

      drow_cactus_arr(cactus_arr)





# PLAY GAME ------------------------------------------
run_game()



git remote add origin https://github.com/Ivan2802/dino.git
git branch -M main
git push -u origin main