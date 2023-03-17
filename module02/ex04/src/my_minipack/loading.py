import time

# (1) Computations that must be done at first but dont need to
#     be repeated on each call are saved.

def ft_progress(list):

    for val in list:
        progress_bar = ""
        progress_bar += "ETA: "
        
        if list.index(val) == 0: # (1)
            expected_time = 0. + (0.01 * len(list)) # Simulate doing a few calculations
            start_time = time.time()

        # Write ETA: 
        progress_bar += "{:.2f}".format(expected_time)

        # Write PROGRESS BAR
        progress_bar += "s ["
        
        # <index of val> / len(list) E [0, 1]
        # floor (<index of val> * k / len(list)
        #           == <index of val> * k // len(list) E [0, k]
        number_of_progress_lines = (list.index(val) * 30 // len(list))
        for x in range(number_of_progress_lines):
            progress_bar += "="
        progress_bar += ">"
        for x in range(number_of_progress_lines, 29):
            progress_bar += " "
        progress_bar += "] "

        # Write fraction of iterations/total
        progress_bar += f'{list.index(val) + 1}/{len(list)}'

        progress_bar += ' | '
        progress_bar += "elapsed time: "
        progress_bar += f'{(time.time() - start_time):.2f}s'

        print("\r", progress_bar, end='')
        yield val

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)

print()
print(ret)
