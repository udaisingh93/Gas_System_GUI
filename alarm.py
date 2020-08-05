from org.csstudio.opibuilder.scriptUtil import ConsoleUtil
from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil
from org.eclipse.jface.dialogs import MessageDialog

#module in the same directory is visible to this script

GREY = ColorFontUtil.getColorFromRGB(180, 180, 180)
RED = ColorFontUtil.RED
BLACK = ColorFontUtil.getColorFromRGB(0, 0, 0)

val0=PVUtil.getDouble(pvs[1])
#val1=PVUtil.getDouble(pvs[1])
if val0>2.06:
	widget.executeAction(1);
	display.getWidget("Label_66").setPropertyValue("text","STS1 Pressure is too high !")
	display.getWidget("Rectangle").setPropertyValue("background_color",RED)
	display.getWidget("Label_66").setPropertyValue("foreground_color",RED)
	#widget.executeAction(1);
if val0<2.06 and val0>1.9:
	display.getWidget("Label_66").setPropertyValue("text","None")
	display.getWidget("Label_66").setPropertyValue("foreground_color",BLACK)
	display.getWidget("Rectangle").setPropertyValue("background_color",GREY)
if val0<1.9:
	widget.executeAction(0);
	display.getWidget("Label_66").setPropertyValue("text","STS1 Pressure is too low !")
	display.getWidget("Rectangle").setPropertyValue("background_color",RED)
	display.getWidget("Label_66").setPropertyValue("foreground_color",RED)
	#widget.executeAction(1);
