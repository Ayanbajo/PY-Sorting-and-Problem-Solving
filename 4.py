# Write an algorithm that takes in a string and sorts the words in the string in alphabetical order. The comparison should be case-insensitive.
string = 'I am not sure what I am doing'
sorted_strings = sorted(string.split(), key = str.lower)
print(sorted_strings)