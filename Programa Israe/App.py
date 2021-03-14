#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-
from IO import *
io = IO()


"""
  MAIN MODULE
  =========================
  The main module recives input from the user through the console. It gives feedback about the action taken
  It concist of an infinite while loop for asking new orders
  @author: Alejandro H.
"""

print("###### Bienvenue dans l'interface de contrôle du registre hospitalier ######")
print('###### (Welcome to the hospital registry control interface) ######\n')
print("Commandes possibles (Possible actions) :")
print(">> create <patient (patient) | personnel (personal)> <nom (surname)> <prénom (name) > <age (age)> <{'symp1':5,'symp2':3} | role (role) >")
print(">> read <all (all) | nom (surname)>")
print(">> update <nom (surname) | prenom (name) | age> <nom (surname) > <valeur (value)>")
print(">> delete <nom (surname) >")
print(">> quit (exit)\n")
print("###### En attente de commande (Awaiting order): ######")

while True:
  cmd = input(">> ")
  cmd = cmd.strip()
  cmdLst = cmd.split(" ")
  size = len(cmdLst)

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
    exit()

  else:
    print(">> Commande incorrecte (Incorrect order)!")
    print(">> Réviser l'orthographe ou les doubles espaces (Review spelling or double spaces)!")
