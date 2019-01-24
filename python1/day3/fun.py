def gen_fib(length):
    fib = [0, 1]
    for i in range(length-2):
        fib.append(fib[-1]+fib[-2])
    return fib

print(gen_fib(10))
print(gen_fib(20))

with open('/tmp/passwd', 'w') as file:
    file.write(str(gen_fib(10)))



