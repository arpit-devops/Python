
file = open("sample.txt")    # here "file" is file pointer to that sample.txt
content = file.read()      # now content of sample.txt will be store in content.
print(content)
file.close()