import numpy as np
import pandas as pd
DNA_Sequence = "AAATTAATTTTAACCCCAATTAAGGTTTTCTAATAATAAATTAATCCAATAATTTAAGTGCTAACTTATTAAGGATTAATTAATAATTAATCCAATAATATTAACCAATAATATTAACCTAAGGATTAATTAATAATATTAACCAATAAT"
#Sample DNA
def dimension_auto(n):
    combinations = []
    optimal_dimensions = []
    # Validate input sequence
    valid_nucleotides = set('ATCG')
    if not set(n).issubset(valid_nucleotides):
        raise ValueError("Invalid DNA sequence. Only 'A', 'T', 'C', 'G' are allowed.")
    #Finding the common factors
    for i in range(1, len(n) + 1):  # Include the length of the sequence
        if len(n) % i == 0:
            factor = [i, len(n) // i]
            combinations.append(factor)
    #Finding the most balanced combination
    for factor in combinations:
        differences = abs(factor[0] - factor[1])
        optimal_dimensions.append(differences)
    
    index = optimal_dimensions.index(min(optimal_dimensions))
    return combinations[index]

def reshape(sequence,size_x=None,size_y=None,compression_auto=True):
    if compression_auto:
        dimension1, dimension2 = dimension_auto(sequence)
        matrix = np.reshape(np.array(list(sequence)), (dimension1, dimension2))
        return matrix
    else:
        if not size_x*size_y == len(sequence):
            raise ValueError(f"Dimensions {size_x} x {size_y} do not equal to {len(sequence)}")
        matrix = np.reshape(np.array(list(sequence)), (size_x, size_y))
        return matrix

def extract(matrix,direction,value):
    if direction == "across":
        row = matrix[:, value]
        row_matrix = np.reshape(row, (len(row), 1))
        return row_matrix
    elif direction == "down":
        col = matrix[:, value]
        col_matrix = np.reshape(col, (len(col), 1))
        return col_matrix
    else:
        print("Invalid Direction. use 'down' for verticle and 'across' for horizontal")

def naturalize(matrix,nucleotide_mapping=None,custom_values=False):
    if not custom_values:
        nucleotide_mapping = {'A': 1, 'T': 2, 'C': 3, 'G': 4}
    # Create a copy of the matrix to avoid modifying the original matrix
    matrix_copy = matrix.copy()
    for nucleotide, number in nucleotide_mapping.items():
        matrix_copy[matrix_copy == nucleotide] = number
    return matrix_copy

def decode(data,type='df'):
    if type == 'numerical':
        nucleotide_mapping = {1: 'A', 2: 'T', 3: 'A', 4: 'G'}
        data.replace(nucleotide_mapping, inplace=True)
        return data
    elif type == 'seq':
        decoded_list = []
        for i in range(0,data.shape[1]):
            row = extract(data,'across',i)
            decoded_row = ''.join(row.flatten().tolist())
            decoded_list.append(decoded_row)
        print(decoded_list)
        decoded_sequence = ''.join(decoded_list)
        return decoded_sequence
  
def nucleotide_frequency(matrix,nucleotide_mapping=None,custom_values=False):
    if not custom_values:
        nucleotides = ['A','T','C','G']
    else:
        nucleotides = nucleotide_mapping
    frequency_dict = {}
    for nucleotide in nucleotides:
        frequency = np.count_nonzero(matrix == nucleotide)
        frequency_dict[nucleotide] = frequency
    frequency_series = pd.Series(frequency_dict)
    return frequency_series

compressed_matrix = reshape(DNA_Sequence,10,15,compression_auto=False)
series = nucleotide_frequency(compressed_matrix)
print(series)
new_matrix = naturalize(compressed_matrix)
print(new_matrix)
print()
print(decode(new_matrix,'seq'))