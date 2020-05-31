#!/usr/bin/env python
# encoding: utf-8

"""
Program to find common friends 
"""

ganshes jenkisn check


from operator import itemgetter
import itertools
import sys
import re
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
from sortedcontainers import SortedDict
from mrjob.job import MRJob
from collections import Counter
import itertools
import time

def map_reduce(i,mapper,reducer):
  
  """
  intermediate results are grouped before passing to reducer
  """
  
  intermediate = []
  print i.items()
  for (key,value) in i.items():
    print (key,value)
    intermediate.extend(mapper(key,value))
  #print intermediate
  groups = {}
  for key, group in itertools.groupby(sorted(intermediate),lambda x: x[0]):
    # groups[key] = list
    groups[key] = list([y for x, y in group])
  print groups
  return [reducer(intermediate_key,groups[intermediate_key]) for intermediate_key in groups]




def sortedKey(couple):
  """sorts list of two strings and returns concatenated string"""
  couple.sort()
  return ''.join(couple)

def cmpByKey(a,b):
  """compare two items by their first key"""
  return cmp(a[0],b[0])

def mapper(input_key,input_value):
  """
  split input in multiple lines and returns a tuple (key,value)

  """
  res = []
  for line in input_value.split('\n'):
    person = line.split('|')[0]
    friends = line.split('|')[1].split(';')
    
    for friend in friends:
      key = sortedKey([person,friend])
      value = friends
      res.append((key,value))
  #print res
  return res


def intersect(lists):
  """ return list of intersections"""
  intersection = []
  if len(lists) > 1:
    for f in lists[1]:
      if f in lists[0]:
        intersection.append(f)
  return intersection

def reducer(intermediate_key,intermediate_value_list):
  return (intermediate_key,intersect(intermediate_value_list))

def main():
  """run mapreduce job and outputs sorted results"""
  
  """
  inputfile should contain something like:
  A|B;C;D
  B|A;C;D;E
  C|A;B;D;E
  D|A;B;C;E
  E|B;C;D
  """
  i = {}
  i["friends"] = open('mutual_friends_list.txt').read()
  friendships =  map_reduce(i,mapper,reducer)
  friendships.sort(cmpByKey)

  for friendship in friendships:
    print "%s & %s have %s as common friends " % (friendship[0][0],friendship[0][1],friendship[1])


if __name__ == '__main__':
    main()
