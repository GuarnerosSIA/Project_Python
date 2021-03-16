#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-

import json

class Registre:
  """
    CLASSE REGISTRE
    This class allows to manage the patient and personal register
    
  """

  # === CONSTRUCTOR ===
  def __init__(self, _chemin):
    self.chemin = _chemin
    self.liste = []

  # --- ADD ---
  def add(self, _occupant):
    # An Occupant is added to the registry
    self.liste.append(_occupant.__dict__)

  # --- UPDATE ---
  def update(self, _param, _nom, _value):
    # Allows the modification of the Occupant name or age
    find = False
    tmpLst = []
    if len(self.liste) > 0:
      for x in self.liste:
        if x['nom'] == _nom:
          print('>> Old information:')
          print(self.printOccup(x))
          x[_param] = _value
          print('>> Update :')
          print(self.printOccup(x))
          find = True
        tmpLst.append(x)
      self.liste = tmpLst
      self.saveJson()
      print()
      return find

  # --- REMOVE ---
  def remove(self, _param):
    # Removes an Occupant from the registry
    tmpLst = []
    find = False
    for x in self.liste:
      if x['nom'] == _param:
        print('>> {0} {1} {2} has been deleted from registry'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age']))
        find = True
      else:
        tmpLst.append(x)
    self.liste = tmpLst
    self.saveJson()
    return find
      

  # --- SORT ---
  def sort(self, _param):
    # Returns for 'all'
    #      either the list of patients classified by medical emergency
    #      either the staff list (depending on the type of dictionary)
    # otherwise for '<name>'
    #      the patient or staff member corresponding to the name
    
    
    find = False
    if len(self.liste) > 0:
        if _param == 'all':
            if self.liste[0]['type'] == 'patient':
                print(">> Patients ordered by medical emergency:")
                newLst = {}
                for x in self.liste:
                    newLst[self.printOccup(x)] = x['etat']
                for key in sorted(newLst, key=newLst.get, reverse=True):
                    print(key)
            else:
                print(">> List of medical personal:")
                for x in self.liste:
                    print(self.printOccup(x))
                    print()
        else:
            for x in self.liste:
                if x['nom'] == _param:
                    print(self.printOccup(x), "\n")
                    find = True
            if not find:    
                print(">> No {0} matching {1} ... PLEASE REVIEW !!!\n".format(self.liste[0]['type'], _param.upper()))
        return True
    else:
      return False    
      

  # --- PRINT OCCUPANT ---
  def printOccup(self, _occupant):
    # Returns the string display of an Occupant corresponding to its type
    x = _occupant
    if self.liste[0]['type'] == 'patient':
        if self.liste[0]['sick'] == True:
            txt = '   - {0} {1} {2} years old (severity: {3}), is sick'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age'], x['etat'])
        else:
            txt = '   - {0} {1} {2} years old (severity: {3})'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age'], x['etat'])
        return txt
    else:
        return '   - {0} {1} {2} years old, {3})'.format(x['nom'].upper(), x['prenom'].capitalize(), x['age'], x['role'])

  # --- DROP LST ---
  def dropLst(self):
    # Clear the registry list
    self.liste = []

  # --- SAVE JSON ---
  def saveJson(self):
    # Save the List in a JSON file
    with open(self.chemin, 'w') as outf:
      json.dump(self.liste, outf, ensure_ascii=False, indent=2)

  # --- LOAD JSON ---
  def loadJson(self):
    # Load data from a JSON file format
    with open(self.chemin, 'r') as inf:
      self.liste = json.load(inf)
