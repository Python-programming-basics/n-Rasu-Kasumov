# 1

my_dict = {1.12:'aa', 67.9:45, 3.11:'ccc', 7.9:'dd', 9.2:'ee',
           7.1:'ff', 0.12:'qq', 1.91:'aa', 10.12:[1,2,3], 99.0:{9,0,1}}

numbers = []

for value in my_dict.values():
    if type(value) == int or type(value) == float:
        numbers.append(value)

print(min(numbers) + max(numbers))



# 2

users = [
    {'name':'Todd', 'phone':'551-1414', 'email':'todd@gmail.com'},
    {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
    {'name':'Olivia', 'phone':'449-3141', 'email':''},
    {'name':'LJ', 'phone':'555-2718', 'email':'lj@gmail.net'},
]

for user in users:
    phone = user['phone']
    if phone[-1] == '8':
        print(user['name'], end=' ')

print()



# 3

users2 = [
    {'name':'Todd', 'phone':'551-1414', 'email':'todd@gmail.com'},
    {'name':'Helga', 'phone':'555-1618'},
    {'name':'Olivia', 'phone':'449-3141', 'email':''},
]

for user in users2:
    email = user.get('email', '')
    if email == '':
        print(user['name'], end=' ')

print()



# 4

digits = input()
numbers2words = {
    "0":"zero","1":"one","2":"two","3":"three","4":"four",
    "5":"five","6":"six","7":"seven","8":"eight","9":"nine"
}

for d in digits:
    print(numbers2words[d], end=' ')

print()



# 5

courses = {
    "CS101": ("3004", "Хайнс", "8:00"),
    "CS102": ("4501", "Альварадо", "9:00"),
    "CS103": ("6755", "Рич", "10:00"),
}

code = input()
room, teacher, time = courses[code]
print(code + ": " + room + ", " + teacher + ", " + time)



# 6

text = input().upper()

keys = {
    'A':'2','B':'22','C':'222',
    'D':'3','E':'33','F':'333',
    ' ':'0'
}

result = ""

for ch in text:
    if ch in keys:
        result += keys[ch]

print(result)



#7

morse = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
    'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
    'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
    'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
    'Y':'-.--','Z':'--..'
}

word = input().upper()

for letter in word:
    print(morse[letter], end=' ')

print()



# 8


result = {}
for i in range(11, 16):
    result[i] = i*i

print(result)



#9


dict1 = {'a':100, 'b':200}
dict2 = {'a':300, 'c':50}

result2 = {}

for k in dict1:
    result2[k] = dict1[k]

for k in dict2:
    if k in result2:
        result2[k] = result2[k] + dict2[k]
    else:
        result2[k] = dict2[k]

print(result2)



# 10


text2 = "hello"
count = {}

for ch in text2:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)



# 11


s = "apple orange apple banana banana banana orange"

words = s.split()
count_words = {}

for w in words:
    if w in count_words:
        count_words[w] += 1
    else:
        count_words[w] = 1

max_count = max(count_words.values())

best_word = None
for w in count_words:
    if count_words[w] == max_count:
        if best_word is None or w < best_word:
            best_word = w

print(best_word)



# 12


pets = [
    ("Hatiko","Parker","Wilson",50),
    ("Rusty","Josh","King",25),
    ("Fido","John","Smith",28)
]

owners = {}

for pet, name, fam, age in pets:
    owner = (name, fam, age)
    if owner not in owners:
        owners[owner] = []
    owners[owner].append(pet)

print(owners)



#13


words = input().split()
count3 = {}

for w in words:
    if w in count3:
        count3[w] += 1
    else:
        count3[w] = 1

print(max(count3, key=count3.get))



# 14

ids = input().split()
seen = {}
result = []

for ident in ids:
    if ident in seen:
        seen[ident] += 1
        result.append(ident + "_" + str(seen[ident]))
    else:
        seen[ident] = 0
        result.append(ident)

print(" ".join(result))
