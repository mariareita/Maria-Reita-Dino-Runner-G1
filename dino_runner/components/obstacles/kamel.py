from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import KAMEL 


class Kamel(Obstacle):
    def __init__(self):
        super().__init__(KAMEL[0], pos_y= 270)