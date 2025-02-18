# Converters
def arrayToString(array):
    result = ''
    for i in array:
        result += i
    return result


def convertStringToArray(string, step):
    result = []
    n = 0
    carrier = ''
    for i in string:
        carrier += i
        n += 1
        if n >= step:
            result.append(carrier)
            carrier = ''
            n = 0
    return result


def decimalToSequenceDna(decimal):
    result = bin(decimal)
    result = binaryToSequenceDna(result[2:])
    return result


# Calculators
def hydrogenBridgeCountDna(sequence):
    result = 0
    for i in sequence:
        if i == 'A' or i == 'T':
            result += 2
        elif i == 'C' or i == 'G':
            result += 3
        else:
            pass
    return result


def denaturationTemperatureDna(sequence):
    result = hydrogenBridgeCountDna(sequence)
    return str(result) + '°C'


# Binary input: '100100110110'
def binaryToSequenceDna(binary):
    string = convertStringToArray(binary, 2)
    dictionary = {
        '00': 'A', '01': 'T',
        '10': 'G', '11': 'G'
    }
    result = ''
    for i in string:
        result += dictionary[i]
    return result


# DNA input: 'ATGC'
def transcriptionDnaToRna(sequence):
    result = ''
    for i in sequence:
        if i == 'T':
            result += 'U'
        else:
            result += i
    return result


# RNA input 'AUGC':
def checkIfStartcodonRna(sequence):
    return 'AUG' in str(sequence)


def checkIfStopcodonRna(sequence):
    return 'UGA' in sequence or 'UAA' in sequence or 'UAG' in sequence


def findStartcodonRna(sequence):
    if checkIfStartcodonRna(sequence):
        return sequence.find('AUG')
    else:
        return False


def findStopcodonRna(sequence):
    if checkIfStopcodonRna(sequence):
        carrier = [sequence.find('UGA'), sequence.find('UAA'), sequence.find('UAG')]
        result = []
        for i in carrier:
            if int(i) < 0:
                pass
            else:
                result.append(i)
        result.sort()
        return result[0]
    else:
        return False


def cutoffStartcodonRna(sequence):
    return sequence[findStartcodonRna(sequence) + 3:]


def orfRna(sequence):
    if checkIfStartcodonRna(sequence) == True and checkIfStopcodonRna(sequence) == True:
        result = cutoffStartcodonRna(sequence)
        result = result[:findStopcodonRna(result)]
        return result
    else:
        return False


def aminoacidsequenceRna(sequence):
    if checkIfStartcodonRna(sequence) == True and checkIfStopcodonRna(sequence) == True:
        result = convertStringToArray(orfRna(sequence), 3)
        return result


def translateRnaToAminonames(sequence):
    array = aminoacidsequenceRna(sequence)
    dictionary = {
        "GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
        "UGC": "C", "UGU": "C", "GAC": "D", "GAU": "D",
        "GAA": "E", "GAG": "E", "UUC": "F", "UUU": "F",
        "GGA": "G", "GGC": "G", "GGG": "G", "GGU": "G",
        "CAC": "H", "CAU": "H", "AUA": "I", "AUC": "I",
        "AUU": "I", "AAA": "K", "AAG": "K", "UUA": "L",
        "UUG": "L", "CUA": "L", "CUC": "L", "CUG": "L",
        "CUU": "L", "AUG": "M", "AAC": "N", "AAU": "N",
        "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
        "CAA": "Q", "CAG": "Q", "AGA": "R", "AGG": "R",
        "CGA": "R", "CGC": "R", "CGU": "R", "CGG": "R",
        "AGC": "S", "AGU": "S", "UCA": "S", "UCC": "S",
        "UCG": "S", "UCU": "S", "ACA": "T", "ACC": "T",
        "ACG": "T", "ACU": "T", "GUA": "V", "GUC": "V",
        "GUG": "V", "GUU": "V", "UGG": "W", "UAC": "Y",
        "UAU": "Y", "UAG": "!", "UAA": "!", "UGA": "!"
    }

    result = []
    for i in array:
        result.append(dictionary[i])
    return result
