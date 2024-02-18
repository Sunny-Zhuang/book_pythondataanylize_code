
import pandas as pd

unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('./pydata-book/datasets/movielens/users.dat',sep="::",header=None, names=unames)

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('./pydata-book/datasets/movielens/ratings.dat',sep="::",header=None, names=rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_table('./pydata-book/datasets/movielens/movies.dat',sep="::",header=None, names=mnames)

data = pd.merge(pd.merge(users,ratings),movies)

# 男女对电影评分的平均得分
mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')

# 获取电影的rating数量
rating_by_title = data.groupby('title').size()

# 选出》250的index
active_titles = rating_by_title.index[rating_by_title>250]

# 在mean_ratings下过滤出rating数量》250的
# loc：这是Pandas提供的一个方法，用于基于行标签（索引）来选择数据。
mean_ratings = mean_ratings.loc[active_titles]

#女性top
top_female_ratings = mean_ratings.sort_values(by='F',ascending = False)

# 男女差异最大
mean_ratings['diff'] = mean_ratings['M']- mean_ratings['F']
sort_by_diff = mean_ratings.sort_values(by='diff')
print(1111,sort_by_diff[:10])
# 对行倒序取前十
print(1111,sort_by_diff[::-1][:10])


