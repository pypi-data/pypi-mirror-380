import pygame
import random
from pygame.locals import *

def space_shooter():
    largura, altura = 480, 700
    vel_player = 5
    vel_tiro = -10
    atraso_inimigo = 1000

    branco = (255, 255, 255)
    preto = (0, 0, 0)
    amarelo = (255, 255, 0)
    vermelho = (255, 0, 0)

    pygame.init()
    tela_principal = pygame.display.set_mode((960, 640))
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 28)
    fonte_maior = pygame.font.SysFont(None, 48)

    tela_jogo = pygame.Surface((largura, altura))

    todos_sprites = pygame.sprite.Group()
    inimigos = pygame.sprite.Group()
    tiros = pygame.sprite.Group()

    linha_perigo = altura - 100

    nave = pygame.sprite.Sprite()
    nave.image = pygame.Surface((40, 30))
    nave.image.fill(preto)
    pygame.draw.polygon(nave.image, branco, [(0, 30), (20, 0), (40, 30)], 2)
    nave.rect = nave.image.get_rect()
    nave.rect.centerx = largura // 2
    nave.rect.bottom = (linha_perigo + altura) // 2
    nave.vidas = 3
    nave.invulneravel = 0
    todos_sprites.add(nave)

    def criar_tiro(x, y):
        tiro = pygame.sprite.Sprite()
        tiro.image = pygame.Surface((4, 12))
        tiro.image.fill(branco)
        tiro.rect = tiro.image.get_rect()
        tiro.rect.centerx = x
        tiro.rect.bottom = y
        tiro.vely = vel_tiro
        tiros.add(tiro)
        todos_sprites.add(tiro)

    def criar_inimigo():
        tipo = random.choices(["normal", "amarelo", "vermelho"], weights=[0.6, 0.3, 0.1])[0]
        tam = random.randint(20, 40)
        inimigo = pygame.sprite.Sprite()
        inimigo.image = pygame.Surface((tam, tam))
        inimigo.image.fill(preto)

        if tipo == "normal":
            cor = branco
            inimigo.vely = random.uniform(1, 2)
            inimigo.vidas = 1
            inimigo.valor = 1
        elif tipo == "amarelo":
            cor = amarelo
            inimigo.vely = random.uniform(2, 3)
            inimigo.vidas = 1
            inimigo.valor = 5
        else:
            cor = vermelho
            inimigo.vely = random.uniform(3, 4)
            inimigo.vidas = 2
            inimigo.valor = 15

        pygame.draw.rect(inimigo.image, cor, (0, 0, tam, tam), 2)
        inimigo.rect = inimigo.image.get_rect()
        inimigo.rect.x = random.randint(0, largura - inimigo.rect.width)
        inimigo.rect.y = -inimigo.rect.height
        inimigo.velx = random.uniform(-0.5, 0.5)
        inimigo.tipo = tipo
        inimigos.add(inimigo)
        todos_sprites.add(inimigo)

    SPAWNINIMIGO = USEREVENT + 1
    pygame.time.set_timer(SPAWNINIMIGO, atraso_inimigo)

    pontos = 0
    ultimo_tiro = 0
    atraso_tiro = 200

    mostrar_instrucoes = True
    usou_movimento = False
    usou_tiro = False

    def tela_gameover():
        tela_jogo.fill(preto)
        txt = fonte_maior.render("GAME OVER", True, branco)
        tela_jogo.blit(txt, txt.get_rect(center=(largura//2, altura//3)))
        txt = fonte.render(f"Pontos: {pontos}", True, branco)
        tela_jogo.blit(txt, txt.get_rect(center=(largura//2, altura//2)))
        txt = fonte.render("Pressione R para reiniciar ou ESC para sair", True, branco)
        tela_jogo.blit(txt, txt.get_rect(center=(largura//2, altura*2//3)))
        tela_principal.blit(tela_jogo, ((960 - largura)//2, (640 - altura)//2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return True
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        return False
                    if event.key == K_ESCAPE:
                        return True

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_SPACE:
                    agora = pygame.time.get_ticks()
                    if agora - ultimo_tiro > atraso_tiro:
                        criar_tiro(nave.rect.centerx, nave.rect.top)
                        ultimo_tiro = agora
                        usou_tiro = True
            elif event.type == SPAWNINIMIGO:
                criar_inimigo()

        tecla = pygame.key.get_pressed()
        if tecla[K_LEFT] or tecla[K_a]:
            nave.rect.x -= vel_player
            usou_movimento = True
        if tecla[K_RIGHT] or tecla[K_d]:
            nave.rect.x += vel_player
            usou_movimento = True
        if nave.rect.left < 0:
            nave.rect.left = 0
        if nave.rect.right > largura:
            nave.rect.right = largura

        for tiro in tiros:
            tiro.rect.y += tiro.vely
            if tiro.rect.bottom < 0:
                tiro.kill()

        for inimigo in inimigos:
            inimigo.rect.y += inimigo.vely
            inimigo.rect.x += inimigo.velx
            if inimigo.rect.top > altura:
                inimigo.kill()
            if inimigo.rect.left < -50 or inimigo.rect.right > largura + 50:
                inimigo.velx *= -1
            if inimigo.rect.bottom >= linha_perigo:
                nave.vidas -= inimigo.vidas
                inimigo.kill()
                if nave.vidas <= 0:
                    if tela_gameover():
                        return
                    inimigos.empty()
                    tiros.empty()
                    todos_sprites.empty()
                    nave.rect.centerx = largura // 2
                    nave.rect.bottom = (linha_perigo + altura) // 2
                    nave.vidas = 3
                    nave.invulneravel = 0
                    todos_sprites.add(nave)
                    pontos = 0
                    mostrar_instrucoes = True
                    usou_movimento = False
                    usou_tiro = False

        acertos = pygame.sprite.groupcollide(inimigos, tiros, False, True)
        for inimigo, tiros_atingiram in acertos.items():
            inimigo.vidas -= len(tiros_atingiram)
            if inimigo.vidas <= 0:
                pontos += inimigo.valor
                inimigo.kill()

        if nave.invulneravel > 0:
            nave.invulneravel -= 1

        tela_jogo.fill(preto)
        todos_sprites.draw(tela_jogo)

        pygame.draw.line(tela_jogo, branco, (0, linha_perigo), (largura, linha_perigo), 1)

        if mostrar_instrucoes:
            if usou_movimento and usou_tiro:
                mostrar_instrucoes = False
            else:
                instrucao1 = fonte.render("Use ← → para mover", True, branco)
                instrucao2 = fonte.render("Use ESPAÇO para atirar", True, branco)
                tela_jogo.blit(instrucao1, (largura//2 - 80, altura//2 - 30))
                tela_jogo.blit(instrucao2, (largura//2 - 100, altura//2))

        tela_principal.fill(preto)
        tela_principal.blit(tela_jogo, ((960 - largura)//2, (640 - altura)//2))
        x_offset = (960 - largura)//2
        y_offset = (640 - altura)//2
        pygame.draw.rect(tela_principal, branco, (x_offset-2, y_offset-2, largura+4, altura+4), 2)

        txt = fonte.render(f"Pontos: {pontos}", True, branco)
        tela_principal.blit(txt, (20, 20))
        txt = fonte.render(f"Vidas: {nave.vidas}", True, branco)
        tela_principal.blit(txt, (20, 50))

        pygame.display.update()
    return

