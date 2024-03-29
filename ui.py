import wx
import config
import dialogs
import actions
import wx.lib.mixins.listctrl



cl_index = ['№', 'Фамилия', 'Имя', 'Отчество', 'Серия, номер паспорта', 'Телефон', 'Email']



cl = {}


class MyListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ColumnSorterMixin,
                 wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin):
    def __init__(self, parent, data, *args, **kw):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(data))
        wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin.__init__(self)
        self.itemDataMap = data

    def add_data_to_listCtrl(self, data_index, data):
        for i, name in enumerate(data_index):
            self.InsertColumn(i, name, width=100)

        items = data.items()

        idx = 0

        for key, inf in items:
            index = self.InsertItem(idx, str(key))
            for i in range(1, len(data_index)):
                self.SetItem(index, i, inf[i-1])
            self.SetItemData(index, key)
            idx += 1

    def clear(self):
        self.ClearAll()

    def GetListCtrl(self):
        return self


class MyPopupMenu(wx.Menu):
    """ create a context menu with items such as copy, paste and cut"""
    def __init__(self):
        super(MyPopupMenu, self).__init__()

        self.create_items()

    def create_items(self):
        """ creates 3 menu items: cut, copy, paste """
        cut_menuitem = wx.MenuItem(self, wx.ID_CUT, 'Вырезать')
        self.Append(cut_menuitem)
        self.Bind(wx.EVT_MENU, self.cut, cut_menuitem)

        copy_menuitem = wx.MenuItem(self, wx.ID_COPY, 'Копировать')
        self.Append(copy_menuitem)
        self.Bind(wx.EVT_MENU, self.copy, copy_menuitem)

        paste_menuitem = wx.MenuItem(self, wx.ID_PASTE, 'Вставить')
        self.Append(paste_menuitem)
        self.Bind(wx.EVT_MENU, self.paste, paste_menuitem)

    def paste(self, e):
        pass

    def copy(self, e):
        pass

    def cut(self, e):
        pass


