import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

def main():
    seq = ""
    #with open(myfile,'r') as current_file:
        #seq = current_file.read()  
        
    seq = seq.upper()
    k = 1
    dataframe = (kmer_count(k, seq))
    print (dataframe)
    complexity = linguistic_complexity(dataframe)
    print ("The linguistic complexity of the data is", complexity)
    plot_data(dataframe)    


def kmer_count(k, example_seq):
    
    kmer = []
    observed = []
    possible = []
    
    if k >=1:
        while k <= len(example_seq):
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
        return ("Please use a k of length between 1 and the length of your sequence! Also use a string longer than 0 characters.") 


def plot_data(dataframe):
    if len(dataframe.index)-1 >=1:
        fig, ax = plt.subplots()
    
        index = np.arange((len(dataframe.index)-2))
        bar_width = 0.35
        
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        
        observed = np.array(dataframe.iloc[0:(len(dataframe.index)-2), 1].tolist())
        possible = np.array(dataframe.iloc[0:(len(dataframe.index)-2), 2].tolist())
        k = np.array(dataframe.iloc[0:(len(dataframe.index)-2), 0].tolist())
        
        rects1 = ax.bar(index, observed, bar_width,
                        alpha=opacity, color='b',
                        label='Observed')   
        
        rects2 = ax.bar(index + bar_width, possible, bar_width,
                        alpha=opacity, color='r',
                        label='Possible')
        
        ax.set_xlabel('Type')
        ax.set_ylabel('Count')
        ax.set_title('Observed kmers Compared to Possible kmers at each Value k')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(k)
        ax.legend()
        
        fig.tight_layout()
        plt.show()    

def linguistic_complexity(dataframe):
    if dataframe.iloc[-1,2] > 0:
        return (dataframe.iloc[-1,1]/dataframe.iloc[-1,2])
    else: 
        return ("Denominator is equivalent to zero meaning string is empty. Please try again.")

if __name__ == "__main__":
    main()
