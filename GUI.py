__author__ = 'wheezy'

from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self,json_object):
        Gtk.Window.__init__(self,title="Json Manipulator")

        header = Gtk.HeaderBar(title="Json Manipulator")
        header.set_subtitle("Programa para manipular Arquivos Json")
        header.props.show_close_button = True

        self.set_titlebar(header)

        self.jsonObject = json_object
        self.tableData(json_object)

        """ Default Window size """
        self.set_default_size(600,400)

        """ Creating GTK3 element and setting the spacing of height columns"""
        hbox = Gtk.HBox(spacing=5)

        """ Adding the container box to super class Gtk.Windows """
        self.add(hbox)

        """ Add button elements """


        self.addButton = Gtk.Button("Adicionar")
        self.addButton.connect("clicked",self.addButtonListener)

        self.txtID = Gtk.Entry()
        self.txtRegion = Gtk.Entry()

        vbox = Gtk.VBox(spacing=5)
        vbox.pack_start(self.txtID,True,True,3)
        vbox.pack_start(self.txtRegion,True,True,3)
        vbox.pack_start(self.addButton,True,True,3)

        hbox.pack_start(vbox,False,False,3)

        """ Adding elements to container box """
        hbox.pack_start(self.treeView,True,True,3)


    def addButtonListener(self,button):
        id = self.txtID.get_text()
        value = self.txtRegion.get_text()

        self.insertData(self.jsonObject,id,value)




    def insertData(self,json_object,id,value):
        try:
            json_object[str(id)]=value

            self.listStore.clear()

            for e in json_object.keys():
                self.listStore.append([e,json_object[e]])
        except:
            print("Erro")

    def tableData(self,json_object):
        self.listStore = Gtk.ListStore(str,str)
        for e in json_object.keys():
            self.listStore.append([e,json_object[e]])

        self.treeView = Gtk.TreeView(model=self.listStore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("ID", renderer_text, text=0)
        self.treeView.append_column(column_text)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Região", renderer_text, text=1)
        self.treeView.append_column(column_text)

    def start(self):
        self.show_all()
        self.connect("delete-event",Gtk.main_quit)
        Gtk.main()