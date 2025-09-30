from .classes import manager
import ipywidgets as widgets

class ImageSelector(widgets.VBox):
    
    def __init__(self, inputDirectory, outputDirectory, *args, **kwargs):
        super(ImageSelector, self).__init__()
        self.manager = manager.Manager(self, inputDirectory, outputDirectory)
