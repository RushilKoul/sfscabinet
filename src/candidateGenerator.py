'''
Program generates candidates.json in the following format:
{
"tagore": { 
"captains": [
    {"name": "c1","img": "..path.."},
    {"name": "c2","img": "..path.."},
    {"name": "c3","img": "..path.."}
    ],
"vice_captains": [
    {"name": "vc1","img": "..path.."},
    {"name": "vc2","img": "..path.."},
    {"name": "vc3","img": "..path.."}
]
}
}
'''

from termcolor import colored

n_captains_tagore = int(input(colored("No. of captains in TAGORE HOUSE: ", "yellow")))
n_vice_captains_tagore = int(input(colored("No. of vice captains in TAGORE HOUSE: ", "yellow")))

n_captains_teresa = int(input(colored("No. of captains in TERESA HOUSE: ", "blue")))
n_vice_captains_teresa = int(input(colored("No. of vice captains in TERESA HOUSE: ", "blue")))

n_captains_gandhi = int(input(colored("No. of captains in GANDHI HOUSE: ", "red")))
n_vice_captains_gandhi = int(input(colored("No. of vice captains in GANDHI HOUSE: ", "red")))

n_captains_nehru = int(input(colored("No. of captains in NEHRU HOUSE: ", "green")))
n_vice_captains_nehru = int(input(colored("No. of vice captains in NEHRU HOUSE: ", "green")))


captains_tagore_name = []
captains_tagore_img = []

captains_teresa_name = []
captains_teresa_img = []

captains_nehru_name = []
captains_nehru_img = []

captains_gandhi_name = []
captains_gandhi_img = []

vice_captains_tagore_name = []
vice_captains_tagore_img = []

vice_captains_teresa_name = []
vice_captains_teresa_img = []

vice_captains_nehru_name = []
vice_captains_nehru_img = []

vice_captains_gandhi_name = []
vice_captains_gandhi_img = []


###################### TAGORE HOUSE ###############################
print(colored("-"*80, "cyan"))
print(colored("TAGORE HOUSE CAPTAINS", "yellow"))
print(colored("-"*80, "cyan"))
print('\n')

for i in range(n_captains_tagore):
    n = input(colored(f"Enter name for candidate {i + 1}: ", "yellow"))
    i = input(colored(f"Enter *ABSOLUTE* image path for candidate {i + 1}: ", "yellow"))
    print('\n')

    captains_tagore_name.append(n)
    captains_tagore_img.append(i)

print(colored("-"*80, "cyan"))
print(colored("TAGORE HOUSE VICE CAPTAINS", "yellow"))
print(colored("-"*80, "cyan"))
print('\n')

for i in range(n_vice_captains_tagore):
    n = input(colored(f"Enter name for candidate {i + 1}: ", "yellow"))
    i = input(colored(f"Enter *ABSOLUTE* image path for candidate {i + 1}: ", "yellow"))
    print('\n')

    vice_captains_tagore_name.append(n)
    vice_captains_tagore_img.append(i)

###################################################################

###################### TERESA HOUSE ###############################
print(colored("-"*80, "cyan"))
print(colored("TERESA HOUSE CAPTAINS", "blue"))
print(colored("-"*80, "cyan"))
print('\n')

for i in range(n_captains_teresa):
    n = input(colored(f"Enter name for candidate {i + 1}: ", "blue"))
    i = input(colored(f"Enter *ABSOLUTE* image path for candidate {i + 1}: ", "blue"))
    print('\n')

    captains_teresa_name.append(n)
    captains_teresa_img.append(i)

print(colored("-"*80, "cyan"))
print(colored("TAGORE HOUSE VICE CAPTAINS", "blue"))
print(colored("-"*80, "cyan"))
print('\n')

for i in range(n_vice_captains_teresa):
    n = input(colored(f"Enter name for candidate {i + 1}: ", "blue"))
    i = input(colored(f"Enter *ABSOLUTE* image path for candidate {i + 1}: ", "blue"))
    print('\n')

    vice_captains_teresa_name.append(n)
    vice_captains_teresa_img.append(i)

