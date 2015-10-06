# -*- coding: cp1252 -*-
#-------------------------------------------------------------------------------
# Name:        AssemblePDF
# Purpose:     Permets d'assembler plusieurs fichiers PDF ensemble.
#
# Author:      Martin Couture *ubliccouture@icloud.com
#              Remplacer * du courriel par p
#
# Created:     24/04/2014
# Copyright:   (c) mcouture 2014
# Licence:     À utiliser à vos propres risques.
# Infos Suppl: Vous devez installer la librairie PyPDF2 pour pouvoir l'utiliser.
#              https://pypi.python.org/pypi/PyPDF2/1.15
#-------------------------------------------------------------------------------

#Import des modules
import os, string, sys
from PyPDF2 import PdfFileMerger, PdfFileReader

#Répertoire où se trouve les fichiers PDF.
repertoire = sys.argv[1]
listeFichiersPDF = os.listdir(repertoire) #Liste des fichiers


CountPage = 0 #Nombre de pages totales mis à 0

merger = PdfFileMerger()

for fichier in listeFichiersPDF:
    if fichier.count(".") >0: #S'il y a des fichiers PDF dans le répertoire.
        nbElementListe = fichier.split(".")

        if nbElementListe[len(nbElementListe)-1] =="pdf":
            print "Assemblage : " + fichier
            filename = repertoire+"\\"+fichier
            merger.append(PdfFileReader(file(filename, 'rb'))) #Assemblage du PDF
            CountPage = CountPage + PdfFileReader(file(filename, 'rb')).getNumPages() #Retourne le nombre de pages dans le fichier

merger.write(repertoire+"\\PDFAssemble.pdf") #Écriture du fichier PDF.
merger.close() #Fermeture du fichier
#Synthèse
print "Pages totaux assemblees = " + str(CountPage)
print "Pages totaux du document = " + str(PdfFileReader(file(repertoire+"\\PDFAssemble.pdf", 'rb')).getNumPages())
