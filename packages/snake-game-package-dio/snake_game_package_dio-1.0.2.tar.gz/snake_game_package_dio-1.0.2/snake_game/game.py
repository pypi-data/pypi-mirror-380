import pygame
import sys
import random
import pkgutil
import io

# ==================== CONFIGURAÇÕES ====================
LARGURA, ALTURA = 600, 400
TAMANHO_QUADRADO = 20

VERDE_NEON    = (57, 255, 20)
AZUL_CIANA    = (0, 180, 255)
AZUL_NEON     = (0, 255, 255)
ROSA          = (255, 100, 180)
VERMELHO      = (255, 0, 0)
VERMELHO_NEON = (255, 0, 60)
ROXO          = (180, 50, 255)
ROXO_NEON     = (180, 0, 255)
BRANCO        = (255, 255, 255)
CINZA_ESCURO  = (20, 20, 20)

NUM_PARTICULAS = 60

CONTADOR_PASSOS = 0
INTERVALO_PASSOS = 5

# ==================== FUNÇÃO PARA CARREGAR SONS ====================
def carregar_som(caminho):
    try:
        dados = pkgutil.get_data("snake_game", caminho)
        if dados:
            return pygame.mixer.Sound(io.BytesIO(dados))
    except Exception as e:
        print(f"Erro ao carregar som {caminho}: {e}")
    return None

