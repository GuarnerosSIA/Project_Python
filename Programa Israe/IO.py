#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Patient import *
from Personnel import *
from Registre import *


class IO:
  """
    CLASS IO
    Defines the 4 methods: create, read, update and delete
    @author: Alejandro H.
  """

  # === CONSTRUCTEUR ===
  def __init__(self):
    self.patients = Registre("patients.json")
    self.personnel = Registre("personnel.json")

  # --- CREATE ---
  def create(self, cmdLst):
    if cmdLst[1].lower() in ("patient", "personnel"):
      if type(cmdLst[2]) == str and type(cmdLst[3]) == str:
        if self.ifInt(cmdLst[4]):
          if cmdLst[1].lower() == "patient":
            try:
              sympLst = eval(cmdLst[5])
            except:
              print(">> La liste des symptomes doit être de type dictionnaire (The list of symptoms must be dictionary type without spaces) !")
              print(">> exemple (example): {'Mal de crâne':1,'toux':5}\n")
            else:
              if type(sympLst) == dict:
                ok = True
                for sever in sympLst.values():
                  if not self.ifInt(sever) or not 1 <= sever <= 5:
                    ok = False
                if ok:
                  if len(sympLst) > 0:
                    self.patients.add(Patient(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), cmdLst[5]))
                    self.patients.saveJson()
                  else:
                    print(">> Le patient doit au moins présenter un symptomes pour être admis (The patient must have at least one symptom to be admitted)!\n")
                else:
                  print(">> La structure de la liste des symptomes est incorrecte (la sévérité doit entre 1 et 5)")
                  print(">> The structure of the symptom list is incorrect (severity must be between 1 and 5)\n")
              else:
                print(">> La liste des symptomes doit être de type dictionnaire (The list of symptoms must be dictionary type without spaces) !")
                print(">> exemple (example): {'Mal de crâne':1,'toux':5}\n")
          elif cmdLst[1].lower() == "personnel" and type(cmdLst[5]) == str:
            self.personnel.add(Personnel(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), cmdLst[5].lower()))
            self.personnel.saveJson()
          else:
            print(">> Le role doit être de type text (The role must be of type text)!\n")
        else:
          print(">> L'age doit être une valeur numérique (Age must be a numeric value)!\n")
      else:
        print(">> Le nom et prénom doivent être de type text (The first and last name must be of type text)!\n")
    else:
      print(">>  !Le deuxième paramètre doit être : patient ou personnel (The second parameter must be: patient or personal)\n")

  # --- READ ---
  def read(self, _param):
    """Displays either: (the list of ordered patients and staff) or (the information of an occupant)"""
    if type(_param) == str:
      x = _param.lower()
      if not self.patients.sort(x):
        print(">> Le registre des patients est vide (Patient register is empty)!\n")
      if not self.personnel.sort(x):
        print(">> Le registre du personnel est vide (The personnel register is empty)!\n")
    else:
      print(">> Le deuxième paramètre est incorrect (The second parameter is incorrect)!\n")

  # --- UPDATE ---
  def update(self, cmdLst):
    """Allows you to update the information of an occupant."""
    if type(cmdLst[2]) == str:
      var = cmdLst[3]
      if cmdLst[1].lower() in ('nom', 'prenom', 'age'):
        if cmdLst[1].lower() == 'age':
          if self.ifInt(var):
            var = int(var)
          else:
            print(">> L'age doit être une valeur numérique (Age must be a numeric value)!\n")
            return False
        else:
          if type(var) == str:
            if not self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Aucun {0} dans le registre patient ({0} Is not in the patient registry)!\n".format(cmdLst[2].upper()))
            if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Aucun {0} dans le registre personnel ({0} Is not in the personnel registry)!\n".format(cmdLst[2].upper()))

          else:
            print(">> L'age doit être une valeur numérique (Age must be a numeric value)!\n")
      else:
        print(">> Le dexième paramètre doit être : nom, prenom ou age (The second parameter must be: name, first name or age)!\n")
    else:
      print(">> Le nom est incorrect (The name is incorrect)!\n")

  # --- DELETE ---
  def delete(self, _param):
    """Allows to delete an Occupant"""
    if type(_param) == str:
      if not self.patients.remove(_param.lower()) and not self.personnel.remove(_param.lower()):
        print(">> L'occupant {0} est introuvable (The Occupant {0} cannot be found)!\n".format(_param.upper()))
    else:
      print(">> Le nom est incorrect (The name is incorrect)!\n")

  # --- TEST 1 ---
  def test_1(self):
    """Test method test 1"""
    self.create(["create", "patient", "Aaron", "Burr", 60, "{'toux':1,'fievre':2, 'douleurs musculaires':5}"])
    self.create(["create", "personnel", "Alexander", "Hamilton", 45, "médecin"])
    self.patients.dropLst()
    self.personnel.dropLst()
    print(">> Le registre a été supprimé (The registry has been deleted)")
    self.patients.loadJson()
    self.personnel.loadJson()
    print(">> Le registre a été chargé à partir d'un fichier JSON (The registry has been loaded from a JSON file)")
    self.read("all")

  # --- TEST 2 ---
  def test_2(self):
    """Test methode 2"""
    self.patients.loadJson()
    self.personnel.loadJson()
    self.read("all")
    self.personnel.update("age", "Alexander", 47)
    self.delete("moser")
    self.read("all")
  
  # --- IF INT ---
  def ifInt(self, arg):
    """Returns True if convertible to Int, otherwise False."""
    try:
      var = int(arg)
    except:
      return False
    else:
      return True
