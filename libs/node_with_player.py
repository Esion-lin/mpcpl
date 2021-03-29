from abc import ABC, abstractmethod
class node_with_player(ABC):
    def __init__(self, player_name):
        self._player_name = player_name
    @abstractmethod
    def __call__(self, *args, **kwargs):
        if 
        pass
    @abstractmethod
    def __build__(self):
        pass

    #only writen init
    @property
    def player_name(self):
        return self._player_name