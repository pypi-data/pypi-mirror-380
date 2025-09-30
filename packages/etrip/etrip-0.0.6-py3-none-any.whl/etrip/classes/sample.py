from jupyter_bbox_widget import BBoxWidget
from ipycanvas import Canvas
import ipywidgets as widgets
import matplotlib as plt
import numpy as np
import cv2

class Sample():

    BLOCK_KERNEL_CONNECTED = 20
    BLOCK_KERNEL_BOUNDARY = 100
    BLOCK_FILL_COLOR = "#ff0000"
    BLOCK_FILL_ALPHA = 0.4
    BLOCK_BORDER_COLOR = "#0000ff"
    BLOCK_BORDER_WIDTH = 5
    BLOCK_SHOW = "show"

    FILTER_ADD_COLOR = "#0000ff"
    FILTER_DEFINED_COLOR = "#0096ff"

    def __init__(self, manager):
        self.manager = manager
        self.widgetHeader = widgets.HTML("""<h2>Image Selector&nbsp;&nbsp;
                                    <span style="color: #AAAAAA;">-&nbsp;&nbsp;automatic detection</span></h2>""")
        self.previousWidget = widgets.Button(icon="arrow-left", tooltip="Back to selection", 
                                                  button_style="info",layout=widgets.Layout( width="5%"))
        self.previousWidget.on_click(self._previousWidgetClick)
        self.nextWidget = widgets.Button(icon="arrow-right", tooltip="Continue", 
                                                  button_style="info",layout=widgets.Layout( width="5%"))
        self.nextWidget.on_click(self._nextWidgetClick)
        self.widgetInfo = widgets.Label("Define the filter(s) for automatic detection of sample images")
        self.widgetMenu = widgets.HBox([self.previousWidget,self.widgetInfo,self.nextWidget],
                                             layout=widgets.Layout(justify_content="space-between"))
        self.widgetFilterList = widgets.VBox([])
        self.selectionWidget = BBoxWidget(image_bytes=self._selectionImage(),
            classes=["sample"], hide_buttons = True, layout={"width":"60%"},)
        self.selectionWidget.observe(self._selectionWidgetChange, names=["bboxes"])
        self.selectionWidget.add_class("imageSelectorSampleSelectionWidget")
        self.manager._css.append(".imageSelectorSampleSelectionWidget div.classes{display: none !important}")
        self.widgetNoRegion = widgets.HTML("""<strong>No region selected</strong><br />
        Use the mouse on the image left to select a region<br />This region can then be used to define a filter""")
        self.widgetRegionHeader = widgets.HTML("""<strong>Region selected</strong><br />
        Use the mouse on the image left to drag or adjust the selected region. A filter can be defined by clicking on the image below""")
        self.widgetRegionReset = widgets.Button(icon="rotate-left", tooltip="Reset region", 
                                                  button_style="warning",layout=widgets.Layout( width="10%"))
        self.widgetRegionReset.on_click(self._widgetRegionResetClick)
        self.widgetRegion = widgets.HBox([self.widgetRegionHeader,self.widgetRegionReset],
                                               layout=widgets.Layout(overflow="visible", justify_content="space-between", align_items="flex-end"))
        self.computedBlockHeaderInfo = widgets.HTML("""<strong>Automatic detection sample images</strong><br />
        Settings for automatic detection based on defined filter(s)""")
        self.computedBlockDisplayInfo = widgets.HTML("""<strong>Display settings sample images</strong>""")
        self.computedBlockKernelConnected = widgets.IntSlider(value=self.BLOCK_KERNEL_CONNECTED, min=0, 
                                     max=max(2*self.BLOCK_KERNEL_CONNECTED,int(max(self.manager.image.shape[0], self.manager.image.shape[1])/50)),
                                    description="connected:")
        self.computedBlockKernelBoundary = widgets.IntSlider(value=self.BLOCK_KERNEL_BOUNDARY, min=0, 
                                     max=max(2*self.BLOCK_KERNEL_BOUNDARY,int(max(self.manager.image.shape[0], self.manager.image.shape[1])/10)),
                                    description="boundary:")
        self.computedBlockFillColorPicker = widgets.ColorPicker(concise=True, value=self.BLOCK_FILL_COLOR, disabled=False, 
                                                            layout=widgets.Layout( width="50%"),description="fill:")
        self.computedBlockFillSlider = widgets.FloatSlider(value=self.BLOCK_FILL_ALPHA, min=0.0, max=1.0, 
                                                           step=0.1, disabled=False, description="alpha:",
                            continuous_update=False, orientation="horizontal", readout=True, readout_format=".1f")
        self.computedBlockBorderColorPicker = widgets.ColorPicker(concise=True, value=self.BLOCK_BORDER_COLOR, disabled=False, 
                                                            layout=widgets.Layout( width="50%"),description="border:")
        self.computedBlockBorderWidth = widgets.IntSlider(description="border:", value=self.BLOCK_BORDER_WIDTH, min=0, max=20, disabled=False,
                                                          continuous_update=False, orientation="horizontal", readout=True)
        self.computedBlockShow = widgets.Select(options=["show","hide"], value=self.BLOCK_SHOW, description="display:", 
                                                rows=1, disabled=False)
        self.computedBlockKernelConnected.observe(self._selectionUpdate, names=["value"])
        self.computedBlockKernelBoundary.observe(self._selectionUpdate, names=["value"])
        self.computedBlockFillColorPicker.observe(self._selectionUpdate, names=["value"])
        self.computedBlockFillSlider.observe(self._selectionUpdate, names=["value"])
        self.computedBlockBorderColorPicker.observe(self._selectionUpdate, names=["value"])
        self.computedBlockBorderWidth.observe(self._selectionUpdate, names=["value"])
        self.computedBlockShow.observe(self._selectionUpdate, names=["value"])
        self.computedBlockReset = widgets.Button(icon="rotate-left", tooltip="Reset settings", 
                                                  button_style="warning",layout=widgets.Layout( width="10%"))
        self.computedBlockReset.on_click(self._computedBlockResetClick)
        self.computedBlockHeader = widgets.HBox([self.computedBlockHeaderInfo,self.computedBlockReset],
                                               layout=widgets.Layout(overflow="visible", justify_content="space-between", 
                                                                     align_items="flex-start"))
        self.computedBlockStatisticsInfo = widgets.HTML("""<strong>Statistics sample images</strong>""")
        self.computedBlockStatisticsNumber = widgets.Text(description="number:", value="", disabled=True)
        self.computedBlockStatisticsSmallest = widgets.Text(description="smallest:", value="", disabled=True)
        self.computedBlockStatisticsLargest = widgets.Text(description="largest:", value="", disabled=True)
        self.computedBlockMenu = widgets.VBox([self.computedBlockHeader,self.computedBlockKernelConnected,
                                               self.computedBlockKernelBoundary,self.computedBlockDisplayInfo,
                                               widgets.HBox([self.computedBlockFillColorPicker,self.computedBlockFillSlider],
                                                            layout=widgets.Layout(overflow="visible")),
                                               widgets.HBox([self.computedBlockBorderColorPicker,self.computedBlockBorderWidth],
                                                            layout=widgets.Layout(overflow="visible")),
                                               self.computedBlockShow,self.computedBlockStatisticsInfo,
                                               self.computedBlockStatisticsNumber,self.computedBlockStatisticsSmallest,
                                               self.computedBlockStatisticsLargest])
        self.widgetColumn = widgets.VBox([self.widgetNoRegion],layout={"width":"40%"})
        self.widgetRow = widgets.HBox([self.selectionWidget,self.widgetColumn])
        slider_settings = {"value":[0,255], "min":0, "max":255, "step":1, "disabled":False,
                           "continuous_update":True, "orientation":"horizontal", "readout":True, "readout_format":"d"}
        self.widgetColorPicker = widgets.ColorPicker(concise=True, value=self.FILTER_ADD_COLOR, 
                                                           disabled=False, layout=widgets.Layout( width="5%"))
        self.widgetHueSlider = widgets.IntRangeSlider(**{**slider_settings, **{"description":"Hue:", "max": 179}})
        self.widgetSatSlider = widgets.IntRangeSlider(**{**slider_settings, **{"description":"Sat:"}})
        self.widgetValSlider = widgets.IntRangeSlider(**{**slider_settings, **{"description":"Val:"}})
        self.widgetAddFilter = widgets.Button(icon="plus", tooltip="Add", button_style="info",layout=widgets.Layout( width="5%"))
        self.widgetAddFilter.on_click(self._widgetAddFilterClick)
        self.widgetResetFilter = widgets.Button(icon="trash", tooltip="Reset", button_style="danger",layout=widgets.Layout( width="5%"))
        self.widgetResetFilter.on_click(self._widgetResetFilterClick)
        self.widgetFilterDefinition = widgets.HBox([self.widgetColorPicker,self.widgetHueSlider,self.widgetSatSlider,
                                                self.widgetValSlider,self.widgetAddFilter,self.widgetResetFilter], 
                                                layout=widgets.Layout(border="1px solid"))
        self.widgetColorPicker.observe(self._canvasUpdate, names=["value"])
        self.widgetHueSlider.observe(self._canvasUpdate, names=["value"])
        self.widgetSatSlider.observe(self._canvasUpdate, names=["value"])
        self.widgetValSlider.observe(self._canvasUpdate, names=["value"])
        self.widgetFilterHeader = widgets.HTML("<h2>Filters</h2>")
        self.widgetFilters = widgets.VBox([])
        self.widgetContainer = widgets.VBox([self.widgetHeader,self.widgetMenu,self.widgetRow,self.widgetFilters])

    def _previousWidgetClick(self,_):
        self.manager.widgetContainer.children = (self.manager.initWidget,self.manager._selection.widgetContainer,)

    def _nextWidgetClick(self,_):
        self.manager._manual._selectionUpdate()
        self.manager.widgetContainer.children = (self.manager.initWidget,self.manager._manual.widgetContainer,)

    def _widgetRegionResetClick(self,_):
        self.selectionWidget.bboxes = []

    def _computedBlockResetClick(self,_):
        if not self.computedBlockKernelConnected.value==self.BLOCK_KERNEL_CONNECTED:
            self.computedBlockKernelConnected.value=self.BLOCK_KERNEL_CONNECTED
        if not self.computedBlockKernelBoundary.value==self.BLOCK_KERNEL_BOUNDARY:
            self.computedBlockKernelBoundary.value=self.BLOCK_KERNEL_BOUNDARY
        if not self.computedBlockFillColorPicker.value==self.BLOCK_FILL_COLOR:
            self.computedBlockFillColorPicker=self.BLOCK_FILL_COLOR
        if not self.computedBlockFillSlider.value==self.BLOCK_FILL_ALPHA:
            self.computedBlockFillSlider.value=self.BLOCK_FILL_ALPHA
        if not self.computedBlockBorderColorPicker.value==self.BLOCK_BORDER_COLOR:
            self.computedBlockBorderColorPicker.value=self.BLOCK_BORDER_COLOR
        if not self.computedBlockBorderWidth.value==self.BLOCK_BORDER_WIDTH:
            self.computedBlockBorderWidth.value=self.BLOCK_BORDER_WIDTH
        if not self.computedBlockShow.value==self.BLOCK_SHOW:
            self.computedBlockShow.value=self.BLOCK_SHOW

    def _widgetAddFilterClick(self,_):
        if self.widgetFilterDefinition in self.widgetFilters.children:
            minHsv = np.array([max(0,self.widgetHueSlider.value[0]), 
                               max(0,self.widgetSatSlider.value[0]), 
                               max(0,self.widgetValSlider.value[0])])
            maxHsv = np.array([min(179,self.widgetHueSlider.value[1]), 
                               min(255,self.widgetSatSlider.value[1]), 
                               min(255,self.widgetValSlider.value[1])])
            #add filter
            slider_settings = {"value":[0,255], "min":0, "max":255, "step":1, "disabled":False,
                           "continuous_update":True, "orientation":"horizontal", "readout":True, "readout_format":"d"}
            colorPicker = widgets.ColorPicker(concise=True, value=self.FILTER_DEFINED_COLOR, 
                                              disabled=False, layout=widgets.Layout( width="5%"))
            hueSlider = widgets.IntRangeSlider(**{**slider_settings, **{"value": [minHsv[0],maxHsv[0]], "description":"Hue:", "max": 179}})
            satSlider = widgets.IntRangeSlider(**{**slider_settings, **{"value": [minHsv[1],maxHsv[1]], "description":"Sat:"}})
            valSlider = widgets.IntRangeSlider(**{**slider_settings, **{"value": [minHsv[2],maxHsv[2]], "description":"Val:"}})
            removeButton = widgets.Button(icon="trash", tooltip="Remove", button_style="danger",layout=widgets.Layout( width="5%"))
            colorPicker.observe(self._selectionCanvasUpdate, names=["value"])
            hueSlider.observe(self._selectionCanvasUpdate, names=["value"])
            satSlider.observe(self._selectionCanvasUpdate, names=["value"])
            valSlider.observe(self._selectionCanvasUpdate, names=["value"])
            removeButton.on_click(self._widgetFilterRemoveClick)
            newFilter = widgets.HBox([colorPicker,hueSlider,satSlider,valSlider,removeButton])
            self.widgetFilterList.children = tuple([x for x in self.widgetFilterList.children] + [newFilter])
            #remove definition and show filters
            if not self.widgetFilterHeader in self.widgetFilters.children:
                self.widgetFilters.children = tuple([x for x in self.widgetFilters.children if not x==self.widgetFilterList] + 
                                                          [self.widgetFilterHeader,self.widgetFilterList])
            self.widgetFilters.children = tuple([x for x in self.widgetFilters.children if not x==self.widgetFilterDefinition])
            self.selectionWidget.bboxes = []
            #update canvas and selection
            self._selectionCanvasUpdate()

    def _widgetFilterRemoveClick(self,button):
        self.widgetFilterList.children = tuple([x for x in self.widgetFilterList.children if not button in x.children])
        #update canvas and selection
        self._selectionCanvasUpdate()
        if len(self.widgetFilterList.children)==0 and self.computedBlockMenu in self.widgetColumn.children:
            self.widgetColumn.children = tuple([x for x in self.widgetColumn.children if not x==self.computedBlockMenu])

    def _widgetResetFilterClick(self,_):
        if self.widgetFilterDefinition in self.widgetFilters.children:
            self.widgetFilters.children = tuple([x for x in self.widgetFilters.children if not x==self.widgetFilterDefinition])
            self._canvasUpdate()
            
    def _selectionWidgetChange(self,change):
        newBboxes = change["new"]
        if len(newBboxes)>1:
            self.selectionWidget.bboxes = [newBboxes[0]]
        if len(self.selectionWidget.bboxes)>0:
            bb = self.selectionWidget.bboxes[0]
            boxY = bb["y"]
            boxH = bb["height"]
            boxX = bb["x"]
            boxW = bb["width"]
            self.subImageRGB = self.manager.imageRGB[boxY:boxY+boxH,boxX:boxX+boxW]
            self.subImageHSV = self.manager.imageHSV[boxY:boxY+boxH,boxX:boxX+boxW]
            self.canvas = Canvas(height=self.subImageRGB.shape[0], width=self.subImageRGB.shape[1], layout=dict())
            self._canvasUpdate()
            self.canvas.on_mouse_down(self._canvasClickHandler)
            self.widgetColumn.children = (self.widgetRegion,self.canvas,)
        else:
            if not self.widgetNoRegion in self.widgetColumn.children:
                if len(self.widgetFilterList.children)>0:
                    self.widgetColumn.children = (self.widgetNoRegion,self.computedBlockMenu,)
                else:
                    self.widgetColumn.children = (self.widgetNoRegion,)
            elif len(self.widgetFilterList.children)>0:
                if not self.computedBlockMenu in self.widgetColumn.children:
                    self.widgetColumn.children = (self.widgetNoRegion,self.computedBlockMenu,)
            else:
                if self.computedBlockMenu in self.widgetColumn.children:
                    self.widgetColumn.children = (self.widgetNoRegion,)

    def _canvasImage(self):
        image_data = self.subImageRGB
        if len(self.widgetFilterList.children)>0:
            for filter in self.widgetFilterList.children:
                color = [int(255*x) for x in plt.colors.to_rgb(filter.children[0].value)]
                hue = filter.children[1].value
                sat = filter.children[2].value
                val = filter.children[3].value
                minHsv = np.array([hue[0],sat[0],val[0]])
                maxHsv = np.array([hue[1],sat[1],val[1]])
                mask = cv2.inRange(self.subImageHSV, minHsv, maxHsv)
                image_data = cv2.bitwise_and(image_data, image_data, mask=cv2.bitwise_not(mask))
                mask_data = np.zeros((image_data.shape[0], image_data.shape[1], 3), np.uint8)
                mask_data[:] = color
                mask_data = cv2.bitwise_and(mask_data, mask_data, mask=mask)
                image_data = cv2.bitwise_xor(mask_data,image_data)   
        if self.widgetFilterDefinition in self.widgetFilters.children:
            color = [int(255*x) for x in plt.colors.to_rgb(self.widgetColorPicker.value)]
            minHsv = np.array([max(0,self.widgetHueSlider.value[0]), 
                               max(0,self.widgetSatSlider.value[0]), 
                               max(0,self.widgetValSlider.value[0])])
            maxHsv = np.array([min(179,self.widgetHueSlider.value[1]), 
                               min(255,self.widgetSatSlider.value[1]), 
                               min(255,self.widgetValSlider.value[1])])
            mask = cv2.inRange(self.subImageHSV, minHsv, maxHsv)
            image_data = cv2.bitwise_and(image_data, image_data, mask=cv2.bitwise_not(mask))
            #add color
            mask_data = np.zeros((image_data.shape[0], image_data.shape[1], 3), np.uint8)
            mask_data[:] = color
            mask_data = cv2.bitwise_and(mask_data, mask_data, mask=mask)
            image_data = cv2.bitwise_xor(mask_data,image_data)
        return image_data

    def _canvasClickHandler(self, x, y):
        hsvValue = self.subImageHSV[int(y),int(x)]
        if not self.widgetFilterDefinition in self.widgetFilters.children:
            self.widgetFilters.children = tuple([self.widgetFilterDefinition] + [x for x in self.widgetFilters.children])
            self.widgetHueSlider.value = [hsvValue[0],hsvValue[0]]
            self.widgetSatSlider.value = [hsvValue[1],hsvValue[1]]
            self.widgetValSlider.value = [hsvValue[2],hsvValue[2]]
        else:
            self.widgetHueSlider.value = [min(self.widgetHueSlider.value[0],hsvValue[0]),
                                                max(self.widgetHueSlider.value[1],hsvValue[0])]
            self.widgetSatSlider.value = [min(self.widgetSatSlider.value[0],hsvValue[1]),
                                                max(self.widgetSatSlider.value[1],hsvValue[1])]
            self.widgetValSlider.value = [min(self.widgetValSlider.value[0],hsvValue[2]),
                                                max(self.widgetValSlider.value[1],hsvValue[2])]
        self._canvasUpdate()

    def _canvasUpdate(self, *args, **kwargs):
        if len(self.selectionWidget.bboxes)>0:
            self.canvas.put_image_data(self._canvasImage(),0,0)

    def _selectionUpdate(self, *args, **kwargs):
        self.selectionWidget.image_bytes = self._selectionImage()

    def _selectionCanvasUpdate(self, *args, **kwargs):
        self._selectionUpdate()
        self._canvasUpdate()

    def _selectionImage(self):
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
        #apply filter within selection
        self.manager.computedBlocks = []
        if len(self.widgetFilterList.children)>0:
            selectionMask = np.zeros((image_data.shape[0], image_data.shape[1]), np.uint8)
            selectionMask[:] = 255
            filterMask = np.zeros((image_data.shape[0], image_data.shape[1]), np.uint8)
            #restrict to selection
            for selection in self.manager._selection.widget.bboxes:
                mask = np.zeros((image_data.shape[0], image_data.shape[1]), np.uint8)
                mask[selection["y"]:selection["y"]+selection["height"],selection["x"]:selection["x"]+selection["width"]] = 255
                selectionMask = cv2.bitwise_and(selectionMask,mask)
            #show effect filters with the specified color
            for filter in self.widgetFilterList.children:
                color = [int(255*x) for x in plt.colors.to_rgb(filter.children[0].value)]
                hue = filter.children[1].value
                sat = filter.children[2].value
                val = filter.children[3].value
                minHsv = np.array([hue[0],sat[0],val[0]])
                maxHsv = np.array([hue[1],sat[1],val[1]])
                mask = cv2.inRange(self.manager.imageHSV, minHsv, maxHsv)
                mask = cv2.bitwise_and(mask,selectionMask)
                filterMask = cv2.bitwise_or(filterMask,mask)
                image_data = cv2.bitwise_and(image_data, image_data, mask=cv2.bitwise_not(mask))
                mask_data = np.zeros((image_data.shape[0], image_data.shape[1], 3), np.uint8)
                mask_data[:] = color
                mask_data = cv2.cvtColor(cv2.bitwise_and(mask_data, mask_data, mask=mask), cv2.COLOR_BGR2RGB)
                image_data = cv2.bitwise_xor(mask_data,image_data)
            #add blocks
            fillColor = [int(255*x) for x in plt.colors.to_rgb(self.computedBlockFillColorPicker.value)[::-1]]
            block_data = np.zeros((self.manager.image.shape[0], self.manager.image.shape[1], 3), np.uint8)
            block_data[:] = fillColor
            fillFraction = self.computedBlockFillSlider.value
            block_data = cv2.addWeighted(self.manager.image,(1-fillFraction),block_data,fillFraction,0)
            #define block kernels
            connectedKernelValue = self.computedBlockKernelConnected.value
            boundaryKernelValue = self.computedBlockKernelBoundary.value
            kernel_connected = np.ones((connectedKernelValue, connectedKernelValue), np.uint8)
            kernel_boundary = np.ones((boundaryKernelValue, boundaryKernelValue), np.uint8)
            blockMask = filterMask
            blockMask = cv2.dilate(blockMask, kernel_connected, iterations=1)
            blockMask = cv2.erode(blockMask, kernel_connected, iterations=1)
            blockMask = cv2.dilate(blockMask, kernel_boundary, iterations=1)
            #compute connected blocks
            blockStats = cv2.connectedComponentsWithStats(blockMask)
            #recompute mask to detect and combine connected blocks
            blockMask = np.zeros((image_data.shape[0], image_data.shape[1]), np.uint8)
            for block in blockStats[2]:
                if block[0]>0:                
                    blockMask[block[1]:block[1]+block[3],block[0]:block[0]+block[2]] = 255
            #recompute connected blocks
            blockStats = cv2.connectedComponentsWithStats(blockMask)
            borderColor = [int(255*x) for x in plt.colors.to_rgb(self.computedBlockBorderColorPicker.value)[::-1]]
            statsN = 0
            statsSmallest = [0,""]
            statsLargest = [0,""]
            for block in blockStats[2]:
                if block[0]>0:
                    #stats
                    if statsN==0:
                        statsSmallest = [block[2]*block[3],"%s x %s" % (block[2],block[3])]
                        statsLargest = [block[2]*block[3],"%s x %s" % (block[2],block[3])]
                    elif block[2]*block[3]<statsSmallest[0]:
                        statsSmallest[1] = "%s x %s" % (block[2],block[3])
                    elif block[2]*block[3]>statsLargest[0]:
                        statsLargest[1] = "%s x %s" % (block[2],block[3])
                    statsN+=1
                    #update
                    self.manager.computedBlocks.append((block[0],block[1],block[2],block[3]))
                    if self.computedBlockShow.value=="show":
                        item = block_data[block[1]:block[1]+block[3],block[0]:block[0]+block[2]]
                        image_data[block[1]:block[1]+block[3],block[0]:block[0]+block[2]] = item
                        borderWidth = max(0,self.computedBlockBorderWidth.value)
                        image_data = cv2.rectangle(image_data, (block[0],block[1]), (block[0]+block[2],block[1]+block[3]), 
                                                   borderColor, borderWidth)
            self.computedBlockStatisticsNumber.value = "%s" % statsN
            self.computedBlockStatisticsSmallest.value = statsSmallest[1]
            self.computedBlockStatisticsLargest.value = statsLargest[1]
        return bytes(cv2.imencode(".jpg", image_data)[1])

