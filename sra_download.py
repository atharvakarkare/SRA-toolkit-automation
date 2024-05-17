############# download sratoolkit using conda and set download dir using vdb-config -i #######################

import subprocess


def read_sra_numbers(file_path):
    sra_numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            sra_numbers.append(line.strip())
    return sra_numbers

########### Add path to you id file here #################
file_path = "/path/to/your/IDs/"
sra_numbers = read_sra_numbers(file_path)
print(sra_numbers)

# this will download the .sra files to  /sra
for sra_id in sra_numbers:
    print ("Currently downloading: " + sra_id)
    prefetch = "prefetch " + sra_id
    print ("The command used was: " + prefetch)
    subprocess.call(prefetch, shell=True)

# this will extract the .sra files 
for sra_id in sra_numbers:
    print ("Generating fastq for: " + sra_id)
    fastq_dump = "fasterq-dump /path/to/sra/files/" + sra_id + ".sra"  ##change the path accordingly
    print ("The command used was: " + fastq_dump)
    subprocess.call(fastq_dump, shell=True)

# this will gzip the fastq files

for sra_id in sra_numbers:
    print ("Gzipping fastq for: " + sra_id)
    gzip1 = "gzip" + " " + sra_id + "_1.fastq"
    print ("The command used was: " + gzip1)
    subprocess.call(gzip1, shell=True)

for sra_id in sra_numbers:
    print ("Gzipping fastq for: " + sra_id)
    gzip2 = "gzip" + " " + sra_id + "_2.fastq"
    print ("The command used was: " + gzip2)
    subprocess.call(gzip2, shell=True)


################## moving gzip files to fq_files ####################
dir = "mkdir fq_files"
subprocess.call(dir, shell=True)

for sra_id in sra_numbers:
    print ("Moving gzip files:" + sra_id)
    move = "mv" + " " + sra_id + "_1.fastq.gz /path/to/fq_files/"      ## change the path
    print ("The command used was: " + move)
    move2 = "mv" + " " + sra_id + "_2.fastq.gz /path/to/fq_files/"     ## change the path
    print ("The command used was: " + move2)
    subprocess.call(move, shell=True)
    subprocess.call(move2, shell=True)
