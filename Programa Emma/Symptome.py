#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-

class Symptome:
  '''
     Class SYMPTOME:
         Manage the object sympton
         add and remove symptons
  '''
  def __init__(self, _symptomesList):
      self.symptomes = _symptomesList
      self.numSymptomes = (len(self.symptomes) / 2)
      gravity = 0;
      for x in self.symptomes:
          if type(x) == int:
              gravity += x
      self.gravity = gravity
      print(self.gravity)
      print(self.symptomes)
      print(self)
      
  def __str__(self):
      return 'The list of symptomes were added'
      
        