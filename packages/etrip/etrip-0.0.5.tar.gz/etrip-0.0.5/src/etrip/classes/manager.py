from . import initialisation, selection, sample, manual, cut
import ipywidgets as widgets
import cv2
import os

class Manager():

    def __init__(self, widgetContainer, inputDirectory, outputDirectory, *args, **kwargs):
        #initialise
        self.inputDirectory = os.path.abspath(inputDirectory)
        self.outputDirectory = os.path.abspath(outputDirectory)
        self.widgetContainer = widgetContainer
        self._css = []
        self.imageFilename = None
        self.inputBasePath = None
        self.inputFilenames = []
        self.outputBasePath = None
        self.selectFile()

    def selectFile(self):
        self._initialisation = initialisation.Initialisation(self)
        self._initWidget()
        #set main container
        self.widgetContainer.children = [self.initWidget,self._initialisation.widgetContainer]

    def loadFile(self, imageFilename, inputBasePath, inputFilenames, outputBasePath):
        fullImageFilename = os.path.abspath(imageFilename)
        #set other variables
        self.inputBasePath = inputBasePath
        self.inputFilenames = inputFilenames
        self.outputBasePath = outputBasePath
        if not self.imageFilename == fullImageFilename:
            self._css = []
            #read image
            self.image = cv2.imread(fullImageFilename, cv2.IMREAD_COLOR)
            self.imageRGB = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.imageHSV = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            #blocks
            self.computedBlocks = []
            self.finalBlocks = []
            #create widgets
            self._selection = selection.Selection(self)
            self._sample = sample.Sample(self)
            self._manual = manual.Manual(self)
            self._cut = cut.Cut(self)
            self._initWidget()
            self.imageFilename = fullImageFilename
        #set main container
        self.widgetContainer.children = [self.initWidget,self._selection.widgetContainer]
    
    def _initWidget(self):
        initCode = "<style>%s</style>" % ("\n".join(self._css))
        self.initWidget = widgets.HTML(initCode)

