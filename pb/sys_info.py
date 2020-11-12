import psutil
import platform
import time


gb = 1024 ** 3
mhz = 1000

svmem = psutil.virtual_memory()
svmem_total = svmem.total
svmem_total_fix = round(svmem_total / gb, 2)

cpu_freq = psutil.cpu_freq()
cpu_freq_total = cpu_freq.max
cpu_total_freq_fix = round(cpu_freq_total / mhz, 2)

dsc = psutil.disk_usage('c:')
dsc_size = dsc.total
dsc_size_fix = round(dsc_size / gb, 2)

processor = platform.processor()
node = platform.node()
plat = platform.platform()
system = platform.system()

print('\nSystem details\n')
print(f'Processor: {processor}')
print(f'Computer name: {node}')
print(f'System: {plat}')

print(f'Total memory: {svmem_total_fix} GB')
print(f'CPU frequency: {cpu_total_freq_fix} Ghz')
print(f'Total storage: {dsc_size_fix} GB')


def switch_process(op):
    if op == '1':
        memon()
    elif op == '2':
        procmon()
    elif op == '3':
        discmon()
    elif op == '4':
        netmon()
    else:
        print('Invalid entry')


def memon():
    svmem_available = svmem.available
    svmem_used = svmem.used
    print(f'\nIn use: {round(svmem_used / gb, 2)} GB')
    print(f'Available: {round(svmem_available / gb, 2)} GB')

    print('\n-m <seconds> to turn on the monitor\n-b to back to main menu\n')

    def intime_memon(refresh):
        for _ in range(10):
            print(f'\nIn use: {round(svmem_used / gb, 2)} GB')
            print(f'Available: {round(svmem_available / gb, 2)} GB')
            time.sleep(int(refresh))

    op = input('> ')

    t = []

    for dig in op:
        if dig.isdigit():
            t.append(dig)
    
    rate = ''.join(t)

    if op == 'm ' + rate:
        intime_memon(rate)
    if op == 'b':
        init()


def procmon():
    print('procmon')


def discmon():
    print('discmon')


def netmon():
    print('netmon')


def init():
    print('\nFor more detailed information enter one option below.\n1 - Memory details\n2 - CPU details\n3 - Disc details\n')
    op = input('> ')
    switch_process(op)


init()
