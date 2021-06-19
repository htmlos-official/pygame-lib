import pygame
pygame.init()

language = True

print("""
Langue / Language :
fr | appuyer sur 1
en | appuyer sur 2
""")

def language_fr():
    print("""
utilise 'open nomdujeu'
exemple : open snake
utilise 'view list' pour voir la liste
""")

def language_en():
  print("""
use 'open gamename'
exemple : open snake
type 'view list' to view the list
""")

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        if language == True:
          language_fr()
      if event.key == pygame.K_2:
        if language == True:
          language_en()
