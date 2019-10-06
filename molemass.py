names=["H", "C", "N", "O","P","S"]
masses=[1.00794,12.0107,14.00674,15.9994,30.973761,32.066]
Dict2={}
for i in range(len(names)):
    Dict2[names[i]]=masses[i]
print(Dict2)


def molemass(formula):
    mass=0
    for i in formula:
        mass=Dict2[i]+mass
    return mass
    print(mass)
