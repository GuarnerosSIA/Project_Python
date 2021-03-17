#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from IO import *
import sys
io = IO()


"""
  MAIN MODULE
  =========================
  The main module recives input from the user through the console. It gives feedback about the action taken
  It concist of an infinite while loop for asking new orders
  @author: José Alejandro Hernández Pérez
"""
print('###### (Welcome to the hospital registry control interface) ######\n')

print("### A previous file is beeing loaded ###")
print("#######################################")
io.patients.loadJson()
io.personnel.loadJson()
print("#######################################")
print("### load complete ###")


def printInstructions():
  print("Possible actions: \n")
  print('--Create a new patient (personal) from surname, name, age and number of symptomes (role)')
  print(">> create // patient | personal // surname // name  // age // numberOfSymptomes | role \n")
  print('--Read all the patients, all the personal list or a specific patient in the registry')
  print(">> read // all | all-personal | surname\n")
  print('--Update an occupant\'s surname, name or age, from its surname')
  print(">> update // surname | name | age // surname // value")
  print('--Delete an occupant from its surname')
  print(">> delete // surname")
  print('--Execute default tests')
  print(">> test // 1 | 2")
  print('--Exit ')
  print(">> quit \n")
  print("###### Awaiting order: ######")
  print("Do not forget to separate with //:")

printInstructions()
while True:
  cmd = input(">> ")
  cmd = cmd.strip()
  cmdLst = cmd.split("//")
  size = len(cmdLst)
  for i in range(size):
    cmdLst[i] = cmdLst[i].strip().lower()

  # --- Option CREATE ---
  if cmdLst[0].lower() == "create" and size == 6:
    io.create(cmdLst)
 
  # --- Option READ ---
  elif cmdLst[0].lower() == "read" and size == 2:
    io.read(cmdLst[1])

  # --- Option UPDATE ---
  elif cmdLst[0].lower() == "update" and size == 4:
    io.update(cmdLst)

  # --- Option DELETE ---
  elif cmdLst[0].lower() == "delete" and size == 2:
    io.delete(cmdLst[1])

  # --- Option TEST ---
  elif cmdLst[0].lower() == "test" and size == 2:
    if cmdLst[1] == "1":
      io.test_1()
    elif cmdLst[1] == "2":
      io.test_2()

  # --- Option QUIT ---
  elif cmdLst[0].lower() == "quit":
    sys.exit()
  
  # --- Option Print Instructions
  elif cmdLst[0].lower() == 'instructions':
    printInstructions()
  
  else:
    print(">> Incorrect order!")
    print(">> Review spelling or the '//' !")