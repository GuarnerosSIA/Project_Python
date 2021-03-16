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
    self.symptomes = eval(_symptomes) # Dictionary creation
    symptomeLst = Symptome(self.symptomes)
    self.type = 'patient' 
    self.etat = symptomeLst.etat()
    print(self)

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.etat})'.format(self=self)

  def __str__(self):
    return '>> Le patient {0} {1} {2} (sévérité : {3}) à été ajouté ! (Patient {0} {1} {2} (severity: {3}) has been added!)'.format(self.nom.upper(), self.prenom.capitalize(), self.age, self.etat)

  # --- IS SICK ---
  def is_sick(self):
    """Return True if the mean average severity of the symptomes is greater or equal than 3"""
    return self.etat >= 3
  
