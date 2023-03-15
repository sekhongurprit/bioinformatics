#!/bin/bash
counter=0
for f1 in *_pass_1.fastq.gz
do
        f2=${f1%%_pass_1.fastq.gz}"_pass_2.fastq.gz"
	output=""$((++counter))"_fastp.json"
	output2=${f1%%_pass_1.fastq.gz}".html"

        fastp  -i $f1 -I $f2 -o "trimmed-$f1" -O "trimmed-$f2" -j $output -h $output2 --cut_right --cut_front -c
done
