import inspect

'''
TODO rewrite
'''
class TraceableObj:
    # like tensorflow/python/framework/traceable_stack
    SUCCESS, HEURISTIC_USED, FAILURE = (0, 1, 2)
    def __init__(self, obj, address=None, line=None):
        self.obj = obj
        self.address = address
        self.line = line
    def set_from_call(self, offset = 0):
        '''
        args:
            offset: 0，使用当前的栈帧，1，上一层的栈帧
        '''
        retcode = self.SUCCESS
        frame = inspect.currentframe()
        for _ in range(offset + 1):
            parent = frame.f_back
            if parent is None:
                retcode = self.HEURISTIC_USED
                break
            frame = parent
        self.address = frame.f_code.co_filename
        self.line = frame.f_lineno
        return retcode
    def copy_metadata(self):
        return self.__class__(None, address=self.address, line=self.line)
    

class TraceableStack:
    def __init__(self, existing_stack=None):
        self._stack = existing_stack[:] if existing_stack else []

    def push_obj(self, obj, offset=0):
        traceable_obj = TraceableObj(obj)
        self._stack.append(traceable_obj)
        return traceable_obj.set_from_call(offset + 1)
    def pop_obj(self):
        return self._stack.pop().obj
    def peek_top_obj(self):
        return self._stack[-1].obj
    def peek_objs(self):
        return (t_obj.obj for t_obj in reversed(self._stack))
    def peek_traceable_objs(self):
        return reversed(self._stack)
    def __len__(self):
        return len(self._stack)
    def copy(self):
        return TraceableStack(self._stack)

if __name__  == '__main__':
    w = TraceableStack()
    ww = 1000
    w.push_obj(ww)
    cc = w.peek_top_obj
    w_n.set_from_call(0)
    print(w_n.address,w_n.line)