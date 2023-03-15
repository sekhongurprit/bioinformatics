#!/usr/bin/bash
read -p "Enter the path of your file:" path
for file in $path/*; do
	if [[ $file == *"P_aeruginosa"* ]] && [[ -s $file ]]; then
		out_file=$(basename -- "$file")
		IFS="."	read -ra out_file_array <<< "$out_file"	
		out_file="$out_file_array"
		awk 'BEGIN {FS="\t"}; {split ($1,a,"#")}; NR>2{print ">"a[1],$9,$11, "\n"$19"\n"}'  $file  > $out_file".fasta"
	fi
done
