import pygame
import time
import random

nome = input('Insira seu nome, integrante da Aliança Rebelde: ')
email = input('Insira seu email, para a próxima revolta contra o Império: ')

pygame.init()
largura = 800
altura = 600
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Vader Rush")
icone = pygame.image.load("assets/vaderIcon.png")
pygame.display.set_icon(icone)
xWing = pygame.image.load("assets/Xwing.png")
larguraXWing = 110
fundo = pygame.image.load("assets/fundo.jpg")
laser = pygame.image.load("assets/laser.png")
somExplosao = pygame.mixer.Sound("assets/explosao.mp3")
laserSom = pygame.mixer.Sound("assets/laserSom.mp3")
laserSom.set_volume(0.1)

def telarNave(x, y):
    gameDisplay.blit(xWing, (x, y))
def telarLaser(x, y):
    gameDisplay.blit(laser, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, white)
    return textSurface, textSurface.get_rect()



def texto(texto):
    fonte = pygame.font.Font(None, 50)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    

def placar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Pontuação de " + nome + ": " +str(contador), True, white)
    gameDisplay.blit(texto, (10, 10))

def arquivo(nome,email,desvios):
    texto = f"Pontos de {nome}: {desvios} \n{email}"
    try:
        nome_arquivo = 'pontos_de_'+nome+'.txt'
        arquivo = open(nome_arquivo, 'r+')
        arquivo.writelines(desvios)
    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w+')
        arquivo.writelines(texto)
   


def morte():
    pygame.mixer.Sound.play(somExplosao)
    pygame.mixer.music.stop()
    texto(nome + " não foi capaz de parar o Império")
  
    jogo()

def jogo():
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load("assets/musicaTatoine.mp3")
    pygame.mixer.music.play(-1)
    alturaLaser = 240
    larguraLaser = 50
    xWingEixoY = altura*0.8
    xWingEixoX = largura*0.42
    laserEixoX = random.randrange(0, largura)
    laserEixoY = -200
    movimentoX = 0
    velocidade = 30
    
    laserVelocidade = 3
   
    desvios = 0
    pygame.mixer.Sound.play(laserSom)
    while True:
        acoes = pygame.event.get()  
        
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0
       
        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))
        placar(desvios)
        laserEixoY = laserEixoY + laserVelocidade
        telarLaser(laserEixoX, laserEixoY)
        if laserEixoY > altura:
            laserEixoY = -200
            laserEixoX = random.randrange(0, largura)
            desvios = desvios+1
            laserVelocidade += 1
            pygame.mixer.Sound.play(laserSom)
        xWingEixoX += movimentoX
        if xWingEixoX < 0:
            xWingEixoX = 0
        elif xWingEixoX > largura-larguraXWing:
            xWingEixoX = largura-larguraXWing
       
        if xWingEixoY < laserEixoY + alturaLaser:
            if xWingEixoX < laserEixoX and xWingEixoX+larguraXWing > laserEixoX or laserEixoX+larguraLaser > xWingEixoX and laserEixoX+larguraLaser < xWingEixoX+larguraXWing:
                arquivo(nome,email,desvios)
                morte()
                
        telarNave(xWingEixoX, xWingEixoY)
        pygame.display.update()
        clock.tick(60) 



jogo()

