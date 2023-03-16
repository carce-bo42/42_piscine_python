from collections.abc import Iterable

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if isinstance(iterable, Iterable):
        try:
            res = function_to_apply(iterable[0], iterable[1])
            for x in iterable[2:]:
                res = function_to_apply(res, x)
            return res
        except Exception as e:
            print(f'ft_reduce: {str(e)}')
    else:
        raise TypeError(f'{type(iterable)} is not iterable')