#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Occupant import *


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
    self.type = 'patient' 
    somme = 0
    for var in self.symptomes.values():
      somme += var
    self.etat = somme / len(self.symptomes)
    print(self)

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.etat})'.format(self=self)

  def __str__(self):
    return '>> Le patient {} {} {} (sévérité : {}) à été ajouté !'.format(self.nom.upper(), self.prenom.capitalize(), self.age, self.etat)

  # --- IS SICK ---
  def is_sick(self):
    """Retourne True si le patient à une moyenne des symptomes >= 3, sinon False"""
    if self.etat >= 3:
      return True
    else:
      return False
