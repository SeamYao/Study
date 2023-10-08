"""
@ProjectName: KNN-study
@Author: SengYew 975258711@qq.com/fung975258711@gmail.com
@Create-Date: 2023-10-08 17:06:00
@LastEditors: SengYew 975258711@qq.com/fung975258711@gmail.com
@LastEditTime: 2023-10-08 17:06:00
@gitHub: https://github.com/SeamYao/Study/tree/main/KNN
@Description:
@memo:
"""
#KNN
import pandas as pd
import math
df = pd.read_csv('iris.csv',header=None)

#給出一個數據#從這裏更改數據
new_data = [5.7,3.8,1.7,0.3]

#初始距離
distance = 200
label = ''

for i in range(len(df)):
    set_distance = 0
    for j in range(4):
        #先加總
        set_distance += (df.iloc[i][j] - new_data[j])**2
    #開根號算出距離
    calculate_distance = abs(math.sqrt(set_distance))
    if distance > calculate_distance:
        #更新當前最短距離
        distance = calculate_distance
        #給出label
        label = df.iloc[i][4]
print("這個數據為:",label)
