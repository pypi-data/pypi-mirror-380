import os, sys, math, pygame

from .adivinhacao import jogar_adivinhacao
from .jogo_da_forca import jogo_da_forca
from .labirinto import jogar_labirinto
from .pac_man import jogar_pacman
from .snake import snake
from .space_shooter import space_shooter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

def resource_path(filename: str) -> str:
    return os.path.join(ASSETS_DIR, filename)

pygame.init()

LARGURA = 960
ALTURA = 640
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Gamehub")

icon = pygame.image.load(resource_path("icon.png"))
pygame.display.set_icon(icon)

AZUL_CEU = (135, 206, 235)
VERDE_GRAMA = (34, 139, 34)
MARROM_TERRA = (139, 69, 19)
AMARELO = (255, 255, 0)
LARANJA = (255, 165, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

fonte_media = pygame.font.Font(None, 28)
fonte_pequena = pygame.font.Font(None, 24)


class Nuvem:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade

    def mover(self):
        self.x += self.velocidade
        if self.x > LARGURA + 100:
            self.x = -100

    def desenhar(self, tela):
        pygame.draw.circle(tela, BRANCO, (int(self.x), int(self.y)), 30)
        pygame.draw.circle(tela, BRANCO, (int(self.x + 25), int(self.y)), 35)
        pygame.draw.circle(tela, BRANCO, (int(self.x + 50), int(self.y)), 30)
        pygame.draw.circle(tela, BRANCO, (int(self.x + 25), int(self.y - 20)), 25)


class Avatar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tamanho = 20

    def desenhar(self, tela):
        pygame.draw.circle(tela, (0, 180, 255), (int(self.x), int(self.y)), self.tamanho)
        pygame.draw.circle(tela, BRANCO, (int(self.x - 7), int(self.y - 6)), 5)
        pygame.draw.circle(tela, BRANCO, (int(self.x + 7), int(self.y - 6)), 5)
        pygame.draw.circle(tela, PRETO, (int(self.x - 7), int(self.y - 6)), 3)
        pygame.draw.circle(tela, PRETO, (int(self.x + 7), int(self.y - 6)), 3)
        pygame.draw.arc(tela, PRETO, (self.x - 10, self.y - 5, 20, 15),
                        math.radians(200), math.radians(340), 2)


class PontoJogo:
    def __init__(self, x, y, nome, funcao, icone_file, cor_fundo=(200, 200, 200)):
        self.x = x
        self.y = y
        self.nome = nome
        self.funcao = funcao
        self.raio = 35
        self.icone = pygame.image.load(resource_path(icone_file)).convert_alpha()
        self.icone = pygame.transform.smoothscale(self.icone, (64, 64))
        self.cor_fundo = cor_fundo

    def desenhar(self, tela, selecionado=False):
        scale = 1.2 if selecionado else (math.sin(pygame.time.get_ticks() * 0.005) + 1) / 10 + 1
        raio_animado = int(self.raio * scale)
        pygame.draw.circle(tela, BRANCO, (int(self.x), int(self.y)), raio_animado + 4)
        pygame.draw.circle(tela, self.cor_fundo, (int(self.x), int(self.y)), raio_animado)
        rect = self.icone.get_rect(center=(self.x, self.y))
        tela.blit(self.icone, rect)


def desenhar_cenario(tela, nuvens):
    tela.fill(AZUL_CEU)
    for nuvem in nuvens:
        nuvem.mover()
        nuvem.desenhar(tela)
    pontos_montanha1 = [(0, 400), (150, 300), (300, 350), (450, 280), (600, 320),
                        (LARGURA, 380), (LARGURA, ALTURA), (0, ALTURA)]
    pygame.draw.polygon(tela, (100, 100, 100), pontos_montanha1)
    pontos_montanha2 = [(200, 450), (350, 350), (500, 400), (650, 330), (800, 380),
                        (LARGURA, 420), (LARGURA, ALTURA), (200, ALTURA)]
    pygame.draw.polygon(tela, (120, 120, 120), pontos_montanha2)
    pygame.draw.rect(tela, VERDE_GRAMA, (0, ALTURA - 100, LARGURA, 100))
    arvores = [(100, ALTURA - 100), (300, ALTURA - 100), (700, ALTURA - 100), (900, ALTURA - 100)]
    for x, y in arvores:
        pygame.draw.rect(tela, MARROM_TERRA, (x - 10, y - 50, 20, 50))
        pygame.draw.circle(tela, (0, 100, 0), (x, y - 60), 30)


def main():
    clock = pygame.time.Clock()
    global tela

    pontos = [
        PontoJogo(150, 500, "Adivinhação", jogar_adivinhacao, "alvo.png", (255, 100, 100)),
        PontoJogo(300, 400, "Forca", jogo_da_forca, "forca.png", (255, 165, 0)),
        PontoJogo(500, 300, "Labirinto", jogar_labirinto, "labirinto.png", (30, 160, 70)),
        PontoJogo(700, 200, "Pac-Man", jogar_pacman, "pacman.png", (255, 255, 100)),
        PontoJogo(850, 300, "Snake", snake, "snake.png", (140, 70, 190)),
        PontoJogo(750, 450, "Space Shooter", space_shooter, "foguete.png", (100, 180, 230)),
        PontoJogo(900, 550, "Sair", None, "sair.png", (220, 50, 50)),
    ]

    current_idx = 0
    avatar = Avatar(pontos[current_idx].x, pontos[current_idx].y)
    nuvens = [Nuvem(100, 80, 0.5), Nuvem(400, 120, 0.3), Nuvem(700, 60, 0.7)]

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                if evento.key in (pygame.K_RIGHT, pygame.K_d):
                    if current_idx < len(pontos) - 1:
                        current_idx += 1
                        avatar.x = pontos[current_idx].x
                        avatar.y = pontos[current_idx].y
                elif evento.key in (pygame.K_LEFT, pygame.K_a):
                    if current_idx > 0:
                        current_idx -= 1
                        avatar.x = pontos[current_idx].x
                        avatar.y = pontos[current_idx].y
                elif evento.key == pygame.K_RETURN:
                    selected = pontos[current_idx]
                    if selected.nome == "Sair":
                        rodando = False
                    else:
                        try:
                            selected.funcao()
                            tela = pygame.display.set_mode((LARGURA, ALTURA))
                            pygame.display.set_caption("Gamehub")
                        except Exception as e:
                            print(f"Erro ao executar {selected.nome}: {e}")
                            pygame.init()
                            tela = pygame.display.set_mode((LARGURA, ALTURA))
                            pygame.display.set_caption("Gamehub")

        desenhar_cenario(tela, nuvens)
        caminhos = [
            (150, 500, 300, 400),
            (300, 400, 500, 300),
            (500, 300, 700, 200),
            (700, 200, 850, 300),
            (850, 300, 750, 450),
            (750, 450, 900, 550),
        ]
        for x1, y1, x2, y2 in caminhos:
            pygame.draw.line(tela, MARROM_TERRA, (x1, y1), (x2, y2), 8)
            pygame.draw.line(tela, AMARELO, (x1, y1), (x2, y2), 4)

        for i, p in enumerate(pontos):
            p.desenhar(tela, selecionado=(i == current_idx))

        avatar.desenhar(tela)
        nome_jogo = pontos[current_idx].nome
        if nome_jogo:
            msg = fonte_media.render(f"Selecionado: {nome_jogo}", True, BRANCO)
            tela.blit(msg, (10, ALTURA - 60))

        controles = fonte_pequena.render("Use A/D ou ← → para mover, ENTER para abrir o jogo", True, BRANCO)
        tela.blit(controles, (10, ALTURA - 30))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
