import pygame
import random

LARGURA = 960
ALTURA = 640
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
ROSA = (255, 192, 203)
LARANJA = (255, 165, 0)

TAMANHO_CELULA = 20

MAPAS = [
    [
        "####################",
        "#........##........#",
        "#.##.###.##.###.##.#",
        "#..................#",
        "#.##.#.######.#.##.#",
        "#....#...##...#....#",
        "####.###.##.###.####",
        "   #.#........#.#   ",
        "####.#.###.##.#.####",
        "#......#   #......#",
        "####.#.#   #.#.####",
        "   #.#.#####.#.#   ",
        "####.#.......#.####",
        "#......#####......#",
        "#.##.#.......#.##.#",
        "#..#.##.###.##.#..#",
        "##.#....###....#.##",
        "#......#   #......#",
        "#.####.#####.####.#",
        "#..................#",
        "####################"
    ],

    [
        "####################",
        "#..................#",
        "#.####.######.####.#",
        "#.#..#........#..#.#",
        "#.#..#.##..##.#..#.#",
        "#......##..##......#",
        "######.##..##.######",
        "     #............##",
        "######.##.##.##.######",
        "#......##....##......#",
        "#.####.########.####.#",
        "#.#..#..........#..#.#",
        "#.#..#.########.#..#.#",
        "#......#......#......#",
        "########.####.########",
        "#........####........#",
        "#.######......######.#",
        "#.#....########....#.#",
        "#.#.##..........##.#.#",
        "#...##.########.##...#",
        "####################"
    ]
]

