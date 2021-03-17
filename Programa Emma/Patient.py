#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Occupant import *
from Symptome import *


class Patient(Occupant):
  """
    CLASS PATIENT
    This class manage the patients in the hospital
    Inherits from Occupant 
    
  """

  # CONSTRUCTOR
  # param:  (name, last name, age, object symptom)
  def __init__(self, nom, prenom, age, symptomes,gravity=0):
    super().__init__(nom, prenom, age)
    self.symptomes = symptomes
    self.gravity = self.comp_gravity()
    print('\n>> Patient {} {} {} (severity: {}) has been added!'.format(self.nom.upper(), self.prenom.capitalize(), self.age, self.gravity))
    

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.gravity})'.format(self=self)

  def __str__(self):
      message = '>> Name: {} {}  Age:{}  Gravity:{} '.format(self.nom.upper(), self.prenom.capitalize(), self.age, self.gravity)
      if self.is_sick():
          message += ' Patient is sick !!'
      return message


  # Verify Equality
  def __eq__(self, other):
    return self.nom == other.nom 

  # Compute the level of gravity
  def comp_gravity(self):
    some = 0
    for item in self.symptomes:
      some += item.niveau
    return some/len(self.symptomes)  

  # --- IS SICK ---
  # Returns True if the patient has an average symptom score >= 3, otherwise False
  def is_sick(self):
    if self.gravity >= 3:
      return True
    else:
      return False
