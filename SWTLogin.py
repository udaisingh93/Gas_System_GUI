from org.eclipse.jface.dialogs import MessageDialog
from org.eclipse.jface.window import Window
from SWTLoginDialog import *    
        
    
dialog = LoginDialog(Display.getCurrent().getActiveShell())
a = dialog.open() 
if a == Window.OK:
    info = dialog.getLoginInfo()
    if info[0] == "admin" and info[1]=="123456":
        display.getWidget("Text Input_7").setEnabled(True)
        display.getWidget("Text Input_3").setEnabled(True)
        display.getWidget("Text Input_2").setEnabled(True)
        display.getWidget("Text Input_4").setEnabled(True)
        display.getWidget("Text Input_5").setEnabled(True)
    else:
        MessageDialog.openError(None, "Error", "The user name or password you input is wrong!")