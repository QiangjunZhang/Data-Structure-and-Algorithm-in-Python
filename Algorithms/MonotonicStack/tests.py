import unittest
from Algorithms.MonotonicStack.jumpGame import JumpGame


class TestJumpGame(unittest.TestCase):

    def test_jump_game(self):
        solver = JumpGame()
        arr = [2,3,1,1,4]
        self.assertEqual(solver.jump(arr), 2)


if __name__ == '__main__':
    unittest.main()