# Dictionary to hold DNA sequences
dna_sequences = {}
def EXE(seq_var, promoter, direction='right', new_var=None):
    """
    Transcribes a promoter site from a DNA sequence variable at a given position and direction.
    Converts DNA to RNA by replacing T with U and inverting nucleotides.
    """
    if seq_var in dna_sequences:
        sequence = dna_sequences[seq_var]
        
        # Find the position of the promoter in the sequence
        pos = sequence.find(promoter)
        
        if pos == -1:
            raise ValueError(f"Promoter {promoter} not found in sequence {seq_var}.")
        
        # Define nucleotide complement dictionary
        complement = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
        
        # Transcribe the sequence based on direction
        if direction == 'right':
            transcribed_seq = sequence[pos + len(promoter):]
        elif direction == 'left':
            transcribed_seq = sequence[:pos]
        else:
            raise ValueError("Invalid direction. Choose 'right' or 'left'.")
        
        # Replace T with U and invert nucleotides
        transcribed_seq = ''.join(complement.get(base, base) for base in transcribed_seq)
        
        # Store the transcribed sequence in a new variable if specified
        if new_var:
            VAR(new_var, transcribed_seq)
            return transcribed_seq
        else:
            dna_sequences[seq_var] = transcribed_seq
            return transcribed_seq
    else:
        raise ValueError(f"Variable {seq_var} not found.")

def SLICE(seq_var, start, end):
    """
    Extracts a slice of DNA from a DNA sequence variable.
    """
    if seq_var in dna_sequences:
        #Get the entire Sequence
        sequence = dna_sequences[seq_var]
        #Seperate the sliced parts
        sliced_seq = sequence[start:end]
        return sliced_seq
    else:
        raise ValueError(f"Variable {seq_var} not found.")
def DNA(seq):
    """
    Returns a DNA sequence.
    """
    return seq
def REP(seq_var,custom_variable,comp=False,rna=False):
    """
    Replicates a DNA strand from a DNA sequence variable.
    """
    if not comp:
        result = DISP(seq_var,giveback=True)
        VAR(custom_variable, result)
    else:
        if not rna:
            complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            result = DISP(seq_var,giveback=True)
            complement_seq = ''.join(complement.get(base, base) for base in result)
            VAR(custom_variable, complement_seq)
        else:
            complement = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
            result = DISP(seq_var,giveback=True)
            complement_seq = ''.join(complement.get(base, base) for base in result)
            VAR(custom_variable, complement_seq)
def PRO(seq_var):
    """
    Converts mRNA into a protein from a DNA sequence variable.
    """
    if seq_var in dna_sequences:
        sequence = dna_sequences[seq_var]
        # Placeholder for protein translation logic
        protein_seq = sequence.replace('T', 'U').replace('A', 'X').replace('C', 'Y').replace('G', 'Z')
        dna_sequences[seq_var] = protein_seq
        return protein_seq
    else:
        raise ValueError(f"Variable {seq_var} not found.")
def VAR(var_name, seq):
    """
    Creates or updates a variable with a DNA sequence.
    """
    dna_sequences[var_name] = seq
def DISP(seq_var,giveback=False):
    """
    Displays the result of a variable.
    """
    if not giveback:
        if seq_var in dna_sequences:
            print(dna_sequences[seq_var])
        else:
            raise ValueError(f"Variable {seq_var} not found.")
    else:
        if seq_var in dna_sequences:
            return dna_sequences[seq_var]
        else:
            raise ValueError(f"Variable {seq_var} not found.")
def MERGE(seq_var1, seq_var2):
    """
    Merges two sequences from DNA sequence variables.
    """
    if seq_var1 in dna_sequences and seq_var2 in dna_sequences:
        merged_seq = dna_sequences[seq_var1] + dna_sequences[seq_var2]
        dna_sequences[seq_var1] = merged_seq
        return merged_seq
    else:
        raise ValueError(f"One or more variables not found.")
# Example usage
# Example 1: Transcribe and make new sequence

VAR("$Seq_1", "TATGATTATCTTTATATAATGCG")
VAR("$Seq_2", "TATGATTATCTTTATATAATGCG")
EXE("$Seq_2","TAT")
EXE("$Seq_1","TAT",new_var="$RNA")
MERGE("$Seq_1","$Seq_2")
DISP("$Seq_1")
DISP("$Seq_2")
DISP("$RNA")
PRO("$RNA")
REP("$Seq_1","$return",comp=True,rna=True)
DISP("$return")
#PRO("$Seq_1")
