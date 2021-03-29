from node_with_player import node_with_player

class arithm:
    class Add(node_with_player):
        @staticmethod
        def __call__(a, b):
            return a + b
        @staticmethod
        def __build__(a, b):
            return (a, b, "add")
    class Mul(node_with_player):
         @staticmethod
        def __call__(a, b):
            return a * b
        @staticmethod
        def __build__(a, b):
            return (a, b, "mul")

