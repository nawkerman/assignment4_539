import pandas as pd
import sys


def kmer_count(k, example_seq):
    
    kmer = []
    observed = []
    possible = []
    
    #make "if k >= 1" function
    if k >=1:
        for i in example_seq:
            if k == 1 and len(example_seq) >= 4:
                possible.append(4)
            elif k == 1 and len(example_seq) < 4:
                possible.append(len(example_seq))
            elif len(example_seq) > 4**k:
                possible.append(4**k)
            elif len(example_seq) <= 4**k:
                possible.append((len(example_seq)-(k-1)))
            
            uniques = []
            frame = 0
            while frame < (len(example_seq)-(k-1)):
                if example_seq[frame:frame+k] not in uniques:
                    uniques.append(example_seq[frame:frame+k])
                frame=frame+1
            observed.append(len(uniques))
            
            
            kmer.append(k)
            k=k+1
    
        kmer.append("Total")
        observed.append(sum(observed))
        possible.append(sum(possible))
        
        k_frame = {"K": kmer,
                   "Observed kmers": observed,
                   "Possible kmers": possible}
        
        
        
        K_data = pd.DataFrame(k_frame)
        return (K_data)
    else: 
        print ("Please use a value that is 1 or greater!") 


def plot_data(dataframe):
    dsa

def linguistic_complexity(dataframe):
    if dataframe.iloc[-1,2] > 0:
        return (dataframe.iloc[-1,1]/dataframe.iloc[-1,2])

    
seq = "ATTTGGATT"
k = 1
dataframe = (kmer_count(k, seq))
complexity = linguistic_complexity(dataframe)

print (complexity)
    
        