from rows.utils import download_file
import pathlib
import zipfile
import os
from os import listdir
import csv

def main():
    data_path = pathlib.Path("Lista de Variaveis")
    if not data_path.exists():
        data_path.mkdir()
            
    download_file("https://dados.fee.tche.br/php/doc_down.php?csv/ListaVars", filename="Lista de Variaveis\\ListaVariaveis.zip", progress=True)
    fileZip = zipfile.ZipFile("Lista de Variaveis\\ListaVariaveis.zip", 'r')
    fileZip.extractall("Lista de Variaveis")
    fileZip.close()
    for fileCSV in os.listdir("Lista de Variaveis"):
            if ".csv" not in fileCSV:
                os.remove("Lista de Variaveis\\"+fileCSV)

if __name__ == "__main__":
    main()

class dowload():
    def CSV(fullPath,fileName, idFile):
        download_file("https://dados.fee.tche.br/php/download.php?csv/Municipio/"+idFile+"/1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016", filename=fullPath + fileName+".zip", progress=True)
        fileZip = zipfile.ZipFile(fullPath+fileName+".zip", 'r')
        fileZip.extractall(fullPath)
        fileZip.close()
        for fileCSV in os.listdir(fullPath):
            if ".csv" not in fileCSV:
                os.remove(fullPath + fileCSV)

class CrateTree():
    for fileCSV in os.listdir("Lista de Variaveis"):
        if ".csv" in fileCSV:
            with open("Lista de Variaveis\\"+fileCSV, newline='\r\n') as f:
                reader = csv.reader(f)
                for index,row in enumerate(reader):
                    if index > 0:
                        cell = str(row).replace("]","").replace("[","").replace("'","").replace("\"","").replace(" ", "").split(";")
                        fullpath = cell[3].split("\\")
                        fileName = cell[1]
                        idFile = cell[0]
                        createdFolder = ""
                        for idx,folder in enumerate(fullpath):
                            if idx > 1:
                                createdFolder += folder+ "\\"
                                if not pathlib.Path(createdFolder).exists():
                                    pathlib.Path(createdFolder).mkdir()
                        dowload.CSV(createdFolder, fileName, idFile)
        else:
            os.remove("Lista de Variaveis\\"+fileCSV)