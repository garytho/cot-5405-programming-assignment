import random
import time

def bwt(input_text):

    n = len(input_text)
    sorted_rotations = sorted([input_text[i:n]+input_text[0:i] for i in range(n)])
    index = sorted_rotations.index(input_text)
    final_column = ''.join([rotation[-1] for rotation in sorted_rotations])
    return (index, final_column)



def evaluate_time_complexity():
    n_vals = [100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000]
    alphabet = "abcde"
     
    for n in n_vals:
        input_text = ''.join(random.choice(alphabet) for i in range(n))
        start_time = time.time()
        _ = bwt(input_text)
        print(time.time() - start_time)
        


def find_h_index(text):
    h = 1
    while True:
        if text.count("a" * h) >= h or text.count("b" * h) >= h or text.count("c" * h) >= h  or text.count("d" * h) >= h or text.count("e" * h) >= h:
            h += 1
        else:
            return h - 1
        

def h_index_evaluation():
    n_vals = [100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000, 40000, 45000, 50000]
    alphabet = "abcde"
     
    for n in n_vals:
        input_text = ''.join(random.choice(alphabet) for i in range(n))
        _, bwt_out = bwt(input_text)
        h1 = find_h_index(input_text)
        h2 = find_h_index(bwt_out)
        print(h1, h2)

h_index_evaluation()
    
    