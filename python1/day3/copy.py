# f1 = open('/tmp/passwd', 'rb')
# f2 = open('/tmp/list', 'wb')
# while True:
#     data = f1.read(4)
#     if len(data) == 0:
#         break
#     f2.write(data)
# f2.flush()
# f1.close()
# f2.close()
######################################
src_fobj = '/tmp/passwd'
dst_fobj = '/tmp/list'
with open(src_fobj, 'rb') as src_fobj:
    with open(dst_fobj, 'wb') as dst_fobj:
        while True:
            data = src_fobj.read(4096)
            if not data:
                break
            dst_fobj.write(data)







