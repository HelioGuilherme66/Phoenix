import wx
from wx.lib.ticker import Ticker
from six import BytesIO

import EnhancedStatusBar as ESB

#----------------------------------------------------------------------
def GetMondrianData():
    return \
b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\x00\x00 \x08\x06\x00\
\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00qID\
ATX\x85\xed\xd6;\n\x800\x10E\xd1{\xc5\x8d\xb9r\x97\x16\x0b\xad$\x8a\x82:\x16\
o\xda\x84pB2\x1f\x81Fa\x8c\x9c\x08\x04Z{\xcf\xa72\xbcv\xfa\xc5\x08 \x80r\x80\
\xfc\xa2\x0e\x1c\xe4\xba\xfaX\x1d\xd0\xde]S\x07\x02\xd8>\xe1wa-`\x9fQ\xe9\
\x86\x01\x04\x10\x00\\(Dk\x1b-\x04\xdc\x1d\x07\x14\x98;\x0bS\x7f\x7f\xf9\x13\
\x04\x10@\xf9X\xbe\x00\xc9 \x14K\xc1<={\x00\x00\x00\x00IEND\xaeB`\x82'

def GetMondrianBitmap():
    return wx.Bitmap(GetMondrianImage())

def GetMondrianImage():
    stream = BytesIO(GetMondrianData())
    return wx.Image(stream)

def GetMondrianIcon():
    icon = wx.Icon()
    icon.CopyFromBitmap(GetMondrianBitmap())
    return icon


class DemoFrame1(wx.Frame):
    def __init__(self, parent, id=-1, title="EnhancedStatusBar Demo 1", pos=wx.DefaultPosition,
                 size=(780,500)):

        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.SetIcon(GetMondrianIcon())

        panel = wx.Panel(self, -1)

        strs = "EnhancedStatusBar Demo 1\n" \
               "By Andrea Gavana @ 31 May 2005"
        text = wx.StaticText(panel, -1, strs, pos=(50, 30))
        text.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False))

        strs = "This Demo Implements An Example Of EnhancedStatusBar\n" \
               "The StatusBar Is Populated By:\n\n" \
               "- 2 wx.StaticBitmap;\n" \
               "- 1 wx.Button;\n" \
               "- 1 wx.Gauge;\n" \
               "- 1 wx.Choice;\n" \
               "- 1 wx.lib.ticker;\n" \
               "- 1 wx.StaticText.\n\n" \
               "All The Controls Are Aligned Using ESB_ALIGN_CENTER_VERTICAL And\n" \
               "ESB_ALIGN_CENTER_HORIZONTAL.\n\n"\
               "The StatusBar Height Has Been Set To 23 Pixels Using SetMinHeight()."

        text = wx.StaticText(panel, -1, strs, pos=(50, 90))        

        self.statusbar = ESB.EnhancedStatusBar(self, -1)
        self.statusbar.SetSize((-1, 23))
        self.statusbar.SetFieldsCount(7)
        self.statusbar.SetStatusWidths([50, 50, 100, 120, 120, 140, -1])
        self.SetStatusBar(self.statusbar)

        bmp = wx.ArtProvider.GetBitmap(wx.ART_ERROR)  # , wx.ART_OTHER, (16,16))  # ART_TOOLBAR
        
        upbmp = wx.StaticBitmap(self.statusbar, -1, bmp)
        self.statusbar.AddWidget(upbmp)

        bmp = wx.ArtProvider.GetBitmap(wx.ART_HELP)  # , wx.ART_OTHER, (16,16))
        
        downbmp = wx.StaticBitmap(self.statusbar, -1, bmp)
        self.statusbar.AddWidget(downbmp)

        btnmio = wx.Button(self.statusbar, -1, "Push Me!")
        self.statusbar.AddWidget(btnmio)

        gauge = wx.Gauge(self.statusbar, -1, 50)
        """
        choice = wx.Choice(self.statusbar, -1, size=(100,-1),
                           choices=['Hello', 'World!', 'What', 'A', 'Beautiful', 'Class!'])
        self.statusbar.AddWidget(choice)
        """
        ticker = Ticker(self.statusbar, -1)
        ticker.SetText("Hello World!")
        ticker.SetBackgroundColour(wx.BLUE)
        ticker.SetForegroundColour(wx.YELLOW)
        ticker.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        """
        statictext = wx.StaticText(self.statusbar, -1, "Welcome To wxPython!")
        self.statusbar.AddWidget(statictext)
        """
        self.ticker = ticker
        self.gauge = gauge
        self.count = 0
        """
        statusbarchildren = self.statusbar.GetChildren()
        for widget in statusbarchildren:
            self.statusbar.AddWidget(widget)
        """
        self.Bind(wx.EVT_IDLE, self.IdleHandler)
        self.Bind(wx.EVT_CLOSE, self.OnClose)


    def IdleHandler(self, event):
        _ = event
        self.count = self.count + 1
        if self.count >= 50:
            self.count = 0
        self.gauge.SetValue(self.count)

    def OnClose(self, event):
        _ = event
        self.ticker.Stop()
        self.Destroy()


