#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-

class Symptome:
  '''
     Class SYMPTOME:
         Manage the object sympton
         add and remove symptons
  '''
  def __init__(self, nom, niveau):
        self.nom = nom
        self.niveau = niveau
        
      
  def __str__(self):
      return 'The list of symptomes were added'
      
        