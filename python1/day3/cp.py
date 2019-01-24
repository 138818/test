import sys

def copy(src, dest):
    with open(src, 'rb') as src:
        with open(dest, 'wb') as dest:
            while True:
                data = src.read(4096)
                if not data:
                    break
                dest.write(data)

if __name__ == '__main__':
    copy(sys.argv[1], sys.argv[2])

