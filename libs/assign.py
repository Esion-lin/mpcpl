from contextlib import contextmanager
from mpcpl.pyhelp.trace_stack import TraceableStack
import threading
class Assign:
    def __init__(self, with_player:str):
        self._player = with_player
        self._player_stack = TraceableStack()
    @contextmanager
    def assign(self):
        self._add_player_to_stack(self._player)
        self.thread_local.now_player = self._player
        try:
            yield self
        finally:
            self._player_stack.pop_obj()
    
    def __call__(func, *args, **kwargs):
        if player.check(self._player):
            return func(*args, **kargs)
        else:
            return None
    def _add_player_to_stack(self, player_name):
        self._player_stack.push_obj(player_name, offset=2)


    @property
    def thread_local(self):
        return threading.local()

    @property
    def player(self):
        return self._player
    @property
    def lock_player(self):
        if self.thread_local.now_player is not None:
            return self.thread_local.now_player
        else:
            return None
        
    @property
    def player_stack(self):
        return self._player_stack

def assign(with_player):
    return Assign(with_player).assign()

