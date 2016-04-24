
from unittest import TestCase

from pycraft.configuration import ConfigurationLoader
from pycraft.objects import player, item, enemy


class TestPlayer(TestCase):

    def setUp(self):
        self.config = ConfigurationLoader().get_configurations()
        self.player = player.Player(self.config['world'])

    def test_collide(self):
        self.player.collide((0, 5, 0), 2, {})

    def test_flying(self):
        self.player.flying = False
        self.player.fly()
        assert self.player.flying, 'Flying is not True'
        self.player.fly()
        assert not self.player.flying, 'Flying is not False'

    def test_strafe(self):
        pass
