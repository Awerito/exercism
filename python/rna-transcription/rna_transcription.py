def to_rna(dna_strand):
    
    dna_strand = dna_strand.upper()
    dna_strand = dna_strand.replace('A', 'U')
    dna_strand = dna_strand.replace('T', 'A')
    dna_strand = dna_strand.replace('G', 'X')
    dna_strand = dna_strand.replace('C', 'G')
    dna_strand = dna_strand.replace('X', 'C')

    return dna_strand
