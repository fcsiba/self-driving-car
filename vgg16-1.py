import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Dropout, Flatten, Dense
from keras import applications
from keras.layers import Activation, Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator

# dimensions of our images.
img_width, img_height = 150, 150

train_data_dir = 'train'
validation_data_dir = 'test'
nb_train_samples = 2000
nb_validation_samples = 800
epochs = 50
batch_size = 16

base_model = applications.VGG16(include_top=False, weights='imagenet', input_shape=(150, 150, 3))
model = Flatten(input_shape=base_model.output_shape[1:])(base_model.output)
model = Dense(1024, activation='relu')(model)
model = Dense(3, activation='softmax')(model)
model = Model(inputs=base_model.input, outputs=model)

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.0,
                                   zoom_range=0.2,
                                   horizontal_flip=False)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory('fyp-data/train',
                                                 target_size=(150, 150),
                                                 batch_size=32,
                                                 class_mode='categorical')

test_set = test_datagen.flow_from_directory('fyp-data/test',
                                            target_size=(150, 150),
                                            batch_size=32,
                                            class_mode='categorical')

from keras import callbacks
from keras import metrics

metrics = ['acc', 'val_acc']
es = callbacks.EarlyStopping(monitor='val_loss', patience=6)
mc = callbacks.ModelCheckpoint('best_model-1.h5', monitor='val_loss')
callback_list = [es, mc]
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['acc'])

model.fit_generator(training_set,
                    steps_per_epoch=300,
                    epochs=40,
                    validation_data=test_set,
                    validation_steps=80,
                    verbose=1,
                    callbacks=callback_list)

model.save('final-1.h5')
