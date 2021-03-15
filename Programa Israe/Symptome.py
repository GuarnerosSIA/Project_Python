#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
class Symptome:
    """
    CLASS SYMPTOME
    This class encapsulate the possible symptomes asscoiated to a patient
    It allows to process the information inside the patient
    """
    def __init__(self, _nom, _niveau):
        self.nom = _nom
        self.niveau = _niveau

    