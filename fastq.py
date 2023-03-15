#***Compilation of three separate functions to Download, validation, extraction, and quality check of SRA Data***#

#!/usr/bin/python3
import sys
import os
import re
import subprocess

current_dir=os.getcwd()
base_dir=current_dir+"/sra_base_Sstrain"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

sra_path=base_dir+"/sra/"
if not os.path.exists(sra_path):
    os.makedirs(sra_path)

log_path=base_dir+"/log/"
if not os.path.exists(log_path):
    os.makedirs(log_path)

fastq_path=base_dir+"/fastq/"
if not os.path.exists(fastq_path):
    os.makedirs(fastq_path)

user_input=input("Enter SRA IDs as a line separated text file:")
assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
with open(user_input, 'r') as f:
        sra_ids=[line.strip() for line in f]

def download_sra(sra_ids):
    '''check if sra_path exists'''
    for id in sra_ids:
        print("Currently Downloading: " + id)
        prefetch = "prefetch -O "+sra_path + " " + id
        result=subprocess.run(prefetch, shell=True, capture_output=True)
        logfile=log_path+"sra.log"
        with open(logfile, 'a') as f:
            f.write(str(result)+"\n")

def sra_to_fasta(sra_ids):
    validation_path=base_dir +"/vdb_validate/"
    if not os.path.exists(validation_path):
        os.makedirs(validation_path)
    for counter, id in enumerate (sra_ids):
        if(counter<=521):
            continue
        sra_file= sra_path+id + "/" + id + ".sra"
        sralite_file=sra_path+id + "/" + id + ".sralite"
        vdb_out=validation_path+id+".vdb_out"

        if os.path.exists(sra_file):
            print("processing sra file",counter)
            vdb="vdb-validate " +sra_file+" >& "+vdb_out
            fastq_dump="fastq-dump  --skip-technical --split-spot --split-3 --clip --readids --read-filter pass --dumpbase "\
                                        + sra_file + " -O "+ fastq_path 
            result=subprocess.run(vdb, shell=True, capture_output=True, executable='/bin/bash')
            logfile=log_path+"vdb_SRA.log"
            with open(logfile, 'a') as f:
                f.write(str(result)+"\n")
            with open(vdb_out, 'r') as f:
                for line in f:
                    if "error" in line:
                            print("sra file is inconsistent: "+ id)
                result=subprocess.run(fastq_dump, shell=True, capture_output=True)
                logfile=log_path+"fastq-dump_log_SRA"
                with open(logfile, 'a') as f:
                    f.write(str(result)+"\n")
        elif os.path.exists(sralite_file):
            print("processing sralite file", counter)
            vdb="vdb-validate " +sralite_file+" >& "+vdb_out
            fastq_dump="fastq-dump  --skip-technical --split-spot --split-3 --clip --readids --read-filter pass --dumpbase "\
                      + sralite_file + " -O "+ fastq_path 
            result=subprocess.run(vdb, shell=True, capture_output=True, executable='/bin/bash')
            logfile=log_path+"vdb_SRALITE.log"
            with open(logfile, 'a') as f:
                    f.write(str(result)+"\n")
            with open(vdb_out, 'r') as f:
                for line in f:
                    if "error" in line:
                        print("sra file is inconsistent: "+ id)
            result=subprocess.run(fastq_dump, shell=True, capture_output=True)
            logfile=log_path+"fastq-dump_log_SRA"
            with open(logfile, 'a') as f:
                f.write(str(result)+"\n")

        else:
            print("sra not found:", counter)

def qc_fastq(sra_ids):
    qc_path=base_dir+"/fastp/"
    if not os.path.exists(qc_path):
        os.makedirs(qc_path)
    trimmed_fastq_path=base_dir+"/"+"trimmed_fastq/"
    if not os.path.exists(trimmed_fastq_path):
        os.makedirs(trimmed_fastq_path)
    for counter, id in enumerate(sra_ids):
        f1=id+"_pass_1.fastq"
        f2=id+"_pass_2.fastq"
        trim1="trimmed_"+f1
        trim2="trimmed_"+f2
        out1=id+"_fastp"+".html"
        out2=id+"_fastp"+".json"
        fastp="fastp --cut_right cut_right_mean_quality=30 cut_right_window_size=8 -c -i " + fastq_path+f1 + " -I " +fastq_path+f2 + \
                " -o "+trimmed_fastq_path+trim1 + " -O "+trimmed_fastq_path+trim2 + " -h "+qc_path+out1 + " -j "+qc_path+out2 
        result=subprocess.run(fastp, shell=True, executable="/bin/bash", capture_output=True)
        print("processing sra file:", counter)
        logfile=log_path+"fastp.log"
        with open(logfile, 'a') as f:
            f.write(str(result)+"\n")

#download_sra(sra_ids)
#sra_to_fasta(sra_ids)
qc_fastq(sra_ids)
