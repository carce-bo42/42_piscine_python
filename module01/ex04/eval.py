
class Evaluator:

    def __init__(self) -> None:
        pass

    def zip_evaluate(coefs, words) -> int:
        if type(words) != list \
            or type(words[0]) != str \
            or type(coefs) != list \
            or type(coefs[0]) != float \
            or len(words) != len(coefs):
            return -1
        else:
            lst = list(zip(words, coefs))
            return sum(len(c[0]) * c[1] for c in lst)

    def enumerate_evaluate(coefs, words) -> int:
        if type(words) != list \
            or type(coefs) != list \
            or len(words) != len(coefs):
            return -1
        else:
            return sum(len(words[idx]) * weight for (idx, weight) in enumerate(coefs))