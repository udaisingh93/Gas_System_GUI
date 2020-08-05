from org.csstudio.opibuilder.scriptUtil import ConsoleUtil
from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil
from org.eclipse.jface.dialogs import MessageDialog

#module in the same directory is visible to this script
val0=PVUtil.getDouble(pvs[0])
val1=PVUtil.getDouble(pvs[1])
val2=PVUtil.getDouble(pvs[2])
val3=PVUtil.getDouble(pvs[3])
val4=PVUtil.getDouble(pvs[4])
val5=PVUtil.getDouble(pvs[5])
PVUtil.writePV("loc://button0",val0)
PVUtil.writePV("loc://button1",val1)
PVUtil.writePV("loc://button2",val2)
PVUtil.writePV("loc://button3",val3)
PVUtil.writePV("loc://button4",val4)
PVUtil.writePV("loc://button5",val5)