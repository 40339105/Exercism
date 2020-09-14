rna_compliments = {
    'G' : 'C',
    'C' : 'G',
    'T' : 'A',
    'A' : 'U'
}

def to_rna(dna_strand):
    rna_compliment = ""
    for dna in dna_strand:
        rna_compliment += rna_compliments[dna]
    return rna_compliment
