# Dictionary to hold DNA sequences
dna_sequences = {}
def EXE(seq_var, promoter, direction='right', new_var=None):
    """
    Transcribes a promoter site from a DNA sequence variable at a given position and direction.
    """
    if seq_var in dna_sequences:
        sequence = dna_sequences[seq_var]
        # Find the position of the promoter in the sequence
        pos = sequence.find(promoter)
        if pos == -1:
            #Raise an Error if the Promoter wasnt found. 
            raise ValueError(f"Promoter {promoter} not found in sequence {seq_var}.")
        if direction == 'right':
            #If the direction is right, then output everything after the promoter
            transcribed_seq = sequence[pos + len(promoter):]
        elif direction == 'left':
            #If the direction is left, then output everything after the promoter
            transcribed_seq = sequence[:pos]
        else:
            #Bad Direction? No problem. It tells us
            raise ValueError("Invalid direction. Choose 'right' or 'left'.'")
        if new_var:
            #Lets create a new varaible just incase we want a different one
            VAR(new_var, transcribed_seq)
            return transcribed_seq
        else:
            #Otherwise, we just modify the varaible we are using
            dna_sequences[seq_var] = transcribed_seq
            return transcribed_seq
    else:
        #Raise an Error if variable is not found 
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
def REP(seq_var,custom_variable):
    """
    Replicates a DNA strand from a DNA sequence variable.
    """
    if seq_var in dna_sequences:
        sequence = dna_sequences[seq_var]
        replicated_seq = sequence + sequence
        dna_sequences[seq_var] = replicated_seq
        return replicated_seq
    else:
        raise ValueError(f"Variable {seq_var} not found.")
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
def DISP(seq_var):
    """
    Displays the result of a variable.
    """
    if seq_var in dna_sequences:
        print(dna_sequences[seq_var])
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

VAR("$Seq_1", "GATTATCTTTATATAATGCG")
EXE("$Seq_1","TAT",new_var="$New_Seq1")
PRO("$Seq_1")
DISP("$Seq_1")
DISP("$New_Seq1")
