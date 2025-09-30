# eTRiP: Easy Tracking Rhythms in Plants

Optimised pipeline to detect periodicity of upwards/downwards movements in plants

This repository contains code for motion detection and modelling based on [PyTRiP](https://github.com/KTgreenham/TRiP/tree/master/code/PyTRiP) from [github.com/KTgreenham/TRiP](https://github.com/KTgreenham/TRiP). Additionaly a widget has been added to handle the cropping of images.

## Installation

The software requires at least Python version 3.12. Optionally you can create and activate a dedicated conda environment for the installation of this software:

```
conda create -n etrip python=3.12
conda activate etrip
```

Install from the [Python Package Index repository](https://pypi.org/project/etrip/) with

```
pip install --upgrade etrip
```

Run the `imageSelector` widget within a jupyter notebook

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

## Functions

**estimateAllMotion**( inputDirectory, outputDirectory, ext="jpg" )

*Estimate motion for multiple plants*

- inputDirectory: directory containing subdirectories for each plant, with each subdirectory containing images for different time points
- outputDirectory: directory where a plant-related subdirectory structure, similar to the inputDirectory, will be created, and where for each plant the detected motion is stored as a CSV file
- ext: extension of the image files to be considered (optional), with a default value of 'jpg'

**estimateSingleMotion**( inputDirectory, ext="jpg" )

Estimate motion for a single plant. Returns an array containing the estimated motion in both the x and y directions

- inputDirectory: directory containing images of different time points for a single plant
- extension of the image files to be considered (optional), with a default value of 'jpg'

**fitAllMotion**( analysisDirectory )

Fit model to the motion data

- analysisDirectory: directory containing subdirectories for each plant, with each subdirectory containing motion data as created by the `estimateAllMotion` function

**imageSelector**( inputDirectory, outputDirectory, *args, **kwargs)

Tool to create semi-automatically cropped plant images from a series of images of different time points containing multiple plants

- inputDirectory: directory containing multiple plant containing images for different time points
- outputDirectory: directory where a plant-related subdirectory structure is created, where each subdirectory contains the cropped images for the different time points

## References
Details of the algorithm, plant imaging set up and examples can be found here: Greenham, K., Lou, P., Remsen, S.E. et al. TRiP: Tracking Rhythms in Plants, an automated leaf movement analysis program for circadian period estimation. Plant Methods 11, 33 (2015). https://doi.org/10.1186/s13007-015-0075-5