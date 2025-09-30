import pygame
from pygame.locals import *
from random import choice

branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 200, 0)
vermelho = (220, 0, 0)
azul = (0, 0, 200)

largura = 960
altura = 640

def desenho_erro(tela, erros):
    if erros >= 1:
        pygame.draw.circle(tela, preto, (170, 200), 30, 8)
    if erros >= 2:
        pygame.draw.line(tela, preto, (170, 230), (170, 300), 8)
    if erros >= 3:
        pygame.draw.line(tela, preto, (170, 230), (200, 280), 8)
    if erros >= 4:
        pygame.draw.line(tela, preto, (170, 230), (140, 280), 8)
    if erros >= 5:
        pygame.draw.line(tela, preto, (170, 300), (200, 350), 8)
    if erros == 6:
        pygame.draw.line(tela, preto, (170, 300), (140, 350), 8)

def alpha_verify(string):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if string in alphabet:
        return True
    return False

def jogo_da_forca():
    pygame.init()
    pygame.display.set_caption('Jogo da Forca')
    tela = pygame.display.set_mode((largura, altura))
    
    # fontes organizadas
    fonte_palavra = pygame.font.SysFont("Arial", 70, True, False)
    fonte_media = pygame.font.SysFont("Arial", 40, True, False)
    fonte_pequena = pygame.font.SysFont("Arial", 30, True, False)
    
    clock = pygame.time.Clock()
    erros = 0

    palavras = [
        "ABACAXI", "GIRASSOL", "TARTARUGA", "ESFINGE",
        "PIRAMIDE", "CACHOEIRA", "LABIRINTO", "VASSOURA",
        "RELOGIO", "FOGUETE"
    ]

    palavra_escolhida = choice(palavras)
    palpites = ''
    fim = False
    venceu = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
                return

            if event.type == KEYDOWN:
                letra = str(pygame.key.name(event.key)).upper()
                if fim:
                    if letra == 'R':
                        palavra_escolhida = choice(palavras)
                        erros = 0
                        palpites = ''
                        fim = False
                        venceu = False

                elif alpha_verify(letra) and letra not in palpites:
                    palpites += letra + ' '
                    if letra not in palavra_escolhida:
                        erros += 1

        display_palavra = ''
        for l in palavra_escolhida:
            if l in palpites:
                display_palavra += l + ' '
            else:
                display_palavra += '_ '

        if erros == 6:
            fim = True
            venceu = False
        elif display_palavra.split() == list(palavra_escolhida):
            fim = True
            venceu = True

        tela.fill(branco)

        pygame.draw.line(tela, preto, (70, 120), (70, 440), 10)
        pygame.draw.line(tela, preto, (30, 440), (110, 440), 10)
        pygame.draw.line(tela, preto, (70, 120), (170, 120), 10)
        pygame.draw.line(tela, preto, (170, 120), (170, 170), 10)
        desenho_erro(tela, erros)

        display_palavra_surface = fonte_palavra.render(display_palavra, True, preto)
        display_palavra_rect = display_palavra_surface.get_rect(center=(largura//2, 400))
        tela.blit(display_palavra_surface, display_palavra_rect)

        if len(palpites) > 0:
            display_palpites = fonte_media.render(f'Palpites: {palpites}', True, preto)
            tela.blit(display_palpites, (50, 50))

        if fim:
            if venceu:
                msg = "VOCÊ VENCEU!"
                display_fim = fonte_media.render(msg, True, verde)
                display_fim_rect = display_fim.get_rect(center=(largura//2, 200))
                tela.blit(display_fim, display_fim_rect)
            else:
                msg = "VOCÊ PERDEU!"
                display_fim = fonte_media.render(msg, True, vermelho)
                display_fim_rect = display_fim.get_rect(center=(largura//2, 200))
                tela.blit(display_fim, display_fim_rect)

                msg_palavra = f"A palavra era: {palavra_escolhida}"
                display_palavra_correta = fonte_pequena.render(msg_palavra, True, vermelho)
                display_palavra_correta_rect = display_palavra_correta.get_rect(center=(largura//2, 250))
                tela.blit(display_palavra_correta, display_palavra_correta_rect)

            display_instr = "Pressione R para reiniciar"
            display_instr_render = fonte_pequena.render(display_instr, True, azul)
            display_instr_rect = display_instr_render.get_rect(center=(largura//2, 550))
            tela.blit(display_instr_render, display_instr_rect)

        display_esc = 'Pressione ESC para voltar ao menu'
        display_esc_render = fonte_pequena.render(display_esc, True, azul)
        display_esc_rect = display_esc_render.get_rect(center=(largura//2, 590))
        tela.blit(display_esc_render, display_esc_rect)

        clock.tick(60)
        pygame.display.update()

