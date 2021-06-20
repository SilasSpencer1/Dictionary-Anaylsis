#Libraries used:


import itertools
#Downloading of all words from dictionary to list:
words = open("words.txt", "r").readlines()
#Words.txt file taken from MIT website https://www.mit.edu/~ecprice/wordlist.10000


#Removing of character \n from words of list:
for i in range(0, len(words)):
    words[i] = words[i].replace("\n", "")
#Getting of string from user:
MyString = input("Enter your string: ")


#Getting of list of letters from string of user:
letters_of_string = list(MyString)


#Forming of all possible strings from letters of user's string:
all_combinations_of_letters = []
for i in list(itertools.permutations(letters_of_string)):
    all_combinations_of_letters.append("".join(i))

#Removing of duplicated strings that are formed from letters of user's string:
all_combinations_of_letters_final = []
for i in all_combinations_of_letters:
    if i not in all_combinations_of_letters_final:
        all_combinations_of_letters_final.append(i)


#Here we check each string that is formed from letters of user's string and if it is in English dictionary, we add this string to final list:
real_words = []
for j in range(0, len(all_combinations_of_letters_final)):
    for i in range(0, len(words)):
        if all_combinations_of_letters_final[j] == words[i].lower():
            real_words.append(all_combinations_of_letters_final[j])
            break

#Here we print all words from final list:
print("Words that can be received from letters of your string: ")
for i in real_words:
    print(i)