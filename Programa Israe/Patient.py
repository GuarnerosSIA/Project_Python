#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Occupant import *
from Symptome import *

class Patient(Occupant):
  """
    CLASE PACIENTE
    Inherits from Occupant for patients with symptoms
    @author: José Alejandro Hernández Pérez
  """

  # CONSTRUCTOR
  def __init__(self, nom, prenom, age, symptomesLst, etat=0):
    super().__init__(nom, prenom, age)
    self.symptomesLst = symptomesLst
    self.etat = self.comp_etat()
    print('>> Patient {} {} {} (severity: {}) has been added!'.format(self.nom.upper(), self.prenom.capitalize(), self.age, self.etat))

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.etat})'.format(self=self)

  def __str__(self):
    myStr = '- {} {} {} (severity: {})'.format(self.nom.upper(), self.prenom.capitalize(), self.age, self.etat)
    if self.is_sick():
      myStr += "\n\t The patient is sick, be careful"
    return myStr
  # Verify Equality
  def __eq__(self, other):
    return self.nom == other.nom
  
  def comp_etat(self):
    some = 0
    for item in self.symptomesLst:
      some += item.niveau
    return some/len(self.symptomesLst)
  # --- IS SICK ---
  def is_sick(self):
    """Return True if the mean average severity of the symptomes is greater or equal than 3"""
    return self.etat >= 3
  
