from libs.node_with_player import node_with_player

import threading
class random(node_with_player):
    def __init__(self, *args, **kwargs):
        super(random, self).__init__(*args, **kwargs)
    def add(self,w = 100):
        return 100
    def __call__(self, *args, **kwargs):
        return self.add()
    def __build__(self):
        pass
    

   