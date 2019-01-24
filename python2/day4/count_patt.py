import re

def count_patt(fname, patt):
    patt_dict = {}
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1
    return patt_dict

if __name__ == '__main__':
    fname = '/var/log/httpd/access_log-20190114'
    ip = '(\d+\.){3}\d+'
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
    print(count_patt('/etc/passwd', 'bash|nologin'))

