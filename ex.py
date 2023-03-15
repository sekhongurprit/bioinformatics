#!/usr/bin/python
###!/Users/bic/miniconda3/bin/python
import os
import sys
import pandas as pd
user_input=input("Enter path of your file:")
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
i=0
for file in os.listdir(user_input):
	path=os.path.join(user_input,file)
	if('P_aeruginosa' in file and os.stat(path).st_size != 0):
		out_file_name = file.split('.')[0]
		df=pd.read_csv(path,  sep='\t', on_bad_lines='skip')
		protein_list=df['Predicted_Protein'].to_list()
		orf_list=df['ORF_ID']
		orf_list_processed=[]
		best_hit_ARO_list=df['Best_Hit_ARO'].to_list()
		for item in orf_list:
			item=item.split('#')[0]
			orf_list_processed.append(item)
		amr_gene_family_list=df['AMR Gene Family'].to_list()
		max_iterations=len(orf_list)
		j=0
		while(j<max_iterations):
			with open (out_file_name, 'a') as of:
				record='>' + orf_list_processed[j] + out_file_name + amr_gene_family_list[j] + best_hit_ARO_list[j] + '\n' + protein_list[j] + '\n'
				of.write(record)
			j=j+1
		i=i+1
		print('total proteins in %s: %s' %(out_file_name, j))
print("total processed files:", i)
#print(orf_list_processed)
#print(protein_list)
#print(orf_list)
#print(amr_gene_family_list)
#print(file_name_list)
#print(max_iterations)
#print(path)
