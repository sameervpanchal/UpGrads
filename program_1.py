# 1. Given a full name, your task is to capitalize the name (only the first letter of all sub names which is separated by space must be in capital letters and rest in small letters).
# 
#  
# 
# Sample input 1 : covid 19 who                             output : Covid 19 Who
# 
# Sample input 2 : who 19covid                              output : Who 19covid
# 
# Explanation :
# 
# for input 1 : c and w are converted into C and W respectively and 19 is not the letter.
# 
# for input 2 : w is converted to W and 19covid remains 19covid because the first letter starts with a digit.
# 
#  
# 
# Please write generic code which is valid for all inputs. 
# 
# Note : Input is taken by user so please use input().

string_data = input()
new_list = []
count = 0

list_data=string_data.split(" ")
for x in list_data:
  new_list.insert(count, x.capitalize())
  count += 1;

new_string = " ".join(new_list)
print (new_string)