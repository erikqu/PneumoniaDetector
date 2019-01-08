from keras.models import load_model
import cv2
import numpy as np

model = load_model('79acc_1_8_19.h5')

print("\n\n\n")
curdir = input("Enter the full directory of the image you would like to classify: ")

image = cv2.imread(curdir)
image = cv2.resize(image, (299,299))
image = np.asarray(image)
image = np.expand_dims(image, axis=0)
ans= model.predict(image)

print("\n\n TRWSUN\n\n THE RADIOLOGIST WILL SEE YOU NOW")
print("\n\n")
print("RESULTS")
print("\n")
if ans < .5:
    print("There is most likely Pneumonia in this image.")
else:
    print("There is most likely NOT Pneumonia in this image.")
print("Closer to zero means Pneumonia, closer to one means otherwise.")
print(ans[0][0])
print("\n")
