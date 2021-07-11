#!/usr/bin/env python3
import os
import json
import sys

# main function
def cli():
  get_args()
  

#get the json data
def load_json():
  filepath = 'ntz.json'
  with open(filepath, 'r') as file:
    data = json.load(file)
  return data

#set new json data
def dump_json(data):
  filepath = 'ntz.json'
  with open(filepath, 'w') as file:
    json.dump(data, file)

def get_args():
  #check input from termial
  #print(sys.argv)

  if len(sys.argv) == 1:
    data = load_json()
    nice_print(data)
  elif sys.argv[1] == 'r':
    remeber()
  elif sys.argv[1] == '-c':
    create()
  elif sys.argv[1] == 'f':
    forget
  elif sys.argv[1] == 'e':
    edit()
  elif sys.argv[1] == 'clear':
    clear()
  elif sys.argv[1] == 'help':
    help()
  else:
    print('Invalid input.')
  #return sys.argv

def nice_print(data):
  for key, values in data.items():
    print()
    print(key,':')
    for v in values:
      print(v)
    print()

def remeber():
  pass

def create():
  pass

def forget():
  pass

def edit():
  data = load_json()
  #get the list to edit
  while True:
    if len(sys.argv) >= 3:
      if sys.argv[2] in data:
        list_to_edit = sys.argv[2]
        break
      else:
        return print('\nInvalid Command.\n')
    else:
      print()
      for key in data:
        print(key)
      list_to_edit = input('\nSelect list to edit: ')
      if list_to_edit in data:
        break
      else:
        print('\nInvalid List.')
  
  #add/drop
  while True:
    if len(sys.argv) >= 4:
      if sys.argv[3] == 'add':
        add(list_to_edit, data)
        break
      elif sys.argv[3] == 'drop':
        drop(list_to_edit, data)
        break
      else:
        return print('Invalid Command')
    action = input('\n"add" to add item to list.\n"drop" to drop an item from list.\nSelect action: ')
    if action == 'add':
      add(list_to_edit, data)
      break
    elif action == 'drop':
      drop(list_to_edit, data)
      break
    else:
      print('\nInvalid Action.\n')

def add(list_to_edit, data):
  if len(sys.argv) >= 5:
    list_to_add = sys.argv[4:]
  else:
    add_to_list_str = input('\nAdd to list: ')
    list_to_add = add_to_list_str.split(', ')
  
  [data[list_to_edit].append(item) for item in list_to_add]
  dump_json(data)
  

  

def drop(list_to_edit, data):
  if len(sys.argv) >= 5:
    list_to_drop = sys.argv[4:]
  else:
    print()
    print(data[list_to_edit])
    drop_to_list_str = input('\nDrop from list: ')
    list_to_drop = drop_to_list_str.split(', ')

  for item in list_to_drop:
    not_in_list = []
    if item in data[list_to_edit]:
      index_pos = data[list_to_edit].index(item)
      data[list_to_edit].pop(index_pos)
    else:
      not_in_list.append(item)
    if len(not_in_list) > 0:
      print('Not found in list:',not_in_list)

  dump_json(data)


  



def clear():
  pass

def help():
  pass

# run the main function
cli()

