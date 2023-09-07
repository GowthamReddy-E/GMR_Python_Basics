# way one
dictionary={"name":"gowtham","age":"27"}

# way two
dictionary=dict(gowtham="value1",name="value2")
print(dictionary)


# way three
my_dict = dict([('key1', 'value1'), ('key2', 'value2')])
print(my_dict)


# fourth way
dictionaryOne={"name":"gowtham","village":"thummalapalli","age":"27","Degree":["diploma","B-tech","M-tech"],
"Interest":{"Technology":"Coding","Study":"P-Hd","Specialization":["magneticFields","NuclearScience","NanoTechnology"]}}

print(dictionaryOne["Interest"]["Specialization"][0])