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
    self.patients = Registre("patientsRegistry.json")
    self.personnel = Registre("personnelRegistry.json")

  # --- CREATE OCCUPANT---
  def create(self, cmdLst):
    """
    Allows the creation of new Occupants. Either Personal or Patient. 
    The reason for using different if else statements, is to provide a better explanation of the possible issues
    """
    # Create a list for 
    occupantType = cmdLst[1]
    nom = cmdLst[2]
    prenom = cmdLst[3]
    age = int(cmdLst[4])
    if(occupantType in ('personal','patient')):
      if (not self.hasNumbers(nom)) and (not self.hasNumbers(prenom)):
        try:
          age = int(cmdLst[4])
        except:
          print('The age has to be a numeric value')
        if (occupantType == 'personal'):
          
        else:
          fffff
      else:
        print('Name and surname have to be non numeric strings')
    else:
      print('Please insert personal or patient')

    """
    nSymptomes = int(cmdLst[5])
    for i in range(nSymptomes):
      symptomeNom = input(">>Symptom: ")
      symptomeSeverity = int(input(">>Severity: "))
      symptomeLst.append(Symptome(symptomeNom, symptomeSeverity))
    """
    
    newOccupant = [Personnel(nom,prenom,age,cmdLst[5]), Personnel(nom,prenom,age,cmdLst[5])]
    with open("personnelRegistry.json", 'w') as outf:
      json.dump(newOccupant, outf,default=self.convert_to_dict, ensure_ascii=False, indent=2)
    print(newOccupant)
    print(type(newOccupant[0]))
    with open("personnelRegistry.json", 'r') as inf:
      _var = json.load(inf,object_hook=self.dict_to_obj)
    print(_var)
    print(type(_var[0]))

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
  
  def convert_to_dict(self,obj):
    """
    A function takes in a custom object and returns a dictionary representation of the object.
    This dict representation includes meta data such as the object's module and class names.
    """
    #  Populate the dictionary with object meta data 
    obj_dict = {
      "__class__": obj.__class__.__name__,
      "__module__": obj.__module__
    }
    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)
    return obj_dict
  def dict_to_obj(self,our_dict):
    """
    Function that takes in a dict and returns a custom object associated with the dict.
    This function makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in our_dict:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = our_dict.pop("__class__")

        # Get the module name from the dict and import it
        module_name = our_dict.pop("__module__")
        
        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)
        
        # Get the class from the module
        class_ = getattr(module,class_name)
        
        # Use dictionary unpacking to initialize the object
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj