# Given DNA index dictionary
import torch

dna_index = {
    'AAA': 'if', 'AAT': 'elif', 'ATA': 'else',
    'TTT': 'global_o2', 'TTA': 'global_co2', 'TAT': 'plant_pop', 'TAC': 'animal_pop',
    'CCC': '>', 'CCA': '<', 'CAA': '=', 'CAT': '==', 'CAC': '>=', 'CAG': '<=',
    'CCT': '+', 'CTA': '-', 'CTT': '*', 'CTC': '/', 'CTG': '%', 'CCG': '**', 'CGA': '//',
    'GGG': '0', 'GGA': '1', 'GAA': '2', 'GAT': '3', 'GAC': '4', 'GAG': '5', 'GGT': '6',
    'GTA': '7', 'GTT': '8', 'GTC': '9', 'UUU': ':', 'UUA': '(', 'UUT': ')', 'UUC': '\n', 'UUG': '\t',
    'UAU': '"', 'UAA': ' '
}

# Python code to encode
python_code = """if global_o2 >= 1:
    global_o2 = global_o2 - 1
    global_co2 = global_co2 + 1
    plant_pop = plant_pop + 1"""

# Encode the Python code into DNA sequence
def encode_DNA(python_code):
    dna_sequence = ""
    i = 0
    while i < len(python_code):
        found = False
        for key, value in dna_index.items():
            if python_code[i:i+len(value)] == value:
                dna_sequence += key
                i += len(value)
                found = True
                break
        if not found:
            i += 1
    
    return dna_sequence

def decode_DNA(dna_sequence):
    i = 0
    decoded_sequence = ""
    while i < len(dna_sequence):
        found = False
        for key, value in dna_index.items():
            if dna_sequence[i:i+len(key)] == key:
                decoded_sequence += value + ""
                i += len(key)
                found = True
                break
        if not found:
            i += 1
    return decoded_sequence

dna_sequence = encode_DNA(python_code)
decoded_sequence = decode_DNA(dna_sequence)

print(dna_sequence)
print(decoded_sequence)
