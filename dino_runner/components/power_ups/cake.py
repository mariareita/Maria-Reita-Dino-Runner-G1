from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import CAKE, CAKE_TYPE


class Cake(PowerUp):
    def __init__(self):
        super().__init__(CAKE, CAKE_TYPE)