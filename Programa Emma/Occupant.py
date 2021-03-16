#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
class Occupant:
  '''  
    CLASS OCCUPANT
    Anyone in the hospital
    Parent class of Patient and Personnel.
  '''
  
  def __init__(self, _nom, _prenom, _age):
    self.nom = _nom
    self.prenom = _prenom
    self.age = _age
