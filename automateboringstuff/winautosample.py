from pywinauto import Desktop, Application, taskbar
import pywinauto
import time 

# texts = taskbar.SystemTrayIcons.texts()
# print (texts)

# taskbar.ClickHiddenSystemTrayIcon("Everything")

app = Application(backend="uia").connect(path="explorer.exe")
st = app.window(class_name="Shell_TrayWnd")

notificationChevronBtn = st.child_window(title="Notification Chevron").wrapper_object()
notificationChevronBtn.click()

iconOverflowApp = Application(backend="uia").connect(class_name="NotifyIconOverflowWindow", timeout=0.25)
iconOverflowWnd = iconOverflowApp.window(class_name="NotifyIconOverflowWindow")
iconOverflowWnd.wait('visible', timeout=30, retry_interval=3)

# main_tray_toolbar = st.child_window(title="Overflow Notification Area", control_type="ToolBar")
# icon = main_tray_toolbar.child_window(title="Everything", control_type="Button")
# icon.click_input(button="right")
ciscovpnWnd = iconOverflowWnd.child_window(title_re="Cisco AnyConnect.*")
ciscovpnWnd.click_input(button="right")
time.sleep(1)

# print(Desktop(backend='uia').ContextMenu.dump_tree()
openAnyconnectItem = Desktop(backend='uia').ContextMenu.child_window(title="Open AnyConnect").wrapper_object()
openAnyconnectItem.invoke()
# showSearchWindowItem.click()
print("launched the cisco client ui")

ciscoApp = Application(backend="uia").connect(title= "Cisco AnyConnect Secure Mobility Client")
# ciscoApp.CiscoAnyConnectSecureMobilityClient.print_control_identifiers()
ciscoDlg = ciscoApp.window()
ciscoDlg.Connect.click()
ciscoDlg.Dialog.wait("ready")
connectDlg = ciscoApp.window().Dialog
connectDlg.child_window(title="Username:", control_type="Edit").set_text("dhirajsuvarna")
connectDlg.child_window(title="Password:", control_type="Edit").set_text("dhirajsuvarna") 
connectDlg.OK.click()

