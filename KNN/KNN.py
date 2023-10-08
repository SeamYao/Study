#KNN
import pandas as pd
import math
df = pd.read_csv('iris.csv',header=None)

#給出一個數據
new_data = [5.7,3.8,1.7,0.3]

#初始距離
distance = 200
type = ''
for i in range(len(df)):
    set_distance = 0
    for j in range(4):
        #先加總
        set_distance += (df.iloc[i][j] - new_data[j])**2
    #開根號算出距離
    commect_distance = abs(math.sqrt(set_distance))
    print(commect_distance)
    if distance > commect_distance:
        distance = commect_distance
        type = df.iloc[i][4]
print(type)