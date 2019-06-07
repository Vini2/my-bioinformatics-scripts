from Bio import SeqIO

ids = set(x[:-1] for x in open(path+"list.lst"))

with open(path+'list.fq', mode='a') as read_bin1:
    
    for seq in SeqIO.parse(path+"sequences.fq", "fastq"):

        if seq.id in ids: 
            read_bin1.write(seq.format("fastq"))
