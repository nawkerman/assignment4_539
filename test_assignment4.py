import pytest
from assignment_4 import *

def test_count():
    example_seq = "ATTTGGATT"
    k=1
    dictionary = {"K": [1, 2, 3, 4, 5, 6, 7, 8, 9, "Total"],
                  "Observed kmers": [3, 5, 6, 6, 5, 4, 3, 2, 1, 35],
                  "Possible kmers": [4, 8, 7, 6, 5, 4, 3, 2, 1, 40]
                  }
    expected_frame = pd.DataFrame(dictionary)
    assert expected_frame.equals(kmer_count(k, example_seq))
    
def test_count2():
    example_seq = "ATTTGGATT"
    k=4
    dictionary = {"K": [4, 5, 6, 7, 8, 9, "Total"],
                  "Observed kmers": [6, 5, 4, 3, 2, 1, 21],
                  "Possible kmers": [6, 5, 4, 3, 2, 1, 21]
                  }
    expected_frame = pd.DataFrame(dictionary)
    assert expected_frame.equals(kmer_count(k, example_seq))
    
def test_count3():
    example_seq = ""
    k=1
    dictionary = {"K": ["Total"],
                  "Observed kmers": [0],
                  "Possible kmers": [0]
                  }
    expected_frame = pd.DataFrame(dictionary)
    assert expected_frame.equals(kmer_count(k, example_seq))
    
def test_complexity():
    dictionary = {"K": ["Total"],
                  "Observed kmers": [0],
                  "Possible kmers": [0]
                  }
    frame = pd.DataFrame(dictionary)
    expected_complexity = "Denominator is equivalent to zero meaning string is empty. Please try again."
    assert expected_complexity == linguistic_complexity(frame)
    
    
test_count()
test_count2()
test_count3()
test_complexity()
