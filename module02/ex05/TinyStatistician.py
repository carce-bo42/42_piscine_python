import numpy as np
import math as m

class TinyStatistician:

    def __init__(self) -> None:
        pass

    def numpy_clear(func):

        def convert_to_list(x):

            if isinstance(x, np.ndarray):
                x = list(x)
            
            return func(sorted(x))

        return convert_to_list

    @numpy_clear
    def mean(lst):
        return sum(lst) / len(lst)

    @numpy_clear
    def median(lst):
        low_idx = (len(lst) - 1) // 2
        if (len(lst) - 1) % 2 == 0:
            return lst[low_idx]
        else:
            return (lst[low_idx] + lst[low_idx + 1]) / 2.

    @numpy_clear
    def quartile(lst):
        idx = (len(lst) - 1) / 4.
        if (len(lst) - 1) % 4 == 0:
            return [lst[int(idx)], lst[3 * int(idx)]]
        else:
            return [(1 - idx) * lst[int(idx)] + idx * lst[int(idx) + 1], \
                    idx * lst[int(3 * idx)] + (1 - idx) * lst[(int(3 * idx)) + 1]]

    @numpy_clear
    def var(lst):
        mean = TinyStatistician.mean(lst)
        return sum(m.pow(value - mean, 2) for value in lst) / len(lst)
    
    @numpy_clear
    def std(lst):
        return m.sqrt(TinyStatistician.var(lst))

if __name__ == "__main__":
    lol = [1., 10., 42., 59.]
    print(np.quantile(lol, .25))
    print(np.quantile(lol, .5))
    print(np.quantile(lol, .75))

    print()
    print()

    print(TinyStatistician.mean(lol))
    print(TinyStatistician.median(lol))
    print(TinyStatistician.quartile(lol))
    print(TinyStatistician.var(lol))
    print(TinyStatistician.std(lol))

    print()
    print()

    a = np.array([1, 42, 300, 10, 59])
    print(TinyStatistician.mean(a))
    print(TinyStatistician.median(a))
    print(TinyStatistician.quartile(a))
    print(TinyStatistician.var(a))
    print(TinyStatistician.std(a))


