'''
## node_with_player
### edit:   Tyan
### remark: Base class for all ops. Identify all operating roles Closely integrated with the assign class.
'''



from abc import ABC, abstractmethod
from libs.assign import Assign
from libs.player import static_player
import threading
import inspect
class emp_type:
    def __call__(self,*args,**kwargs):
        pass
    def __getattr__(self,obj):
        def pass_fun(*args,**kargs):
            pass
        return pass_fun
class node_with_player(ABC):

    def __init__(self, *args, **kwargs):
        if not self._check(offset = 1):
            self = emp_type()
    #Find the assign class in the function stack
    def trace_var(self, offset = 1):
        local = inspect.stack()[offset][0].f_locals
        if "sn" in local:
            sn = local["sn"]
            assert isinstance(sn, Assign)
            return sn.player
        else:
            for ele in local:
                if isinstance(local[ele], Assign):
                    return local[ele].player
            return ""


    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass
    @abstractmethod
    def __build__(self):
        pass

    #The second interception ensures that the role is correct
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
            local_frame = frame.f_back.f_locals
            if local_frame.get('self', None) is self:
                return temp
            else:
                if not self._check(offset = 1):
                    return pass_fun
                return temp
        finally:
            del frame

        return temp
            
    def __getattr__(self,obj):
        raise AttributeError("{}: Error attributes".format(obj))
    def _check(self,player_name = static_player.player_name, offset = 1):
        current_player = self.trace_var(2 + offset)
        self._run_players = current_player
        if isinstance(current_player, set):
            return player_name in current_player
        return  current_player == player_name or current_player == ""