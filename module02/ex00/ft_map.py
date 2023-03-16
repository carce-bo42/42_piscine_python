from collections.abc import Iterable

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
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
                yield function_to_apply(x)
        except Exception as e:
            print(f'ft_map: {str(e)}')
    else:
        raise TypeError(f'{type(iterable)} is not iterable')        
