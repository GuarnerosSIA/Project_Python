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
  def __init__(self, _nom, _prenom, _age, _symptomes):
    super().__init__(_nom, _prenom, _age)
    self.symptomes = _symptomes
    # self.symptomes = eval(_symptomes) # Dictionary creation
    
    self.type = 'patient' 
    # somme = 0
    # for var in self.symptomes.values():
    #   somme +=  
    self.gravedad = self.symptomes.gravity
    self.etat = self.symptomes.numSymptomes / self.symptomes.gravity
    self.sick = self.is_sick()
    print(self)
    
    
    
    
    

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.etat})'.format(self=self)

  def __str__(self):
      cadena = '>> The patient {} {} {} (severity: {}) has been added! '.format(self.nom.upper(), self.prenom.capitalize(), self.age, self.etat)
      if(self.sick):
          cadena += ' Patient is sick'
      return cadena 

  # --- IS SICK ---
  def is_sick(self):
    # Returns True if the patient has an average symptom score >= 3, otherwise False
    if self.etat >= 3:
      return True
    else:
      return False
