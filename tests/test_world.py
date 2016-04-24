
from unittest import TestCase
from pycraft import world
import mock


class TestWorld(TestCase):

    def setUp(self):
        world.World.init_gl = mock.MagicMock()
        world.World.init_shader = mock.MagicMock()
        self.world = world.World()
