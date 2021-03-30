# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:32:24 2020

@author: quent
"""

import time as tm
import numpy as np

valeurs_x = np.arange(0, 6)
valeurs_y = np.arange(0, 12)

def Plateau_Initial():
    plateau = list(range(6))
    ligne = list(range(12))
    for i in range(12):
        ligne[i] = '-'
    for j in range(6):            
        plateau[j] = ligne
    retour = np.array(plateau)
    return retour

def Affichage_Plateau(plateau):
    for i in range(6):
        for j in range(12):
            print(plateau[i][j], end = ' ')
        print('')

def Actions(plateau):
    liste = []
    for i in range(6):
        for j in range(12):
            if (plateau[i][j] == '-'):
                liste.append((i, j))
    return liste

def Result(plateau, action, estMax):
    if (Faisabilite(plateau, action) == True):
        if (estMax == True):
            plateau[action[0]][action[1]] = 'X'
        else:
            plateau[action[0]][action[1]] = 'O'
    return plateau
        
def Gravite(plateau, action):
    if (action[0] == 5):
        return True
    action1 = (action[0] + 1, action[1])
    if ((action1 in Actions(plateau)) == False):
        return True
    else:
        return False
    
def Faisabilite(plateau, action):
    retour = False
    if (((action in Actions(plateau)) == True) and ((Gravite(plateau, action)) == True)):
        retour = True
    return retour

# def Terminal_Test(plateau):
#     test = '_'
#     if (Test_Ligne(plateau) == 'X' or Test_Colonne(plateau) == 'X' or Test_Diagonale(plateau) == 'X'):
#         test = 'X'
#     else:
#         if (Test_Ligne(plateau) == 'O' or Test_Colonne(plateau) == 'O' or Test_Diagonale(plateau) == 'O'):
#             test = 'O'
#         else:
#             compteur = 0
#             for i in range(3): 
#                 for j in range(3): 
#                     if (plateau[i][j] == '-'):
#                         compteur += 1
#             if (compteur == 0):
#                 test = 'Nul'   
#     return test    
    
def Test_Ligne(plateau):
    test = '_'
    for i in range(0, 6):
        for j in range(0, 9):
            if ((plateau[0][i] == plateau[1][i] == plateau[2][i] == plateau[3][i]) 
                and (plateau[0][i] != '-')):
                test = plateau[0][i]
    return test        

def Test_Colonne(plateau):
    test = '_'
    for i in range(0, 3):
        for j in range(0, 12):
            if ((plateau[i][0] == plateau[i][1] == plateau[i][2] == plateau[i][3]) 
                and (plateau[i][0] != '-')):
                test = plateau[i][0]    
    return test

# REPRISE ICI
#    
def Test_Diagonale(plateau):
    test = '_'
    if ((plateau[0][0] == plateau[1][1] == plateau[2][2]) and (plateau[0][0] != '-')):
        test = plateau[0][0]

    if ((plateau[2][0] == plateau[1][1] == plateau[0][2]) and (plateau[2][0] != '-')):
        test = plateau[2][0]

    return test
#
# REPRISE ICI

plateau = Plateau_Initial()
Affichage_Plateau(plateau)
# Result(plateau, (5,0), False)
# Affichage_Plateau(plateau)
Result(plateau, (4,0), False)
Affichage_Plateau(plateau)
