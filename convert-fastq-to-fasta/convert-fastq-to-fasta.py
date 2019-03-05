from Bio import SeqIO

with open("path/to/fastq/file.fastq", "r") as input_handle:
    with open("path/to/fasta/file.fasta", "w") as output_handle:
        sequences = SeqIO.parse(input_handle, "fastq")
        count = SeqIO.write(sequences, output_handle, "fasta")
        
print("Converted %i records" % count)
