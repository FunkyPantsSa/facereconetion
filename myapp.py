import wx
import os
from importlib import reload
import face_img_register
import face_recognize_punchcard
# import blinks
import sys



file_path = os.getcwd()+r'\data\logcat.csv' #签到日志文件
class   Mainui(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self,parent=superion,title="人脸识别考勤系统",size=(600,600), )
        self.SetBackgroundColour('#2EA9DF') #修改背景色
        self.Center()
        self.frame = ''

        # 背景图片和按钮
        image_file = r'.\icon\background.png'
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY,-1).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (200, 0))
        self.RegisterButton = wx.Button(self.bitmap, -1, label='人脸录入', pos=(200, 205),size=(210,25),style=wx.BORDER_NONE)
        self.PunchcardButton = wx.Button(self.bitmap, -1, label='签到考勤', pos=(200, 265),size=(210,25),style=wx.BORDER_NONE)
        self.LogcatButton = wx.Button(self.bitmap, -1, label='签到日志', pos=(200, 325),size=(210,25),style=wx.BORDER_NONE)
        self.InstructButton = wx.Button(self.bitmap, -1, label='操作指南', pos=(200, 385),size=(210,25),style=wx.BORDER_NONE)
        # self.BlinkButton = wx.Button(parent=self,pos=(500,120),size=(80,50),label='活体检测')




        font = wx.Font(13, wx.DECORATIVE, wx.BOLD, wx.BOLD)
        self.InstructButton.SetFont(font)
        self.RegisterButton.SetFont(font)
        self.PunchcardButton.SetFont(font)
        self.LogcatButton.SetFont(font)

        self.RegisterButton.SetForegroundColour('#00A1FC')
        self.RegisterButton.SetBackgroundColour('#001e82')

        self.PunchcardButton.SetForegroundColour('#00A1FC')
        self.PunchcardButton.SetBackgroundColour('#001e82')

        self.LogcatButton.SetForegroundColour('#00A1FC')
        self.LogcatButton.SetBackgroundColour('#001e82')

        self.InstructButton.SetForegroundColour('#00A1FC')
        self.InstructButton.SetBackgroundColour('#001e82')
        # 按钮绑定的事件
        self.Bind(wx.EVT_BUTTON,self.OnRegisterButtonClicked,self.RegisterButton)
        self.Bind(wx.EVT_BUTTON,self.OnPunchCardButtonClicked,self.PunchcardButton)
        self.Bind(wx.EVT_BUTTON,self.OnLogcatButtonClicked,self.LogcatButton)
        self.Bind(wx.EVT_BUTTON,self.OnInstructButtonClicked,self.InstructButton)
        # self.Bind(wx.EVT_BUTTON, self.BlinkButtonClicked, self.BlinkButton)
        # self.Bind(wx.EVT_BUTTON,self.OnForkButtonClicked,self.ForkButton)
        # self.Bind(wx.EVT_BUTTON,self.OnAboutButtonClicked,self.AboutButton)



    def OnRegisterButtonClicked(self,event):
        reload(face_img_register)

        #del sys.modules['face_img_register']
        #import face_img_register
        #runpy.run_path("face_img_register.py")
        #frame = face_img_register.RegisterUi(None)

        app.frame = face_img_register.RegisterUi(None)
        app.frame.Show()

    def OnPunchCardButtonClicked(self,event):
        #del sys.modules['face_recognize_punchcard']
        reload(face_recognize_punchcard)
        #import face_recognize_punchcard
        app.frame = face_recognize_punchcard.PunchcardUi(None)
        app.frame.Show()

    def OnLogcatButtonClicked(self,event):
        if os.path.exists(file_path):
            #调用系统默认程序打开文件
            os.startfile(file_path)
        else:
            wx.MessageBox(message="要先运行过一次刷脸签到系统，才有日志", caption="警告")
        pass


    def OnInstructButtonClicked(self,event):
        wx.MessageBox(message="一、人脸的录入\n"
                              "1、点击人脸录入按钮，输入管理员密码。\n"
                              "2、输入您的学号和姓名.\n"
                              "3、点击开始录入.\n"
                              "4、待摄像头获取视频流之后，点击截图保存。请保存4-7张照片\n"
                              "5、点击完成录入，结束人脸录入。\n"
                              "二、签到考勤\n"
                              "1、在主页面点击考勤签到按钮\n"
                              "2、在考勤页面点击开始签到按钮\n",caption="操作说明")
        pass

    # def BlinkButtonClicked (self,event):
    #     app.frame = blinks(None)
    #     app.frame.Show()

class MainApp(wx.App):
    def OnInit(self):
        self.frame = Mainui(None)
        self.frame.Show()
        return True

app = MainApp()
app.MainLoop()