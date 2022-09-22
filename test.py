import re

with open('test.txt', "rt") as f:
    for line in f:
        line = re.sub(r'\s+',',',line)
        print(line)
        print('---------')
        
        w = open('result.csv','a',encoding= 'utf-8-sig')
        w.write(f'\n{line}')
        w.close()

