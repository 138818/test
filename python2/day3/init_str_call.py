class book:
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '<%s>' % self.title

    def __call__(self):
        print("<%s> shi %s xie de" % (self.title, self.author))

if __name__ == '__main__':
    wjy = book('hai de liang wang li', 'wj')
    print(wjy)
    wjy()