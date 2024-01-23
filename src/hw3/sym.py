import math


class SYM:
    def __init__(self, s=None, n=None):
        self.txt = s if s else " "
        self.at = n if n else 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for v in self.has.values():
            e += -v / self.n * math.log2(v / self.n)
        return e

    def small(self):
        return 0

    #change
    def like(self, x, prior):
        return ((self.has.get(x, 0) or 0) + self.the['m'] * prior) / (self.n + self.the['m'])