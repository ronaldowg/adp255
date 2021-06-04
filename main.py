import pandas as pd
import matplotlib.pyplot as plt
from numpy import array 
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

dados = dados['2014-01-01':'2019-12-01']

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

# dados de 2014 até final 2018
train = dataset[0:60]
y_2019 = dataset[60:72,-1]

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
y_pred = list()
for i in range(12):
    X=X_pred[-1-i].reshape(1,n_steps,n_features)
    yhat = model.predict(X, verbose=0)
    y_pred.append(yhat[0][0])

y_pred/y_2019

d = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(d,y_pred,d,y_2019)
plt.show()