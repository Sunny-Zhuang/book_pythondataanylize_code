
import pandas as pd
path = './pydata-book/datasets/fec/P00000001-ALL.csv'
#获取数值专程json
fec = pd.read_csv(path)

# iloc 是 Pandas 库中的一个功能，全称为 "integer location"，即整数位置索引。它允许用户通过行和列的整数位置来选择和访问 DataFrame 中的数据。
# 具体来说，iloc 的语法格式是 df.iloc[<行表达式>, <列表达式>]。其中，行和列的表达式都可以是整数、切片（slice）或者整数列表
print('第3行',fec.iloc[3])
# 获取唯一的政治候选人
unique_cands = fec.cand_nm.unique()
print('unique_cands',unique_cands)
# 给予党派
parties={
'Bachmann, Michelle':'Republic',
'Cain, Herman':'Republic',
'Gingrich, Newt':'Republic',
'Huntsman, Jon':'Republic',
'Johnson, Gary Earl':'Republic',
'McCotter, Thaddeus G':'Republic',
'Obama, Barack':'Democrat',
'Paul, Ron':'Republic',
'Perry, Rick':'Republic',
"Roemer, Charles E. 'Buddy' III":'Republic',
'Romney, Mitt':'Republic',
'Santorum, Rick':'Republic'
}
fec['partie'] = fec.cand_nm.map(parties)
print('第3行',fec.iloc[3])
# 捐款正向信息
fec = fec[fec.contb_receipt_amt > 0]
# 查看主要的两个候选人
fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]

by_occupation = fec_mrbo.pivot_table('contb_receipt_amt',columns='partie',index='contbr_occupation',aggfunc='sum')
print('by_occupation',by_occupation[:5])
over_2mm = by_occupation[by_occupation.sum(1)>2000000]
over_2mm.plot(kind='barh')





