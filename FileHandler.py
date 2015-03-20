__author__ = 'wheezy'
class FileHandler:
    def __init__(self,file_location):
        self.file_location = file_location

    def loadFile(self):
        try:
            self.file_descriptor = open(self.file_location,encoding='utf-8',mode='r+')
            print("Arquivo carregado com sucesso")
        except Exception as error:
            print("Erro ao abrir arquivo:",format(error))
            self.file_descriptor = None
        finally:
            return self.file_descriptor

    def data_string(self):
        if (self.file_descriptor != None):

            file_descriptor = self.file_descriptor

            file_dump = (line.rstrip() for line in file_descriptor.readlines())

            file_descriptor.close()

            file_data_string = ""

            for x in file_dump:
                file_data_string += str(x)

            return file_data_string

    def write_string(self,string):
        try:
            self.file_descriptor = open(self.file_location,mode="w",encoding="utf-8")
            self.file_descriptor.write(string)
        except Exception as error:
            print("Houve algum problema ao escrever no arquivo: {0}".format(error))







