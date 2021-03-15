#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
import json


class Registre:
  """
    CLASSE REGISTRE
    This class allows to manage the patient and staff register
    @author: Alejandro H.
  """
  # === CONSTRUCTOR ===
  def __init__(self, _chemin):
    """The path is use to find the File"""
    self.chemin = _chemin
    self.liste = []

  # --- ADD ---
  def add(self, _occupant):
    """An Occupant is added to the registry"""
    self.liste.append(_occupant.__dict__)

  # --- UPDATE ---
  def update(self, _param, _nom, _value):
    """Allows the modification of the Occupant name, surname or age"""
    find = False
    tmpLst = []
    if len(self.liste) > 0:
      for x in self.liste:
        #In order to review the updated information. It is shown the previous and current Occupant
        if x['nom'] == _nom:
          print('>> Information précédente (Previous information):')
          print(self.printOccup(x))
          x[_param] = _value
          print('>> Informations actuelles (Current information) :')
          print(self.printOccup(x))
          find = True
        tmpLst.append(x)
      self.liste = tmpLst
      self.saveJson()
      return find

  # --- REMOVE ---
  def remove(self, _param):
    """Removes an Occupant from the registry"""
    tmpLst = [] #Create a new list to removed the occupant
    find = False
    for x in self.liste:
      if x['nom'] == _param:
        print('>> {0} {1} {2} a été effacé du registre ! ({0} {1} {2} has been erased from the registry)'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age']))
        find = True
      else:
        tmpLst.append(x)# Add one by the the new list
    self.liste = tmpLst # Update the list
    self.saveJson() # Actualized the registry
    return find

  # --- SORT ---
  def sort(self, _param):
    """
      Returns for 'all'
         either the list of patients classified by medical emergency
         either the staff list (depending on the type of dictionary). Just for demonstrative purposes
       otherwise for '<name>'
         the patient member corresponding to the name
    """
    find = False
    if len(self.liste) > 0:
      if _param == 'all':
        if self.liste[0]['type'] == 'patient':#Review all the patients
          print(">> Ordre actuel des patients par risque médical (Current patients order by medical risk):")
          newLst = {}
          for x in self.liste:
            newLst[self.printOccup(x)] = x['etat']
          for key in sorted(newLst, key=newLst.get, reverse=True):#order all the patients by their severity
            print(key)
        else:#This action is just in case the update proces failed, then the list of personal is shown
          print(">> La liste des personnels est la suivante (The list of personal is the following):")
          for x in self.liste:
            print(self.printOccup(x))
        print()
      else:#This part is use implemented in for seeking a specific patient
        for x in self.liste:
          if x['nom'] == _param:
            print(self.printOccup(x), "\n")
            find = True
        if not find:
          print(">> Aucun {0} correspondant à {1} (No {0} corresponds to {1})!\n".format(self.liste[0]['type'], _param.upper()))
      return True
    else:
      return False

  # --- PRINT OCCUPANT ---
  def printOccup(self, _occupant):
    """Returns the string display of an Occupant corresponding to its type"""
    x = _occupant
    if self.liste[0]['type'] == 'patient':
      return '   - {0} {1} {2} ans (sévérité: {3}) ({0} {1} {2} years old (severity: {3}))'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age'], x['etat'])
    else:
      return '   - {0} {1} {2} ans, {3} ({0} {1} {2} years old, {3})'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age'], x['role'])

  # --- EREASE LST ---
  def dropLst(self):
    """Clear the registry list"""
    self.liste.clear()

  # --- SAVE JSON ---
  def saveJson(self):
    """Save the List in a JSON file"""
    with open(self.chemin, 'w') as outf:
      json.dump(self.liste, outf, ensure_ascii=False, indent=2)
      

  # --- LOAD JSON ---
  def loadJson(self):
    """
    Load data from a JASON file format. Verify the existence of the file
    """
    try:
      with open(self.chemin, 'r') as inf:
        self.liste = json.load(inf)
        print("{} Registre précédent chargé (Previous registry loaded)".format(self.chemin))
    except IOError:
      print(">> Il n'y a pas de fichier précédent à charger (Ther is no previous file to load) !")
