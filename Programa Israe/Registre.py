#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
import json


class Registre:
  """
    CLASSE REGISTRE
    This class allows to manage the patient and staff register
    @author: Alejandro H.
  """
  # === CONSTRUCTOR ===
  def __init__(self, _chemin):
    """The path is use to find the File"""
    self.chemin = _chemin
    self.liste = []

  # --- ADD ---
  def add(self, _occupant):
    """An Occupant is added to the registry"""
    self.liste.append(_occupant)
    self.saveJson()

  # --- UPDATE ---
  def update(self, _param, _nom, _value):
    """Allows the modification of the Occupant name, surname or age"""
    find = False
    tmpLst = []
    if len(self.liste) > 0:
      for x in self.liste:
        #In order to review the updated information. It is shown the previous and current Occupant
        if x.nom.lower() == _nom.lower():
          print('>> Previous information:')
          print(x)
          x.updateElement(_param, _value)
          print('>> Current information:')
          print(x)
          print()
          find = True
        tmpLst.append(x)
      self.liste = tmpLst
      self.saveJson()
      return find

  # --- REMOVE ---
  def remove(self, _param):
    """Removes an Occupant from the registry"""
    tmpLst = [] #Create a new list to removed the occupant
    find = False
    for x in self.liste:
      if x.nom.lower() == _param.lower():
        print('>> {} {} {} has been erased from the registry'.format(x.nom.upper(), x.prenom.capitalize(), x.age))
        find = True
      else:
        tmpLst.append(x)# Add one by the the new list
    self.liste = tmpLst # Update the list
    self.saveJson() # Actualized the registry
    return find

  # --- SORT ---
  def sort(self, _param):
    """
      Returns for 'all'
         either the list of patients classified by medical emergency
         either the staff list (depending on the type of dictionary). Just for demonstrative purposes
       otherwise for '<name>'
         the patient member corresponding to the name
    """
    find = False
    if len(self.liste) > 0:
      if _param == 'all':
        print(">> Current patients order by medical risk:")
        newLst = {}
        for x in self.liste:
          newLst[str(x)] = x.etat
        for key in sorted(newLst, key=newLst.get, reverse=True):#order all the patients by their severity
          print(key)
      elif _param.lower() == 'all-personal':
        for x in self.liste:
          print(x)
      else:#This part is use implemented in for seeking a specific patient
        for x in self.liste:
          if x.nom == _param:
            print(x, "\n")
            find = True
        if not find:
          print(">> No patient corresponds to {} !\n".format( _param.upper()))
      return True
    else:
      return False

  # --- EREASE LST ---
  def dropLst(self):
    """Clear the registry list"""
    self.liste.clear()

  # --- SAVE JSON ---
  def saveJson(self):
    """Save the List in a JSON file"""
    with open(self.chemin, 'w') as outf:
      json.dump(self.liste, outf,default=self.convert_to_dict, ensure_ascii=False, indent=2)
  # --- LOAD JSON ---
  def loadJson(self):
    """
    Load data from a JASON file format. Verify the existence of the file
    """
    try:
      with open(self.chemin, 'r') as inf:
        self.liste = json.load(inf,object_hook=self.dict_to_obj)
        print(">> The registry with name {} has been succesfully loaded".format(self.chemin))
    except IOError:
      print(">> There is no file with name {} please try again!".format(self.chemin))
  
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
