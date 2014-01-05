# implement a binary search using a recursive algorithm

def binary_search(array, focus_value, current_index = 0):
  '''
  search the array for the focus value, if found return the index of that
  value
  '''
  length = len(array)
  midpoint_index = (length - 1)//2
  midpoint_value = array[midpoint_index]
  if midpoint_value == focus_value:
    return current_index + midpoint_index
  elif midpoint_value > focus_value:
    return binary_search(array[:midpoint_index], focus_value, current_index)
  else:
    midpoint_index += 1
    return binary_search(array[midpoint_index:], focus_value, current_index + midpoint_index)


