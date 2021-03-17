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


  def updateElement(self, _param, _new_param):
    if(_param == 'name'):
      self.prenom = _new_param
    elif _param == 'lastname':
      self.nom = _new_param
    elif _param == 'age':
      self.age = _new_param
    else:
      print('{} not recognized as parameter for patient. Please repeat !!'.format(_param))