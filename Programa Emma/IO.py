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
    # self.patients.loadJson()
    # self.personnel.loadJson()

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
                      if self.ifInt(cmdLst[5]) and (int(cmdLst[5]) > 0):
                          listSymptomes = []
                          for s in range(int(cmdLst[5]) ):
                              # Check for the symptomes
                              hasSymptome = True
                              while hasSymptome:
                                print ('Enter the < name > < pain_level > of symptome', s + 1)
                                name, pain = input('>> ').split()
                                if not self.hasNumbers(name): 
                                  if self.ifInt(pain):
                                          if 1 <= int(pain) <= 5:
                                              listSymptomes.append(Symptome(name, int(pain)))
                                              hasSymptome = False
                                          else:
                                              print('The pain must be an integer between 1 - 5 !!')
                                              print('Please try again !!')
                                  else:
                                    print('The pain of a symptom must be an integer !! \n Please repeat')
                                else:
                                  print('The name of a symptom must be a string !! \n Please repeat')
                          newPatient = Patient(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), listSymptomes)
                          self.patients.add(newPatient)
                          print()
                      else:
                          print('The last argument needs to be numerical!')
                  # If 'personal'
                  elif cmdLst[1].lower() == "personal" and (not self.hasNumbers(cmdLst[5])):
                      newPersonal = Personnel(cmdLst[2].lower(), cmdLst[3].lower(), int(cmdLst[4]), cmdLst[5]) 
                      self.personnel.add(newPersonal)
                  else:
                      print(">> The role must be of type text !\n")
              else:
                  print(">> The age must be a numerical value !\n")
          else:
              print(">> The name and last name must be of type text !\n")
      else:
          print(">>  The first parameter for <<create>> must be: patient or personal!\n")


  # --- READ ---
  # Displays the list of ordered patients | personal
  def read(self, _param, _type):
      # Check for a string in first argument
      if (not self.hasNumbers(_param)):
          if (_type == 'patient'):
               x = _param.lower()
               if not self.patients.sort(x):
                   print(">> Patient register is empty!\n")
          elif(_type == 'personal'):
              x = _param.lower()
              if not self.personnel.sort(x):
                  print(">> Personal register is empty!\n")
          else:
            print('The last argument is < patient | personal >. \n Please repeat')
      else:
          print(">> The main parameter must be 'all' or <last name>. Please repeat!\n")

  # --- UPDATE ---
  # Allows you to update the information of an occupant.
  def update(self, cmdLst):
    # Check for numbers in the <lastname> parameter
    if (not self.hasNumbers(cmdLst[2])):
      var = cmdLst[3]
      if cmdLst[1].lower() in ('name', 'lastname', 'age'):
        # if first paramater is <age>
        if cmdLst[1].lower() == 'age':
          # Verify for an integer in last parameter 
          if self.ifInt(var):
            var = int(var)
            found = self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var) 
            if not found:
              print(">> Last name {} can't be found in patients register!\n".format(cmdLst[2].upper()))
            # if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
            #   print(">> Last name {} can't be found in personal register!\n".format(cmdLst[2].upper()))
          # else check the input
          else:
            print(">> The age must be a numerical value !\n")
            return False
        else:
          # check for a string in the last parameter
          if (not self.hasNumbers(var)):
            if not self.patients.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
              print(">> Last name {} not found in patient register !\n".format(cmdLst[2].upper()))
            # if not self.personnel.update(cmdLst[1].lower(), cmdLst[2].lower(), var):
            #   print(">> Last name {} not found in personal register !\n".format(cmdLst[2].upper()))
          else:
            print(">> The name can't contain numbers !\n")
      else:
        print(">> The second parameter must be : name, lastname or age !\n")
    else:
      print(">> The name is incorrect !\n")
      
  # --- DELETE ---
  # Allows you to delete an occupant.
  def delete(self, _param):
    if not self.hasNumbers(_param):
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
  