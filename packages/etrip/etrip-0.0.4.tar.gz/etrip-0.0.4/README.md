# ETRIP: 

Easy Tracking Rhythms in Plants: optimise the pipeline to detect periodicity of upwards/downwards movements in plants

This repository contains code for motion detection and modelling based on [PyTRiP](https://github.com/KTgreenham/TRiP/tree/master/code/PyTRiP) from [github.com/KTgreenham/TRiP](https://github.com/KTgreenham/TRiP). Additionaly a widget has been added to handle the cropping of images.


```
import etrip

#crop images 
etrip.imageSelector("/my/data/directory/original/", "/my/data/directory/cropped/")

#compute motion
etrip.estimateAllMotion("/my/data/directory/cropped/", "/my/data/directory/analysis/")

#fit model
etrip.fitAllMotion("/my/data/directory/analysis/")
```

Details of the algorithm, plant imaging set up and examples can be found here: Greenham, K., Lou, P., Remsen, S.E. et al. TRiP: Tracking Rhythms in Plants, an automated leaf movement analysis program for circadian period estimation. Plant Methods 11, 33 (2015). https://doi.org/10.1186/s13007-015-0075-5