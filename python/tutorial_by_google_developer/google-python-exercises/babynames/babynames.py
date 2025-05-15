#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import pdb

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


# EN LA TERMINAL TOCA PONER ESTE COMANDO PARA LA RESPUESTA 

# python2 babynames.py --summaryfile baby*.html
# python2 babynames.py --summaryfile baby*.html
# python2 babynames.py --summaryfile baby*.html
# python2 babynames.py --summaryfile baby*.html
# python2 babynames.py --summaryfile baby*.html
# python2 babynames.py --summaryfile baby*.html
# python2 babynames.py --summaryfile baby*.html
# python2 babynames.py --summaryfile baby*.html
# python2 babynames.py --summaryfile baby*.html


def Name(name):
  return name[1]

def year_match_method(pat,file):
  match = re.search(pat, file)
  if match:
    match = match.group(1)
  else:
    match = 'not found'
  return match 

def tuple_names(pat,file):
  file_names_tuple = re.findall(pat,file)
  if not file_names_tuple:
    file_names_tuple = 'Not found'
  else:
    file_names_tuple = sorted(file_names_tuple,key=Name)
  return file_names_tuple

def mix_year_name(year_match,names):
  return names.insert(0,year_match)

def create_file(filename,names):
  file_name = filename + '.summary'
  f = open(file_name,'w+')
  for index, name in enumerate(names):
    if index == 0:
      f.write(name+'\n')
      print name
    else:
      f.write("%s %s \n"%(name[0], name[1]))

  f.close()


def extract_names(filename):
  f = open(filename, 'rU')
  file_string = f.read()
  year_match = year_match_method(r'Popularity\sin\s(\d\d\d\d)',file_string)
  names = tuple_names(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',file_string)
  mix_year_name(year_match,names)

  create_file(filename,names)










  # pdb.set_trace()
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    # pdb.set_trace()
    del args[0]

  # +++your code here+++

  filename = sys.argv[1]

  if summary:
    # pdb.set_trace()
    for file in args:
      extract_names(file)





  extract_names(filename)
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
