
class emp:
    w = 1000
class DictWrapper:
    pass
def add(self, other):
    other = emp()
    return 1000

setattr(DictWrapper, "__add__", add)

w = DictWrapper()
k = None

print(w + k)
print(k.w)