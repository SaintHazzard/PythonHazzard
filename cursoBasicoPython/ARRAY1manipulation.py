source_array1 = [5, 3, 1, 8, 0]
source_array = [5, 3, 2, 8, 1, 4]
# print(sorted(source_array1, key=lambda x: x%2 == 0))
def sort_array1(source_array):
    odd = sorted([i for i in source_array if i%2 == 1])
    order_list = []
    con = 0
    for k in source_array:
        if k%2 == 1:
            order_list.append(odd[con])
            con +=1
        else:
            order_list.append(k)
    return order_list


def sort_array(arr):
  odds = sorted([x for x in arr if x % 2 == 1])
  print(odds)
  # el pop() remueve el item y devuelve el valor removido
  return [x if x % 2 == 0 else odds.pop() for x in arr]



print(sort_array(source_array))
