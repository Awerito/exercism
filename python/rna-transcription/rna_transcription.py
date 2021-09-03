def to_rna(dna_strand):

    dna_strand = (
        dna_strand.upper()
        .replace("A", "U")
        .replace("T", "A")
        .replace("G", "X")
        .replace("C", "G")
        .replace("X", "C")
    )

    return dna_strand
