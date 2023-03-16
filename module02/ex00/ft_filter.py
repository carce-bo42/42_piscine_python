from collections.abc import Iterable

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if isinstance(iterable, Iterable):
        try:
            for x in iterable:
                if function_to_apply(x):
                    yield x
                else:
                    continue
        except Exception as e:
            print(f'ft_filter: {str(e)}')
    else:
        raise TypeError(f'{type(iterable)} is not iterable')