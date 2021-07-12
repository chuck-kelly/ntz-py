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
    remember()
  elif sys.argv[1] == '-c':
    create()
  elif sys.argv[1] == 'f':
    forget()
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
    print()
    for v in values:
      print('-',v)


def remember():
  data = load_json()

  if len(sys.argv) >= 3:
    list_to_remember = sys.argv[2]
    if list_to_remember in data:
      new_dict ={list_to_remember:data[list_to_remember]}
      nice_print(new_dict)
  
  else:
    new_dict = {'Lists in storage':[]}
    for key in data:
      new_dict['Lists in storage'].append(key)
    nice_print(new_dict)
  

def create():

  data = load_json()

  if len(sys.argv) >= 3:
    new_list = sys.argv[2]
    if new_list == 'q':
      print('\nq is a restricted work.\n')
    elif new_list not in data:
      new_dict = {new_list:[]}
      data = data | new_dict
      dump_json(data)
    else:
      print("\nList already Exists.\n")

  else:
    while True:
      new_list = input("Name new list: ")
      if new_list == 'q':
        print('\nq is a restricted work.\n')
        break
      elif new_list not in data:
        new_dict = {new_list:[]}
        data = data | new_dict
        dump_json(data)
        break
      else:
        print("\nList already Exists.\n")


def forget():

  data = load_json()

  if len(sys.argv) >= 3:
    bye_list = sys.argv[2]

    if bye_list == '_genral_list':
      print('\nCannot Forget _genral_list.\n')

    elif bye_list in data:
      while True:
        double_check = input('\nAre your sure you want to forget '+bye_list+' (y/n): ')
        if double_check == 'y':
          dump_json(data.pop(bye_list))
          break
        elif double_check == 'n':
          break
        else:
          print('\nInvalid Command.')
  elif len(data) == 1:
    print('\nNo lists to forget.\n')
  else:
    print()
    for key in data:
        if key != '_genral_list':
          print(key)
    while True:
      bye_list = input('\nWhat list to forget: ')
      if bye_list == '_genral_list':
        print('\nCannot Forget _genral_list.\n')
      elif bye_list == 'q':
        print()
        break
      elif bye_list in data:
          double_check = input('\nAre your sure you want to forget '+bye_list+' (y/n): ')
          if double_check == 'y':
            dump_json(data.pop(bye_list))
            break
          elif double_check == 'n':
            pass
          else:
            print('\nInvalid Command.')
      else:
        print('\nInvalid List.')


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

  data = load_json()

  if len(sys.argv) == 2:
    while True:
        choice = input('\nDelete all items in _genral_list (y/n):')
        if choice == 'y':
          data['_genral_list']=[]
          dump_json(data)
          break
        elif choice == 'n':
          break
        else:
          print('\nInvalid Command.')
  elif len(sys.argv) >= 3:
    clear_list = sys.argv[2]
    if clear_list in data:
      while True:
        choice = input('\nDelete all items in '+clear_list+' (y/n):')
        if choice == 'y':
          data[clear_list]=[]
          dump_json(data)
          break
        elif choice == 'n':
          break
        else:
          print('\nInvalid Command.')
    else:
      print('\nInvalid Command.\n')


def help():
  print('\nTo remember a list and items -> ntz r <list name>')
  print('\nTo make a new list -> ntz -c <new list name>')
  print('\nTo forget a list -> ntz f <list name>')
  print('\nTo edit a list -> ntz e <list name> <add/drop> <item> <...> ...')
  print('\nTo clear all items in a list -> ntz clear <list name>')
  print('\n<> are optional commands.\n')

# run the main function
cli()

