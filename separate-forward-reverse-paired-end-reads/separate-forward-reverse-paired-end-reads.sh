# Separate forward reads
awk 'c-->0;$0~s{if(b)for(c=b+1;c>1;c--)print r[(NR-c+1)%b];print;c=a}b{r[NR%b]=$0}' b=0 a=3 s="/1" /path/to/combined/reads_file.fq > R1_fq

# Separate reverse reads
awk 'c-->0;$0~s{if(b)for(c=b+1;c>1;c--)print r[(NR-c+1)%b];print;c=a}b{r[NR%b]=$0}' b=0 a=3 s="/2" /path/to/combined/reads_file.fq > R2_fq

#b - before
#b - after
