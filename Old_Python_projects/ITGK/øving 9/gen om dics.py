my_fam={"bror": "bjørnar","mamma": "bergny"}
def add_fam(role,names):
    my_fam[role]= names.split(", ")
add_fam("søster", "sunniva, guro")
print (my_fam)
for key, val in my_fam.items():
    print (key,":",val)



