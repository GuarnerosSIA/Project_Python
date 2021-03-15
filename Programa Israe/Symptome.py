#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-

#This part will be a test for reviewing the posibility of inherity from a dictionary

import json


class Symptome(dict):
    """
    CLASS SYMPTOME
    This class encapsulate the possible symptomes asscoiated to a patient
    It allows to process the information inside the patient
    """
    def __init__(self, _nom, _niveau):
        self.nom = _nom
        self.niveau = _niveau
    @staticmethod
    def severity(some,length):
        return some/length
