import json
import pandas as pd
path = './pydata-book/datasets/usda_food/database.json'
#获取数值专程json
db = json.load(open(path))

info_keys = ['description','group','id','manufacturer']
info = pd.DataFrame(db, columns=info_keys)

# 看每个group的分布情况
# pd.value_counts() 是 Pandas 库中的一个函数，用于统计一个序列（Series）中每个唯一值的出现次数，并按次数从高到低进行排序。
print(111,pd.value_counts(info.group)[:5])

# nutrients = pd.DataFrame(db[0]['nutrients'])
# 初始化一个空的DataFrame列表  
nutrient_dfs = []  
  
# 遍历每个数据项  
for item in db[:2]:  
    # 遍历每个营养元素  
    for nutrient in item['nutrients']:  
        # 为每个营养元素创建一个新的DataFrame，并添加id列  
        nutrient_df = pd.DataFrame([nutrient], columns=['value', 'units', 'description', 'group'])  
        nutrient_df['id'] = item['id']  # 添加id列  
        # 将DataFrame添加到列表中  
        nutrient_dfs.append(nutrient_df)  
  
# 使用pd.concat连接所有的DataFrame  
nutrients = pd.concat(nutrient_dfs, ignore_index=True)  

print(777,nutrients[:5])



# 查看重复的数量
duplicateNum = nutrients.duplicated().sum()
# 去除重复
nutrients = nutrients.drop_duplicates()
print(222,nutrients)
# 重命名 description和group
col_mapping={'description':'food','group':'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
print(444,info[:5])
col_mapping={'description':'nutrient','group':'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)
print(333,nutrients[:5])

# # 合并info和nutrients
ndata = pd.merge(nutrients,info,on='id',how='outer')
print(555,ndata[:5])
by_nutrient = ndata.groupby(['nutgroup','nutrient'])
# print(9999,by_nutrient.size())
get_max = lambda x : x.loc[x.value.idxmax()]
max_foods = by_nutrient.apply(get_max)[['value','food']]
print(9999,max_foods)



