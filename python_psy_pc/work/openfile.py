# -*- coding: cp936 -*-
poem='''\
programming is fun
when the work is done
if you wanna make your work also fun:
    use python!
'''
#д���ļ�
f=open('poem.txt','w')
f.write(poem)
f.close()

#��ȡ�ļ�
f=open('poem.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print line,
f.close()
    
