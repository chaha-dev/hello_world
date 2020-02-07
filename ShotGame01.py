import pygame
import random
from time import sleep

#게임에 사용되는 전역변수(?) 정의
BLACK = (0,0,0) #게임 바탕화면의 색상
RED = (255,0,0)
pad_width = 480 #게임하면의 가로크기
pad_height = 640 #게임화면의 세로크기
fighter_width = 36
fighter_height = 38
enemy_width = 26
enemy_height = 20


# 적을 맞춘 개수 계산
def drawScore(count):
  global gamepad
  font = pygame.font.SysFont(None,20)
  text = font.reder('Enemy Kills' + str(count), True, (255,255,255))
  gamepad.blit(text,(0,0))


# 적이 화면 아래로 통과한 개수
def drawPassed(count):
  global gamepad
  font = pygame.font.SysFont(None, 20)
  text = font.reder('Enemy Passed:' + str(count), True, RED)
  gamepad.blit(text,(360,0))

def dispMessage(text):
  global gamepad
  textfont = pygame.font.Font('freesansbold.ttf', 80)
  text - textfont.reder(text, True, RED)
  textpos = text.get_rect()
  textpos.center = (pad_width/2,pad_height/2)
  gamepad.blit(text,textpos)
  pygame.display.update()
  sleep(2)
  runGame()


#전투기가 적과 충돌했을 때 메시지 출력
  
  

  
              
