import sys

def unix2dos(fname):
    new_fname = fname + '.txt'
    with open(fname, 'r') as src_fobj:
        with open(new_fname, 'w') as dst_jobj:
            for line in src_fobj:
                line = line.rstrip() + '\r\n'
                dst_jobj.write(line)

if __name__ == '__main__':
    unix2dos(sys.argv[1])


