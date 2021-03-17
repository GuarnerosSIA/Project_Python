#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Occupant import *


class Personnel(Occupant):
  """
    CLASS PERSONNEL
    This class allows the functions to the Personnel
    Inherits from Occupant class
    
  """

  # === CONSTRUCTOR ===
  def __init__(self, _nom, _prenom, _age, _role):
    super().__init__(_nom, _prenom, _age)
    self.role = _role
    print('>> The {0} {1} {2} is {3} years old and was added to the personal register'.format(self.role, self.nom.upper(), self.prenom.capitalize(), self.age))

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.role})'.format(self=self)

  def __str__(self):
    return '>> {1} {2} is a {3} years old {0}'.format(self.role, self.nom.upper(), self.prenom.capitalize(), self.age)

  def __eq__(self,other):
    return self.nom == other.nom