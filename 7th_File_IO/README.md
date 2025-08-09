# 7th_File_IO

Key commands you should know:

1. ```with open(file_name, mode) as file:``` this will open a file in a certain 'mode'
  a. The modes are: "r" - read mode, "w" - write mode, "a" append mode
  b. Be careful with "w" mode! It will completely overwrite your file!

2. ```file.seek()``` this allows you to navigate through a file to a certain index within the file
  a. When you open a file, you may move through the data to a specific character with .seek(index)

3. String methods like ```.strip()``` allow you to quickly format and manipulate your data!
  b. Additional commands you should try out include:
   ```.lower()``` - makes a string lowercase
   ```.upper()``` - makes a string uppercase
   ```.replace(a,b)``` - replaces 'a' with 'b'
   ```.strip()``` - strips away spaces at the ends of a string
