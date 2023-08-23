from timeit import default_timer as timer

start = timer()
qq = print


# https://www.codewars.com/kata/541a354c39c5efa5fa001372

def ip_to_num(ip):

    chunks = [bin(int(i))[2:] for i in ip.split('.')]

    for i, j in enumerate(chunks):
        chunks[i] = j.zfill(8)

    return int(''.join(chunks), 2)


def num_to_ip(num):

    chunks = [bin(num)[2:].zfill(32)[8*i:8*i+8] for i in range(4)]

    return '.'.join([str(int(i, 2)) for i in chunks])



ip = '192.168.1.1'
num = 167772160
print(ip_to_num(ip))
print(num_to_ip(num))

end = timer()
print(end - start)
