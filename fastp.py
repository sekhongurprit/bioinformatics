def qc_fastq(sra_ids):
    for id in sra_ids:
        f1=id+"_1.fastq"
        f2=id+"_2.fastq"
        trim1="trimmed_"+f1
        trim2="trimmed_"+f2
        #out1=str(counter)+"_fastp"+".html"
        #out2=str(counter)+"_fastp"+".json"
        out1=id+"_fastp"+".html"
        out2=id+"_fastp"+".json"
        fastp="fastp --cut_right --cut_front --cut_right_mean_quality=30 --cut_front_mean_quality=30 -c -i " + fastq_path+f1 \
                + " -I "+fastq_path+f2 + " -o "+trim_path+trim1 + " -O "+trim_path+trim3 + " -h "+qc_path+out1 + " -j "+qc_path+out2
        print(fastp)
        subprocess.call(fastp, shell=True, executable="/bin/bash")
