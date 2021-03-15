#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
class Symptome:
    """
    CLASS SYMPTOME
    This class encapsulate the possible symptomes asscoiated to a patient
    It allows to process the information inside the patient
    """
    def __init__(self, _params):
        self.nom = []
        self.niveau = []
        for key, value in _params.items():
            self.nom.append(key)
            self.niveau.append(value)
    def etat(self):
        some = 0
        for value in self.niveau:
            some += value
        return some/len(self.niveau)
    