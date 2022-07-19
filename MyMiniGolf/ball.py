from settings import *
from numpy import abs, sqrt
from copy import copy


class Ball():
    def __init__(self):
        self.color = (255, 255, 255)
        self.radius = 8
        self.position = pygame.math.Vector2((screen_width / 2 - self.radius / 2, screen_height - 120))
        self.startPos = copy(self.position)
        self.velocity = pygame.math.Vector2((0, 0))
        self.prevPositions = [self.position]
        self.isInBunker = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 0)

    def shoot(self, startPos, endPos):
        if self.isInBunker:
            if startPos[0] > endPos[0]:
                self.velocity.x = 20 * bunker_loss * sqrt(int(startPos[0] - endPos[0]))
            else:
                self.velocity.x = 20 * bunker_loss * -sqrt(int(endPos[0] - startPos[0]))
            if startPos[1] > endPos[1]:
                self.velocity.y = 20 * bunker_loss * sqrt(int(startPos[1] - endPos[1]))
            else:
                self.velocity.y = 20 * bunker_loss * -sqrt(int(endPos[1] - startPos[1]))
            self.isInBunker = False
        else:
            if startPos[0] - endPos[0] > 0:
                self.velocity.x = sqrt(int(startPos[0] - endPos[0]))
            else:
                self.velocity.x = -sqrt(int(endPos[0] - startPos[0]))
            if startPos[1] - endPos[1] > 0:
                self.velocity.y = sqrt(int(startPos[1] - endPos[1]))
            else:
                self.velocity.y = -sqrt(int(endPos[1] - startPos[1]))

            if abs(endPos[0] - startPos[0]) > 500:
                if endPos[0] < startPos[0]:
                    self.velocity.x = sqrt(500)
                else:
                    self.velocity.x = -sqrt(500)
            if abs(endPos[1] - startPos[1]) > 500:
                if endPos[1] < startPos[1]:
                    self.velocity.y = sqrt(500)
                else:
                    self.velocity.y = -sqrt(500)
            if abs(endPos[0] - startPos[0]) < 2 and abs(endPos[1] - startPos[1]) < 2:
                self.velocity.x = 0
                self.velocity.y = 0



        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    def update(self):
        self.velocity.x *= friction
        self.velocity.y *= friction

        if abs(self.velocity.x) < 0.8 and abs(self.velocity.y) < 0.8:
            self.velocity.x = 0
            self.velocity.y = 0

        self.edge_collision()
        if self.isGoal():
            return 'goal'
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.prevPositions.append(copy(self.position))

    #def simulate_path(self, screen, startPos, endPos):


    def edge_collision(self):
        if self.position.x + self.radius >= screen_width - edge_thickness:
            if self.velocity.x > 0:
                self.position.x = screen_width - edge_thickness - self.radius - 0.01
                self.velocity.x *= -energy_loss_factor
                self.velocity.y *= energy_loss_factor

        elif self.position.x - self.radius <= edge_thickness:
            if self.velocity.x < 0:
                self.position.x = edge_thickness + self.radius + 0.01
                self.velocity.x *= -energy_loss_factor
                self.velocity.y *= energy_loss_factor

        if self.position.y + self.radius >= screen_height - edge_thickness:
            if self.velocity.y > 0:
                self.position.y = screen_height - edge_thickness - self.radius - 0.01
                self.velocity.y *= -energy_loss_factor
                self.velocity.x *= energy_loss_factor

        elif self.position.y - self.radius <= edge_thickness:
            if self.velocity.y < 0:
                self.position.y = edge_thickness + self.radius + 0.01
                self.velocity.y *= -energy_loss_factor
                self.velocity.x *= energy_loss_factor

    def isGoal(self) -> bool:
        if self.position.x + self.radius/2 >= screen_width / 2 - 5 and self.position.x - self.radius/2 <= screen_width / 2 + 5 and self.position.y + self.radius/2 >= 75 and self.position.y - self.radius/2 <= 85 and sqrt(
                pow(self.velocity.x, 2) + pow(self.velocity.y, 2)) < 18:
            self.radius = 0
            return True

    def box_collision(self, box):
        if self.position.x + self.radius >= box.position.x and self.position.x - self.radius <= box.position.x + box.size:
            if self.position.y - self.radius <= box.position.y + box.size and self.position.y + self.radius >= box.position.y:
                if self.position.x + self.radius > box.position.x + box.size or self.position.x - self.radius < box.position.x:
                    self.velocity.x *= -energy_loss_factor
                else:
                    self.velocity.y *= -energy_loss_factor
                self.position = copy(self.prevPositions[len(self.prevPositions) - 1])

    def bunker_collision(self, bunker):
        if self.position.x + 2.5*self.radius / 4 >= bunker.position1.x - bunker.radius1 and self.position.x - 2.5*self.radius / 4 <= bunker.position1.x + bunker.radius1:
            if self.position.y + 2.5*self.radius / 4 >= bunker.position1.y - bunker.radius1 and self.position.y - 2.5*self.radius / 4 <= bunker.position1.y - bunker.radius1:
                self.velocity.x *= bunker_loss
                self.velocity.y *= bunker_loss
                self.isInBunker = True

        elif self.position.x + 2.5*self.radius / 4 >= bunker.position2.x - bunker.radius2 and self.position.x - 2.5*self.radius / 4 <= bunker.position2.x + bunker.radius2:
            if self.position.y + 2.5*self.radius / 4 >= bunker.position2.y - bunker.radius2 and self.position.y - 2.5*self.radius / 4 <= bunker.position2.y - bunker.radius2:
                self.velocity.x *= bunker_loss
                self.velocity.y *= bunker_loss
                self.isInBunker = True
    def water_collision(self, water):
        if self.position.x + self.radius / 4 >= water.position1.x - water.radius1 and self.position.x - self.radius / 4<= water.position1.x + water.radius1:
            if self.position.y + self.radius / 4 >= water.position1.y - water.radius1 and self.position.y - self.radius / 4<= water.position1.y + water.radius1:
                self.position = copy(self.startPos)
                self.velocity = pygame.math.Vector2(0, 0)

        if self.position.x + self.radius/4 >= water.position2.x - water.radius2 and self.position.x - self.radius/4 <= water.position2.x + water.radius2:
            if self.position.y + self.radius/4 >= water.position2.y - water.radius2 and self.position.y - self.radius/4 <= water.position2.y + water.radius2:
                self.position = copy(self.startPos)
                self.velocity = pygame.math.Vector2(0, 0)



