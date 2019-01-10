# TRWSUN  (THE RADIOLOGIST WILL SEE YOU NOW)
Quick and dirty Pneumonia detector that is on par with radiologists' ability to determine whether there is pneumonia in an xray or not.

Current accuracy on a single training epoch is 79%.
The network is based on INCEPTION_V3 architecture with a custom top.

Please note the accuracy printed is after *two* epochs, so leave it at one epoch when training ;)

Based on Chest X-Ray dataset from Kaggle.com


### USAGE

#### After the images are resized, simply train the model for a single epoch (no more) and then save.
#### Once the model is saved (all the code is there already) use TRWSUN to load the model and then you can predict on any image.

### DEPENDENCIES

#### NumPy, Keras, Cv2

### TODO

#### -clean up generators 
#### -make all images generated from in-memory, rather on disk (in-memory wasn't terribly slow-- ~20s initial epoch, ~12s following epochs on RTX 2080)
#### -integer division makes ytrue, ypred different lengths (sometimes) 
#### -use basenet with smaller footprint for other devices (?)
