#For separating paired end reads generated from MetaSim

from Bio import SeqIO

with open("read_1.fasta", "w") as read1:
    with open("read_2.fasta", "w") as read2:
        for index, record in enumerate(SeqIO.parse("path/to/paired-end/reads/file.fna", "fasta")):
            if "bw" in record.description:
                SeqIO.write(record, read2, "fasta")
            elif "fw" in record.description:
                SeqIO.write(record, read1, "fasta")