def jogar_pacman():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pac-Man")
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 48)
    fonte_pequena = pygame.font.Font(None, 24)
    
    mapa_atual = 0
    mapa = [list(linha) for linha in MAPAS[mapa_atual]]
    
    pacman_x, pacman_y = 0, 0
    for y, linha in enumerate(mapa):
        for x, celula in enumerate(linha):
            if celula == '.':
                pacman_x, pacman_y = x, y
                break
        if pacman_x > 0:
            break
    
    pacman_dir = (0, 0)
    proxima_dir = (0, 0)
    
    fantasmas = []
    cores = [VERMELHO, ROSA, LARANJA]
    tipos = ['perseguidor', 'aleatorio', 'aleatorio']
    
    for i in range(3):
        while True:
            x = random.randint(1, len(mapa[0]) - 2)
            y = random.randint(1, len(mapa) - 2)
            if mapa[y][x] != '#':
                fantasmas.append({
                    'x': x, 'y': y, 'cor': cores[i], 'tipo': tipos[i],
                    'contador': 0
                })
                break
    
    pontuacao = 0
    vidas = 3
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
                    mapa_atual = 0
                    mapa = [list(linha) for linha in MAPAS[mapa_atual]]
                    
                    for y, linha in enumerate(mapa):
                        for x, celula in enumerate(linha):
                            if celula == '.':
                                pacman_x, pacman_y = x, y
                                break
                        if pacman_x > 0:
                            break
                    
                    pacman_dir = (0, 0)
                    proxima_dir = (0, 0)
                    
                    fantasmas = []
                    for i in range(3):
                        while True:
                            x = random.randint(1, len(mapa[0]) - 2)
                            y = random.randint(1, len(mapa) - 2)
                            if mapa[y][x] != '#':
                                fantasmas.append({
                                    'x': x, 'y': y, 'cor': cores[i], 'tipo': tipos[i],
                                    'contador': 0
                                })
                                break
                    
                    pontuacao = 0
                    vidas = 3
                    jogo_terminado = False
                    venceu = False
                
                elif not jogo_terminado:
                    if evento.key == pygame.K_UP:
                        proxima_dir = (0, -1)
                    elif evento.key == pygame.K_DOWN:
                        proxima_dir = (0, 1)
                    elif evento.key == pygame.K_LEFT:
                        proxima_dir = (-1, 0)
                    elif evento.key == pygame.K_RIGHT:
                        proxima_dir = (1, 0)
        
        if not jogo_terminado:
            nova_x = pacman_x + proxima_dir[0]
            nova_y = pacman_y + proxima_dir[1]
            
            if (0 <= nova_y < len(mapa) and 0 <= nova_x < len(mapa[0]) and 
                mapa[nova_y][nova_x] != '#'):
                pacman_dir = proxima_dir
            
            nova_x = pacman_x + pacman_dir[0]
            nova_y = pacman_y + pacman_dir[1]
            
            if (0 <= nova_y < len(mapa) and 0 <= nova_x < len(mapa[0]) and 
                mapa[nova_y][nova_x] != '#'):
                pacman_x, pacman_y = nova_x, nova_y
            
            if mapa[pacman_y][pacman_x] == '.':
                mapa[pacman_y][pacman_x] = ' '
                pontuacao += 10
            
            if not any('.' in linha for linha in mapa):
                mapa_atual = (mapa_atual + 1) % len(MAPAS)
                if mapa_atual == 0:  
                    venceu = True
                    jogo_terminado = True
                else:
                    mapa = [list(linha) for linha in MAPAS[mapa_atual]]
                    for y, linha in enumerate(mapa):
                        for x, celula in enumerate(linha):
                            if celula == '.':
                                pacman_x, pacman_y = x, y
                                break
                        if pacman_x > 0:
                            break
                    
                    fantasmas = []
                    for i in range(3):
                        while True:
                            x = random.randint(1, len(mapa[0]) - 2)
                            y = random.randint(1, len(mapa) - 2)
                            if mapa[y][x] != '#':
                                fantasmas.append({
                                    'x': x, 'y': y, 'cor': cores[i], 'tipo': tipos[i],
                                    'contador': 0
                                })
                                break
            

            for fantasma in fantasmas:
                fantasma['contador'] += 1
                
                if fantasma['contador'] % 3 != 0:  
                    continue
                
                if fantasma['tipo'] == 'perseguidor':
                    direcoes = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                    melhor_dir = None
                    menor_dist = float('inf')
                    
                    for direcao in direcoes:
                        nova_x = fantasma['x'] + direcao[0]
                        nova_y = fantasma['y'] + direcao[1]
                        
                        if (0 <= nova_y < len(mapa) and 0 <= nova_x < len(mapa[0]) and 
                            mapa[nova_y][nova_x] != '#'):
                            dist = abs(nova_x - pacman_x) + abs(nova_y - pacman_y)
                            if dist < menor_dist:
                                menor_dist = dist
                                melhor_dir = direcao
                    
                    if melhor_dir:
                        fantasma['x'] += melhor_dir[0]
                        fantasma['y'] += melhor_dir[1]
                else:
                    direcoes = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                    random.shuffle(direcoes)
                    
                    for direcao in direcoes:
                        nova_x = fantasma['x'] + direcao[0]
                        nova_y = fantasma['y'] + direcao[1]
                        
                        if (0 <= nova_y < len(mapa) and 0 <= nova_x < len(mapa[0]) and 
                            mapa[nova_y][nova_x] != '#'):
                            fantasma['x'] = nova_x
                            fantasma['y'] = nova_y
                            break
            
            for fantasma in fantasmas:
                if pacman_x == fantasma['x'] and pacman_y == fantasma['y']:
                    vidas -= 1
                    if vidas <= 0:
                        jogo_terminado = True
                    else:
                        for y, linha in enumerate(mapa):
                            for x, celula in enumerate(linha):
                                if celula == '.' or celula == ' ':
                                    pacman_x, pacman_y = x, y
                                    break
                            if pacman_x > 0:
                                break
                        
                        for i, fantasma in enumerate(fantasmas):
                            while True:
                                x = random.randint(1, len(mapa[0]) - 2)
                                y = random.randint(1, len(mapa) - 2)
                                if mapa[y][x] != '#':
                                    fantasma['x'], fantasma['y'] = x, y
                                    break
                    break
        
        tela.fill(PRETO)
        
        largura_mapa = len(mapa[0]) * TAMANHO_CELULA
        offset_x = (LARGURA - largura_mapa) // 2
        offset_y = 80
        
        for y, linha in enumerate(mapa):
            for x, celula in enumerate(linha):
                x_pixel = offset_x + x * TAMANHO_CELULA
                y_pixel = offset_y + y * TAMANHO_CELULA
                
                if celula == '#':
                    pygame.draw.rect(tela, AZUL, 
                                   (x_pixel, y_pixel, TAMANHO_CELULA, TAMANHO_CELULA))
                elif celula == '.':
                    pygame.draw.circle(tela, BRANCO, 
                                     (x_pixel + TAMANHO_CELULA//2, y_pixel + TAMANHO_CELULA//2), 2)
        
        x_pixel = offset_x + pacman_x * TAMANHO_CELULA + TAMANHO_CELULA // 2
        y_pixel = offset_y + pacman_y * TAMANHO_CELULA + TAMANHO_CELULA // 2
        pygame.draw.circle(tela, AMARELO, (x_pixel, y_pixel), TAMANHO_CELULA // 2 - 2)
        
        for fantasma in fantasmas:
            x_pixel = offset_x + fantasma['x'] * TAMANHO_CELULA + TAMANHO_CELULA // 2
            y_pixel = offset_y + fantasma['y'] * TAMANHO_CELULA + TAMANHO_CELULA // 2
            pygame.draw.circle(tela, fantasma['cor'], (x_pixel, y_pixel), TAMANHO_CELULA // 2 - 2)
        
        titulo = fonte.render("PAC-MAN", True, AMARELO)
        titulo_rect = titulo.get_rect(center=(LARGURA//2, 30))
        tela.blit(titulo, titulo_rect)
        
        info = f"Pontos: {pontuacao} | Vidas: {vidas} | Fase: {mapa_atual + 1}"
        info_texto = fonte_pequena.render(info, True, BRANCO)
        tela.blit(info_texto, (20, 50))
        
        if jogo_terminado:
            if venceu:
                mensagem = "PARABÉNS! Você completou todos os mapas!"
                cor = AMARELO
            else:
                mensagem = "GAME OVER!"
                cor = VERMELHO
            
            mensagem_texto = fonte.render(mensagem, True, cor)
            mensagem_rect = mensagem_texto.get_rect(center=(LARGURA//2, ALTURA - 80))
            tela.blit(mensagem_texto, mensagem_rect)
            
            instrucao = "Pressione R para jogar novamente ou ESC para voltar ao menu"
            instrucao_texto = fonte_pequena.render(instrucao, True, BRANCO)
            instrucao_rect = instrucao_texto.get_rect(center=(LARGURA//2, ALTURA - 50))
            tela.blit(instrucao_texto, instrucao_rect)
        else:
            instrucao = "Use as setas para mover | ESC para voltar ao menu"
            instrucao_texto = fonte_pequena.render(instrucao, True, BRANCO)
            instrucao_rect = instrucao_texto.get_rect(center=(LARGURA//2, ALTURA - 30))
            tela.blit(instrucao_texto, instrucao_rect)
        
        pygame.display.flip()
        clock.tick(10)
    
