'''
Created on 2020年6月16日

@author: 44786
'''
import time
scale = 50
print('{:-^14}'.format('执行开始'))
for i in range(scale + 1):
    a = '*' * i
    b = '-' * (scale - i)
    c = (i/scale)*100
    print('\r{:^4.0f}% [{} -> {}]'.format(c,a,b),end='')
    time.sleep(0.1)
    
print('')
print('执行结束')
     