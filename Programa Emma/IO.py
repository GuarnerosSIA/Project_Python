#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from Patient import *
from Personnel import *
from Registre import *


class IO:
  """
    CLASS IO
    Defines the 4 methods: create, read, update and delete
  """
  # === CONSTRUCTOR ===
  def __init__(self):
    self.patients = Registre("patients.json")
    self.personnel = Registre("personnel.json")
    self.patients.loadJson()
    self.personnel.loadJson()

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
                      if self.ifInt(cmdLst[5]):
                          listSymptome = []
                          for s in range(int(cmdLst[5])):
                              print ('Enter the < name > < pain_level > of symptome', s + 1)
                              name, pain = input('>> ').split()
                              if type(name) == str: 
                                  listSymptome.append(name)
                                  if self.ifInt(pain):
                                      listSymptome.append(int(pain))
                                  else:
                                      print('The pain of a symptom must be an integer!! ')
                              else:
                                  print('The name of a symptom must be a string!! ')
                          objectSymptom =  Symptome(listSymptome)
                          self.patients.add(Patient(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), objectSymptom))
                          self.patients.saveJson()
            
                      else:
                          print('The last argument needs to be numerical!')
                    
                    
                      # #  Verify the dictionary
                      # try:
                      #     sympLst = eval(cmdLst[5])
                      # except:
                      #     print(">> The list of symptoms must be dictionary type without spaces !!")
                      #     print(">> example: {'toux':1,'fievre':5}\n")
                          
                      # else:
                      #     if type(sympLst) == dict:
                      #         severity = True
                      #         for sever in sympLst.values():
                      #             if not self.ifInt(sever) or not 1 <= sever <= 5:
                      #                 severity = False
                      #         if severity:
                      #             if len(sympLst) > 0:
                      #                 self.patients.add(Patient(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), cmdLst[5]))
                      #                 self.patients.saveJson()
                      #         else:
                      #             print(">> The patient must have at least one symptom to be admitted!\n")
                      #     else:
                      #         print(">> The structure of the symptom list is incorrect (severity must be between 1 and 5)\n")
                  
                    
                  # If 'personal'
                  elif cmdLst[1].lower() == "personal" and type(cmdLst[5]) == str:
                      self.personnel.add(Personnel(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]),  cmdLst[5]))
                      self.personnel.saveJson()
                  else:
                      print(">> The role must be of type text !\n")
              else:
                  print(">> The age must be a numerical value !\n")
          else:
              print(">> The first and last name must be of type text !\n")
      else:
          print(">>  The second parameter for <<create>> must be: patient or personal!\n")


  # --- READ ---
  # Displays the list of ordered patients | personal
  
  def read(self, _param, _type):
      # Check for a string
      if type(_param) == str:
          if (_type == 'patient'):
               x = _param.lower()
               if not self.patients.sort(x):
                   print(">> Patient register is empty!\n")
          else:
              x = _param.lower()
              if not self.personnel.sort(x):
                  print(">> Personal register is empty!\n")
      else:
          print(">> The second parameter is incorrect!\n")

  # --- UPDATE ---
  def update(self, cmdLst):
    # Allows you to update the information of an occupant.
    if type(cmdLst[2]) == str:
      var = cmdLst[3]
      if cmdLst[1].lower() in ('nom', 'prenom', 'age'):
        if cmdLst[1].lower() == 'age':
          if self.ifInt(var):
            var = int(var)
          else:
            print(">> The age must be a numerical value !\n")
            return False
        else:
          if type(var) == str:
            if not self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> No {} in the patient register !\n".format(cmdLst[2].upper()))
            if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> No {} in the personal register !\n".format(cmdLst[2].upper()))

          else:
            print(">> The age must be a numerical value !\n")
      else:
        print(">> The second parameter must be : name, last name or age !\n")
    else:
      print(">> The name is incorrect !\n")
      
  # --- DELETE ---
  def delete(self, _param):
    # Allows you to delete an occupant.
    if type(_param) == str:
      if not self.patients.remove(_param.lower()) and not self.personnel.remove(_param.lower()):
        print(">> The occupant {} cannot be found !\n".format(_param.upper()))
    else:
      print(">> The name is incorrect !\n")

  # --- TEST 1 ---
  def test_1(self):
    # Test method 1
    self.create(["create", "patient", "smith", "john", 25, "{'toux':2,'fievre':4}"])
    self.create(["create", "personnel", "moser", "mau-britt", 54, "neuroscientist"])
    self.patients.dropLst()
    self.personnel.dropLst()
    print(">> Patient and personal lists deleted.")
    self.patients.loadJson()
    self.personnel.loadJson()
    print(">> Patient and persoael lists loaded from json files.")
    self.read("all")

  # --- TEST 2 ---
  def test_2(self):
    # Test method 2
    self.patients.loadJson()
    self.personnel.loadJson()
    print(">> Patient and personal lists loaded from json files.")
    self.read("all")
    self.patients.update("nom", "smith", "travis")
    self.delete("moser")
    self.read("all")

  # --- IF INT ---
  # Returns True if convertible to Int, otherwise False.
  def ifInt(self, arg):
    
    try:
      var = int(arg)
    except:
      return False
    else:
      return True
   
  # --- HAS NUMBERS ---
  # This method verifies if a string contains a number. 
  def hasNumbers(self, myString):
    return any(char.isdigit() for char in myString)
  

