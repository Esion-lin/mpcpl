from libs.node_with_player import node_with_player


class Add(node_with_player):
    def __call__(self, a, b):
        return a + b
    @staticmethod
    def __build__(a, b):
        return (a, b, "add")
class Mul(node_with_player):
    def __call__(a, b):
        return a * b
    @staticmethod
    def __build__(a, b):
        return (a, b, "mul")

