import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import random

data = pd.read_csv('../input/train_V2.csv')

# train 0.3 test 0.7 train
# https://datascienceschool.net/view-notebook/266d699d748847b3a3aa7b9805b846ae/ Reference code

N = len(data)
ratio = 0.7
np.random.seed(0)
index_train = np.random.choice(np.arange(N), np.int(ratio * N))

data_train = data.iloc[index_train]

####
train_X = pd.DataFrame(data_train, columns = ['kills', 'walkDistance', 'weaponsAcquired', 'longestKill', 'heals', 'boosts', 'damageDealt'])
train_Y = data_train.winPlacePerc

model = RandomForestRegressor(n_estimators=30, n_jobs=-1)
model.fit(train_X,train_Y)


test_data = pd.read_csv('../input/test_V2.csv')
test_data_Id = test_data.Id

new_test_data =  pd.DataFrame(test_data, columns = ['kills', 'walkDistance', 'weaponsAcquired', 'longestKill', 'heals', 'boosts', 'damageDealt'])
test_predict_result = model.predict(new_test_data)

output = pd.DataFrame({'Id': test_data_Id, 'winPlacePerc': test_predict_result})
output.to_csv('result_xsubmissionV4.csv', index=False)

