from jupyter_bbox_widget import BBoxWidget
import ipywidgets as widgets
import numpy as np
import cv2

class Manual():

    def __init__(self, manager):
        self.manager = manager
        self.widgetHeader = widgets.HTML("""<h2>Image Selector&nbsp;&nbsp;
                                    <span style="color: #AAAAAA;">-&nbsp;&nbsp;manually adjusting images</span></h2>""")
        self.previousWidget = widgets.Button(icon="arrow-left", tooltip="Back to sample", 
                                                  button_style="info",layout=widgets.Layout( width="5%"))
        self.previousWidget.on_click(self._previousWidgetClick)
        self.resetWidget = widgets.Button(icon="rotate-left", tooltip="Reset to automatic detection", 
                                                  button_style="warning",layout=widgets.Layout( width="5%"))
        self.resetWidget.on_click(self._resetWidgetClick)
        self.resetWidget.layout.visibility = "hidden"
        self.nextWidget = widgets.Button(icon="arrow-right", tooltip="Continue", 
                                                  button_style="info",layout=widgets.Layout( width="5%"))
        self.nextWidget.on_click(self._nextWidgetClick)
        self.nextWidget.disabled = True
        self.widgetInfo = widgets.Label("",layout=widgets.Layout( width="90%"))
        self.widgetMenu = widgets.HBox([self.previousWidget, self.resetWidget,self.widgetInfo,self.nextWidget],
                                             layout=widgets.Layout(justify_content="space-between"))        
        self.widgetFilterList = widgets.VBox([])
        self.selectionWidget = BBoxWidget(image_bytes=self._selectionImage(),
            classes=[""], hide_buttons = True, )
        self.selectionWidget.observe(self._selectionWidgetChange, names=["bboxes"])
        self.selectionWidget.add_class("imageDetectSelectionWidget")
        self.manager._css.append(".imageDetectSelectionWidget div.classes{display: none !important}")
        self.widgetContainer = widgets.VBox([self.widgetHeader,self.widgetMenu,self.selectionWidget])

    def _resetWidgetClick(self,_):
        self._selectionUpdate()
        
    def _previousWidgetClick(self,_):
        self.manager.widgetContainer.children = (self.manager.initWidget,self.manager._sample.widgetContainer,)

    def _nextWidgetClick(self,_):
        self.manager._cut._initialise()
        self.manager.widgetContainer.children = (self.manager.initWidget,self.manager._cut.widgetContainer)

    def _selectionWidgetChange(self,change):
        newBboxes = change["new"]
        self._selectionWidgetLabel(newBboxes)
            
    def _selectionWidgetLabel(self,newBboxes=None):
        bboxes = []
        labels = []
        self.manager.finalBlocks = []
        if newBboxes is None:
            newBboxes = self.selectionWidget.bboxes.copy()
        for item in newBboxes:
            bboxes.append((item["x"],item["y"],item["width"],item["height"]))
            labels.append(None)
            self.manager.finalBlocks.append([(item["x"],item["y"],item["width"],item["height"])])
        #manage visibility buttons
        if len(newBboxes)>0:
            self.nextWidget.disabled = False
        else:
            self.nextWidget.disabled = True
        changeDetected = False
        if len(bboxes)==len(self.manager.computedBlocks):
            for computedBlock in self.manager.computedBlocks:
                if not computedBlock in bboxes:
                    changeDetected = True
                    break
        else:
            changeDetected = True
        if changeDetected:
            self.previousWidget.disabled = True
            self.resetWidget.layout.visibility = "visible"
        else:
            self.previousWidget.disabled = False
            self.resetWidget.layout.visibility = "hidden"
        rowCounter = 0
        while True:
            yTop = None
            heightTop = None
            #compute highest unlabeled
            for i in range(len(bboxes)):
                if not labels[i] is None:
                    continue
                elif (yTop is None) or (yTop > bboxes[i][1]) or (yTop == bboxes[i][1] and heightTop<bboxes[i][3]):
                        yTop = bboxes[i][1]
                        heightTop = bboxes[i][3]
            if yTop is None:
                break
            #compute unlabeled row
            rowSelection = []
            for i in range(len(bboxes)):
                if not labels[i] is None:
                    continue
                elif bboxes[i][1] <= (yTop+heightTop):
                    rowSelection.append((i,bboxes[i][0]))
            #sort row
            rowSelection.sort(key=lambda x: x[1])
            #set labels
            for i in range(len(rowSelection)):
                label = "%02d-%02d" % (rowCounter, i)
                labels[rowSelection[i][0]] = label
                self.manager.finalBlocks[rowSelection[i][0]].append((rowCounter, i, label))
            rowCounter+=1
        #redefine bboxes to add labels
        labelBboxes = []
        relabel = False
        for i in range(len(newBboxes)):
            bbox = newBboxes[i]
            if not bbox["label"]==labels[i]:
                relabel = True
            labelBboxes.append({"x": bbox["x"], "y": bbox["y"], "width": bbox["width"], "height": bbox["height"], "label": labels[i]})
        if relabel:
            self.selectionWidget.bboxes = labelBboxes
        #update cut
        self.manager._cut._initialise()

    def _selectionUpdate(self, *args, **kwargs):
        self.selectionWidget.image_bytes = self._selectionImage()
        newBboxes = []
        for block in self.manager.computedBlocks:
            newBboxes.append({"x": block[0], "y": block[1], "width": block[2], "height": block[3], "label": ""})    
        self.selectionWidget.bboxes = newBboxes

    def _selectionImage(self, force=False):
        #define initial image
        if len(self.manager._selection.widget.bboxes)>0:
            image_data = np.zeros((self.manager.image.shape[0], self.manager.image.shape[1], 3), np.uint8)
            image_data[:] = (0, 0, 0)
            image_data = cv2.addWeighted(self.manager.image,0.2,image_data,0.8,0)
            for selection in self.manager._selection.widget.bboxes:
                selectionBlock = self.manager.image[selection["y"]:selection["y"]+selection["height"], 
                    selection["x"]:selection["x"]+selection["width"]]
                image_data[selection["y"]:selection["y"]+selection["height"],selection["x"]:selection["x"]+selection["width"]] = selectionBlock
        else:
            image_data = self.manager.image
        #return
        return bytes(cv2.imencode(".jpg", image_data)[1])

