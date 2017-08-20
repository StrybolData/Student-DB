def find_text (string, substring):
#no_text = 0
#error= "mistake in string"

   while len(string)> 0:
      x= string.find(substring, no_text)
   if len(string) == -1:
           print("mistake in the string")
#return error

print("found text in:", x)


#def find_text (string, substring):

#string_index = 0

#while string_index < len(string):
 #       substring_index = string.find(substring, string_index)
  #      if index == -1:
   #         break
 #       print('Text found at', substring_index)
#
