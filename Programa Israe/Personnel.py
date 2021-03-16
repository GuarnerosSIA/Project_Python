#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Occupant import *


class Personnel(Occupant):
  """
    CLASS PERSONNEL
    These class inherits from Occupant class
    @author: Alejandro H.    
  """

  # === CONSTRUCTOR ===
  def __init__(self, nom, prenom, age, role):
    super().__init__(nom, prenom, age)
    self.role = role
    print('>> The {} {} {} {} years old, was added'.format(self.role.capitalize(), self.nom.upper(), self.prenom.capitalize(), self.age))

  def __repr__(self):
    return '{self.__class__.__name__}({self.nom}, {self.prenom}, {self.age}, {self.role})'.format(self=self)

  def __str__(self):
    myStr = '- {} {} {} {} years old'.format(self.role.capitalize(), self.nom.upper(), self.prenom.capitalize(), self.age)
    return myStr
  
  def __eq__(self,other):
    return self.nom == other.nom
