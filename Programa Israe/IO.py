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
    """
    Create 2 registers for saving patients and personal
    """
    self.patients = Registre("patients.json")
    self.personnel = Registre("personnel.json")

  # --- CREATE OCCUPANT---
  def create(self, cmdLst):
    """
    Allows the creation of new Occupants. Either Personal or Patient. 
    The reason for using different if else statements, is to provide a better explanation of the possible issues
    """
    # Verify if was use a patient or a personal in the input string
    if cmdLst[1].lower() in ("patient", "personnel"):
      if (not self.hasNumbers(cmdLst[2])) and (not self.hasNumbers(cmdLst[3])):#Check if name and surname are valid
        if self.ifInt(cmdLst[4]):#Verify if the age was provided
          if cmdLst[1].lower() == "patient":
            try:
              sympLst = eval(cmdLst[5])#Verify if the last input was a dictionary
            except:
              print(">> La liste des symptomes doit être de type dictionnaire (The list of symptoms must be dictionary type without spaces) !")
              print(">> exemple (example): {'Mal de crâne':1,'toux':5}\n")
            else:
              if type(sympLst) == dict:#Verify if a dictionary was created
                ok = True
                for sever in sympLst.values():#Check if all the values in the dictionary are numbers between 1-5
                  if not self.ifInt(sever) or not 1 <= sever <= 5:
                    ok = False
                if ok:
                  if len(sympLst) > 0:
                    self.patients.add(Patient(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), cmdLst[5]))
                    self.patients.saveJson() #save the created patient
                  else:#Verify if the dictionary is not an empty one
                    print(">> Le patient doit avoir au moins un symptôme pour être admis à l'hôpital (The patient must have at least one symptom to be admitted to the hospital)!\n")
                else:
                  print(">> La gravité est classée de 1 à 5 dans des intervalles entiers")
                  print(">> The severity is categorized from 1 up to 5 in integer intervals \n")
              else:
                print(">> La liste des symptomes doit être de type dictionnaire (The list of symptoms must be dictionary type) !")
                print(">> exemple (example): {'Mal de crâne':1,'toux':5}\n")
          elif cmdLst[1].lower() == "personnel" and (not self.hasNumbers(cmdLst[5])): #Verify if the role contains a number
            self.personnel.add(Personnel(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), cmdLst[5].lower()))
            self.personnel.saveJson() #Save the created personal
          else:
            print(">> Le rôle ne doit contenir aucun nombre (The role mustn't contain any number)!\n")
        else:
          print(">> L'age doit être une valeur numérique (Age must be a numeric value)!\n")
      else:
        print(">> Le nom et le prénom ne sont pas autorisés à avoir des numéros (Name and surname are not allowed to have numbers)!\n")
    else:
      print(">>  !Le deuxième paramètre doit être : patient ou personnel (The second parameter must be: patient or personal)\n")

  # --- READ ---
  def read(self, _param):
    """
    Displays either: (the list of ordered patients and staff) or (the information of an occupant)
    It also verifies that the surname hasn't any number 
    """
    if (not self.hasNumbers(_param)):#Verify if the surname to seek is valid
      x = _param.lower()
      if not self.patients.sort(x):
        print(">> Le registre des patients est vide (Patient register is empty)!\n")
    else:
      print(">> Le deuxième paramètre est incorrect (The second parameter is incorrect)!\n")

  # --- UPDATE ---
  def update(self, cmdLst):
    """Allows you to update the information of an occupant."""
    if (not self.hasNumbers(cmdLst[2])):
      var = cmdLst[3]
      if cmdLst[1].lower() in ('nom', 'prenom', 'age'):
        if cmdLst[1].lower() == 'age':
          if self.ifInt(var):
            var = int(var)
            if not self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Aucun {0} dans le registre patient ({0} Is not in the patient registry)!\n".format(cmdLst[2].upper()))
            if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Aucun {0} dans le registre personnel ({0} Is not in the personnel registry)!\n".format(cmdLst[2].upper()))
              self.personnel.sort('all') #For displaying the personal list (To show how the personal can be modifed)
          else:
            print(">> L'age doit être une valeur numérique (Age must be a numeric value)!\n")
            return False
        else:
          if (not self.hasNumbers(var)):
            if not self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Aucun {0} dans le registre patient ({0} Is not in the patient registry)!\n".format(cmdLst[2].upper()))
            if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Aucun {0} dans le registre personnel ({0} Is not in the personnel registry)!\n".format(cmdLst[2].upper()))
              self.personnel.sort('all') #For displaying the personal list (To show how the personal can be modifed)
          else:
            print(">> Le nom ne doit pas être une valeur numérique (Name mustn't be a numeric value)!\n")
            # New name can't contain numbers
      else:
        print(">> Insérer une mise à jour d'attribut valide : nom, prenom ou age (Insert a valid attribute update: name, first name or age)!\n")
    else:
      print(">> Le nom est incorrect (The name is incorrect)!\n")

  # --- DELETE ---
  def delete(self, _param):
    """Allows to delete an Occupant based on the name provided"""
    if (not self.hasNumbers(_param)):
      if not self.patients.remove(_param.lower()) and not self.personnel.remove(_param.lower()):
        print(">> L'occupant {0} est introuvable (The Occupant {0} cannot be found)!\n".format(_param.upper()))
    else:
      print(">> Le nom est incorrect (The name is incorrect)!\n")

  # --- TEST 1 ---
  def test_1(self):
    """
    Test method test 1
    This method creates a patient, and a personal.
    Writes both Occupants into the list and JSON registry
    Erase the list and then recover the data from the JSON file
    """
    self.create(["create", "patient", "Aaron", "Burr", 60, "{'toux':1,'fievre':2,'douleurs musculaires':5}"])
    self.create(["create", "personnel", "Alexander", "Hamilton", 45, "médecin"])
    self.personnel.dropLst()
    self.patients.dropLst()
    print(">> Le registre a été supprimé (The registry has been deleted)")
    self.personnel.loadJson()
    self.patients.loadJson()
    print(">> L'effacement et la mise à jour du registre ont réussi (Erased and update of the registry has been successful)")
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
    self.read("all")
    self.personnel.update("age", "Alexander", 47)
    self.delete("Alexander")
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
