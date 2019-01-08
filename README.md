# TRWSUN  (THE RADIOLOGIST WILL SEE YOU NOW)
Quick and dirty Pneumonia detector that is on par with radiologists' ability to determine whether there is pneumonia in an xray or not.

Current accuracy on a single training epoch is 79%.
The network is based on INCEPTION_V3 architecture with a custom top.

Contact me for the original model code or the dataset.


### TODO

#### -clean up generators 
#### -make all images generated from in-memory, rather on disk (in-memory wasn't terribly slow)
#### -integer division makes ytrue, ypred different lengths (sometimes) 
#### -use basenet with smaller footprint for other devices (?)
