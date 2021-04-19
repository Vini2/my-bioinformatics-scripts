# Source: https://bioinformatics.stackexchange.com/questions/4911/calculating-read-average-length-in-a-fastq-file-with-bioawk-awk/4918

awk '{if(NR%4==2) {count++; bases += length} } END{print bases/count}' <fastq_file>
