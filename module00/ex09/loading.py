import time

# (1) Computations that must be done at first but dont need to
#     be repeated on each call are saved.

def ft_progress(list):

    for val in list:
        progress_bar = ""
        progress_bar += "ETA: "
        
        if list.index(val) == 0: # (1)
            expected_time = time.time()
            for k in list:
                time.sleep(0.01) # Simulate doing a few calculations
            expected_time = time.time() - expected_time
            yield expected_time

            time_passed = time.time()
            yield time_passed

        # Write ETA: 
        progress_bar += "{:.2f}".format(expected_time)

        # Write PROGRESS BAR
        progress_bar += "s ["
        
        # <index of val> / length of list E [0, 1]
        # floor (<index of val> / length of list) == <index of val> // length of list E [0, 10]
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
        progress_bar += f'{(time.time() - time_passed):.2f}s'

        print("\r", progress_bar, end='')
        yield val

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)

print()
print(ret)
