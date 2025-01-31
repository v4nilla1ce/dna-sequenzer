# DNA Sequence Analysis and Manipulation

## Overview
This Python project provides tools for working with DNA sequences. It includes functionalities for converting between DNA and binary representations, transcribing DNA to RNA, detecting open reading frames (ORFs), and translating RNA into amino acid sequences. These processes are fundamental in bioinformatics and genetic analysis.

## Features
- **Binary to DNA Conversion**: Convert binary strings into DNA sequences.
- **DNA Transcription**: Convert DNA sequences to RNA sequences.
- **Open Reading Frame (ORF) Detection**: Identify regions in RNA sequences that can code for proteins.
- **RNA Translation**: Convert RNA sequences into amino acid names based on genetic code translation.

## Installation
Ensure you have Python installed (version 3.x recommended). Clone this repository and navigate to the project directory.

```bash
git clone <repository_url>
cd <project_directory>
```

No additional dependencies are required for basic usage.

## Usage
Run the main script to perform DNA sequence operations.

```bash
python main.py
```

### Example
An example of using the project:

```python
import dnaClass

sequence = "100001101111111101010101010101110101111bz1101101010101101011110110111011011100111100111111101010101011101010101010111100010100100001010"

dna = dnaClass.binaryToSequenceDna(sequence)
print("DNA Sequence:", dna)

rna = dnaClass.transcriptionDnaToRna(dna)
print("RNA Sequence:", rna)

orf = dnaClass.orfRna(rna)
print("Open Reading Frames:", orf)

amino_acids = dnaClass.translateRnaToAminonames(rna)
print("Amino Acid Sequence:", amino_acids)
```

## Background Information
### DNA and RNA
DNA (Deoxyribonucleic Acid) is the genetic material of most organisms, consisting of nucleotide bases: Adenine (A), Cytosine (C), Guanine (G), and Thymine (T). RNA (Ribonucleic Acid) is a transcribed version of DNA where Thymine (T) is replaced by Uracil (U).

### Transcription and Translation
- **Transcription**: DNA is transcribed into RNA by replacing Thymine (T) with Uracil (U).
- **Translation**: RNA sequences are translated into amino acids using codon mapping, which determines protein synthesis.

### Open Reading Frames (ORFs)
An ORF is a sequence in RNA that has the potential to code for proteins. It starts with a start codon (AUG) and ends with a stop codon (UAA, UAG, UGA).

## Contributing
Feel free to submit pull requests for improvements or additional features.

## License
This project is licensed under the MIT License.
