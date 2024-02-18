import pandas as pd
import numpy as np
from datetime import datetime, timedelta

#date
now = datetime.now()
print('now',now)

#delta 时间差
start = datetime(2011,1,7)
print('start day',start+timedelta(days=12))

#format
value = '2023-01-03'
print('format',datetime.strptime(value,'%Y-%m-%d'))

#date range
tz = pd.date_range('2000-01-01','2000-12-01',freq='BM')
print('date range',tz)
#转换utc时间
print('tz utc', tz.tz_localize('UTC'))
#转换本地化时间
print('tz us', tz.tz_localize('UTC').tz_convert('America/New_York'))
#区间频率转化
p = pd.Period('2007',freq='A-DEC')
print('result',p.asfreq('M',how='start'))
#重新采样 
tz1 = pd.date_range('2000-01-01',periods=100,freq='d')
ts1 = pd.Series(np.random.randn(100),index=tz1)
print('resample',ts1.resample('M',kind='preiod').mean())

#移动窗口函数
import pandas as pd  
  
# 创建一个简单的数据框  
df = pd.DataFrame({  
    'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
})  
  
# 使用rolling方法计算5天移动平均值  
df['rolling_mean'] = df['values'].rolling(window=5).mean()  
print(df)

