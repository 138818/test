# file = open('/tmp/passwd', 'w')
# file.write('hello world\n')
# file.writelines(['aaaaaaaaaaaa\n', 'bbbbbbbb\n'])
# file.close()
# ##########################

# with open('/tmp/passwd') as file:
#     data = file.readline()
#     print(data)

#################################

with open('/tmp/passwd', 'rb') as f:
    print(f.readlines())
    f.seek(6, 0)
    print(f.read(5))
    f.seek(1, 1)
    print(f.read(4))
    f.seek(-6, 2)
    print(f.read(5))

