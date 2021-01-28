import wx
import wx.adv
import config
import db

def create_about_dialog():
    info = wx.adv.AboutDialogInfo()

    info.SetIcon(wx.Icon(config.path_img + config.icon_name, wx.BITMAP_TYPE_ANY))
    info.SetName(config.program_name)
    info.SetVersion(config.version)
    info.SetDescription(config.description)
    info.SetCopyright(config.copyright)
    info.SetWebSite(config.web_site)
    info.AddDeveloper(config.developer)
    info.AddDocWriter(config.doc_writer)

    wx.adv.AboutBox(info)


class AdditionDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super(AdditionDialog, self).__init__(*args, **kwargs)

        self.create_dialog()

    def create_dialog(self):
        panel = wx.Panel(self)

        mainbox = wx.GridBagSizer(4, 4)

        label = wx.StaticText(panel, label='Введите название:')
        mainbox.Add(label, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=15)

        self.text = wx.TextCtrl(panel)
        mainbox.Add(self.text, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        button_ok = wx.Button(panel, label='Добавить', size=(90, 28), id=wx.ID_OK)
        mainbox.Add(button_ok, pos=(3, 3))

        button_cancel = wx.Button(panel, label="Отмена", size=(90,28), id=wx.ID_CANCEL)
        mainbox.Add(button_cancel, pos=(3, 4), flag=wx.RIGHT|wx.BOTTOM, border=10)

        mainbox.AddGrowableCol(1)
        mainbox.AddGrowableRow(2)
        panel.SetSizer(mainbox)


class MyAskDialog(wx.Dialog):
    def __init__(self, *args, **kw):
        super(MyAskDialog, self).__init__( *args, **kw)

    def create_car(self):
        """ create a dialog with form of a car's addtition  """
        pnl = wx.Panel(self)

        mainbox = wx.GridBagSizer(8, 4)

        # model
        model_label = wx.StaticText(pnl, label='Марка:')
        mainbox.Add(model_label, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=15)

        model_cb = wx.ComboBox(pnl, choices=['asdsdfsdfdsf', 'bsdfsdfsf', 'csdfsdfdf'], 
                               style=wx.CB_READONLY) # DB.MODEL_NAMES DON'T EXIST!
        mainbox.Add(model_cb, pos=(0, 1), span=(1, 2),
                    flag=wx.TOP | wx.LEFT | wx.EXPAND, border=5)  

        add_model_button = wx.Button(pnl, label='+', size=(40, 40), id=1)
        mainbox.Add(add_model_button, pos=(0, 3), flag=wx.LEFT | wx.TOP | wx.RIGHT, border=10)
        add_model_button.Bind(wx.EVT_BUTTON, self.on_add_model)

        # body_type
        body_type_label = wx.StaticText(pnl, label='Модель:')
        mainbox.Add(body_type_label, pos=(1, 0), flag=wx.LEFT | wx.TOP, border=15)

        body_type_cb = wx.ComboBox(pnl, choices=['dsd', 'sdfdf', 'fsdfsdf'], 
                                   style=wx.CB_READONLY) # !!!!!!!!!!!!!!!!!!!!!!!!111
        mainbox.Add(body_type_cb, pos=(1, 1), span=(1, 2), 
                    flag=wx.TOP | wx.LEFT | wx.EXPAND, border=5)

        add_bodytype_button = wx.Button(pnl, label='+', size=(40, 40), id=2)
        mainbox.Add(add_bodytype_button, pos=(1, 3), flag=wx.LEFT | wx.TOP, border=10)
        add_bodytype_button.Bind(wx.EVT_BUTTON, self.on_add_bodytype)

        # color
        color_label = wx.StaticText(pnl, label='Цвет:')
        mainbox.Add(color_label, pos=(2, 0), flag=wx.LEFT | wx.TOP, border=15)

        color_cb = wx.ComboBox(pnl, choices=['wer', 'erwrwe', 'erwer'],
                               style=wx.CB_READONLY)                       # !!!!!!!!!!!!!!!!!!!!1
        mainbox.Add(color_cb, pos=(2, 1), span=(1, 2), flag=wx.TOP | wx.LEFT | wx.EXPAND, border=5)

        add_color_button = wx.Button(pnl, label='+', size=(40, 40), id=3)
        mainbox.Add(add_color_button, pos=(2, 3), flag=wx.LEFT | wx.TOP, border=10)
        add_color_button.Bind(wx.EVT_BUTTON, self.on_add_color)

        # ptc number
        ptcnum_label = wx.StaticText(pnl, label='№ РТС:')
        mainbox.Add(ptcnum_label, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=15)

        ptc_text = wx.TextCtrl(pnl)
        mainbox.Add(ptc_text, pos=(3, 1), span=(1, 2), flag=wx.TOP | wx.LEFT | wx.EXPAND, border=5)

        # mileage
        mileage_label = wx.StaticText(pnl, label='Пробег:')
        mainbox.Add(mileage_label, pos=(4, 0), flag=wx.LEFT | wx.TOP, border=15)

        mileage_text = wx.TextCtrl(pnl)
        mainbox.Add(mileage_text, pos=(4, 1), span=(1, 2), flag=wx.TOP | wx.LEFT | wx.EXPAND, border=5)

        # engine capacity
        eng_capacity_label = wx.StaticText(pnl, label='Объем двигателя:')
        mainbox.Add(eng_capacity_label, pos=(5, 0), flag=wx.LEFT | wx.TOP, border=15)

        eng_capacity_text = wx.TextCtrl(pnl)
        mainbox.Add(eng_capacity_text, pos=(5, 1), span=(1, 2), flag=wx.TOP | wx.LEFT | wx.EXPAND, border=5)

        # transmition
        transmition_label = wx.StaticText(pnl, label='Коробка передач:')
        mainbox.Add(transmition_label, pos=(6, 0), flag=wx.LEFT | wx.TOP, border=15)

        mech_t_radbut = wx.RadioButton(pnl, label='МКПП')
        mainbox.Add(mech_t_radbut, pos=(6, 1), flag=wx.TOP | wx.LEFT, border=10)

        auto_t_radbut = wx.RadioButton(pnl, label='АКПП')
        mainbox.Add(auto_t_radbut, pos=(6, 2), flag=wx.TOP | wx.LEFT, border=10)

        # cost
        price_label = wx.StaticText(pnl, label='Цена')
        mainbox.Add(price_label, pos=(7, 0), flag=wx.TOP | wx.LEFT, border=15)

        price_slider = wx.Slider(pnl, value=1000000, minValue=200000, 
                                 maxValue=40000000, style=wx.SL_HORIZONTAL)
        price_slider.Bind(wx.EVT_SCROLL, self.on_slider_scroll)
        mainbox.Add(price_slider, pos=(7, 1), span=(1, 2), flag=wx.TOP | wx.LEFT | wx.EXPAND, border=5)

        self.price_val = wx.StaticText(pnl, label='1000000')
        mainbox.Add(self.price_val, pos=(7, 3), flag=wx.TOP | wx.LEFT, border=10)

        save_button = wx.Button(pnl, label='Сохранить', id=wx.ID_OK)
        mainbox.Add(save_button, pos=(8, 2), flag=wx.TOP | wx.LEFT, border=10)

        cancel_button = wx.Button(pnl, label='Отмена', id=wx.ID_CANCEL)
        mainbox.Add(cancel_button, pos=(8, 3), flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)

        mainbox.AddGrowableCol(1)

        pnl.SetSizer(mainbox)
        mainbox.SetMinSize((600, 500))
        mainbox.Fit(self)

    def on_slider_scroll(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()

        self.price_val.SetLabel(str(val))

    def on_add_model(self, e):
        with AdditionDialog(None, title='Добавить марку') as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                db.add_model(dlg.text.GetValue())
            else:
                print('bye')

    def on_add_bodytype(self, e):
        with AdditionDialog(None, title='Добавить модель') as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                db.add_body_type(dlg.text.GetValue())
            else:
                print('bye')

    def on_add_color(self, e):
        with AdditionDialog(None, title='Добавить цвет') as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                db.add_color(dlg.text.GetValue())
            else:
                print('bye')