# ==================== UTILIDADES ====================
def gerar_comida(largura, altura, tamanho, cobra=None):
    while True:
        x = random.randint(0, (largura - tamanho) // tamanho) * tamanho
        y = random.randint(0, (altura - tamanho) // tamanho) * tamanho
        if cobra is None or [x, y] not in cobra:
            return [x, y]

def cobra_comeu_comida(cabeca, comida, tamanho=TAMANHO_QUADRADO):
    cabeca_rect = pygame.Rect(cabeca[0], cabeca[1], tamanho, tamanho)
    comida_rect = pygame.Rect(comida[0], comida[1], tamanho, tamanho)
    return cabeca_rect.colliderect(comida_rect)

def desenhar_cobra(tela, cobra, contador):
    for i, bloco in enumerate(cobra):
        cor = VERDE_NEON if i % 2 == 0 else AZUL_NEON
        brilho = (abs((contador*5)%100-50)*2)
        cor_pulsante = tuple(min(255,max(0,c+brilho)) for c in cor)
        pygame.draw.rect(tela, cor_pulsante, [bloco[0], bloco[1], TAMANHO_QUADRADO, TAMANHO_QUADRADO], border_radius=6)

def desenhar_comida(tela, comida, contador):
    x,y = comida
    brilho = (abs((contador*8)%100-50)*2)
    cor_pulsante = tuple(min(255,max(0,c+brilho)) for c in ROXO_NEON)
    pygame.draw.circle(tela, cor_pulsante, (x+TAMANHO_QUADRADO//2, y+TAMANHO_QUADRADO//2), TAMANHO_QUADRADO//2)
    pygame.draw.circle(tela, BRANCO, (x+TAMANHO_QUADRADO//2, y+TAMANHO_QUADRADO//2), TAMANHO_QUADRADO//4, 1)

def mostrar_placar(tela, fonte, pontos):
    texto = fonte.render(f"Pontuação: {pontos}", True, BRANCO)
    tela.blit(texto, (10,10))

def desenhar_botao(tela, texto, fonte, x, y, largura, altura, cor_normal, cor_hover):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    acao = False

    deslocamento_sombra = 3
    cor_sombra_botao = CINZA_ESCURO
    pygame.draw.rect(tela, cor_sombra_botao, (x + deslocamento_sombra, y + deslocamento_sombra, largura, altura), border_radius=10)

    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(tela, cor_hover, (x, y, largura, altura), border_radius=10)
        if click[0] == 1:
            acao = True
    else:
        pygame.draw.rect(tela, cor_normal, (x, y, largura, altura), border_radius=10)

    texto_sombra = fonte.render(texto, True, CINZA_ESCURO) 
    texto_normal = fonte.render(texto, True, BRANCO)

    texto_x = x + (largura - texto_normal.get_width()) // 2
    texto_y = y + (altura - texto_normal.get_height()) // 2

    tela.blit(texto_sombra, (texto_x + 2, texto_y + 2))
    tela.blit(texto_normal, (texto_x, texto_y))

    return acao

# ==================== FUNDO ESTRADA ANIMADO ====================
offset_linhas = 0

def desenhar_fundo_estrada_synthwave(tela):
    global offset_linhas

    for y in range(ALTURA):
        ratio = y / ALTURA
        r = int(255*(1-ratio)*0.8 + 50*ratio)
        g = int(100*(1-ratio)*0.5 + 0*ratio)
        b = int(180*(1-ratio)*0.7 + 30*ratio)
        pygame.draw.line(tela, (r,g,b), (0,y), (LARGURA,y))

    centro_x = LARGURA // 2
    sol_y = ALTURA//2.2
    raio_sol = 50
    pygame.draw.circle(tela, ROSA, (centro_x, sol_y), raio_sol)

    cor_montanha = (50, 0, 80)
    montanhas = [
        [(0, ALTURA//2+50), (100, ALTURA//2-20), (200, ALTURA//2+50)],
        [(150, ALTURA//2+50), (300, ALTURA//2-40), (450, ALTURA//2+50)],
        [(ALTURA, ALTURA//2+50), (500, ALTURA//2-30), (LARGURA, ALTURA//2+50)]
    ]
    for pontos in montanhas:
        pygame.draw.polygon(tela, cor_montanha, pontos)

    horizonte_y = ALTURA//2 + 50
    centro_x = LARGURA//2
    linhas_horizontais = 20
    linhas_verticais = 20

    offset_linhas = (offset_linhas + 4) % 100

    for i in range(linhas_horizontais):
        y = horizonte_y + ((i*20 + offset_linhas) % (ALTURA - horizonte_y))
        largura_estrada = LARGURA * ((y - horizonte_y)/(ALTURA - horizonte_y))
        x_inicio = centro_x - largura_estrada//2
        x_fim = centro_x + largura_estrada//2
        pygame.draw.line(tela, AZUL_CIANA, (x_inicio, y), (x_fim, y), 2)

    for i in range(-linhas_verticais//2, linhas_verticais//2 + 1):
        x_offset = i * 30
        pygame.draw.line(tela, AZUL_CIANA, (centro_x + x_offset, ALTURA), (centro_x, horizonte_y), 1)

    for _ in range(NUM_PARTICULAS):
        x = random.randint(0,LARGURA)
        y = random.randint(0,horizonte_y)
        pygame.draw.circle(tela, ROXO, (x,y), 1)

# ==================== MENU ====================
def menu_inicial(tela, fonte_grande, fonte_botao, musica_ligada=True):
    contador = 0
    while True:
        desenhar_fundo_estrada_synthwave(tela)
        titulo = fonte_grande.render("JOGO DA COBRINHA", True, VERDE_NEON)
        tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 60))

        if desenhar_botao(tela, "Fácil", fonte_botao, LARGURA//2-80,130,160,50, AZUL_NEON, VERDE_NEON): return 8, musica_ligada
        if desenhar_botao(tela, "Médio", fonte_botao, LARGURA//2-80,190,160,50, AZUL_NEON, VERDE_NEON): return 12, musica_ligada
        if desenhar_botao(tela, "Difícil", fonte_botao, LARGURA//2-80,250,160,50, AZUL_NEON, VERDE_NEON): return 18, musica_ligada

        if desenhar_botao(tela, f"Som: {'ON' if musica_ligada else 'OFF'}", fonte_botao, LARGURA-155,10,140,35, ROXO_NEON, VERMELHO_NEON):
            musica_ligada = not musica_ligada
            if musica_ligada: pygame.mixer.music.unpause()
            else: pygame.mixer.music.pause()

        if desenhar_botao(tela, "Sair", fonte_botao, LARGURA//2-80,320,160,50, VERMELHO_NEON, VERMELHO):
            pygame.quit(); sys.exit()

        pygame.display.update()
        contador += 1
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()

# ==================== GAME OVER ====================
def game_over(tela, fonte_grande, fonte_botao, pontos):
    contador = 0
    while True:
        desenhar_fundo_estrada_synthwave(tela)
        msg = fonte_grande.render("VOCÊ PERDEU :(", True, BRANCO)
        score = fonte_grande.render(f"Pontuação: {pontos}", True, BRANCO)
        tela.blit(msg,(LARGURA//2 - msg.get_width()//2, 120))
        tela.blit(score,(LARGURA//2 - score.get_width()//2, 180))
        if desenhar_botao(tela, "Jogar", fonte_grande, LARGURA//2-80,250,160,50, AZUL_NEON, VERDE_NEON): return True
        if desenhar_botao(tela, "Sair", fonte_grande, LARGURA//2-80,320,160,50, VERMELHO_NEON, VERMELHO): pygame.quit(); sys.exit()
        pygame.display.update()
        contador += 1
        for e in pygame.event.get():
            if e.type==pygame.QUIT: pygame.quit(); sys.exit()

# ==================== JOGO ====================
def main():
    global CONTADOR_PASSOS

    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))  # Janela padrão, permite maximizar
    pygame.display.set_caption("Jogo da Cobrinha")
    clock = pygame.time.Clock()
    pygame.mixer.init()

    # Sons
    som_comida = carregar_som("assets/sounds/som_comer.wav")
    som_crash  = carregar_som("assets/sounds/som_fim_jogo.wav")
    som_passo  = carregar_som("assets/sounds/som_passo.wav")

    # Música de fundo
    try:
        dados_musica = pkgutil.get_data("snake_game", "assets/sounds/som_fundo.wav")
        if dados_musica:
            pygame.mixer.music.load(io.BytesIO(dados_musica))
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Erro ao carregar música de fundo: {e}")

    fonte = pygame.font.SysFont("Courier New", 24, bold=True)
    fonte_grande = pygame.font.SysFont("Courier New", 32, bold=True)
    fonte_botao = pygame.font.SysFont("Courier New", 26, bold=True)

    velocidade, musica_ligada = menu_inicial(tela, fonte_grande, fonte_botao)

    contador = 0

    while True:
        cobra = [[100,50]]
        direcao = "DIREITA"
        comida = gerar_comida(LARGURA, ALTURA, TAMANHO_QUADRADO, cobra)
        pontos = 0
        jogando = True

        while jogando:
            contador += 1
            for e in pygame.event.get():
                if e.type==pygame.QUIT: pygame.quit(); sys.exit()
                elif e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_UP and direcao!="BAIXO": direcao="CIMA"
                    elif e.key==pygame.K_DOWN and direcao!="CIMA": direcao="BAIXO"
                    elif e.key==pygame.K_LEFT and direcao!="DIREITA": direcao="ESQUERDA"
                    elif e.key==pygame.K_RIGHT and direcao!="ESQUERDA": direcao="DIREITA"
                    elif e.key==pygame.K_m:
                        musica_ligada = not musica_ligada
                        if musica_ligada: pygame.mixer.music.unpause()
                        else: pygame.mixer.music.pause()

            x,y = cobra[0]
            if direcao=="CIMA": y-=TAMANHO_QUADRADO
            elif direcao=="BAIXO": y+=TAMANHO_QUADRADO
            elif direcao=="ESQUERDA": x-=TAMANHO_QUADRADO
            elif direcao=="DIREITA": x+=TAMANHO_QUADRADO
            nova_cabeca = [x,y]
            cobra.insert(0,nova_cabeca)

            # Som do passo com intervalo
            CONTADOR_PASSOS += 1
            if CONTADOR_PASSOS >= INTERVALO_PASSOS:
                if som_passo:
                    som_passo.stop()
                    som_passo.play()
                CONTADOR_PASSOS = 0

            if cobra_comeu_comida(cobra[0], comida):
                pontos += 10
                comida = gerar_comida(LARGURA, ALTURA, TAMANHO_QUADRADO, cobra)
                if som_comida: som_comida.play()
            else:
                cobra.pop()

            if x<0 or x>=LARGURA or y<0 or y>=ALTURA or nova_cabeca in cobra[1:]:
                if som_crash: som_crash.play()
                pygame.time.delay(500)
                jogando = not game_over(tela, fonte_grande, fonte_botao, pontos)

            desenhar_fundo_estrada_synthwave(tela)
            desenhar_cobra(tela, cobra, contador)
            desenhar_comida(tela, comida, contador)
            mostrar_placar(tela, fonte, pontos)

            if desenhar_botao(tela, f"Som: {'ON' if musica_ligada else 'OFF'}", fonte_botao, LARGURA-155,10,140,35, ROXO_NEON, VERMELHO_NEON):
                musica_ligada = not musica_ligada
                if musica_ligada: pygame.mixer.music.unpause()
                else: pygame.mixer.music.pause()

            pygame.display.update()
            clock.tick(velocidade)

if __name__ == "__main__":
    main()
