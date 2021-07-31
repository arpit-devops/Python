string = "this is String"
print (string.upper())   # this will just print upper case , original file does not modified
print(string)

new_string = string.upper()  # this will store upper case in new_string

print (new_string)

string = string.upper  # this will modified our original string as well.

print (string)