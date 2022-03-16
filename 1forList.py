programing_languages=['Java','Python','C++','C','Ruby','PHP','JavaScript']
for programming_language in programing_languages:
    print(programming_language)
print(f"I leard {programing_languages[0]} and {programing_languages[2]} before,so they are good "+
f"but I haven't leared {programing_languages[3]} and {programing_languages[4]} and {programing_languages[5]}"+
f" and {programing_languages[6]}, so they are bad,so I'll delete them")
#Code below is not required for the homework
#Test pop here
for i in range(3):
    programing_languages.pop()
print("Now we have:")
for n in range(len(programing_languages)):
    print(programing_languages[n])
#Test append here
print("I remember languages again,it's GO and HTML! I'll add it into the list")
programing_languages.append("go")
#Test insert here
programing_languages.insert(0,"HTML")
for programming_language in programing_languages:
    print(programming_language)
#Test pop here
print(f"But I forget delete {programing_languages.pop(4)},let me delete it first.")
for programming_language in programing_languages:
    print(programming_language)
print(f"I didn't learn go as well,so i 'll delete {programing_languages.pop()}.")
for programming_language in programing_languages:
    print(programming_language)
#Test remove
print("Delete HTML")
programing_languages.remove('HTML')
for programming_language in programing_languages:
    print(programming_language)