PIECES = {
    'O': [[1, 2, 5, 6]],
    'I': [[1, 5, 9, 13], [0, 1, 2, 3]],
    'S': [[1, 2, 4, 5], [1, 5, 6, 10]],
    'Z': [[1, 2, 6, 7], [2, 5, 6, 9]],
    'L': [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [1, 2, 3, 5]],
    'J': [[2, 6, 9, 10], [0, 1, 2, 6], [1, 2, 5, 9], [1, 5, 6, 7]],
    'T': [[1, 5, 6, 9], [1, 4, 5, 6], [2, 5, 6, 10], [1, 2, 3, 6]],
}


class Piece:

    def __init__(self, name: str):
        self.states = PIECES[name]
        self.index = 0
        self.state = self.states[0]

    def rotate(self):
        self.index = (self.index + 1) % len(self.states)
        self.state = self.states[self.index]

    def low_boundary(self):
        return max(map(lambda x: x // 4, self.state))

    def right_boundary(self):
        return max(map(lambda x: x % 4, self.state))

    def left_boundary(self):
        return min(map(lambda x: x % 4, self.state))