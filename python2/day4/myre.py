import re
import shutil

# res = re.match('a', 'back')
# res1 = re.search('a.', 'back read')
# res2 = re.search('^a', 'back')
# res3 = re.findall('a.', 'back read')
# res4 = re.finditer('a.', 'back read')
#
# print(res1.group())
# print(res2)
# print(res3)
# for m in res4:
#     print(m.group())
re.compile
str = re.compile('wjy')
m = str.search('nice to meet your wjy!')
print(m.group())

alist = re.split(',|\*', 'ni*hao,hao*are,your')
print(alist)

ss = re.sub('x', 'wjy', 'x nic to meet your')
print(ss)
