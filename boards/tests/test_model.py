from django.test import TestCase

from ..models import Board


class BoardModelTests(TestCase):
    def setUp(self):
        """ Create a board instance to use. """
        Board.objects.create(name='Django', description='Django board.')

    def test_str_method(self):
        """ Method `__str__` should be equal to field `name`. """
        board = Board.objects.get(pk=1)
        self.assertEqual(str(board), board.name)