###################################################################

###################### GANDHI HOUSE ###############################
print(colored("-"*80, "cyan"))
print(colored("GANDHI HOUSE CAPTAINS", "red"))
print(colored("-"*80, "cyan"))
print('\n')

for i in range(n_captains_gandhi):
    n = input(colored(f"Enter name for candidate {i + 1}: ", "red"))
    i = input(colored(f"Enter *ABSOLUTE* image path for candidate {i + 1}: ", "red"))
    print('\n') 

    captains_gandhi_name.append(n)
    captains_gandhi_img.append(i)

print(colored("-"*80, "cyan"))
print(colored("TAGORE HOUSE VICE CAPTAINS", "red"))
print(colored("-"*80, "cyan"))
print('\n')

for i in range(n_vice_captains_gandhi):
    n = input(colored(f"Enter name for candidate {i + 1}: ", "red"))
    i = input(colored(f"Enter *ABSOLUTE* image path for candidate {i + 1}: ", "red"))
    print('\n')

    vice_captains_gandhi_name.append(n)
    vice_captains_gandhi_img.append(i)

###################################################################

###################### NEHRU HOUSE ###############################
print(colored("-"*80, "cyan"))
print(colored("NEHRU HOUSE CAPTAINS", "green"))
print(colored("-"*80, "cyan"))
print('\n')

for i in range(n_captains_nehru):
    n = input(colored(f"Enter name for candidate {i + 1}: ", "green"))
    i = input(colored(f"Enter *ABSOLUTE* image path for candidate {i + 1}: ", "green"))
    print('\n')

    captains_nehru_name.append(n)
    captains_nehru_img.append(i)

print(colored("-"*80, "cyan"))
print(colored("TAGORE HOUSE VICE CAPTAINS", "green"))
print(colored("-"*80, "cyan"))
print('\n')

for i in range(n_vice_captains_nehru):
    n = input(colored(f"Enter name for candidate {i + 1}: ", "green"))
    i = input(colored(f"Enter *ABSOLUTE* image path for candidate {i + 1}: ", "green"))
    print('\n')

    vice_captains_nehru_name.append(n)
    vice_captains_nehru_img.append(i)

###################################################################

