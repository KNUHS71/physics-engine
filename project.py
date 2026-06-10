import pygame
import math

pygame.init()
WIDTH, HEIGHT = 1500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("포물선 시뮬레이터 (V를 눌러 리셋)")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

gravity = 0.5
launch_angle = 70
power = 24
ball_pos = [50, 550]
velocity = [0, 0]
launched = False
path = []

def launch():
    rad = math.radians(launch_angle)
    vx = power * math.cos(rad)
    vy = -power * math.sin(rad)
    return [vx, vy] 

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not launched:
                velocity = launch()
                launched = True
            
            # --- 리셋 코드 추가 시작 ---
            # V 키: 초기화 (발사 중이든 발사가 끝났든 상관없이 처음으로)
            if event.key == pygame.K_v:
                ball_pos = [50, 550]  # 초기 위치로
                velocity = [0, 0]      # 속도 0으로
                launched = False       # 발사 전 상태로
                path = []              # 그려진 궤적 싹 지우기
    

    if launched:
        velocity[1] += gravity
        ball_pos[0] += velocity[0]
        ball_pos[1] += velocity[1]
        path.append((int(ball_pos[0]), int(ball_pos[1])))
        
        if ball_pos[1] >= 550:
            ball_pos[1] = 550
            launched = False
            velocity = [0, 0]

    # 5. 그리기
    line_len = 100
    line_x = 50 + math.cos(math.radians(launch_angle)) * line_len
    line_y = 550 - math.sin(math.radians(launch_angle)) * line_len
    pygame.draw.line(screen, BLACK, (50, 550), (line_x, line_y), 2)

    for p in path:
        pygame.draw.circle(screen, RED, p, 2)

    pygame.draw.circle(screen, BLUE, (int(ball_pos[0]), int(ball_pos[1])), 15)

    font = pygame.font.SysFont(None, 30)
    # 안내 문구에 V 리셋 안내 추가
    img = font.render(f"Angle: {launch_angle}  Power: {power} (SPACE: Launch / V: Reset)", True, BLACK)
    screen.blit(img, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()