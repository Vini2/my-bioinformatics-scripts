from Bio import SeqIO

for index, record in enumerate(SeqIO.parse("path/to/fasta/file.fasta", "fasta")):
    filename = "path/to/individual/files/"+str(record.id)+".fasta"
#         if len(record.seq) >= 1000:
    SeqIO.write(record, filename, "fasta")
    length.append(len(record.seq))
#         else:
#             tooshort.write(record.name + "\t" + str(len(record.seq))+"\n")
