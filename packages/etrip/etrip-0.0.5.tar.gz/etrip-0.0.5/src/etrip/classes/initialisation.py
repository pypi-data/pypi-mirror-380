from jupyter_bbox_widget import BBoxWidget
from ipyfilechooser import FileChooser
import ipywidgets as widgets
from html import escape
import os

class Initialisation():

    IMAGEFILE_EXTENSIONS = [".jpg", ".jpeg",".png"]
    IMAGEFILE_PATTERNS = ["*.jpg", "*.jpeg","*.png"]
    

    def __init__(self, manager):
        self.manager = manager
        self.inputFullFilename = None
        self.inputFilename = None
        self.inputPath = None
        self.inputBasePath = None
        self.inputFilenames = []
        self.outputBasePath = None
        #widgets
        self.widgetHeader = widgets.HTML("""<h2>Image Selector&nbsp;&nbsp;
                                    <span style="color: #AAAAAA;">-&nbsp;&nbsp;initialisation</span></h2>""")
        self.inputLocation = widgets.HTML("""<hr noshade/><strong>Input location</strong>: %s""" % escape(self.manager.inputDirectory))
        self.fileChooser = FileChooser(self.manager.inputDirectory)
        self.fileChooser.sandbox_path = os.path.abspath(self.manager.inputDirectory)
        self.fileChooser.filter_pattern = self.IMAGEFILE_PATTERNS
        self.fileChooser.title = "<b>Initial image</b>"
        self.fileChooser.register_callback(self._initialiseLocation)
        self.inputLocationReport = widgets.VBox()
        self.outputLocation = widgets.HTML("""<hr noshade/><strong>Output location</strong>: %s""" % escape(self.manager.outputDirectory))
        self.outputLocationReport = widgets.VBox()
        self.confirm = widgets.HTML("""<hr noshade/>""")
        self.confirmButton = widgets.Button(description="Continue", disabled=False, button_style="info")
        self.confirmButton.on_click(self._confirmLocation)
        self.confirmMenu = widgets.VBox()
        self.widgetContainer = widgets.VBox([self.widgetHeader,
                                             self.inputLocation,self.inputLocationReport,
                                             self.fileChooser,
                                             self.outputLocation,self.outputLocationReport,
                                             self.confirm, self.confirmMenu])

    def _confirmLocation(self,_):
        try:
            self.manager.loadFile(self.inputFullFilename, self.inputBasePath, self.inputFilenames, self.outputBasePath)
        except Exception as ex:
            self.inputLocationReport.children=[]
            self.outputLocationReport.children=[]
            widgetError = widgets.HTML(description="Problem", value="%s" % str(ex))
            self.confirmMenu.children=[widgetError]
            
    def _initialiseLocation(self):
        #reset
        self.inputLocationReport.children=[]
        self.outputLocationReport.children=[]
        self.confirmMenu.children=[]
        self.inputFullFilename = None
        self.inputFilename = None
        self.inputPath = None
        self.inputBasePath = None
        self.inputFilenames = []
        self.outputPath = None
        self.outputBasePath = None
        #initialise
        self.inputFullFilename = self.fileChooser.selected
        if self.inputFullFilename is None:
            widgetInputError = widgets.HTML(description="Problem", value="nothing selected")
            self.inputLocationReport.children = [widgetInputError]
        elif os.path.isfile(self.inputFullFilename):
            if not os.access(self.inputFullFilename,os.R_OK):
                widgetInputError = widgets.HTML(description="Problem", value="imput file not readable")
                self.inputLocationReport.children = [widgetInputError]
            else:
                try:
                    errorList = []
                    self.inputFilename = self.fileChooser.selected_filename
                    self.inputPath = self.fileChooser.selected_path
                    assert self.inputPath.startswith(self.manager.inputDirectory), "input path not allowed"
                    self.inputBasePath = self.fileChooser.selected_path[len(self.manager.inputDirectory)+1:]
                    self.inputFilenames = sorted([fn for fn in os.listdir(self.inputPath)
                                          if os.path.isfile(os.path.join(self.inputPath,fn))
                                          and os.access(os.path.join(self.inputPath,fn),os.R_OK)
                                          and any(fn.lower().endswith(ext) for ext in self.IMAGEFILE_EXTENSIONS)])
                    widgetInputFilename = widgets.HTML(description="Filename", value=escape(os.path.join(self.inputBasePath,self.inputFilename)))
                    widgetInputPath = widgets.HTML(description="Path", value=escape(self.inputBasePath))
                    assert len(self.inputFilenames)>0, "no input files found"
                    widgetInputNumber = widgets.HTML(description="Number", value="%d image files: %s ... %s" % (len(self.inputFilenames),
                        escape(self.inputFilenames[0]), escape(self.inputFilenames[-1])))
                    self.outputBasePath = self.inputBasePath
                    self.outputPath = os.path.join(self.manager.outputDirectory,self.outputBasePath)
                    widgetOutputPath = widgets.HTML(description="Path", value=escape(self.outputBasePath))
                    widgetOutputReport = widgets.HTML(description="Report", value=escape(os.path.join(self.outputBasePath,"report.txt")))
                    outputFilenamesText = []
                    for row in range(1):
                        for column in range(1):
                            for i in range(min(2,len(self.inputFilenames))):
                                outputFilenamesText.append(escape(os.path.join(self.outputBasePath,
                                                   "%02d_%02d/%s" % (row,column,self.inputFilenames[i]))))
                    outputFilenamesText.append(escape("..."))
                    widgetOutputFilenames = widgets.HTML(description="Filenames", value="<br/>".join(outputFilenamesText))
                    self.inputLocationReport.children = [widgetInputFilename,widgetInputPath,widgetInputNumber]
                    self.outputLocationReport.children=[widgetOutputPath,widgetOutputReport,widgetOutputFilenames]
                    if os.path.exists(self.outputPath):
                        if not os.path.isdir(self.outputPath):
                            errorList.append("Location %s exists but not a directory" % self.outputBasePath)
                        elif len(os.listdir(self.outputPath))>0:
                            errorList.append("Directory %s not empty" % self.outputBasePath)
                    if len(errorList)==0:
                        self.confirmMenu.children=[self.confirmButton]
                    else:
                        errorText = []
                        for error in errorList:
                            errorText.append(escape("%s" % escape(error)))
                        errorHtmlText = "<span style=\"font-weight: bold; color: #FF0000;\">" + ("<br/>".join(errorText)) + "</span>"
                        widgetOutputError = widgets.HTML(description="Problem", 
                                                         value=errorHtmlText, icon="check")
                        self.confirmMenu.children=[widgetOutputError]
                except Exception as ex:
                    widgetInputError = widgets.HTML(description="Problem", value="%s" % str(ex))
                    self.inputLocationReport.children = [widgetInputError]
        else:
            widgetInputError = widgets.HTML(description="Problem", value="input file not readable")
            self.inputLocationReport.children = [widgetInputError]

    

    

