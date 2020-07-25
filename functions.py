# get the value of state s, when action is a

def srpossibilityonsa(s, r, sa, a):
    possibility = 0.0
    if s == sa + a and r == a:
        possibility = 0.4
    if s == sa - a and r == a:
        possibility = 0.6

    return possibility


def eachvalueona(s, a):
    r = [a, -a]
    s_next = [s+ a, s-a]
    data = 0
    for i in [0, 1]:
        data = data + srpossibilityonsa(s_next[i], r[i], s, a)

    return data