with open('./candidates.json', 'a+') as f:
    f.write("{\n")
    # WRITE DATA HERE
    f.write('"tagore": { \n\t"captains": [\n')
    json_tagore_captains = []
    for cap in range(n_captains_tagore):

        if cap != n_captains_tagore - 1:
            json_tagore_captains.append('\t\t{"name":"' + captains_tagore_name[cap] + '","img":"' + captains_tagore_img[cap]+ '"},\n')
        elif cap == n_captains_tagore - 1:
            json_tagore_captains.append('\t\t{"name":"' + captains_tagore_name[cap] + '","img":"' + captains_tagore_img[cap]+ '"}\n')
        
    f.writelines(json_tagore_captains)
    f.write("\t\t],\n")

    f.write('\t"vice_captains": [\n')
    json_tagore_vice_captains = []
    for vcap in range(n_vice_captains_tagore):
        if vcap != n_vice_captains_tagore - 1:
            json_tagore_vice_captains.append('\t\t{"name":"' + vice_captains_tagore_name[cap] + '","img":"' + vice_captains_tagore_img[cap]+ '"},\n')
        elif cap == n_captains_tagore - 1:
            json_tagore_vice_captains.append('\t\t{"name":"' + vice_captains_tagore_name[cap] + '","img":"' + vice_captains_tagore_img[cap]+ '"}\n')
        
    f.writelines(json_tagore_vice_captains)

    f.write("\t\t]\n")

    f.write("\t},\n")

    f.write('"teresa": { \n\t"captains": [\n')
    json_teresa_captains = []
    for cap in range(n_captains_teresa):

        if cap != n_captains_teresa - 1:
            json_teresa_captains.append('\t\t{"name":"' + captains_teresa_name[cap] + '","img":"' + captains_teresa_img[cap]+ '"},\n')
        elif cap == n_captains_teresa - 1:
            json_teresa_captains.append('\t\t{"name":"' + captains_teresa_name[cap] + '","img":"' + captains_teresa_img[cap]+ '"}\n')
        
    f.writelines(json_teresa_captains)
    f.write("\t\t],\n")

    f.write('\t"vice_captains": [\n')
    json_teresa_vice_captains = []
    for vcap in range(n_vice_captains_teresa):
        if vcap != n_vice_captains_teresa - 1:
            json_teresa_vice_captains.append('\t\t{"name":"' + vice_captains_teresa_name[cap] + '","img":"' + vice_captains_teresa_img[cap]+ '"},\n')
        elif cap == n_captains_teresa - 1:
            json_teresa_vice_captains.append('\t\t{"name":"' + vice_captains_teresa_name[cap] + '","img":"' + vice_captains_teresa_img[cap]+ '"}\n')
        
    f.writelines(json_teresa_vice_captains)
        
    f.write("\t\t]\n")
    f.write("\t},\n")

    f.write('"gandhi": { \n\t"captains": [\n')
    json_gandhi_captains = []
    for cap in range(n_captains_gandhi):

        if cap != n_captains_gandhi - 1:
            json_gandhi_captains.append('\t\t{"name":"' + captains_gandhi_name[cap] + '","img":"' + captains_gandhi_img[cap]+ '"},\n')
        elif cap == n_captains_gandhi - 1:
            json_gandhi_captains.append('\t\t{"name":"' + captains_gandhi_name[cap] + '","img":"' + captains_gandhi_img[cap]+ '"}\n')
        
    f.writelines(json_gandhi_captains)
    f.write("\t\t],\n")

    f.write('\t"vice_captains": [\n')
    json_gandhi_vice_captains = []
    for vcap in range(n_vice_captains_gandhi):
        if vcap != n_vice_captains_gandhi - 1:
            json_gandhi_vice_captains.append('\t\t{"name":"' + vice_captains_gandhi_name[cap] + '","img":"' + vice_captains_gandhi_img[cap]+ '"},\n')
        elif cap == n_captains_gandhi - 1:
            json_gandhi_vice_captains.append('\t\t{"name":"' + vice_captains_gandhi_name[cap] + '","img":"' + vice_captains_gandhi_img[cap]+ '"}\n')
        
    f.writelines(json_gandhi_vice_captains)
        
    f.write("\t\t]\n")

    f.write("\t},\n")

    f.write('"nehru": { \n\t"captains": [\n')
    json_nehru_captains = []
    for cap in range(n_captains_nehru):

        if cap != n_captains_nehru - 1:
            json_nehru_captains.append('\t\t{"name":"' + captains_nehru_name[cap] + '","img":"' + captains_nehru_img[cap]+ '"},\n')
        elif cap == n_captains_nehru - 1:
            json_nehru_captains.append('\t\t{"name":"' + captains_nehru_name[cap] + '","img":"' + captains_nehru_img[cap]+ '"}\n')
        
    f.writelines(json_nehru_captains)
    f.write("\t\t],\n")

    f.write('\t"vice_captains": [\n')
    json_nehru_vice_captains = []
    for vcap in range(n_vice_captains_nehru):
        if vcap != n_vice_captains_nehru - 1:
            json_nehru_vice_captains.append('\t\t{"name":"' + vice_captains_nehru_name[cap] + '","img":"' + vice_captains_nehru_img[cap]+ '"},\n')
        elif cap == n_captains_nehru - 1:
            json_nehru_vice_captains.append('\t\t{"name":"' + vice_captains_nehru_name[cap] + '","img":"' + vice_captains_nehru_img[cap]+ '"}\n')
        
    f.writelines(json_nehru_vice_captains)
    f.write("\t\t]\n")
    f.write("\t}")
    f.write("\n}")