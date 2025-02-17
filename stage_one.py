print("\nTask 1:Translating DNA to Protein")

dna = '''
CCGAGTTTACAACTCCCAAACCCAATGTGAACGTTACCAAACTGTTGCCTCGGCGGGGTCACGCCCCGGG
TGCGTCGCAGCCCCGGAACCAGGCGCCCGCCGGAGGAACCAACCAAACTCTTTCTGTAGTCCCCTCGCGG
ACGTATTTCTTTACAGCTCTGAGCAAAAATTCAAAATGAATCAAAACTTTCAACAACGGATCTCTTGGTT
CTGGCATCGATGAAGAACGCAGCGAAATGCGATAAGTAATGTGAATTGCAGAATTCAGTGAATCATCGAA
TCTTTGAACGCACATTGCGCCCGCCAGTATTCTGGCGGGCATGCCTGTCCGAGCGTCATTTCAACCCTCG
AACCCCTCCGGGGGATCGGCGTTGGGGATCGGGACCCCTCACACGGGTGCCGGCCCCTAAATACAGTGGC
GGTCTCGCCGCAGCCTCTCCTGCGCAGTAGTTTGCACAACTCGCACCGGGAGCGCGGCGCGTCCACGTCC
GTAAAACACCCAACTTTCTG
'''
dna_seq = dna.replace("\n", "") #to remove the new lines in the dna sequence 
print(f"\nThe DNA sequence of Trichoderma asperellum is: \n{dna_seq}")

#to translate to protein


DNA_Codons = {
    # 'M' - START, '*' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "*", "TAG": "*", "TGA": "*"
}
protein = ""
for i in range(0, len(dna_seq), 3):
    codon = dna_seq[i:i+3]
    protein = protein + DNA_Codons[codon]

print(f"\nThe translated protein is: \n{protein}\n")

#Task 2: Calculating the logistic curve 

def logistic_growth(initial_population, max_population, growth_rate, time, t_lag):
    population = initial_population
    for hour in range(time):
        population = max_population / (1 + (2.71828 ** (-growth_rate*(hour - t_lag))))
        print(f"Hour {hour + 1}: Population = {population:.2f}")
    return population



print("Task 2 \n ")
logistic_growth(0,100,1.5,20, 10)



 #Task 4 - Calculate the hamming distance
print(f"\nTask 4: Calculating the Hammind Distance")
slack_username = "AS-Lateefat"
twitter_handle = "SA_Lateefat"
def hamming_distance(slack_username, twitter_handle):
    distance = 0
    for position in range(len(slack_username)):
        if slack_username[position] != twitter_handle[position]:
            distance += 1
    return distance

print(f'The hamming distance between the Slack Username and the Twitter handle is: {hamming_distance(slack_username, twitter_handle)}')

'''
Link to Members Github
Lateefat Shuaib: https://github.com/LateefatSA/hackbio-biocoding-internship/
Pelumi: https://github.com/Akinsete07/Hackbio_Biocoding_Internship.git
Damilola: https://github.com/DamilolaeO/hackbio-biocoding-internship
'''


