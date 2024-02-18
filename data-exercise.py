import json
path = './pydata-book/datasets/bitly_usagov/example.txt'
#获取数值专程json
records = [json.loads(line) for line in open(path)]
print(records[0])

#获取tz并且做一些操作
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# print('time_zones',time_zones)
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
counts = get_counts(time_zones)
# print(counts['America/New_York'])
# print(len(time_zones))
# print(counts.items())
def top_counts(count_dict,n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
# print(top_counts(counts))

import pandas as pd
frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()
# print('tz_counts',tz_counts)
#填充空数据
clean_tz = frame['tz'].fillna('missing')
clean_tz[clean_tz==''] = 'unknowm'
# print('clean_tz',clean_tz.value_counts()[:10])
#画图
import seaborn as sns
import matplotlib.pyplot as plt  
subset = tz_counts[:10]
sns.barplot(y=subset.index,x=subset.values)
# plt.show()

#
results = pd.Series([x.split()[0] for x in frame.a.dropna()])
# print(results[:5])
# print(results.value_counts()[:8])
import numpy as np
cframe = frame[frame.a.notnull()]
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
# print(cframe['os'][:5])
# print(cframe[:5])
by_tz_os = cframe.groupby(['tz','os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
# print(by_tz_os.size().unstack().fillna(0))
indexer = agg_counts.sum(1).argsort()
# print(indexer[-10:])
count_subset = agg_counts.take(indexer[-10:])
# print(count_subset)

count_subset = count_subset.stack()
print(count_subset)
count_subset.name = 'total'
count_subset = count_subset.reset_index()
print(count_subset[:10])

#归一化
def norm_total(group):
    group['normed_total'] = group.total / group.total.sum()
    return group
results1 = count_subset.groupby('tz').apply(norm_total)
sns.barplot(x='normed_total',y='tz',hue='os',data=results1)
plt.show()








