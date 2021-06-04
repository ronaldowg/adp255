import pandas as pd
import matplotlib.pyplot as plt
from numpy import array 
import numpy as np
from keras.models import Sequential 
from keras.layers import Dense
from keras.layers import Flatten 
from keras.layers.convolutional import Conv1D 
from keras.layers.convolutional import MaxPooling1D
from datetime import timedelta, date
from dateutil. relativedelta import relativedelta

from sklearn.preprocessing import Normalizer, MinMaxScaler, StandardScaler

dados = pd.read_csv("adp255/datasets/dados.csv")
dados = dados.rename(columns={'Unnamed: 0':'mes'})
dados = dados.set_index('mes')

dados = dados[['ibc','pib','consumo','ICST-R','geracaoGWh','IndGeral','total']]

dados = dados['2014-01-01':'2020-12-01']

# split a multivariate sequence into samples 
def split_sequences(sequences, n_steps): 
    X, y = list(), list() 
    for i in range(len(sequences)): 
        # find the end of this pattern 
        end_ix = i + n_steps 
        # check if we are beyond the dataset 
        if end_ix == len(sequences): 
            break
        # gather input and output parts of the pattern 
        seq_x, seq_y = sequences[i:end_ix, :-1], sequences[end_ix, -1] 
        X.append(seq_x) 
        y.append(seq_y)
    return array(X), array(y)

n_steps = 12

dataset = dados.to_numpy()

scaler = MinMaxScaler(feature_range=(-1,1))

dataset = scaler.fit_transform(dataset)

# dados de 2014 até final 2019
train = dataset[0:72]
y_2019 = dataset[72:84,-1]

X, y = split_sequences(train, n_steps)

print(X.shape, y.shape)

# the dataset knows the number of features, e.g. 2 
n_features = X.shape[2]

model = Sequential() 
model.add(Conv1D(filters=64, kernel_size=2, activation='relu' , input_shape=(n_steps, n_features)))
model.add(MaxPooling1D(pool_size=2)) 
model.add(Flatten()) 
model.add(Dense(50, activation='relu' )) 
model.add(Dense(1)) 
model.compile(optimizer='adam' , loss='mse' )

model.fit(X, y, epochs=1000, verbose=0)

score = model.evaluate(X, y)

model.save("adp255/datasets/cnn.h5")

begin_ix = 72-n_steps #72 é posição onde está janeiro 2020
dataset_X_pred = dataset[begin_ix:83, :-1] #71 é novembro, pois max que vamos é até dez/20

def split_sequences_pred(sequences, n_steps):
    X = list()
    for i in range(12):
        end = len(sequences)-i
        seq_x = sequences[end-n_steps:end]
        X.append(seq_x) 
    return array(X)

X_pred = split_sequences_pred(dataset_X_pred , n_steps)
#começa em -1 e vai diminuindo
y_pred = list()
for i in range(12):
    X=X_pred[-1-i].reshape(1,n_steps,n_features)
    yhat = model.predict(X, verbose=0)
    y_pred.append(yhat[0][0])

y_pred/y_2019

#d = [1,2,3,4,5,6,7,8,9,10,11,12]
#plt.plot(d,y_pred,d,y_2019)
#plt.show()

y_todos_anos = dataset[:,-1:]

X_sem_Y_2020 = dataset[72:84,:6]

y_2020 = array(y_pred).reshape(12,1)

novo_2020 = np.hstack((X_sem_Y_2020,y_2020))

dataset_pred = np.vstack((dataset[:72],novo_2020))

dados_pred = scaler.inverse_transform(dataset_pred)

y_dados_pred_2020 = dados_pred[72:84,-1:]

dados = scaler.inverse_transform(dataset)

y_todos_anos = dados[:,-1:]

y_todos_anos = y_todos_anos.reshape(84,)
y_dados_pred_2020 = y_dados_pred_2020.reshape(12,)

d_total = list(range(1,85))
d_2020 = list(range(73,85))
plt.plot(d_total, y_todos_anos,d_2020,y_dados_pred_2020)
#plt.plot(d_2020,y_dados_pred_2020)
plt.show() 



##############

# dados de 2014 até final 2018
train = dataset[0:60]
y_2018 = dataset[60:72,-1]

X, y = split_sequences(train, n_steps)

print(X.shape, y.shape)

# the dataset knows the number of features, e.g. 2 
n_features = X.shape[2]

model = Sequential() 
model.add(Conv1D(filters=64, kernel_size=2, activation='relu' , input_shape=(n_steps, n_features)))
model.add(MaxPooling1D(pool_size=2)) 
model.add(Flatten()) 
model.add(Dense(50, activation='relu' )) 
model.add(Dense(1)) 
model.compile(optimizer='adam' , loss='mse' )

model.fit(X, y, epochs=1000, verbose=0)

score = model.evaluate(X, y)

model.save("adp255/datasets/cnn.h5")

begin_ix = 60-n_steps #72 é posição onde está janeiro 2019
dataset_X_pred = dataset[begin_ix:71, :-1] #71 é novembro, pois max que vamos é até dez/19

def split_sequences_pred(sequences, n_steps):
    X = list()
    for i in range(12):
        end = len(sequences)-i
        seq_x = sequences[end-n_steps:end]
        X.append(seq_x) 
    return array(X)

X_pred = split_sequences_pred(dataset_X_pred , n_steps)
#começa em -1 e vai diminuindo
y_pred_19 = list()
for i in range(12):
    X=X_pred[-1-i].reshape(1,n_steps,n_features)
    yhat = model.predict(X, verbose=0)
    y_pred_19.append(yhat[0][0])




y_2019 = array(y_pred_19).reshape(12,1)

dataset[:60]

d = np.hstack((dataset[60:72,:6],y_2019))

dataset[72:84]

dataset_novo = np.vstack((dataset[:60],d,dataset[72:84]))

dados_2019pred = scaler.inverse_transform(dataset_novo)

y_dados_pred_2019 = dados_2019pred[60:72,-1:]

y_dados_pred_2019 = y_dados_pred_2019.reshape(12,)

d_total = list(range(1,85))
d_2020 = list(range(73,85))
d_2019 = list(range(61,73))
plt.plot(d_total, y_todos_anos,d_2020,y_dados_pred_2020,d_2019,y_dados_pred_2019)
#plt.plot(d_2020,y_dados_pred_2020)
plt.show() 
