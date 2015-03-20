__author__ = 'wheezy'
import json
class JsonHandler:

    @staticmethod
    def construyObject(json_string):
        try:
            json_object = json.loads(json_string)
            print("JSON object carregado com sucesso")

        except Exception as error:
            print("Erro ao processar o arquivo JSON: ")
            json_object = None

        finally:
            return json_object

    @staticmethod
    def removeKey(json_file,key):
        try:
            json_deleted = json_file[str(key)]
            del json_file[str(key)]
            print("Chave removida com sucesso")
        except:
            json_deleted = ""
            print("Chave inexistente")
        finally:
            return json_deleted

    @staticmethod
    def getJson(json_object):
        return json.dumps(json_object)

    @staticmethod
    def addElement(json_object,key,value):
        for checked in json_object.keys():
            if checked == str(key):
                raise Exception("Chave já Existente")

        json_object[str(key)] = value

