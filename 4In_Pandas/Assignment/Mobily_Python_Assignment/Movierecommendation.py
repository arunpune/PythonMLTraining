# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:55:47 2020

@author: Lenovo
"""

import pandas as pd
from difflib import SequenceMatcher
import warnings


warnings.filterwarnings("ignore")

name=input("Please enter movie name :")
rat=int(input("Please enter movie rating :"))
rat1=rat-0.5
rat2=rat+0.5
print(rat,rat1,rat2)
df=pd.read_csv("movies.csv")

df1=pd.read_csv("ratings.csv")

data = pd.merge(df1, df, on='movieId') 
#print(data.columns)

data.drop(["genres","timestamp"],axis=1,inplace=True)

ratings = pd.DataFrame(data.groupby('title')['rating'].mean())  
  
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 
#print(ratings.columns)  
#################################

movie=list(data.title.unique())

titles=pd.DataFrame(movie,columns=["title"])

movies=[]
for i in movie:        
        movies.append(SequenceMatcher(None,i,name).ratio())

movies=pd.DataFrame(movies,columns=["similar"])
###################################################
movie1=list(data.title)


movies1=[]
for i in movie1:        
        movies1.append(SequenceMatcher(None,i,name).ratio())

movies1=pd.DataFrame(movies1,columns=["similar"])

###################################
#print(data.shape)
#print(movies.shape)
data=pd.concat([data,movies1],axis=1)
data=data.sort_values(['similar'],ascending=False)
print(data.iloc[:,2:])
#############################
moviemat = data.pivot_table(index ='userId',columns ='title', values ='rating') 

movies=pd.concat([movies,titles],axis=1)
movies.set_index('title',inplace=True)
ratings=pd.concat([ratings,movies],axis=1)

ratings = ratings[ratings['num of ratings'] >= 10]

ratings=ratings.sort_values(['similar','num of ratings'], ascending=[False,False])
print(ratings)

moviename=ratings.index[0]
print("movie name is:  ",moviename)
First_user_rating = moviemat[moviename]
#print(First_user_rating)
similar_to_first = moviemat.corrwith(First_user_rating)


corr_first = pd.DataFrame(similar_to_first, columns =['Correlation']) 
corr_first.dropna(inplace = True) 

corr_first.sort_values('Correlation', ascending = False)
corr_first = corr_first.join(ratings['num of ratings'])
corr_first = corr_first.join(ratings['rating'])

corr_first=corr_first[(corr_first['num of ratings'] >10)]

corr_first=corr_first[(corr_first['rating'] >= rat1)&(corr_first['rating'] <= rat2)]


#corr_first=corr_first[corr_first['num of ratings'] == rat]
corr_first=corr_first.sort_values('Correlation', ascending=False)

print(corr_first.head(10))


######################
rat_list=[]

for i in range(0,5):
    rat_list.append(corr_first.index[i])

#print(rat_list)
#####################

name_list=[]

for i in range(0,5):
    name_list.append(ratings.index[i])
#print(name_list)
    

for i in range(0,5):
    name_list.append(rat_list[i])
    
name_list=pd.DataFrame(name_list,columns=["Recomended Movies"])
print(name_list)