from keras import Model, applications
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

base_model = applications.VGG16(include_top=False, weights='imagenet', input_shape=(150, 150, 3))
model = Flatten(input_shape=base_model.output_shape[1:])(base_model.output)
model = Dense(1024, activation='relu')(model)
model = Dense(3, activation='softmax')(model)
model = Model(inputs=base_model.input, outputs=model)

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['acc'])

model.load_weights('best_model.h5')
import numpy as np
from keras.preprocessing import image

test_image = image.load_img('car12.jpg', target_size=(150, 150))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = model.predict(test_image)

print(result)
