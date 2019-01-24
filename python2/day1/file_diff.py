import sys

def file_diff(src_fname, dst_fname):
    with open(src_fname) as src_fobj:
        aset = set(src_fobj)
    with open(dst_fname) as dst_fobj:
        bset = set(dst_fobj)
    with open('/root/file_diff.txt', 'w') as reobj:
        reobj.writelines(aset-bset)

if __name__ == '__main__':
    file_diff(sys.argv[1], sys.argv[2])