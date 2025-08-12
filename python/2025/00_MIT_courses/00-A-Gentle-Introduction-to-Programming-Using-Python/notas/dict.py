import json 

my_dict  = {
    "id": 105,
    "nombre": "William Pérez",
    "edad": 32,
    "email": "william.perez@example.com",
    "activo": True,
    "roles": ["admin", "editor", "tester"],
}
print(my_dict["id"])
my_dict["id"] = 234
print(my_dict["id"])
print(my_dict)

print(json.dumps(my_dict, indent=4, ensure_ascii=False))

print(json.dumps(my_dict,indent=4))

print("~~~~~~~~~~~~~~~~~")
del my_dict["nombre"]
print(json.dumps(my_dict,indent=4))

edad = my_dict["edad"]
print(edad)
print(json.dumps(my_dict,indent=4))

print("~~~~~~~~~~~~~~~~~")
if "activo" in my_dict:
    print("active exists")

print("~~~~~~~~~~~~~~~~~")
print(my_dict.keys())
print("~~~~~~~~~~~~~~~~~")
print(my_dict.values())
print("~~~~~~~~~~~~~~~~~")
print(my_dict.items())
print("~~~~~~~~~~~~~~~~~")

print("~~~~~~~~~~~~~~~~~")

a  = {
    "id": 105,
    "nombre": "William Pérez",
    "edad": 32,
    "email": "william.perez@example.com",
    "activo": True,
    "roles": ["admin", "editor", "tester"],
}
