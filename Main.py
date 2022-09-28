from typing import List

def insertionSort(array) -> List[int]:
  for j in range (1, length[array]
     key = array[j]
     i = j - 1  
     while i >= 0 and key < array[i]:  
      array[i + 1] = array[i]  
      i -= 1  
     array[i + 1] = key  
  return array  
                  

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
