
def analyze_dna(sequence):

    sequence = sequence.upper()

    valid_bases = "ATGC"

    # Check whether sequence is valid
    for base in sequence:
        if base not in valid_bases:
            print("Invalid DNA sequence!")
            return

    # Count nucleotides
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    # Calculate length
    length = len(sequence)

    # Calculate GC percentage
    if length > 0:
        gc_percentage = ((g_count + c_count) / length) * 100
    else:
        gc_percentage = 0

    # Complementary strand
    complement = sequence.translate(
        str.maketrans("ATGC", "TACG")
    )

    # Reverse complement
    reverse_complement = complement[::-1]

    # Display results
    print("DNA SEQUENCE ANALYSIS")
    print("---------------------")
    print("Sequence:", sequence)
    print("Length:", length)
    print("A count:", a_count)
    print("T count:", t_count)
    print("G count:", g_count)
    print("C count:", c_count)
    print("GC percentage:", round(gc_percentage, 2), "%")
    print("Complement:", complement)
    print("Reverse complement:", reverse_complement)


dna = input("Enter a DNA sequence: ")

analyze_dna(dna)
