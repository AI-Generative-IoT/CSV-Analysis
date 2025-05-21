################################################################################################################################################
#                                                                                                                                              #
#    Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                              #
################################################################################################################################################

# PYTHON ROUTINE zur Implementierung der Python Library pandas #

import os
import sys

import pandas
import pandas as pd

from IPython.display import display

dt = {'Student':["Student 1", "Student 2", "Student 3"], 'Fachrichtung' : ["Fachrichtung Student 1", "Fachrichtung Student 2", "Fachrichtung Student 3"], 
'Geburtsdatum':["Geburtsdatum Student 1", "Geburtsdatum Student 2", "Geburtsdatum Student 3"]} # Definition einer Python Liste bze. eines Dictionaries

dt_pandas = pd.DataFrame(dt) # Erzeuge Pandas Data Framework (Pandas Tabelle)
display(dt_pandas) # Zeige Pandas Tabelle
