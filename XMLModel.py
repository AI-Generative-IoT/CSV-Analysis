################################################################################################################################################
#                                                                                                                                              #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                              #
################################################################################################################################################

#############################################################################
#                                                                           # 
#   PYTHON ROUTINE zum Auslesen von Variablen aus einem XML Metadatenfile   #
#                                                                           # 
############################################################################# 

import os
import sys
import math
import numpy
import numpy as np
import matplotlib.pyplot as plt

import csv
import random
import pandas

f = open("metadata.xml", "r") # Lese die Daten aus dem XML File zum Vergleich der Zeichenketten - setze den korrekten Pfad mit pwd

entity_id = 'entityID' # Definiere die Variablen entityID
key_size = 'KeySize' # Definiere die Variable KeyDescriptor     
key_info = 'KeyInfo' # Definere Variable KeyInfo      

with f : # Lese die Zeilen einzelnd in der Funktion f, wie oben definiert
    
    for line in f : # Iteriere über die Zeilen im XML File
        
        if entity_id in line : # Prüfe die Variable entityID
            
            entity_id = line

        if key_size in line : # Prüfe die Variable KeyDescriptor
        
            key_size = line

        if key_info in line : # Prüfe die Variable EncryptionMethod
        
            key_info = line

print('EntityID :', entity_id) # Schreibe die Information, welche die Variable entityID enthält
print('KeySize :', key_size) # Schreibe die Information, welche die Variable KeyDescriptor enthält
print('KeyInfo :', key_info) # Schreibe die Information, welche die Variable KeyInfo
