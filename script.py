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
DISPLAY_BACKGROUND = pygame.image.load('background.png')



# INIT PYGAME ------------------------------------------
pygame.init()

# DISPLAY ------------------------------------------
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Run DINO!')
# pygame.display.set_icon(pygame.image.load('Dino/dinoz.png'))

def update_dispalay():
   pygame.display.update()
   display.blit(DISPLAY_BACKGROUND, (0, 0))
   

def set_fps():
   pygame.time.Clock().tick(FPS)





# DINO  ------------------------------------------
user_width = 60
user_height = 100
user_x = WIDTH // 3
user_y = HEIGHT - user_height - 100
jump_counter = 30

dino_img_array = [pygame.image.load('d1.png'), pygame.image.load('d2.png'), pygame.image.load('d3.png'), pygame.image.load('d4.png'), pygame.image.load('d5.png'),]
dino_img_counter = 0

# draw dino
def draw_dino():
   pygame.draw.rect(display, DINO_COLOR, (user_x, user_y, user_width, user_height))
   pygame.draw.rect(display, (255, 165, 0), (user_x, user_y, user_width, user_height), 3)

# jump animation
is_make_jump = False

def is_jump():
   global is_make_jump, keys

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

def draw_dino_animation():
   global dino_img_counter
   if dino_img_counter == 25:
      dino_img_counter = 0
   display.blit(dino_img_array[dino_img_counter // 5], (user_x, user_y))
   dino_img_counter += 1



# CACTUS ------------------------------------------
class Object:
   def __init__(self, x, y, width, image, speed):
      self.x = x
      self.y = y
      self.width = width
      self.image = image
      self.speed = speed
   
   def move_cactus(self) -> bool:
      if self.x >= -self.width:
         # pygame.draw.rect(display, CACTUS_COLOR, (self.x, self.y, self.width, self.height))
         # pygame.draw.rect(display, (0, 128, 0), (self.x, self.y, self.width, self.height), 3)
         display.blit(self.image, (self.x, self.y))
         self.x -= self.speed
         return True
      else:
         self.x = WIDTH + 50 + randint(-30, 60)
         return False
      
   def return_self(self, radius, y, width, image):
      self.x = radius
      self.y = y
      self.width = width
      self.image = image
      display.blit(self.image, (self.x, self.y))


cactus_arr = []
cactus_options = [35, 430, 50, 420, 60, 435]
cactus_img_array = [pygame.image.load('cact1.jpg'), pygame.image.load('cact2.jpg'), pygame.image.load('cact3.jpg')]


def create_cactuses_arr(array):

   choise = randint(0, 2)
   img = cactus_img_array[choise]
   width = cactus_options[choise * 2]
   height = cactus_options[choise * 2 + 1]
   array.append(Object(WIDTH + 50, height, width, img, GAME_SPEED))

   choise = randint(0, 2)
   img = cactus_img_array[choise]
   width = cactus_options[choise * 2]
   height = cactus_options[choise * 2 + 1]
   array.append(Object(WIDTH + 50, height, width, img, GAME_SPEED))

   choise = randint(0, 2)
   img = cactus_img_array[choise]
   width = cactus_options[choise * 2]
   height = cactus_options[choise * 2 + 1]
   array.append(Object(WIDTH + 50, height, width, img, GAME_SPEED))
  



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

         choise = randint(0, 2)
         img = cactus_img_array[choise]
         width = cactus_options[choise * 2]
         height = cactus_options[choise * 2 + 1]

         cactus.return_self(radius, height, width, img)

   



# CLOUDS
cloud_img_array = [pygame.image.load('cloud1.png'), pygame.image.load('cloud2.png')]

def render_clouds():
   choise = randint(0, 1)
   img_of_cloud = cloud_img_array[choise]
   cloud =  Object(WIDTH, 80, 80, img_of_cloud, 1.4)
   return cloud

def move_cloud(cloud):
   check = cloud.move_cactus()
   if not check:
      choice = randint(0, 1)
      img_of_cloud = cloud_img_array[choice]
      cloud.return_self(WIDTH, randint(10, 200), cloud.width, img_of_cloud)


# TEXT
font = pygame.font.get_default_font()
def print_text(message, x, y, font_color = (0, 0, 0), font_size = 30):
   font_type = pygame.font.Font(pygame.font.get_default_font(), font_size)
   text = font_type.render(message, 1, font_color, None)
   display.blit(text, (x, y))

# PAUSE
def pause():
   paused = True
   while paused:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            game = False
            pygame.quit()
         
      print_text('Игра на паузе, чтобы продолжить нажмите Enter!', 30, 300)

      if keys[pygame.K_RETURN]:
         paused = False 
         
      pygame.display.update()
      set_fps()



# RUN GAME FUNC ------------------------------------------
def run_game():
   game = True

   cloud = render_clouds()
   create_cactuses_arr(cactus_arr)

   while game:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            game = False
            pygame.quit()

      update_dispalay()
      set_fps()

      # draw_dino()
      draw_dino_animation()
      is_jump()

      drow_cactus_arr(cactus_arr)

      move_cloud(cloud)

      if keys[pygame.K_ESCAPE]:
         pause()






# PLAY GAME ------------------------------------------
run_game()