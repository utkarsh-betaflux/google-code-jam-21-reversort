import fileinput 

def reverse_list(input_list):
    L = len(input_list)
    if L > 1:
        N = int((L)/2) if L%2 > 0 else int(L/2)
        for i in range(N):
            input_list[i], input_list[L-1-i] = input_list[L-1-i], input_list[i]
    return input_list

def calc_cost(L, test_case):
    cost=0
    for start_pos in range(L-1):
        num = test_case[start_pos]
        end_pos =  start_pos
        end_num = num
        
        for k in range(start_pos+1, L):
            next_num = test_case[k]
            if next_num < end_num:
                end_pos = k
                end_num = next_num
            
            # print(f"k={k}   num={num}   next_num={next_num}    end_pos={end_pos}   end_num={end_num}")
        
        to_be_reversed = test_case[start_pos: end_pos+1]
        # print(f"to_be_reversed: {to_be_reversed}")

        reversed_list = reverse_list(to_be_reversed)
        head = test_case[0:start_pos]
        tail = test_case[end_pos+1: L]
        # print(f"head: {head} reversed: {reversed_list}  tail:{tail}")

        test_case = head + reversed_list + tail
        
        i = start_pos + 1
        j = end_pos + 1
        c = j-i+1
        cost = cost + c

        # print(f"{test_case} i={i}   j={j}   c={c}\n")
    return cost

def get_clean_inputs(f):
    arr = []
    counter= T = int(f[0])
    i=1
    while counter > 0:
        single_input = [f[i], f[i+1]]
        single_input = [i[0:-1]if '\n' in i else i for i in single_input]
        arr.append(single_input)
        i+=2
        counter-=1
    return arr

def __main__():
    with fileinput.input() as f:
        arr = get_clean_inputs(f)
        
        for x, test_case_array in enumerate(arr):
            L, test_case = test_case_array
            L = int(L)
            
            test_case = test_case.split(' ')
            test_case = [int(num) for num in test_case]

            y = calc_cost(L, test_case)
            print(f"Case #{x+1}: {y}")

__main__()

