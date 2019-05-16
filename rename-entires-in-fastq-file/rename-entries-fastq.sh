awk '/^@Start_Seq_In_File/{print "@Your_Sequence_" ++i; next}{print}' < path/to/file.fastq > path/to/new_file.fastq
