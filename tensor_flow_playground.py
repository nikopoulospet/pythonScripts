#! usr/bin/python3
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist #import training dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data() #unpack data

#plt.imshow(x_train[4]) #print data from [i] index in data set
#plt.show() # show using matplot lib

#atm data varies from 0 255
x_train = tf.keras.utils.normalize(x_train, axis=1) #normalize data 0 255 -> 0 1
x_test = tf.keras.utils.normalize(x_test, axis=1) #normalized data makes the model learn easier
#print(x_train[0]) # show normalized data

#we will create a sequental model (feed forward)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten()) 
#change multi dimentional array to be flat, only for this case, #TODO learn more later 
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) #2 layers
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) #128 nodes, relu is default activation
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax)) #output layer, nodes == output possibilities

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=['accuracy']) 
#train model, play with these to see changes
model.fit(x_train, y_train, epochs=3)

#did the model actually train itself or did it just memorize
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)


model.save("hello_world.model")