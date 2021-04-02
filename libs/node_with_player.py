from abc import ABC, abstractmethod
from libs.assign import Assign
from libs.player import static_player
import threading
import inspect
class node_with_player(ABC):
    
    def __init__(self, *args, **kwargs):
        pass
    
    def trace_var(self, offset = 1):
        local = inspect.stack()[offset][0].f_locals
        if "sn" in local:
            sn = local["sn"]
            assert isinstance(sn, Assign)
            return sn.player
        else:
            return ""


    @abstractmethod
    def __call__(self, *args, **kwargs):
        print("callll")
        pass
    @abstractmethod
    def __build__(self):
        pass

    def __getattribute__(self,obj):
        ban = ["trace_var", "_check"]
        def pass_fun(*args,**kargs):
            pass
        temp = object.__getattribute__(self,obj)
        if obj in ban:
            return temp
        # check whether call out-of-class
        frame = inspect.currentframe()
        try:
            locals = frame.f_back.f_locals
            if locals.get('self', None) is self:
                return temp
            else:
                print("check....",obj)
                if not self._check(offset = 1):
                    return pass_fun
                return temp
        finally:
            del frame

        return temp
            
    def __getattr__(self,obj):
        print(obj)
    def _check(self,player_name = static_player.player_name, offset = 1):
        current_player = self.trace_var(2 + offset)
        return  current_player == player_name or current_player == ""