class DemoFrame2(wx.Frame):

    def __init__(self, parent, id=-1, title="EnhancedStatusBar Demo 2", pos=wx.DefaultPosition,
                 size=(780,540)):

        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.SetIcon(GetMondrianIcon())
        
        panel = wx.Panel(self, -1)

        strs = "EnhancedStatusBar Demo 2\n" \
               "By Andrea Gavana @ 31 May 2005"
        text = wx.StaticText(panel, -1, strs, pos=(50, 30))
        text.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False))

        strs = "This Demo Implements An Example Of EnhancedStatusBar\n" \
               "The StatusBar Is Populated By:\n\n" \
               "- 1 wx.ListBox (Aligned Using ESB.ESB_EXACT_FIT, ESB.ESB_EXACT_FIT);\n\n" \
               "- 1 wx.RadioBox (Aligned Using The Default (Both Centered));\n\n" \
               "- 1 wx.Slider (Aligned Using ESB.ESB_ALIGN_LEFT, ESB.ESB_ALIGN_BOTTOM);\n\n" \
               "- 1 wx.SpinCtrl (Aligned Using ESB.ESB_ALIGN_RIGHT, ESB.ESB_ALIGN_TOP);\n\n" \
               "- 1 wx.TreeCtrl (Aligned Using ESB.ESB_EXACT_FIT, ESB.ESB_EXACT_FIT);\n\n" \
               "The StatusBar Height Has Been Set To 150 Pixels Using SetMinHeight()."
        
        text = wx.StaticText(panel, -1, strs, pos=(50, 90))        

        self.statusbar = ESB.EnhancedStatusBar(self, -1)
        self.statusbar.SetSize((-1, 150))
        self.statusbar.SetFieldsCount(5)
        self.statusbar.SetStatusWidths([100, 200, 120, 130, -1])
        self.SetStatusBar(self.statusbar)

        sample_list = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven']

        listbox = wx.ListBox(self.statusbar, -1, choices=sample_list,
                             style=wx.LB_SINGLE)
        
        radiobox = wx.RadioBox(self.statusbar, -1, "RadioBox",
                         wx.DefaultPosition, wx.DefaultSize,
                         sample_list, 3, wx.RA_SPECIFY_COLS | wx.NO_BORDER)
                
        slider = wx.Slider(self.statusbar, -1, 25, 1, 100,
                           style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        slider.SetTickFreq(5)
        
        spinctrl = wx.SpinCtrl(self.statusbar, -1, "SpinCtrl")
        spinctrl.SetRange(1,100)
        spinctrl.SetValue(5)
        
        self.tree = wx.TreeCtrl(self.statusbar, -1, wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_HAS_BUTTONS)
        
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        fldridx     = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,   wx.ART_OTHER, isz))
        fileidx     = il.Add(wx.ArtProvider.GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER, isz))

        self.tree.SetImageList(il)
        self.il = il

        root = self.tree.AddRoot("Root")
        self.tree.SetItemData(root, None)
        self.tree.SetItemImage(root, fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, fldropenidx, wx.TreeItemIcon_Selected)

        for x in range(15):
            child = self.tree.AppendItem(root, "Item %d" % x)
            self.tree.SetItemData(child, None)
            self.tree.SetItemImage(child, fldridx, wx.TreeItemIcon_Normal)
            self.tree.SetItemImage(child, fldropenidx, wx.TreeItemIcon_Selected)

        self.tree.Expand(root)
        
        statusbarchildren = self.statusbar.GetChildren()
        
        self.statusbar.AddWidget(listbox, ESB.ESB_EXACT_FIT, ESB.ESB_EXACT_FIT)
        self.statusbar.AddWidget(radiobox)
        self.statusbar.AddWidget(slider, ESB.ESB_ALIGN_LEFT, ESB.ESB_ALIGN_BOTTOM)
        self.statusbar.AddWidget(spinctrl, ESB.ESB_ALIGN_RIGHT, ESB.ESB_ALIGN_TOP)
        self.statusbar.AddWidget(self.tree, ESB.ESB_EXACT_FIT, ESB.ESB_EXACT_FIT)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        _ = event
        self.Destroy()


class DemoFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, id=-1, parent=parent, pos=wx.DefaultPosition, size=wx.Size(410, 396),
                          title='EnhancedStatusBar Demo 2')
        self.statusbarText = None
        self.statusbarConnIcon = None
        self.connected = False
        self._init_ctrls()
        self.SetConnected(False)

    def _init_ctrls(self):
        self.SetIcon(GetMondrianIcon())
        panel = wx.Panel(self, -1)

        strs = "EnhancedStatusBar Demo 3\n" \
               "By Nitro @ 21 September 2005"

        text = wx.StaticText(panel, -1, strs, pos=(50, 30))        
        text.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False))

        strs = "The ESB is populated with\n\n" \
               " - A simple TextCtrl\n" \
               " - A simple StaticBitmap\n\n" \
               "Click the icon to change the status\n\n" \
               "This demo shows that you can replace widgets once you've placed\n" \
               "them into the ESB. This was not possible before. Enjoy!"

        text = wx.StaticText(panel, -1, strs, pos=(50, 90))        

        self.statusbar = ESB.EnhancedStatusBar(self, -1)
        self.statusbar.SetSize((-1, 25))
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-1, 60])
        self.SetStatusBar(self.statusbar)

    def SetStatusMsg(self, msg):
        self.statusbarText = wx.StaticText(self.statusbar, -1, msg)
        self.statusbar.AddWidget(self.statusbarText, pos=0)
    
    def SetConnected(self, connected):
        self.connected = connected
        
        if connected:
            img = wx.ART_TICK_MARK
            self.SetStatusMsg('Connected')
        else:
            img = wx.ART_ERROR
            self.SetStatusMsg('Not connected')

        bmp = wx.ArtProvider.GetBitmap(img, wx.ART_TOOLBAR, (16,16))

        self.statusbarConnIcon = wx.StaticBitmap(self.statusbar, -1, bmp)
        self.statusbarConnIcon.Bind(wx.EVT_LEFT_UP, self.ChangeIcon)
        self.statusbar.AddWidget(self.statusbarConnIcon, pos=1)

    def ChangeIcon(self, event):
        _ = event
        self.SetConnected(not self.connected)        


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title="EnhancedStatusBar Demo Main Frame",
                 pos=wx.DefaultPosition, size=(500,300))

        self.SetIcon(GetMondrianIcon())
        panel = wx.Panel(self, -1)

        button1 = wx.Button(panel, -1, "Start Demo 1", pos=(50,100))
        button2 = wx.Button(panel, -1, "Start Demo 2", pos=(50,150))
        button3 = wx.Button(panel, -1, "Start Demo 3", pos=(50,200))

        strs = "EnhancedStatusBar Demo\n" \
               "By Andrea Gavana @ 31 May 2005"
        text = wx.StaticText(panel, -1, strs, pos=(50, 30))
        text.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False))

        text = wx.StaticText(panel, -1, "Starts The EnhancedStatusBar Demo 1", pos=(170, 105))
        text.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        text.SetForegroundColour(wx.BLUE)
        text = wx.StaticText(panel, -1, "Starts The EnhancedStatusBar Demo 2", pos=(170, 155))
        text.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        text.SetForegroundColour(wx.RED)
        text = wx.StaticText(panel, -1, "Starts The EnhancedStatusBar Demo 3", pos=(170, 205))
        text.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        text.SetForegroundColour(wx.BLACK)
        
        button1.Bind(wx.EVT_BUTTON, self.OnButton1)
        button2.Bind(wx.EVT_BUTTON, self.OnButton2)
        button3.Bind(wx.EVT_BUTTON, self.OnButton3)

    def OnButton1(self, event):
        frame = DemoFrame1(self)
        frame.CenterOnScreen()
        frame.Show()
        event.Skip()

    def OnButton2(self, event):
        frame = DemoFrame2(self)
        frame.CenterOnScreen()
        frame.Show()
        event.Skip()

    def OnButton3(self, event):
        frame = DemoFrame3(self)
        frame.CenterOnScreen()
        frame.Show()
        event.Skip()


def main():
    app = wx.App()
    frame = MainFrame(None)
    frame.CenterOnScreen()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
