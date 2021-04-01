from mpcpl.libs.node_with_player import node_with_player

import threading
class random(node_with_player):
    def __init__(self, *args, **kwargs):
        super(random, self).__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        return super()._check("Alice")
    def __build__(self):
        pass
    

   