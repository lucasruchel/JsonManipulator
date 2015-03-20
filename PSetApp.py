__author__ = 'wheezy'

import FileHandler as f
from JsonHandler import JsonHandler as jsonMethods
from GUI import MyWindow

if __name__ == "__main__":
    fd = f.FileHandler("/data/00_UTFPR/00_disciplinas/04_BancoDeDados/pSet01/json_file")



    fd.loadFile()

    json_string = fd.data_string()

    json_object = jsonMethods.construyObject(json_string)

    print(json_object)

    """print(jsonMethods.removeKey(json_object['regions'], 1))

    print(json_object)

    jsonMethods.addElement(json_object['regions'],3,"Portugal")

    print(json_object)

    "Write changes in json_file"
    fd.write_string(jsonMethods.getJson(json_object))

    """

    windows = MyWindow(json_object["regions"])
    windows.insertData(json_object["regions"],1,"Venezuela")
    windows.start()









