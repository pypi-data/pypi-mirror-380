# eTRiP: 

Easy Tracking Rhythms in Plants: optimise the pipeline to detect periodicity of upwards/downwards movements in plants

This repository contains code for motion detection and modelling based on [PyTRiP](https://github.com/KTgreenham/TRiP/tree/master/code/PyTRiP) from [github.com/KTgreenham/TRiP](https://github.com/KTgreenham/TRiP). Additionaly a widget has been added to handle the cropping of images.

Install from the Python Package Index repository with

```
pip install --upgrade etrip
```

Example code to run the `imageSelector` widget within a jupyter notebook

```
import etrip

#crop images
etrip.imageSelector("/my/data/directory/original/", "/my/data/directory/cropped/")
```

Further analysis

```
#compute motion
etrip.estimateAllMotion("/my/data/directory/cropped/", "/my/data/directory/analysis/")

#fit model
etrip.fitAllMotion("/my/data/directory/analysis/")
```

See `help(etrip)` for more information about the parameters for each function.

Details of the algorithm, plant imaging set up and examples can be found here: Greenham, K., Lou, P., Remsen, S.E. et al. TRiP: Tracking Rhythms in Plants, an automated leaf movement analysis program for circadian period estimation. Plant Methods 11, 33 (2015). https://doi.org/10.1186/s13007-015-0075-5