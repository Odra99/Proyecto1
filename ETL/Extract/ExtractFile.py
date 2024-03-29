from sys import path
from os.path import dirname as dir
from tkinter import END
path.append(dir(path[0]))
import pandas as pd


class Extract:
    
    
    relabel = {
        'Primer Nombre': 'Primer_Nombre',
        'Segundo Nombre': 'Segundo_Nombre',
        'Primer Apellido': 'Primer_Apellido',
        'Segundo Apellido': 'Segundo_Apellido',
        'Apellido Casada' : 'Apellido_Casada',        
        'Fecha Nacimiento' : 'Fecha_Nacimiento',
        'Nacimiento':'Fecha_Nacimiento',
        'Puesto': 'Nombre_Puesto',
        'Nombre Puesto':'Nombre_Puesto',
        'Mes': 'Mes_Planilla',
        'Mes Planilla':'Mes_Planilla',
        'Email Trabajo':'Correo_Electronico_Trabajo',
        'Email' : 'Correo_Electronico_Trabajo',
        'Correo Electronico Trabajo': 'Correo_Electronico_Trabajo',
        'Correo Electronico': 'Correo_Electronico_Trabajo',
        'Correo_Electronico': 'Correo_Electronico_Trabajo',
        'Fecha Inicial': 'Fecha_Inicial',
        'Fecha Final': 'Fecha_Final',
        'Codigo Empresa': 'Codigo_Unico_Empresa',
        'Codigo Unico Empresa': 'Codigo_Unico_Empresa',
        'Nombre Empresa': 'Nombre_Empresa',
        'Direccion Empresa': 'Direccion_Empresa',
        'Telefono Empresa': 'Telefono_Empresa',
        'Nit Empresa': 'Nit_Empresa',
        'Condicion Laboral' : 'Condicion_Laboral',
        'Estado Laboral': 'Condicion_Laboral',
        'Departamento':'Departamento_Trabajo',
        'Departamento Trabajo':'Departamento_Trabajo',
        'Municipio':'Municipio_Trabajo',
        'Municipio Trabajo':'Municipio_Trabajo',
        'Cedula Orden':'Cedula_Orden',
        'Cedula Registro':'Cedula_Registro',
        'Sexo':'Genero'
    }
    
    requiredColumns = [
        'Dpi',
        'Nit',
        'Fecha_Inicial',
        'Fecha_Final',
        'Nombre_Empresa',
        'Nit_Empresa',
        'Codigo_Unico_Empresa'
        
    ]
    
    requiredColumnsName1 = [
        'Primer_Nombre',
        'Segundo_Nombre',
        'Primer_Apellido',
        'Segundo_Apellido',
        'Apellido_Casada',
    ]
    
    requiredColumnCedula = [
        'Cedula_Orden'
    ]
    requiredColumnCedula2 = [
        'Cedula_Registro'
    ]
     
    
    def __init__(self,consoleText):
        self.files = []
        self.filesNames = []
        self.consoleText = consoleText
        
    def readFile(self,pathFile):
        try:
            return pd.read_csv(pathFile)
        except:
            self.consoleText.insert(END,"Removiendo archivo: "+pathFile+'\n')
            self.consoleText.insert(END,"No cumple con los criterios establecidos"+'\n')
               
        
    def verifyFiles(self):
        i = 0
        for file in self.files:    
            file = self.renameColumns(file)
            if not self.verifyColumns(file):
                #time.sleep(5) 
                self.consoleText.insert(END,"Removiendo archivo: "+self.filesNames.pop(i)+'\n')
                self.consoleText.insert(END,"No cumple con los criterios establecidos"+'\n')
                self.files.pop(i)
                i=i-1
            i=i+1
            
        
    def storageFiles(self, pathFile):
        self.consoleText.insert(END,"Leyendo archivo: "+pathFile+'\n')
        self.filesNames.append(pathFile)
        self.files.append(self.readFile(pathFile))
        
    def renameColumns(self,file):
        #Uppercase and Strip
        file.columns = file.columns.str.title().str.strip()
        #Rename labels
        for label in file:
            if label in self.relabel:
                file = file.rename(columns = {label: self.relabel[label]})
        return file
        
    def verifyColumns(self,file):
        if set(self.requiredColumns).issubset(file.columns):
            return  set(self.requiredColumnsName1).issubset(file.columns):
        return False

    def verifyCedulaColumns(self, file):
        if not set(self.requiredColumnCedula).issubset(file.columns) and not set(self.requiredColumnCedula2).issubset(file.columns):
            if "Cedula_Orden" in file:
                del file['Cedula_Orden']
            if "Cedula_Registro" in file:
                del file['Cedula_Registro']
            
        
    
        

    
    
