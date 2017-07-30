#!/usr/bin/env python
# encoding: utf-8



#The merge method takes in the two subarrays and creates a output array
# worst case time complexity is O(nlg n)
def merge(left, right):
  sorted = []
  
  while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
      sorted.append(left.pop(0))
    else:
      sorted.append(right.pop(0))

  if len(left) > 0:
    sorted.extend(left)
  else:
    sorted.extend(right)

  return sorted;


def string_sort(arr):
  if len(arr) < 2:
    return arr 
    
  mid = len(arr) / 2
  left = arr[:mid]
  right = arr[mid:]
  
  return merge(string_sort(left), string_sort(right));
  



if __name__ == '__main__':
    print string_sort([1,2,3,4,5,0,4,3,2,1])
    print string_sort(['A','C','B','D','B'])
    print string_sort(['GANESH','PRABU','ARUN','KOUSHIK','VIKRAM'])