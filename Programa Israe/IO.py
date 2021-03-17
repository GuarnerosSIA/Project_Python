#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Patient import *
from Personnel import *
from Registre import *


class IO:
  """
    CLASS IO
    Defines the 4 methods: create, read, update and delete
    @author: José Alejandro Hernández Pérez
  """

  # === CONSTRUCTEUR ===
  def __init__(self):
    """
    Create 2 registers for saving patients and personal
    """
    self.patients = Registre("patientsRegistry.json")
    self.personnel = Registre("personnelRegistry.json")

  # --- CREATE ---
  def create(self, cmdLst):
      # Chek first argument in cmdLst
      if cmdLst[1].lower() in ("patient", "personal"):
          # Verify for string in argumens 2 y 3
          if (not self.hasNumbers(cmdLst[2])) and (not self.hasNumbers(cmdLst[3])):
              # Verify the age
              if self.ifInt(cmdLst[4]):
                  # if 'patient' 
                  if cmdLst[1].lower() == "patient":
                      # Needs to be an integer 
                      nom = cmdLst[2]
                      prenom = cmdLst[3]
                      age = cmdLst[4]
                      if self.ifInt(cmdLst[5]) and (int(cmdLst[5])>0):
                          symptomeLst = []
                          for s in range(int(cmdLst[5])):
                              Flag = True
                              while Flag:
                                  symptomeNom = input(">>Symptom: ")
                                  symptomeSeverity = input(">>Severity: ")
                                  if not self.hasNumbers(symptomeNom):
                                      if self.ifInt(symptomeSeverity):
                                          if 1 <= int(symptomeSeverity) <= 5:
                                              symptomeLst.append(Symptome(symptomeNom, int(symptomeSeverity)))
                                              Flag = False
                                          else:
                                              print('The severity integer must be between 1 and 5!!')
                                              print('Please try again')
                                      else:
                                          print('The severity of a symptom must be an integer!!')
                                          print('Please try again')
                                  else:
                                      print('The name of a symptom cannot contain numbers !! ')
                                      print('Please try again')
                          newOccupant = Patient(nom,prenom,age,symptomeLst)
                          self.patients.add(newOccupant)
                      else:
                          print('The last argument needs to be numerical!')
                  elif cmdLst[1].lower() == "personal" and (not self.hasNumbers(cmdLst[5])):
                      nom = cmdLst[2]
                      prenom = cmdLst[3]
                      age = cmdLst[4]
                      newOccupant = Personnel(nom,prenom,age,cmdLst[5])
                      self.personnel.add(newOccupant)
                  else:
                      print(">> The role must be of type text !\n")
              else:
                  print(">> The age must be a numerical value !\n")
          else:
              print(">> The first and last name must be of type text !\n")
      else:
          print(">>  The second parameter must be: patient or personal!\n")
  
  # --- READ ---
  def read(self, _param):
    """
    Displays either: (the list of ordered patients and staff) or (the information of an occupant)
    It also verifies that the surname hasn't any number 
    """
    if (not self.hasNumbers(_param)):#Verify if the surname to seek is valid
      x = _param.lower()
      if(x =='all-personal'):
        if not self.personnel.sort(x):
          print(">> Personal register is empty!\n")
      elif not self.patients.sort(x):
        print(">> Patient register is empty!\n")
    else:
      print(">> The second parameter is incorrect!\n")

  # --- UPDATE ---
  def update(self, cmdLst):
    """Allows you to update the information of an occupant."""
    if (not self.hasNumbers(cmdLst[2])):
      var = cmdLst[3]
      if cmdLst[1].lower() in ('name', 'surname', 'age'):
        if cmdLst[1].lower() == 'age':
          if self.ifInt(var):
            var = int(var)
            if not self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> {} Is not in the patient registry!\n".format(cmdLst[2].upper()))
            if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> {} Is not in the personnel registry!\n".format(cmdLst[2].upper()))
              print(">> The Following is the complete list of personal")
              self.personnel.sort('all-personal') #For displaying the personal list (To show how the personal can be modifed)
          else:
            print(">> Age must be a numeric value!\n")
            return False
        else:
          if (not self.hasNumbers(var)):
            if not self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> {} Is not in the patient registry!\n".format(cmdLst[2].upper()))
            if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> {} Is not in the personnel registry!\n".format(cmdLst[2].upper()))
              print(">> The Following is the complete list of personal")
              self.personnel.sort('all-personal') #For displaying the personal list (To show how the personal can be modifed)
          else:
            print(">> Name mustn't be a numeric value!\n")
            # New name can't contain numbers
      else:
        print(">> Insert a valid attribute update: name, first name or age!\n")
    else:
      print(">> The name is incorrect!\n")

  # --- DELETE ---
  def delete(self, _param):
    """Allows to delete an Occupant based on the name provided"""
    if (not self.hasNumbers(_param)):
      if not self.patients.remove(_param.lower()) and not self.personnel.remove(_param.lower()):
        print(">> The Occupant {} cannot be found!\n".format(_param.upper()))
    else:
      print(">> The name is incorrect!\n")

  # --- TEST 1 ---
  def test_1(self):
    """
    Test method test 1
    This method creates a patient, and a personal.
    Writes both Occupants into the list and JSON registry
    Erase the list and then recover the data from the JSON file
    """
    self.create(["create", "patient", "Aaron", "Burr", 60, '2'])
    self.create(["create", "personal", "Alexander", "Hamilton", 45, "médecin"])
    self.personnel.dropLst()
    self.patients.dropLst()
    print(">> The registry has been deleted")
    self.personnel.loadJson()
    self.patients.loadJson()
    print(">> Erased and update of the registry has been successful")
    self.read("all")

  # --- TEST 2 ---
  def test_2(self):
    """
    Test methode 2
    This method loads a JSON file
    Modifies some values of an Occupant
    Deletes another occupant 
    and finally saves the values inside a JSON file
    """
    self.personnel.loadJson()
    self.patients.loadJson()
    self.read("all-personal")
    self.personnel.update("age", "Hamilton", 47)
    self.delete("Hamilton")
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
  
  def hasNumbers(self, myString):
    """
    This method verifies if a string contains a number. Thus it can be used for verifying the suitability of a name or surname
    """
    return any(char.isdigit() for char in myString)

  def loadRegistry(self):
    self.personnel.loadJson()
    self.patients.loadJson()