class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.SetIcon(wx.Icon(config.path_img + config.icon_name,
                             wx.BITMAP_TYPE_ANY))
        self.SetMenuBar(self.create_menubar())
        self.create_toolbar()
        self.disable_toolbar()
        self.status_bar = self.CreateStatusBar()
        self.SetSize(config.size)
        self.Centre()
        self.SetTitle(config.title)
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_RIGHT_DOWN, self.onright_down)
        wx.StaticLine(self, size=(1050, 1))
        self.fSizer = wx.BoxSizer(wx.VERTICAL)
        self.panel_catalog = self.create_panel()
        self.fSizer.Add(self.panel_catalog, 1, wx.EXPAND)
        self.SetSizer(self.fSizer)
        wx.StaticLine(self, size=(1050, 1))
        self.status_bar.SetStatusText('Главная')

    def create_panel(self, data=actions.get_cars_data(), data_index=config.cars_index):
        """ creates panel, which includes a table and buttons,
            has default arguements such as data and data_index,
            which takes data from database """
        panel = wx.Panel(self)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(2, 1, 9, 25)

        button_sizer = self.create_buttons()
        self.data_list = MyListCtrl(self, data)
        self.data_list.add_data_to_listCtrl(data_index, data)

        fgs.AddMany([(self.data_list, 1, wx.EXPAND),
                     (button_sizer, 1, wx.EXPAND)])

        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableCol(0, 1)

        main_sizer.Add(fgs, 1, wx.CENTER | wx.ALL | wx.EXPAND, 10)
        panel.SetSizer(main_sizer)
        return panel

    def onright_down(self, e):
        ''' show contex menu when right mouse button is clicked '''
        self.PopupMenu(MyPopupMenu(), e.GetPosition())

    def create_menubar(self):
        '''create menu bar '''
        menubar = wx.MenuBar()

        file_menu = wx.Menu()
        open_mi = wx.MenuItem(file_menu, wx.ID_OPEN, 'Открыть')
        save_mi = wx.MenuItem(file_menu, wx.ID_SAVE, 'Сохранить')
        save_as_mi = wx.MenuItem(file_menu, wx.ID_ANY, 'Сохранить как...')
        quit_mi = wx.MenuItem(file_menu, wx.ID_ANY, 'Выход')

        file_menu.Append(open_mi)
        file_menu.Append(save_mi)
        file_menu.Append(save_as_mi)
        file_menu.Append(quit_mi)

        self.Bind(wx.EVT_MENU, self.upload_data, open_mi)
        self.Bind(wx.EVT_MENU, self.save_data, save_mi)
        self.Bind(wx.EVT_MENU, self.save_as, save_as_mi)
        self.Bind(wx.EVT_MENU, self.on_close, quit_mi)

        menubar.Append(file_menu, 'Файл')

        edit_menu = MyPopupMenu()
        menubar.Append(edit_menu, 'Редактировать')

        display_menu = wx.Menu()
        catalogue_mi = wx.MenuItem(display_menu, wx.ID_ANY, 'Каталог')
        orders_mi = wx.MenuItem(display_menu, wx.ID_ANY, 'Заказы')
        clients_mi = wx.MenuItem(display_menu, wx.ID_ANY, 'Клиенты')
        docs_mi = wx.MenuItem(display_menu, wx.ID_ANY, 'Документы')

        display_menu.Append(catalogue_mi)
        display_menu.Append(orders_mi)
        display_menu.Append(clients_mi)
        display_menu.Append(docs_mi)

        self.Bind(wx.EVT_MENU, self.show_catalogue, catalogue_mi)
        self.Bind(wx.EVT_MENU, self.show_orders, orders_mi)
        self.Bind(wx.EVT_MENU, self.show_clients, clients_mi)
        self.Bind(wx.EVT_MENU, self.show_docs, docs_mi)

        menubar.Append(display_menu, 'Показать')

        about_menu = wx.Menu()
        about_mi = wx.MenuItem(about_menu, wx.ID_ANY, 'О нас')
        about_menu.Append(about_mi)
        self.Bind(wx.EVT_MENU, self.show_about, about_mi)

        menubar.Append(about_menu, 'Справка')

        return menubar

    def create_toolbar(self):
        """ creates toolbar """
        self.toolbar = self.CreateToolBar(wx.TB_HORIZONTAL | wx.TB_DOCKABLE | wx.TB_FLAT)

        home_tool = self.toolbar.AddTool(30, 'На главную',
                                    wx.Bitmap(config.path_img + config.home_img))
        newfile_tool = self.toolbar.AddTool(10, 'Создать',
                                       wx.Bitmap(config.path_img + config.file_img))
        save_tool = self.toolbar.AddTool(20, 'Сохранить',
                                    wx.Bitmap(config.path_img + config.save_img))
        print_tool = self.toolbar.AddTool(50, 'Печать',
                                     wx.Bitmap(config.path_img + config.print_img))
        search_tool = self.toolbar.AddTool(40, 'Поиск',
                                      wx.Bitmap(config.path_img + config.search_img))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.show_start_page, home_tool)
        self.Bind(wx.EVT_TOOL, self.create_data, newfile_tool)
        self.Bind(wx.EVT_TOOL, self.save_data, save_tool)
        self.Bind(wx.EVT_TOOL, self.print_data, print_tool)
        self.Bind(wx.EVT_TOOL, self.search, search_tool)

    def disable_toolbar(self):
        """ disables toolbar"""
        self.toolbar.EnableTool(30, False)
        self.toolbar.EnableTool(10, False)
        self.toolbar.EnableTool(20, False)
        self.toolbar.EnableTool(50, False)
        self.toolbar.EnableTool(40, False)

    def enable_toolbar(self):
        self.toolbar.EnableTool(30, True)
        self.toolbar.EnableTool(10, True)
        self.toolbar.EnableTool(20, True)
        self.toolbar.EnableTool(50, True)
        self.toolbar.EnableTool(40, True)        

    def create_buttons(self):
        button_sizer = wx.GridSizer(1, 4, 5, 5)

        open_but = wx.Button(self, config.ID_BUTTON + 1,
                             'Открыть', size=(50, 30))
        edit_but = wx.Button(self, config.ID_BUTTON + 2,
                             'Изменить', size=(50, 30))
        delete_but = wx.Button(self, config.ID_BUTTON + 3,
                               'Удалить', size=(50, 30))
        saveas_but = wx.Button(self, config.ID_BUTTON + 4,
                               'Сохранить...', size=(50, 30))

        button_sizer.AddMany([(open_but, 0, wx.EXPAND),
                              (edit_but, 0, wx.EXPAND),
                              (delete_but, 0, wx.EXPAND),
                              (saveas_but, 0, wx.EXPAND)])

        self.Bind(wx.EVT_BUTTON, self.upload_data, open_but)
        self.Bind(wx.EVT_BUTTON, self.edit_data, edit_but)
        self.Bind(wx.EVT_BUTTON, self.delete_data, delete_but)
        self.Bind(wx.EVT_BUTTON, self.save_as, saveas_but)

        return button_sizer

    def edit_data(self, e):
        pass

    def delete_data(self, e):
        pass

    def upload_data(self, e):
        pass

    def save_data(self, e):
        pass

    def save_as(self, e):
        pass

    def on_close(self, e):
        self.Close()

    def show_catalogue(self, e):
        """ displays data from catalog table"""
        name_mode = 'Каталог'
        catalogue_index, catalogue = config.cars_index, actions.get_cars_data()
        self.enable_toolbar()
        self.switch_mode(catalogue_index, catalogue, name_mode)

    def show_orders(self, e):
        """ displays data from orders table """
        name_mode = 'Заказы'
        orders_index, orders = config.orders_index, actions.get_orders_data()
        self.enable_toolbar()
        self.switch_mode(orders_index, orders, name_mode)

    def show_clients(self, e):
        """ displays data from clients table """
        name_mode = 'Клиенты'
        clients_index, clients = config.clients_index, actions.get_clients_data() 
        self.enable_toolbar()
        self.switch_mode(clients_index, clients, name_mode)

    def show_docs(self, e):
        pass

    def show_about(self, e):
        """ dispays 'about window' """
        dialogs.create_about_dialog()

    def show_start_page(self, e):
        """ returns us to the main page """
        name_mode = 'Главная'
        self.switch_mode(config.cars_index, config.cars, name_mode)
        self.disable_toolbar()
        
    def create_data(self, e):
        if self.name_mode == 'Каталог':
            with dialogs.MyAskDialog(None, title='Добавить машину') as dlg:
                dlg.create_car()
                if dlg.ShowModal() == wx.ID_OK:
                    print('hello')
                else:
                    print('bye')
                    # делает что-то после того, как была нажата кнопка ОК(сохранить)
    
        elif self.name_mode == 'Заказы':
            dialogs.create_order()
        elif self.name_mode == 'Клиенты':
            dialogs.create_client()
        elif self.name_mode == 'Главная':
            pass
        

    def print_data(self, e):
        pass

    def search(self, e):
        pass

    def switch_mode(self, data_index, data, name_mode):
        """ adds new data to listctrl and changes status mode,
            takes arguements data_index: list, data: dict, name_mode: str """
        self.data_list.clear()
        self.data_list.add_data_to_listCtrl(data_index, data)
        self.status_bar.SetStatusText(name_mode)
        self.name_mode = self.status_bar.GetStatusText()



def main():
    app = wx.App(False)
    win = Window(None)
    win.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

