# write a python function, check_anagram() which accepts two strings and returns True, 
#if one strings is a special anagram of another string.

def is_anagram(data1, data2):
    list_data1 = list(data1)
    list_data1.sort()
    list_data2 = list(data2)
    list_data2.sort()
    
    #another solutions
    if list_data1==list_data2:
    print(True)
    else:
    Print(False)
    
  #solution for check_anagram
    return (list_data1 == list_data2)

print(is_anagram('anagram','nagaram'))
print(is_anagram('cat','rat'))
