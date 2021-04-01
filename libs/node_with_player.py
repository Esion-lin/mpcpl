from abc import ABC, abstractmethod
from mpcpl.libs.assign import Assign
from mpcpl.libs.player import static_player
import threading
import inspect
class node_with_player(ABC):
    
    def __init__(self, *args, **kwargs):
        pass
    
    def trace_var(self, offset = 1):
        sn = inspect.stack()[offset][0].f_locals["sn"]
        assert isinstance(sn, Assign)
        return sn.player


    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass
    @abstractmethod
    def __build__(self):
        pass

    def __getattribute__(self,obj):
        ban = ["trace_var", "_check"]
        def pass_fun(*args,**kargs):
            pass
        if obj in ban:
            return object.__getattribute__(self,obj)
        temp = object.__getattribute__(self,obj)
        
        if callable(temp):
            print("check....")
            if not self._check(offset = 2):
                return pass_fun
            else:
                return temp
        else:
            return temp
        #     if 
            

    def _check(self,player_name = static_player.player_name, offset = 1):
        return self.trace_var(2 + offset) == player_name