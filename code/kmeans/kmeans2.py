

# Commented out IPython magic to ensure Python compatibility.
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
# %matplotlib inline

df = pd.read_csv('D:\TY-BTECH\DWDM\code\kmeans\income.csv')
df.head()

plt.scatter(df['Age'],df['Income($)'])

km =  KMeans(n_clusters=3)
km

y_predicted = km.fit_predict(df[['Age','Income($)']])
y_predicted

df['cluster'] = y_predicted
df.head()

df1 = df[df.cluster ==0]
df2 = df[df.cluster ==1]
df3 = df[df.cluster ==2]

plt.scatter(df1.Age,df1['Income($)'],color='green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')

plt.xlabel('Age')
plt.ylabel('Income ($)')
plt.legend()

scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])
df['Income($)'] = scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])
df.head()

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['Age','Income($)']])
df.head()

df['cluster'] = y_predicted
# df.drop(['cluster'],axis='columns',inplace=True)
df.head()

km.cluster_centers_

df1 = df[df.cluster ==0]
df2 = df[df.cluster ==1]
df3 = df[df.cluster ==2]

plt.scatter(df1.Age,df1['Income($)'],color='green')
plt.scatter(df2.Age,df2['Income($)'],color='red')
plt.scatter(df3.Age,df3['Income($)'],color='black')

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')

plt.xlabel('Age')
plt.ylabel('Income ($)')
plt.legend()

# elbow plot method
k_rng = range(1,10)
sse= []

for k in k_rng:
  km = KMeans(n_clusters=k)
  km.fit(df[['Age','Income($)']])
  sse.append(km.inertia_)

sse

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)