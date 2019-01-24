import re
from collections import Counter

class CountPatt:

    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        cpatt = re.compile(patt)
        c = Counter()
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    c.update([m.group()])
        return c


if __name__ == '__main__':
    fname = '/etc/passwd'
    ip = '(\d+\.){3}\d+'
    str = 'bash|nologin$'
    br = 'Firefox|Chrone|MSIE'
    cp = CountPatt(fname)
    print(cp.count_patt(str))
