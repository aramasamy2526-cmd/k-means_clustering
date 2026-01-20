a = {"name":"Ramasamy",
     "age": 27,
     "Designation": "Technical Analyst",
     "Marital_status": "Yes",
     "Sibblings": ["Chandru","Sathish Kumar"]
    }

print(a.get("name"))
a["name"]="ram" # one type of assignmet
print(a)

a.pop("age")
print(a)

a.update({"name": "som"})
print(a)


print(a.items())
for key,value in a.items():
    print(key , "->", value)


# dictionary support get(), keys(), values(), items(), update(), thisdict["key"] = "value", thisdict.pop("key"), del dict, clear()
