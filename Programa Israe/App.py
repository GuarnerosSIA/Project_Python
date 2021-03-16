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
  @author: Alejandro H.
"""


print('###### (Welcome to the hospital registry control interface) ######\n')
print("Possible actions: ")
print(">> create // patient | personal // surname // name  // age // {'Symptom':5,'Symptom':3} | role")
print(">> read // all | all-personal | surname")
print(">> update // surname | name | age // surname // value")
print(">> delete // surname")
print(">> test // 1 | 2")
print(">> quit (exit)\n")
print("###### Awaiting order: ######")
print("Do not forget to separate with //:")

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

  else:
    print(">> Incorrect order!")
    print(">> Review spelling or the '//' !")