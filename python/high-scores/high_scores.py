def latest(scores):

    return scores[-1]


def personal_best(scores):

    aux = scores.copy()
    aux.sort(reverse=True)
    return aux[0]


def personal_top_three(scores):
    
    aux = scores.copy()
    aux.sort(reverse=True)
    return aux[:3]
