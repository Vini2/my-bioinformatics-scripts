import subprocess

from collections import defaultdict

refs_folder = "Refs"
nthreads = 8
reads_file = "reads.fastq"
intermediate_file = "all_reads.paf"
output_file = "all_reads.output"
threshold = 0.5

# Concatenate all references
command = f"cat {refs_folder}/*.fna > refs.fna"
subprocess.run(command, shell=True)

# Run minimap2
command = f"minimap2 -t {nthreads} refs.fna {reads_file} > {intermediate_file}"
subprocess.run(command, shell=True)

contig_ref = defaultdict(list)
contig_ref_aln_length = defaultdict(list)
read_length = {}

# Read minimap2 result
for line in open(f"{intermediate_file}"):
    data = line.strip().split("\t")
    #     1	string	Query sequence name
    #     2	int	Query sequence length
    #     3	int	Query start (0-based; BED-like; closed)
    #     4	int	Query end (0-based; BED-like; open)
    #     5	char	Relative strand: "+" or "-"
    #     6	string	Target sequence name
    #     7	int	Target sequence length
    #     8	int	Target start on original strand (0-based)
    #     9	int	Target end on original strand (0-based)
    #     10	int	Number of residue matches
    #     11	int	Alignment block length
    #     12	int	Mapping quality (0-255; 255 for missing)

    qname = data[0]
    qlen = int(data[1])
    qstart = int(data[2])
    qqend = int(data[3])
    char = data[4]
    tname = data[5]
    tlen = int(data[6])
    tstart = int(data[7])
    aln_len = int(data[10])
    flag = int(data[11])

    # Make sure read is not paired and not unmapped
    if not flag == 255:
        contig_ref[qname].append(tname)
        contig_ref_aln_length[qname].append(aln_len)
        read_length[qname] = qlen

# Write mapping result to file
with open(f"{output_file}", "w+") as f:
    for k, v in contig_ref.items():
        best = None
        best_len = 0
        c_len = read_length[k]

        if len(v) > 1:
            align_sum = 0

            for ref, l in zip(contig_ref[k], contig_ref_aln_length[k]):
                align_sum += l

            if align_sum >= threshold * c_len and best_len < align_sum:
                best_len = align_sum
                best = ref

        elif contig_ref_aln_length[k][0] >= threshold * c_len:
            best = contig_ref[k][0]
            best_len = contig_ref_aln_length[k][0]
        else:
            best = "POOR MAPPING"
        f.write(f"{k}\t{best}\t{best_len}\n")