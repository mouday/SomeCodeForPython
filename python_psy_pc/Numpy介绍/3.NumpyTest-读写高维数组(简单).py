import numpy as np

a=np.arange(100).reshape(5,10,2)
np.save("a.npy",a)
# print(a)

b=np.load("a.npy")
print(b)

# np.save(frame,array)或np.savez(fname,array)(压缩)
# + frame：文件名，以.npy为扩展名，压缩扩展名为.npz
# + array：数组变量
# np.load(fname)