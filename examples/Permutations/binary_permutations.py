#!12/12/2014

import smact
from os import path

def pauling_test(ox, paul):
	makes_sense = True
	for i, ox_i in enumerate(ox):
		for j, ox_j in enumerate(ox[i+1:]):
			#!print ox_i, ox_j, paul[i], paul[i+1+j]
			if ox_i < ox_j:
				if paul[i] < paul[i+1+j]:
					makes_sense = False
			if ox_i > ox_j:
				if paul[i] > paul[i+1+j]:
					makes_sense = False	
			if ox_i == ox_j:
				if paul[i] != paul[i+1+j]:
					makes_sense = False
	return makes_sense

with open(path.join(smact.data_directory, 'element.txt'),'r') as f:
	data = f.readlines()

list_of_elements = []

for line in data:
	if not line.startswith('#'):
		species = line.split()
		if int(species[0]) > 0 and int(species[0]) < 101:
			#if len(smact.Element(species[1]).oxidation_states) > 0:
			if smact.Element(species[1]).oxidation_states:
			    list_of_elements.append(species[1])
			
count_of_ternary = 0
count_raw_ternary = 0
element_count = 0
ion_count = 0
charge_neutral_count = 0
pauling_count = 0
for i, ele_a in enumerate(list_of_elements):
 	element_count = element_count + 1
	paul_a = smact.Element(ele_a).pauling_eneg
	for ox_a in smact.Element(ele_a).oxidation_states:
		ion_count = ion_count + 1
		for j, ele_b in enumerate(list_of_elements[i+1:]):
			element_count = element_count + 1
			paul_b = smact.Element(ele_b).pauling_eneg
			for ox_b in smact.Element(ele_b).oxidation_states:
				ion_count = ion_count + 1
				element = [ele_a, ele_b]
				print element
				oxidation_states = [ox_a, ox_b]
				pauling_electro = [paul_a, paul_b]
				electroneg_makes_sense = pauling_test(oxidation_states, pauling_electro)
				cn_e, cn_r = smact.charge_neutrality([ox_a, ox_b],threshold=1)
				if cn_e:
					charge_neutral_count = charge_neutral_count + 1
					if electroneg_makes_sense:
						pauling_count = pauling_count + 1

print "  "
print "------------------------------------------"
print "------------------------------------------"
print "Summary of screening for ternary compounds"
print "------------------------------------------"
print "Total from atoms: ", element_count
print "Total from ions:  ", ion_count
print "Total charge neutral: ", charge_neutral_count
print "Total Pauling allowed: ", pauling_count
print "------------------------------------------"
print "I owe you nothing!"
