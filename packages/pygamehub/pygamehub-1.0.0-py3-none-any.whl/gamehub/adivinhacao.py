import pygame
import random

LARGURA = 960
ALTURA = 640
BRANCO = (245, 245, 245)
PRETO = (30, 30, 30)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
AZUL = (0, 100, 200)
CINZA_CLARO = (200, 200, 200)

def jogar_adivinhacao():

    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo da Adivinhação")
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 64)
    fonte_media = pygame.font.Font(None, 40)
    fonte_pequena = pygame.font.Font(None, 30)
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    palpite_atual = ""
    mensagem = "Adivinhe um número entre 1 e 100!"
    cor_mensagem = PRETO
    jogo_terminado = False
    venceu = False
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                
                elif evento.key == pygame.K_r and jogo_terminado:
                    numero_secreto = random.randint(1, 100)
                    tentativas = 0
                    palpite_atual = ""
                    mensagem = "Adivinhe um número entre 1 e 100!"
                    cor_mensagem = PRETO
                    jogo_terminado = False
                    venceu = False
                
                elif not jogo_terminado:
                    if evento.key == pygame.K_RETURN:
                        if palpite_atual:
                            try:
                                numero = int(palpite_atual)
                                tentativas += 1
                                
                                if numero == numero_secreto:
                                    mensagem = f"🎉 Você acertou em {tentativas} tentativas!"
                                    cor_mensagem = VERDE
                                    jogo_terminado = True
                                    venceu = True
                                elif numero < numero_secreto:
                                    mensagem = f"⬇️ Muito baixo! Tentativa {tentativas}/{max_tentativas}"
                                    cor_mensagem = AZUL
                                else:
                                    mensagem = f"⬆️ Muito alto! Tentativa {tentativas}/{max_tentativas}"
                                    cor_mensagem = AZUL
                                
                                if tentativas >= max_tentativas and not venceu:
                                    mensagem = f"❌ Fim de jogo! O número era {numero_secreto}"
                                    cor_mensagem = VERMELHO
                                    jogo_terminado = True
                                    
                            except ValueError:
                                mensagem = "Digite apenas números!"
                                cor_mensagem = VERMELHO
                            
                            palpite_atual = ""
                    
                    elif evento.key == pygame.K_BACKSPACE:
                        palpite_atual = palpite_atual[:-1]
                    
                    else:
                        if evento.unicode.isdigit() and len(palpite_atual) < 3:
                            palpite_atual += evento.unicode
        
        tela.fill(BRANCO)
        
        titulo = fonte.render("🎯 JOGO DA ADIVINHAÇÃO", True, PRETO)
        titulo_rect = titulo.get_rect(center=(LARGURA//2, 80))
        tela.blit(titulo, titulo_rect)
        
        mensagem_texto = fonte_media.render(mensagem, True, cor_mensagem)
        mensagem_rect = mensagem_texto.get_rect(center=(LARGURA//2, 200))
        tela.blit(mensagem_texto, mensagem_rect)
        
        if not jogo_terminado:
            entrada_texto = f"Seu palpite: {palpite_atual}"
            entrada = fonte_media.render(entrada_texto, True, PRETO)
            entrada_rect = entrada.get_rect(center=(LARGURA//2, 300))
            tela.blit(entrada, entrada_rect)
        
        info_tentativas = f"Tentativas: {tentativas}/{max_tentativas}"
        info = fonte_pequena.render(info_tentativas, True, PRETO)
        info_rect = info.get_rect(center=(LARGURA//2, 380))
        tela.blit(info, info_rect)
        
        if jogo_terminado:
            instrucoes = [
                "Pressione R para jogar novamente",
                "Pressione ESC para sair"
            ]
        else:
            instrucoes = [
                "Digite seu palpite e pressione ENTER",
                "Pressione ESC para sair"
            ]
        
        for i, instrucao in enumerate(instrucoes):
            texto = fonte_pequena.render(instrucao, True, CINZA_CLARO)
            texto_rect = texto.get_rect(center=(LARGURA//2, 480 + i * 30))
            tela.blit(texto, texto_rect)
        
        pygame.display.flip()
        clock.tick(60)
    
