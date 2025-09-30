from jupyter_bbox_widget import BBoxWidget
from . import initialisation
import ipywidgets as widgets
import numpy as np
from html import escape
from pathlib import Path
from PIL import Image
import os

class Cut():

    def __init__(self, manager):
        self.manager = manager
        self.widgetHeader = widgets.HTML("""<h2>Image Selector&nbsp;&nbsp;
                                    <span style="color: #AAAAAA;">-&nbsp;&nbsp;create images</span></h2>""")
        self.previousWidget = widgets.Button(icon="arrow-left", tooltip="Back to manual selection", 
                                                  button_style="info",layout=widgets.Layout( width="5%"))
        self.previousWidget.on_click(self._previousWidgetClick)
        self.widgetInfo = widgets.Label("",layout=widgets.Layout( width="95%"))
        self.widgetMenu = widgets.HBox([self.previousWidget, self.widgetInfo],
                                             layout=widgets.Layout(justify_content="space-between"))  
        self.inputLocation = widgets.HTML("""<hr noshade/><strong>Input location</strong>: %s""" % escape(self.manager.inputDirectory))
        self.inputLocationReport = widgets.VBox([])
        self.outputLocation = widgets.HTML("""<hr noshade/><strong>Output location</strong>: %s""" % escape(self.manager.outputDirectory))
        self.outputLocationReport = widgets.VBox([])
        self.confirm = widgets.HTML("""<hr noshade/>""")
        self.confirmButton = widgets.Button(description="Start", disabled=False, button_style="info")
        self.confirmButton.on_click(self._confirmCut)
        self.confirmMenu = widgets.VBox([self.confirmButton])
        self.widgetContainer = widgets.VBox([self.widgetHeader,self.widgetMenu,self.inputLocation,self.inputLocationReport,
                                            self.outputLocation,self.outputLocationReport,self.confirm,self.confirmMenu])

    def _initialise(self):
        widgetInputPath = widgets.HTML(description="Path", value=escape(self.manager.inputBasePath))
        widgetInputNumber = widgets.HTML(description="Number", value="%d image files" % len(self.manager.inputFilenames))
        widgetInputSelection = widgets.HTML(description="Selection", value="%dx" % len(self.manager.finalBlocks))
        self.inputLocationReport.children = [widgetInputPath,widgetInputNumber,widgetInputSelection]
        widgetOutputPath = widgets.HTML(description="Path", value=escape(self.manager.outputBasePath))
        widgetOutputImages = widgets.HTML(description="Images", value="%d x %d = %d cropped images to be created" % 
                                          (len(self.manager.inputFilenames), len(self.manager.finalBlocks), 
                                           len(self.manager.inputFilenames)*len(self.manager.finalBlocks)))
        self.outputLocationReport.children = [widgetOutputPath,widgetOutputImages]

    def _previousWidgetClick(self,_):
        self.manager.widgetContainer.children = (self.manager.initWidget,self.manager._manual.widgetContainer,)

    def _confirmCut(self,_):
        #show progress
        self.progressWidget = widgets.IntProgress(value=0, min=0, max=100, description="Processing:", orientation="horizontal")
        self.confirmMenu.children = [self.progressWidget]
        
        #progress stats
        totalFiles = len(self.manager.inputFilenames)
        n = 0
        self.progressWidget.value = int(100*n/totalFiles)

        #create
        outputPath = os.path.join(self.manager.outputDirectory,self.manager.outputBasePath)
        Path(outputPath).mkdir(parents=True, exist_ok=True)
        with open(os.path.join(outputPath,"report.txt"), "w") as reportFile:
            reportFile.write("# ---------------\n")
            reportFile.write("# ORIGINAL IMAGES\n")
            reportFile.write("# ---------------\n")
            reportFile.write("# number of images: %d x\n" % len(self.manager.inputFilenames))
            reportFile.write("# location images: %s\n" % os.path.join(self.manager.inputDirectory,self.manager.inputBasePath))
            for imageFilename in self.manager.inputFilenames:
                reportFile.write("# - %s\n" % imageFilename)
            reportFile.write("# ---------\n")
            reportFile.write("# SELECTION\n")
            reportFile.write("# ---------\n")
            reportFile.write("# image for selection: %s\n" % os.path.basename(self.manager.imageFilename))
            reportFile.write("# selections: %d x\n\n" % len(self.manager.finalBlocks))
            reportFile.write("# format: x,y,width,height,row,column,directory\n")
            for finalBlock in self.manager.finalBlocks:
                reportFile.write("%d,%d,%d,%d,%d,%d,%s\n" % (finalBlock[0][0],finalBlock[0][1],
                     finalBlock[0][2],finalBlock[0][3],finalBlock[1][0],finalBlock[1][1],
                     "%02d_%02d" % (finalBlock[1][0],finalBlock[1][1])))
            #create directories
            for finalBlock in self.manager.finalBlocks:
                newDir = os.path.join(outputPath,"%02d_%02d" % (finalBlock[1][0],finalBlock[1][1]))
                Path(newDir).mkdir(parents=True, exist_ok=True)
            #create cropped images
            for inputFilename in self.manager.inputFilenames:
                imageFilename = os.path.join(self.manager.inputDirectory,self.manager.inputBasePath,inputFilename)
                image = Image.open(imageFilename)
                for finalBlock in self.manager.finalBlocks:
                    newDir = os.path.join(outputPath,"%02d_%02d" % (finalBlock[1][0],finalBlock[1][1]))
                    box = (finalBlock[0][0],finalBlock[0][1],finalBlock[0][0]+finalBlock[0][2],finalBlock[0][1]+finalBlock[0][3])
                    croppedImage = image.crop(box)
                    croppedImage.save(os.path.join(newDir,inputFilename))
                n+=1
                self.progressWidget.value = int(100*n/totalFiles)

        #reset
        self.manager._initialisation = initialisation.Initialisation(self.manager)
        self.manager._initWidget()
        self.manager.widgetContainer.children = (self.manager.initWidget,self.manager._initialisation.widgetContainer,)

    