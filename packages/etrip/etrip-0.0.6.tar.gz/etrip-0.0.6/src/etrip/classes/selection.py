from jupyter_bbox_widget import BBoxWidget
import ipywidgets as widgets
import cv2

class Selection():

    def __init__(self, manager):
        self.manager = manager
        self.widgetHeader = widgets.HTML("""<h2>Image Selector&nbsp;&nbsp;
                                    <span style="color: #AAAAAA;">-&nbsp;&nbsp;region of interest</span></h2>""")
        self.previousWidget = widgets.Button(icon="arrow-left", tooltip="Back to initialisation", 
                                                  button_style="info",layout=widgets.Layout( width="5%"))
        self.previousWidget.on_click(self._previousWidgetClick)
        self.nextWidget = widgets.Button(icon="arrow-right", tooltip="Continue", 
                                                  button_style="info",layout=widgets.Layout( width="5%"))
        self.nextWidget.on_click(self._nextWidgetClick)
        self.widgetInfo = widgets.Label("Optionally select first a region of interest")
        self.widgetMenu = widgets.HBox([self.previousWidget,self.widgetInfo,self.nextWidget],
                                                layout=widgets.Layout(justify_content="space-between"))
        self.widget = BBoxWidget(image_bytes = bytes(cv2.imencode(".jpg", self.manager.image)[1]), 
                                          classes=["selection"], hide_buttons = True)
        self.widget.observe(self._widgetChange, names=["bboxes"])
        self.widget.add_class("imageSelectorSelectionWidget")
        self.manager._css.append(".imageSelectorSelectionWidget div.classes{display:none !important}")
        self.widgetContainer = widgets.VBox([self.widgetHeader,self.widgetMenu,self.widget])

    def _widgetChange(self,change):
        newBboxes = change["new"]
        if len(newBboxes)>1:
            self.widget.bboxes = [newBboxes[0]]
        self.manager._sample._selectionCanvasUpdate()
        self.manager._detect._selectionUpdate()

    def _previousWidgetClick(self,_):
        self.manager.widgetContainer.children = (self.manager.initWidget,self.manager._initialisation.widgetContainer,)
        
    def _nextWidgetClick(self,_):
        self.manager.widgetContainer.children = (self.manager.initWidget,self.manager._sample.widgetContainer,)
        

    

