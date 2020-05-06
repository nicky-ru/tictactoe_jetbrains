vowels = 'aeiou'
# create your list here
string = input()
vowels_list = [letter for letter in string if letter in vowels]
print(vowels_list)
