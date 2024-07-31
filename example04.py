text = 'Clarusway'
print(text[3])
print(text[4:7])
print(text [6:]) 
print(text [0:6]) 
print(text [:6])   
print(text [1:8])   
print(text [1:8:2])   
print(text [1::3])   
print(text [::2])   
print(text[5:1])
print(text[5:1:-1])
print(text[5:1:-2])
print(text[:: -1])
print('python candir' [2:10:2])
text= 'kayak'
print(text == text[:: -1])
yeni_text = 'abcdef'
print(yeni_text == yeni_text[:: -1])
print(yeni_text[:: -1])
city = 'Phoenix'
print(city[1:])
print(city[:6])
print(city[::2])
print(city[1::2])
print(city[-3:])
print(city[::-1])
text ="Clarusway"
print(text[8])
print(text [-1])
print(text [8] == text[-1])
animal = "hippopotamus"
print (animal[1:])
print(animal[:6])
print (animal[::2])
print(animal[1:7:2])
print(animal[-3:])
print(animal[::-1])
print(text[ -3:: -1])

vegetable = "Tomato"
print( 'length of the word', vegetable,'is',len(vegetable) )

print('a'+'b')
text ="Clarusway"
print( text[:4] + text[-3:])
print( text[:5] + "k" + text[-3:])
print(text[:5] + 'k')
print( text[:5] + 'k'+ text[6:])
print(len(text))
print(text)

print(text[0]+text[len(text)//2] + text[-1])

print(len(text))
print(len (text)/2)
print(len (text) //2)

ilk = text[0]
son = text[-1]
orta = len(text)//2

print(ilk+text[orta]+son)
orta = text[len(text)//2]
ilk + orta + son
print(text, 'kelimesinin uzunlugu', len(text), 'harften olusur')

str_one = 'upper'
str_two = 'case'
str_comb = str_one + str_two
print('upper' + 'case')
print(str_one + str_two)
print(str_comb)
print(5 * 3)

str_one = 'upper'
str_two = 3 * 'upper'
str_comb = str_one * 3
print(str_two)
print (str_comb)
print(* str_one)

print (text)
print(*text)
print(3*'upper',sep='----->')
print(3*'upper ',sep='----->')

string_1 = 'I am angry...'
string_2 = '1453'

string_1 = 'I am angry...'
print(* string_1)
string_2 = '1453'
print(* string_2)
print(* 'joseph@clarusway.com')

str_one = 'upper'
str_one += 'case'
print (str_one)
str_one += 'letter'
print (str_one)
str_one += 'end'
print(str_one)

a = 5
a = a + 1
a += 1
print(a)

name = 'Yasin'
print( 'Merhaba, %s' % name)

name = 'Yasin'
age = 43
meslek ='Content Creator'

print( 'Merhaba, ismin %s yasin %d meslegin ise % s' % (name, age,meslek))

name = 'Yasin'
age = 43
melek = 'Content Creator'
print( 'Merhaba, ismin %s yasin %f meslegin ise % s' % (name, age, meslek))
print('Merhaba, ismin {} yasin {} meslegin ise {}'.format(name, age ,meslek))

fruit = 'Orange'
vegetable = 'Tomato'
amount = 4
print( 'The amount of {} we bought is {} pounds'. format(fruit, amount) )

name = 'Yasin'
age = 43
meslek ='Content Creator'
print('Merhaba, ismin {} yasin {} meslegin ise {}'. format (name,age, meslek))
print('Merhaba, ismin {} yasin {} meslegin ise {}'.format(age, meslek, name))
print('Merhaba, ismin {2} yasin {0} meslegin ise {1}'.format(age, meslek, name))
print('Merhaba, ismin {a} yasin {b} meslegin ise {c}'.format(b = age,c= meslek, a = name))
print('Merhaba, ismin {}, yasin {} meslegin ise {}'.format(name, age, meslek))
print('[state] is the most (adjective] state of the [country]'.format(state='California',
country='USA', adjective='crowded'))
print('{state} is the most {adjective} state of the {country}'.format(state='California',
country='USA', adjective='crowded'))
print('{0} is the most {adjective} state of the {country}'.format('California', country
='USA', adjective ='crowded'))
print('Merhaba, ismin {},yasin {b} meslegin ise {c}'.format(name, b = age, c = meslek))
print('Merhaba, ismin {}, yasin {b} meslegin ise {c}'.format(name, c = meslek, b = age))

taban = 6
yukseklik = 4
print('burada hesaplama gosterecegim {}'.format(taban*yukseklik/2))

print("{}-{}-{}".format("12", "Feb", "Feb"))
print("{no}-{month}-{month}".format(no="12", month= "Feb"))

print("{6} {5} {0} {1} {3} {4} {2}".format("a new", "job", "months", "in", 6, "have started", "I will"))

name ='Ali'
age = 43
meslek = 'Content Creator'
print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}')

print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}')

print('Merhaba, ismin {},yasin {b} meslegin ise {c}'.format(name, c = meslek, b = age))
print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}', 'Merhaba, ismin {},yasin {b} meslegin ise {c}'.format(name, b = age, c = meslek))

fruit ='Orange'
vegetable= 'Tomato'
amount = 6
output= f"The amount of {fruit} and {vegetable} we bought are totally {amount} pounds"
print(output)

sample = f"{2 ** 3}"
print(sample)
print(f'burada hespalama yapiyor {taban* yukseklik/2}')

name='MARIAM'
print (F'My name is {name.capitalize()}')
print(f'saga hizalama {name: >20}')
print(f'saga hizalama {name: <20}')
print(f'saga hizalama {name:*^20}')


name = "Joseph"
job = "teachers"
domain = "Data Science"
message= f"Hi {name}. "\
f"You are one of the {job}"\
f"in the {domain} section."
print(message)

name ="Susan"
age ="young"
gender = 'lady'
school ="CLRWY IT university"
output = (
f" {name} is a {age}"
f" {gender} and she is a student"
f" at the {school}."
)
print (output)

