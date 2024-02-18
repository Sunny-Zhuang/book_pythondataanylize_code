import pandas as pd
import numpy as np
import re

#Series 类字典
obj = pd.Series([4,7,-5,3],index=['a','b','c','d'])
print('series',obj)

#dataframe
data = {
    'state':['ohio','neveda','shanghai','sanya','dongbei','guangdong'],
    'year':[2000,2013,2023,2024,2024,2024],
    'pop':[1.5,1.7,3.6,2.4,3.4,2.4]
}
frame = pd.DataFrame(data,columns=['year','state','pop'],index=['one','two','three','four','five','six'])
print('dataframe',frame)
print('列检索',frame['state'])
#根据位置筛选
print('行检索',frame.loc['five'])
#根据位置和行列
# print('根据位置和行列',frame.ix[1,'five'])
# #根据index
# print('根据index',frame[frame.one<10])
frame['eastern'] = frame.state=='shanghai'
print('new dataframe',frame)
del frame['eastern']
print('del new dataframe',frame)
print('dataframe values',frame.values)
frame2 = frame.reindex(['a','b','c','d','e','f']) 
print('dataframe reindex',frame2)

#drop
new_series = obj.drop(['a','b'])
print('series drop',new_series,obj)
new_frame = frame.drop(['state'],axis=1)
print('new_frame drop',new_frame)
#frame split
print('前两行',frame[:2])
##根据行列筛选
print('第2行第3，1，2列',frame.iloc[1,[2,0,1]])
#series frame并集相当于outer join
f1 = pd.DataFrame(np.arange(12.).reshape(3,4),columns=list('abcd'))
f2 = pd.DataFrame(np.arange(20.).reshape(4,5),columns=list('abcde'))
print('f1',f1)
print('f2',f2)
print('f1 f2 outer join1',f1+f2)
print('f1 f2 outer join 自动填充',f1.add(f2,fill_value=0))
#用函数
f = lambda x: x.max()-x.min()
print('apply',f1.apply(f))

# dates
dates = pd.date_range('20230101',periods=6)
print('dates',dates)

#排序
f3 = pd.DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])
print('sort 按照行排序 降序',f3.sort_index(axis=1,ascending=False))
print('sort 根据指定value',f3.sort_values(by='a'))
s1 = pd.Series([4,7,-3,2])
print('series sort',s1.sort_values())

#获取一些属性
print('获取描述', f3.describe())
print('转置', f3.T)

###数据处理
##处理缺省值
#过滤缺省值
seriesdata = pd.Series([1,np.nan,3.5,np.nan,7])
print('series 过滤缺省值',seriesdata.dropna())
dataframedata = pd.DataFrame([[1,6.5,3],[2,np.nan,32],[np.nan,np.nan,np.nan]])
print('dataframe 过滤缺省值',dataframedata.dropna(how='all'))

#补充缺省值
print('dataframe 补充缺省值',dataframedata.fillna({1:0.5,2:1}))

#example: 获取web api数据,获取github关于pandas的30条buglist信息
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
datawebapi = resp.json()
webapidataframe = pd.DataFrame(datawebapi,columns=['number','title','labels','state'])
print('web api result',webapidataframe)

#删除重复值
changedata = pd.DataFrame({'k1':['one','two']*3+['two'],'k2':[1,1,2,3,3,4,4]})
print('通过k1去除重复值',changedata.drop_duplicates(['k1']))

#替换
replaceseries = pd.Series([1,-999,2,-999])
print('替换-999位4，并且产生新的',replaceseries.replace([-999],4))
replacedata = pd.DataFrame(np.arange(12).reshape((3,4)),index=['one','two','three'],columns=['ooo','bbb','ccc','ddd'])
print('替换，并且产生新的',replacedata.rename(index={'one':'haha'},columns={'ooo':'aaa'}))

# 正则
text = 'foo   bar\t baz'
regex = re.compile('\s+')
print('正则结果', regex.split(text))

# 分层
splitseries = pd.Series(np.random.randn(6),index=[['a','a','b','b','c','c'],[1,2,3,1,3,2]])
print('series分层结果', splitseries)
splitdata = pd.DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=['aaa','bbb','ccc',])
splitdata.index.names = ['key1','key2']
# 根据层级处理函数
# print('data 根据层级处理函数', splitdata.sum(level='key2'))

##数据合并
df1 = pd.DataFrame({'data1':range(7),'key':['b','b','a','c','a','a','c']})
df2 = pd.DataFrame({'data1':range(3),'key':['a','b','d']})
print('df1', df1)
print('df2', df2)

#merge根据索引，内外左右链接
print('merge', pd.merge(df1,df2,on='key'))

#concat根据轴
print('concat', pd.concat([df1,df2]))

#重塑 stack 列索引变行索引

#透视
# 创建一个示例 DataFrame 
# 这个方法允许你创建一个透视表，将数据按照指定的列进行分组，并计算每个组的汇总统计量。你可以指定要使用的聚合函数（如求和、平均值等），以及要作为行索引和列索引的列。 
data111 = {'A': ['foo', 'foo', 'foo', 'bar', 'bar'],  
        'B': ['one', 'one', 'two', 'two', 'one'],  
        'C': ['small', 'large', 'large', 'small', 'small'],  
        'D': [1, 2, 3, 4, 5],  
        'E': [10, 20, 30, 40, 50]}  
df11 = pd.DataFrame(data111)  
  
# 创建透视表，按照列 'A' 和 'B' 进行分组，计算列 'D' 和 'E' 的平均值  
pivot_table = df11.pivot_table(values=['D', 'E'], index=['A'], columns=['B'], aggfunc='mean')  
print(pivot_table)

#melt 这个方法可以将宽格式的 DataFrame 重塑为长格式。它接受一个或多个标识符列作为参数，并将其他列转换为行。这对于将数据从宽格式转换为长格式进行可视化或分析非常有用。例如：
# 创建一个示例 DataFrame  
df = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'],  
                   'B': ['one', 'two', 'one', 'two'],  
                   'C': [1, 2, 3, 4],  
                   'D': [5, 6, 7, 8]})  
  
# 使用 melt 方法将宽格式重塑为长格式  
melted_df = df.melt(id_vars=['A', 'B'], value_vars=['C', 'D'])  
print(df)
print(melted_df)

#分组操作
groupdata = pd.DataFrame({'key1':['a','a','b','b','a'],
'key2':['one','two','one','two','one'],
'data1':np.random.randn(5),
'data2':np.random.randn(5)}
)
group = groupdata['data1'].groupby(groupdata['key1'])
mean = group.mean()
print('group mean result',mean)








