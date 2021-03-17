#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-

import json

class Registre:
  """
    CLASSE REGISTRE
    This class allows to manage the patient and personal register
    
  """

  # === CONSTRUCTOR ===
  # Initialize th register
  def __init__(self, _chemin):
    self.chemin = _chemin
    self.liste = []

  # --- ADD ---
  # An Occupant is added to the registry
  def add(self, _occupant):
    self.liste.append(_occupant)
    self.saveJson()

  # --- UPDATE ---
  # Allows the modification of the Occupant name or age
  def update(self, _param, _nom, _newValue):
    find = False
    tmpLst = []
    if len(self.liste) > 0:
      for x in self.liste:
        if x.nom.lower() == _nom.lower():
          print('>> Old information:')
          print(x)
          print()
          x.updateElement(_param, _newValue)
          print('>> New information :')
          print(x)
          print()
          find = True
        tmpLst.append(x)
      self.liste = tmpLst
      self.saveJson()
      print()
      return find

  # --- REMOVE ---
  # Removes an Occupant from the register
  def remove(self, _param):
    # Create a temporary list for storage a list without the removed object
    tmpLst = []
    find = False
    for x in self.liste:
      # if the name of the register match with the parameter
      if x.nom.lower() == _param.lower():
        print('>> {0} {1} {2} has been deleted from registry'.format(x.nom.upper(), x.prenom.capitalize(), x.age))
        find = True
      # else add to the temporary list
      else:
        tmpLst.append(x)
    # rewrite the JSON with the info in temporary list
    self.liste = tmpLst
    self.saveJson()
    return find
      
  # --- SORT ---
  # Returns for 'all'
  # 
    #      the list of patients classified by medical emergency. Second parameter must be 'patient'
    # or   the list of personal. Second parameter must be 'personal'
  # 
  # otherwise for '<name>'
    #      the < patient | personal > member corresponding to the last name

  def sort(self, _param):
    find = False
    if len(self.liste) > 0:
        # If the parameter of search is all
        if _param == 'all':
          print("\n>> Patients ordered by medical emergency:")
          newLst = {}
          for x in self.liste:
            newLst[str(x)] = x.gravity
          for key in sorted(newLst, key=newLst.get, reverse=True):
            print(key)  
          print('\n')
        # For a specific patient in the register
        else:
            for x in self.liste:
                if x.nom == _param:
                    print(x, "\n")
                    find = True
            if not find:    
                print(">> No {0} matching ... PLEASE REVIEW !!!\n".format(_param.upper()))
        return True
    else:
      return False    
      
  # --- DROP LST ---
  def dropLst(self):
    # Clear the registry list
    self.liste.clear()

  # --- SAVE JSON ---
  # Save the List in a JSON file
  def saveJson(self):
    with open(self.chemin, 'w') as outf:
      json.dump(self.liste, outf,default=self.convert_to_dict, ensure_ascii=False, indent=2)


  # --- LOAD JSON ---
  # Load data from a JSON file format. 
  # Verify the existence of file in chemin  
  def loadJson(self):
    try:
      with open(self.chemin, 'r') as inf:
        self.liste = json.load(inf,object_hook=self.dict_to_obj)
        print(">> Succes !!   The {} has been succesfully loaded".format(self.chemin))
    except IOError:
      print(">> File {} no exist.  Please try again!".format(self.chemin))

  
  
  # A function takes in a custom object and returns a dictionary representation of the object.
  # This dict representation includes meta data such as the object's module and class names.
  
  def convert_to_dict(self,obj):
    #  Populate the dictionary with object meta data 
    obj_dict = {
      "__class__": obj.__class__.__name__,
      "__module__": obj.__module__
    }
    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)
    return obj_dict
  
  
  # Function that takes in a dict and returns a custom object associated with the dict.
  # This function makes use of the "__module__" and "__class__" metadata in the dictionary
  # to know which object type to create.
  def dict_to_obj(self,our_dict):
    if "__class__" in our_dict:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = our_dict.pop("__class__")

        # Get the module name from the dict and import it
        module_name = our_dict.pop("__module__")
        
        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)
        
        # Get the class from the module
        class_ = getattr(module,class_name)
        # print("Im here")
        # print(module_name)
        # print(module)
        # print(class_)
        # Use dictionary unpacking to initialize the object
        obj = class_(**our_dict)
        # print(obj)
    else:
        obj = our_dict
    print("Im here now")
    return obj
