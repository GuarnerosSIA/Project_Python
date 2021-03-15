#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Occupant import *
from Symptome import *

class Patient(Occupant):
  """
    CLASE PACIENTE
    Inherits from Occupant for patients with symptoms
    @author: Alejandro H.
  """

  # CONSTRUCTOR
  def __init__(self, _nom, _prenom, _age, _symptomes):
    super().__init__(_nom, _prenom, _age)
    tmpDictionary = eval(_symptomes)
    self.symptomeLst = []
    some = 0
    for key, value in tmpDictionary.items():
        _var = Symptome(key, value)
        some += value
        self.symptomeLst.append(_var.__dict__)
    self.type = 'patient' 
    self.etat = Symptome.severity(some,len(tmpDictionary.items()))
    self.sick = self.is_sick()
    print(self)

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.etat})'.format(self=self)

  def __str__(self):
    myStr = '>> Le patient {0} {1} {2} (sévérité : {3}) à été ajouté ! (Patient {0} {1} {2} (severity: {3}) has been added!) '.format(self.nom.upper(), self.prenom.capitalize(), self.age, self.etat)
    if self.sick:
      myStr += "\n The patient is sick"
    return myStr

  # --- IS SICK ---
  def is_sick(self):
    """Return True if the mean average severity of the symptomes is greater or equal than 3"""
    return self.etat >= 3
  
