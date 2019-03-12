awk '/^>/{print ">Sequence_" ++i; next}{print}' < path/to/file.fasta > path/to/new_file.fasta
