try:

    from math import log2

except ImportError:

    from math import log
    log2 = lambda x: log(x) / float(log(2))

from math import log
log2 = lambda x: log(x) / float(log(2))


def bpow(x):
    """Get the maximal binary pow <= x

    For example, bpow(9) == 3 <=> 2**3 <= 9.
    """

    return int(log2(x))


def pivot(x, v=None):
    """Get the pivot value in [2^n; 2^n+1[ around x.

    :rtype: float"""

    if v is None:
        n = bpow(x)
        v = 2 ** (n + 2)

    result = (v - 1) / float(3)

    return result

def prct(x, inf=None, sup=None):
    """Get pourcentage value.

    :rtype: float"""

    if inf is None:
        n = bpow(x)

        inf = 2 ** n

    if sup is None:
        n = bpow(x)

        sup = 2 ** (n + 1)

    return float(100) * (x - inf) / (sup - inf)


class Sequence(object):

    def __init__(self, x):

        self.x = x
        self.n = bpow(x)
        self.pivot = pivot(x)
        self.ppivot = pivot(x, self.pivot) * 4
        self.prct = prct(x)
        self.inf = 2 ** self.n
        self.middle = self.inf + self.inf / 2

        if x < self.pivot:
            self.z = 1
            inf = self.inf
            sup = self.pivot

        elif x < self.middle:
            self.z = 2
            inf = self.pivot
            sup = self.middle

        elif x < self.ppivot:
            self.z = 3
            inf = self.middle
            sup = self.ppivot

        else:
            self.z = 4
            inf = self.ppivot
            sup = self.inf * 2

        self.fprct = prct(self.x, inf=inf, sup=sup)
        self.tprct = prct(
            self.x,
            inf=self.inf if self.n % 2 == 0 else self.inf / 2,
            sup=self.inf * 4 if self.n % 2 == 0 else self.inf * 2
        )

    def __repr__(self):

        return 'x: {0}, n: {1}[{2}; {3}; {4}[, z: {5}, prct: {6}/{7}/{8}'.format(
            self.x, self.n, self.inf, self.pivot, self.ppivot, self.z, self.prct, self.fprct, self.tprct
        )


def syracuse(x, odd=False):
    """Print a syracuse sequence."""

    result = []

    while x != 1:
        if x % 2 == 0:
            if odd:
                result.append(Sequence(x))
            x /= 2

        else:
            result.append(Sequence(x))
            x = 3*x + 1

    result.append(Sequence(x))

    return result


def pivots(x):

    result = []

    for n in range(x):

        inf = 2 ** n + 1

        p = pivot(inf)

        if p == int(p):

            result.append((n, p))

    return result


if __name__ == '__main__':
    from sys import argv

    x = int(argv[1])
    odd = len(argv) > 2

    sequences = syracuse(x, odd)

    for index, sequence in enumerate(sequences):
        print('{0}: {1}'.format(index, sequence))
