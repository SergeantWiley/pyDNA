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
        else:
            print("No common Factors found. Most likely a prime number")
    #Finding the most balanced combination
    for factor in combinations:
        differences = abs(factor[0] - factor[1])
        optimal_dimensions.append(differences)
    # Find and return the smallest differences
    index = optimal_dimensions.index(min(optimal_dimensions))
    return combinations[index]

def reshape(sequence,size_x=None,size_y=None,compression_auto=True):
    #Convert a sequence (1D string) into a matrix
    if compression_auto:
        #Auto find the best dimensions
        dimension1, dimension2 = dimension_auto(sequence)
        matrix = np.reshape(np.array(list(sequence)), (dimension1, dimension2))
        return matrix
    else:
        #Make sure manaul sizes do equal the legnth
        if not size_x*size_y == len(sequence):
            raise ValueError(f"Dimensions {size_x} x {size_y} do not equal to {len(sequence)}")
        matrix = np.reshape(np.array(list(sequence)), (size_x, size_y))
        return matrix

def extract(matrix,direction,value):
    #Grab a row
    if direction == "across":
        row = matrix[:, value]
        row_matrix = np.reshape(row, (len(row), 1))
        return row_matrix
    #Grab a column
    elif direction == "down":
        col = matrix[:, value]
        col_matrix = np.reshape(col, (len(col), 1))
        return col_matrix
    else:
        #Invalid direction returns the right terms
        print("Invalid Direction. use 'down' for verticle and 'across' for horizontal")

def naturalize(matrix,nucleotide_mapping=None,custom_values=False):
    #convert the nucleotides into numerical numbers
    if not custom_values:
        nucleotide_mapping = {'A': 1, 'T': 2, 'C': 3, 'G': 4}
    # Create a copy of the matrix to avoid modifying the original matrix
    matrix_copy = matrix.copy()
    for nucleotide, number in nucleotide_mapping.items():
        matrix_copy[matrix_copy == nucleotide] = number
    return matrix_copy

def sequence(data,type='seq'):
    if not isinstance(data,np.ndarray):
        raise ValueError("In order to decode sequence, data must be in numpy array")
    else:
        if type == 'seq':
            decoded_list = []
            for i in range(0,data.shape[1]):
                row = extract(data,'across',i)
                decoded_row = ''.join(row.flatten().tolist())
                decoded_list.append(decoded_row)
            decoded_sequence = ''.join(decoded_list)
            return decoded_sequence

def swap_type(matrix):
    if isinstance(matrix, pd.DataFrame):
        array = matrix.to_numpy()
        return array
    elif isinstance(matrix, np.ndarray):
        columns = [i for i in range(0, matrix.shape[1])]
        df = pd.DataFrame(matrix, columns=columns)
        return df

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

def reshape3D(DNA_Sequence,size_x,size_y,size_z):
    if len(DNA_Sequence) == size_x*size_y*size_z:
        pass
    else:
        raise ValueError(f"Dimensions {size_x} x {size_y} x {size_z} do not equal to {len(DNA_Sequence)}")
new_matrix = naturalize(compressed_matrix)
#new_matrix = swap_type(new_matrix)
swapped = swap_type(new_matrix)
print(new_matrix)
print(swapped)
swapped = swap_type(swapped)
print(swapped)