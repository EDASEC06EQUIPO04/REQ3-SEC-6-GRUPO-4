"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
import datetime
import csv
import copy
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer=model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    #accidentes=[]
    accidentsfile = cf.data_dir + accidentsfile
    """
    archivo = open(accidentsfile,'r')
    archivo.readline()
    linea = archivo.readline()
    while len(linea)>0:
        datos=linea.split(",")
        accidente=crear_accidente(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5].rstrip("\n"))
        accidentes.append(accidente)
        #model.addAccident(analyzer, accidente)
    """
    #accidentsfile = cf.data_dir + accidentsfile
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),delimiter=",")
    for accidente in input_file:

        """
        accidente ={

        "ID":accidente['ID'],
        "Severity":accidente['Severity'],
        "Start_Time":accidente['Start_Time'],
        "Start_Lat":accidente['Start_Lat'],
        "Start_Lng":accidente['Start_Lng'],
        "State":accidente['State']}
        """

        #accidente1=copy.deepcopy(accidente)

        #accidente1.values= {accident['ID'],accident['Severity'],accident['Severity'],accident['Start_Lat'],accident['Start_Lat'],accident['State']}
        model.addAccident(analyzer, accidente)
    
    #input ("Clic para continuar")
    return analyzer 

def compareIds (id1,id2):
    
    # compara los crimenes
    if (id1==id2):
        return 0
    elif (id1>id2):
        return 1
    else:
        return -1

def crear_accidente(ID:str,Severity:int,Start_Time:datetime,Start_Lat:None,Start_Lng:None,State:str)-> dict:
    
    Start_Time=datetime.datetime.now()
    Start_Time = datetime.datetime.strftime(Start_Time, '%Y-%m-%d %H:%M:%S')

    #Start_Time = datetime.datetime.strptime(Start_Time, "%a %b %d %H:%M:%S %Y")
    


    return {
    "ID":ID,
    "Severity":Severity,
    "Start_Time":Start_Time,
    "Start_Lat":Start_Lat,
    "Start_Lng":Start_Lng,
    "State":State}



# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def getAccidentsByRange(analyzer, initialDate,finalDate):    
    return model.getAccidentsByRange(analyzer, initialDate.date(),finalDate.date())

def getAccidentsByDate(analyzer, Date):    
    return model.getAccidentsByDate(analyzer, Date.date())


def getAccidentsByState (analyzer, stateInput):

    return model.getAccidentsByState(analyzer, stateInput)


def accidentSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.accidentSize(analyzer)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)

 
def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)                

def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)