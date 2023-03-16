
class Evaluator:

    def __init__(self) -> None:
        pass

    def zip_evaluate(coefs, words) -> int:
        if type(words) is not list \
            or type(words[0]) is not str \
            or type(coefs) is not list \
            or type(coefs[0]) is not float \
            or len(words) is not len(coefs):
            return -1
        else:
            lst = list(zip(words, coefs))
            return sum(len(c[0]) * c[1] for c in lst)

    def enumerate_evaluate(coefs, words) -> int:
        if type(words) is not list \
            or type(coefs) is not list \
            or len(words) is not len(coefs):
            return -1
        else:
            return sum(len(words[idx]) * weight for idx, weight in enumerate(coefs))