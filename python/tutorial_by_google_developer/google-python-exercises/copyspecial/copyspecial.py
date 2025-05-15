#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import pdb

"""
forma larga
def primer_ejercicio_made_absolutely_path(dir):
  list_files = os.listdir(dir)
  new_array = []
  for file in list_files:
    print file
    match = re.search(r'\w+__\w+__\.\w+',file)
    if match:
      new_array.append(file)
    
"""


"""
la forma de trigerlo el primer ejercicios es esta
python2 copyspecial.py .
y nos va mostrar el path absoluto de los nombres es especiales 
en este caso los nombres especiales son dos 
zz__something__.jpg
xyz__hello__.txt


"""

"""
python2 copyspecial.py --todir .

"""



def primer_ejercicio_made_absolutely_path(dir):
  list_files = os.listdir(dir)
  matches_files = [file for file in list_files if re.search(r'\w+__\w+__\.\w+',file)]
  for file in matches_files: print os.path.abspath('./'+file)

def copiararchivo(dir):
  list_files = os.listdir(dir)
  matches_files = [file for file in list_files if re.search(r'\w+__\w+__\.\w+',file)]
  os.mkdir('carpetacreadoporcomando')
  for file in matches_files:
    cmd = 'cp ' +file+ ' ./carpetacreadoporcomando'
    (status,output) = commands.getstatusoutput(cmd)
    print output

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    copiararchivo(todir)
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  if not (todir and tozip):
    primer_ejercicio_made_absolutely_path(sys.argv[1]) 

  # +++your code here+++
  # Call your functions

  
if __name__ == "__main__":
  main()
