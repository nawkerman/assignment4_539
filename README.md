# CMB 539 Assignment 4

This project was designed to perform a data analysis on a DNA sequence in python. The type of analysis was specifically a summary of unique kmer counts as well as the linguistic complexity of any sequence entered via the console. The program will compile the observed unique kmers for that sequence along with the possible unique kmers and the range of k values into a dataframe in order to further process. Linguistic complexity can then be ascertained by dividing the sum of the observed kmer counts by the sum of the possible kmer counts. Additionally the data can be represented graphically.

## Files included in this repository

* assignment_4.py: the main program containing all of the necessary functions to produce the kmer dataframe and a representative graph. Takes two inputs at the command line, a file as input 1 and an integer greater than 1 as input 2.
* test_assignment4.py: a sub-program used to run the function in assignment_4.py through pytest to try to elimate any inputs that would confound the program
* text.txt: a test text file containing a string of nucleotides used to test the program on a potential sample
* README.md: this file explaining the repository contents
