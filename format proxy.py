import time

read_file = "proxies_to_read.txt"
write_file = f"./proxy/new_proxies_{time.time()}.txt"

f = open("proxies_to_read.txt").readlines()

with open(write_file, 'w') as w:
    for proxy in f:
        w.write(f'http://{proxy.strip()}\n')