from ._version import __version__
from .imageselector import ImageSelector
from .etrip import eTRiP

def imageSelector(inputDirectory, outputDirectory, *args, **kwargs):
    """
    Tool to create semi-automatically cropped plant images from a series of images of different 
    time points containing multiple plants

    :param inputDirectory: directory containing multiple plant containing images for different time points
    :param outputDirectory: directory where a plant-related subdirectory structure is created, where each 
        subdirectory contains the cropped images for the different time points
    """
    return ImageSelector(inputDirectory, outputDirectory, *args, **kwargs)
    
def estimateSingleMotion(inputDirectory,ext="jpg"):
    """
    Estimate motion for a single plant

    :param inputDirectory: directory containing images of different time points for a single plant
    :param ext: extension of the image files to be considered (optional), with a default value of 'jpg'
    :return: array containing the estimated motion in both the x and y directions
    """
    return eTRiP.estimateMotion(inputDirectory,ext)

def estimateAllMotion(inputDirectory, outputDirectory, ext="jpg"):
    """
    Estimate motion for multiple plants

    :param inputDirectory: directory containing subdirectories for each plant, with each subdirectory 
        containing images for different time points
    :param outputDirectory: directory where a plant-related subdirectory structure, similar to the 
        inputDirectory, will be created, and where for each plant the detected motion is stored 
        as a CSV file
    :param ext: extension of the image files to be considered (optional), with a default value of 'jpg'
    """
    return eTRiP.estimateAll(inputDirectory, outputDirectory, ext)

def fitAllMotion(analysisDirectory):
    """
    Fit model to the motion data
    
    :param inputDirectory: directory containing subdirectories for each plant, with each subdirectory 
        containing motion data as created by the `estimateAllMotion` function
    """
    return eTRiP.modelFitAll(analysisDirectory)

__author__ = "Matthijs Brouwer"