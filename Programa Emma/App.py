#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
import sys
from IO import *
from Registre import *

io = IO()


"""
  MAIN MODULE
  =========================
  The main module manage all the interactions with the user.   
  
"""
def printIstruction():
    print("The available commands are:\n")
    print(">> create < (patient) | (personal)> < lastname > < name > < age > < (numberOfSymptomes) | (role) >")
    # print(">> create < (patient) | (personal)> < lastname > < name > < age > < {'symp1':1,'symp2':5} | (role) >")
    print(">> read < (all) | lastname > < (patient) | (personal)")
    print(">> update < (lastname) | (name) | (age) > < lastname > < value >")
    print(">> delete < lastname>")
    print(">> istructions (show instructions)")
    print(">> quit (exit)\n")
    print("###### Awaiting for a command: ######")


# START PROGRAM

print('\n###### Welcome to the hospital registry control interface! ######\n')
printIstruction()
while True:
  cmd = input(">> ")
  cmdLst = cmd.split()
  size = len(cmdLst)

  # --- CREATE ---
  if cmdLst[0].lower() == "create" and size == 6:
    io.create(cmdLst)

  # --- READ ---
  elif cmdLst[0].lower() == "read" and size == 3:
    io.read(cmdLst[1],cmdLst[2])

  # --- UPDATE ---
  elif cmdLst[0].lower() == "update" and size == 4:
    io.update(cmdLst)

  # --- DELETE ---
  elif cmdLst[0].lower() == "delete" and size == 2:
    io.delete(cmdLst[1])

  # --- TEST ---
  elif cmdLst[0].lower() == "test" and size == 2:
    if cmdLst[1] == "1":
      io.test_1()
    elif cmdLst[1] == "2":
      io.test_2()
  
  # --- INSTRUCIONS ---
  elif cmdLst[0].lower() == "instructions":
    printIstruction()

  # --- QUIT ---
  elif cmdLst[0].lower() == "quit":
    sys.exit()
    
  else:
    print(">> Invalid command! \n")
