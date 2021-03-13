#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
class Occupant:
  """
    CLASS OCCUPANT
    Toute personne dans l'hopital.
    Classe mère de Patient et Personnel.
    @author: Scott RIDEL
  """
  def __init__(self, _nom, _prenom, _age):
    self.nom = _nom
    self.prenom = _prenom
    self.age = _age
