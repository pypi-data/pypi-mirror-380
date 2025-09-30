import pygame
import random

LARGURA = 960
ALTURA = 640
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 100, 200)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
AMARELO = (255, 255, 0)
CINZA = (128, 128, 128)

def jogar_labirinto():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo do Labirinto, Se Não Tiver solução, Reinicie.")
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 48)
    fonte_pequena = pygame.font.Font(None, 24)
    
    tamanho_celula = 20
    linhas = (ALTURA - 100) // tamanho_celula
    colunas = LARGURA // tamanho_celula
    
    labirinto = [[1 for _ in range(colunas)] for _ in range(linhas)]
    
    def gerar_labirinto():
        for linha in range(1, linhas-1, 2):
            for coluna in range(1, colunas-1, 2):
                labirinto[linha][coluna] = 0
                
                if random.random() < 0.7:  
                    if coluna + 2 < colunas - 1:
                        labirinto[linha][coluna + 1] = 0
                if random.random() < 0.7:
                    if linha + 2 < linhas - 1:
                        labirinto[linha + 1][coluna] = 0
        
        labirinto[1][1] = 0  
        labirinto[linhas-2][colunas-2] = 0  
        
        for _ in range(50):
            linha = random.randint(1, linhas-2)
            coluna = random.randint(1, colunas-2)
            if random.random() < 0.3:
                labirinto[linha][coluna] = 0
    
    gerar_labirinto()
    
    jogador_linha = 1
    jogador_coluna = 1
    
    objetivo_linha = linhas - 2
    objetivo_coluna = colunas - 2
    
    jogo_terminado = False
    tempo_inicio = pygame.time.get_ticks()
    movimentos = 0
    
    rodando = True
    while rodando:
        tempo_atual = pygame.time.get_ticks()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.key == pygame.K_r and jogo_terminado:
                    labirinto = [[1 for _ in range(colunas)] for _ in range(linhas)]
                    gerar_labirinto()
                    jogador_linha = 1
                    jogador_coluna = 1
                    jogo_terminado = False
                    tempo_inicio = pygame.time.get_ticks()
                    movimentos = 0
                
                elif not jogo_terminado:
                    nova_linha = jogador_linha
                    nova_coluna = jogador_coluna
                    
                    if evento.key == pygame.K_UP:
                        nova_linha -= 1
                    elif evento.key == pygame.K_DOWN:
                        nova_linha += 1
                    elif evento.key == pygame.K_LEFT:
                        nova_coluna -= 1
                    elif evento.key == pygame.K_RIGHT:
                        nova_coluna += 1
                    
                    if (0 <= nova_linha < linhas and 0 <= nova_coluna < colunas and
                        labirinto[nova_linha][nova_coluna] == 0):
                        jogador_linha = nova_linha
                        jogador_coluna = nova_coluna
                        movimentos += 1
                        
                        if jogador_linha == objetivo_linha and jogador_coluna == objetivo_coluna:
                            jogo_terminado = True
        
        tela.fill(BRANCO)
        
        titulo = fonte.render("JOGO DO LABIRINTO", True, PRETO)
        titulo_rect = titulo.get_rect(center=(LARGURA//2, 30))
        tela.blit(titulo, titulo_rect)
        
        tempo_decorrido = (tempo_atual - tempo_inicio) // 1000
        info = f"Movimentos: {movimentos} | Tempo: {tempo_decorrido}s"
        info_texto = fonte_pequena.render(info, True, PRETO)
        info_rect = info_texto.get_rect(center=(LARGURA//2, 70))
        tela.blit(info_texto, info_rect)
        
        offset_y = 100
        for linha in range(linhas):
            for coluna in range(colunas):
                x = coluna * tamanho_celula
                y = linha * tamanho_celula + offset_y
                rect = pygame.Rect(x, y, tamanho_celula, tamanho_celula)
                
                if labirinto[linha][coluna] == 1:
                    pygame.draw.rect(tela, PRETO, rect)
                else:
                    pygame.draw.rect(tela, BRANCO, rect)
                    pygame.draw.rect(tela, CINZA, rect, 1)
        
        obj_x = objetivo_coluna * tamanho_celula
        obj_y = objetivo_linha * tamanho_celula + offset_y
        obj_rect = pygame.Rect(obj_x, obj_y, tamanho_celula, tamanho_celula)
        pygame.draw.rect(tela, AMARELO, obj_rect)
        pygame.draw.rect(tela, PRETO, obj_rect, 2)
        
        jog_x = jogador_coluna * tamanho_celula
        jog_y = jogador_linha * tamanho_celula + offset_y
        jog_rect = pygame.Rect(jog_x, jog_y, tamanho_celula, tamanho_celula)
        pygame.draw.rect(tela, AZUL, jog_rect)
        pygame.draw.rect(tela, PRETO, jog_rect, 2)
        
        if jogo_terminado:
            tempo_final = (tempo_atual - tempo_inicio) // 1000
            mensagem = f"PARABÉNS! Completou em {movimentos} movimentos e {tempo_final} segundos!"
            mensagem_texto = fonte_pequena.render(mensagem, True, VERDE)
            mensagem_rect = mensagem_texto.get_rect(center=(LARGURA//2, ALTURA - 60))
            tela.blit(mensagem_texto, mensagem_rect)
            
            instrucao = "Pressione R para jogar novamente ou ESC para voltar ao menu"
            instrucao_texto = fonte_pequena.render(instrucao, True, AZUL)
            instrucao_rect = instrucao_texto.get_rect(center=(LARGURA//2, ALTURA - 30))
            tela.blit(instrucao_texto, instrucao_rect)
        else:
            instrucao = "Use as setas para mover | Chegue ao quadrado amarelo | ESC para voltar"
            instrucao_texto = fonte_pequena.render(instrucao, True, AZUL)
            instrucao_rect = instrucao_texto.get_rect(center=(LARGURA//2, ALTURA - 30))
            tela.blit(instrucao_texto, instrucao_rect)
        
        pygame.display.flip()
        clock.tick(60)
    

