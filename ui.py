import wx
import os
import config

class MyPopupMenu(wx.Menu):
    """ create a context menu with items such as copy, paste and cut"""
    def __init__(self):
        super(MyPopupMenu, self).__init__()

        self.create_items()

    def create_items(self):
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

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap(config.icon_name, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        self.SetSize(config.size)
        self.Centre()
        self.SetTitle(config.title)
        self.InitUI()


    def InitUI(self):
        self.Bind(wx.EVT_RIGHT_DOWN, self.onright_down)

        self.SetMenuBar(self.create_menubar())
        


    def onright_down(self, e):
        ''' show contex menu when right mouse button is clicked '''
        self.PopupMenu(MyPopupMenu(), e.GetPosition())

    def create_menubar(self):
        '''create menu bar'''
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
        
    def upload_data(self, e):
        pass

    def save_data(self, e):
        pass

    def save_as(self, e):
        pass

    def on_close(self, e):
        self.Close()

    def show_catalogue(self):
        pass

    def show_orders(self):
        pass

    def show_clients(self):
        pass

    def show_docs(self):
        pass

    def show_about(self):
        pass


def main():
    app = wx.App()
    win = Window(None)
    win.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
