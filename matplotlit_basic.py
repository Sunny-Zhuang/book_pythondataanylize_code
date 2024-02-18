import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
# ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
# fig, axes=plt.subplots(2,2)
# print(ax1)
#两个图例在一个子图中
ax1.plot(np.random.randn(1000).cumsum(),'k',label='one')
ax1.plot(np.random.randn(1000).cumsum(),'k--',label='two')
# plt.show()

#pandas画图
f1 = pd.DataFrame(np.random.randn(6,4),index=['one','two','three','four','five','six'],columns=pd.Index(['A','B','C','D'],name='Cenus'))
f1.plot.barh(stacked=True,alpha=0.5)
f1.plot.show()


