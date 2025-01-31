import dnaClass

sequence = '100001101111111101010101010101110101111bz1101101010101101011110110111011011100111100111111101010101011101010101010111100010100100001010'

dna = dnaClass.binaryToSequenceDna(sequence)
print(dna)
rna = dnaClass.transcriptionDnaToRna(dna)
print(rna)
print(dnaClass.orfRna(rna))
print(dnaClass.translateRnaToAminonames(rna))
