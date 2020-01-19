# import keras 버전이 맞지 않아서 오류가 발생함
import tensorflow.keras as keras
import numpy

x= numpy.array([0,1,2,3,4])
y= x*2+1

model= keras.models.Sequential()
model.add(keras.layers.Dense(1,input_shape=(1,)))
model.compile('SGD','mse')
model.fit(x[:2],y[:2], epochs=1000,verbose=0)

print('Target:', y[2:])
print('Predictions:', model.predict(x[2:]).flatten())