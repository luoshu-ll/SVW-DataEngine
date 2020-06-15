#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Action1
sum = 0
for number in range(2,101,2):
    sum = sum +  number
print(sum)


# In[4]:


#Action1
import numpy as np
a = np.arange(2,101,2)
print(np.sum(a))


# In[6]:


#Action2
import pandas as pd
data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df = pd.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
#print(df)
#统计平均成绩、最小成绩、最大成绩、方差、标准差
print(df.agg({'语文':['mean','min','max','var','std'],'数学':['mean','min','max','var','std'],'英语':['mean','min','max','var','std']}))
#总成绩排序
df2=df
df2['总分']=df['语文']+df['英语']+df['数学']
df2['名次']=df2['总分'].rank(method='min',ascending=False)
df2['名次']=df2['名次'].astype('int')
print(df2)


# In[8]:


#Action3
import pandas as pd
from pandas import Series, DataFrame
#Step1 数据加载
df = pd.read_csv("/Users\luolan\Desktop\Data_Engine_with_Python-master\L1\car_data_analyze\car_complain.csv")
#print(df)

#Step2 拆分problem类型为多列
df_new=df.drop(['problem'],axis=1).join(df['problem'].str.get_dummies(','))
#print(df_new)

#Step3 数据统计
#统计品牌投诉总数并降序排列
df1=df.groupby('brand')['id'].nunique()
df1=pd.DataFrame(df1)
df1.rename(columns={'id':'品牌投诉总数'},inplace=True)
df1=df1.sort_values(by="品牌投诉总数",ascending=False)
print(df1)
#统计车型投诉总数并降序排列
df2=df.groupby('car_model')['id'].nunique()
df2=pd.DataFrame(df2)
df2.rename(columns={'id':'车型投诉总数'},inplace=True)
df2=df2.sort_values(by="车型投诉总数",ascending=False)
print(df2)
#计算品牌车型数，通过表连接合并计算得到平均车型投诉
df3=df.groupby('brand')['car_model'].nunique()
df3=pd.DataFrame(df3)
df3.rename(columns={'car_model':'品牌车型数'},inplace=True)
df4=pd.merge(df1, df3, on='brand')
df4['平均车型投诉']=df4['品牌投诉总数']/df4['品牌车型数']
df4=df4.sort_values(by="平均车型投诉",ascending=False)
#print(df4)
print("平均车型投诉值最大品牌")
df4=df4.loc[df4['平均车型投诉'] == df4['平均车型投诉'].max()]
print(df4)#请问怎样可以只输出品牌名称而不是输出一行？


# In[ ]:




