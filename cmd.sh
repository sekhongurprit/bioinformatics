p3-all-genomes --eq "genome_name, acinetobacter baumannii" --public >all.tbl
cat all.tbl | p3-get-genome-drugs --eq "evidence, laboratory_method" --eq "resistant_phenotype, susceptible" --attr antibiotic > susceptible.tbl
cat all.tbl | p3-get-genome-drugs --eq "evidence, laboratory_method" --eq "resistant_phenotype, resistant" --attr antibiotic > resistant.tbl&
cat resistant.tbl |grep penem | awk '{print $1}' |sort| uniq >carb_res.tbl 
cat susceptible.tbl |grep penem | awk '{print $1}' |sort| uniq >carb_sus.tbl 
comm -12i carb_res.tbl carb_sus.tbl >common.tbl
grep -xvf  common.tbl  carb_res.tbl  >carb_res_unique.tbl 
grep -xvf  common.tbl  carb_sus.tbl  >carb_sus_unique.tbl 
cat carb_res_unique.tbl |p3-get-genome-data --attr sra_accession >tmp.tbl
cat tmp.tbl|awk '{print $1}'|p3-get-genome-data --attr sra_accession --attr strain|sort -k 3 >Rstrain.tbl
###Remove not applicable strains
cat carb_sus_unique.tbl |p3-get-genome-data --attr sra_accession >tmp.tbl
cat tmp.tbl|awk '{print $1}'|p3-get-genome-data --attr sra_accession --attr strain|sort -k 3 >Sstrain.tbl
###Extracting only SRA_IDs
cat Rstrain.tbl |awk '{print $2}' |awk -F ',' '{print $1}' >Rstrain.txt
cat Sstrain.tbl |awk '{print $2}' |awk -F ',' '{print $1}' >Sstrain.txt

###find Rstrain/  -mindepth 1 -type d |wc -l
###find Sstrain/  -mindepth 1 -type d |wc -l


