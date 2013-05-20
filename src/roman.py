_literals = {
    5: 'V',
    1: 'I'
}

def roman(arabic):
    if arabic == 0:
        return ''

    def small_enough(x): return arabic >= x
    max_fitting_literal = max(filter(small_enough, _literals.keys()))
    return _literals[max_fitting_literal] + roman(arabic - max_fitting_literal)

