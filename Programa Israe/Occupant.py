#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
class Occupant:
  """
    CLASS OCCUPANT
    Anyone in the hospital.
    Parent class of Patient and Staff.
    @author: José Alejandro Hernández Pérez
  """
  def __init__(self, _nom, _prenom, _age):
    self.nom = _nom
    self.prenom = _prenom
    self.age = _age
  
  def updateElement(self, _param, _new_param):
    if(_param == 'name'):
      self.prenom = _new_param
    elif _param == 'surname':
      self.nom = _new_param
    else:
      self.age = _new_param