import pygame, time, random


class Ball:
    def __init__(self, screen, color, x_start, y_start, radius, speed):
        self.sc = screen
        self.w, self.h = pygame.display.get_surface().get_size()
        self.color = color
        self.radius = radius
        self.speed = speed
        pygame.draw.circle(self.sc, self.color, (x_start, y_start), self.radius)
        self.x_pos = x_start
        self.y_pos = y_start
        self.x = - speed
        self.y = - speed

    def draw(self):
        pygame.draw.circle(self.sc, self.color, (self.x_pos, self.y_pos), self.radius)
        self.x_pos += self.x
        self.y_pos += self.y

        if self.x_pos - self.radius <= 0:
            self.x = self.speed
        if self.x_pos + self.radius >= self.w:
            self.x = - self.speed
        if self.y_pos - self.radius <= 0:
            self.y = self.speed
        if self.y_pos + self.radius >= self.h:
            self.y = - self.speed


pygame.init()
sc = pygame.display.set_mode((500, 500))
running = True
sc.fill((0, 0, 0))
fps = 30
pygame.display.set_caption('Balls')
clock = pygame.time.Clock()

balls = []
с = 10
s = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            balls.append(Ball(sc, (255, 255, 255), x, y, с, s))
    sc.fill((0, 0, 0))
    for ball in balls:
        ball.draw()
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
