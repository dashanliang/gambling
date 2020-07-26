import numpy as np
import copy




def getValueByState(s, valuedatas):
    tmps = s -1
    # print(tmps)
    if tmps < 0:
        return 0
    if tmps == 99:
        return 1
    return valuedatas[s-1]

def eachvalueona(s, a, valuedatas):
    s_next = [s+ a, s-a]
    p = [0.4, 0.6]
    data = 0
    for i in [0, 1]:
        data = data + p[i] * (0 + getValueByState(s_next[i], valuedatas))
    return data

def getactionsfors(s):
    if s <= 100 -s:
        return np.arange(1, s+1, 1)
    else:
        return np.arange(1, 101-s, 1)

def getmaxdata(s, valuedatas, maxactions):
    actionsforcal = getactionsfors(s)
    tmp = 0
    action = 0
    for a in actionsforcal:
        if tmp <= eachvalueona(s, a, valuedatas):
            action = a
            tmp = eachvalueona(s, a, valuedatas)
    maxactions[s-1] = action
    print(tmp)
    return tmp


if __name__ == '__main__':
    valuedatas = np.zeros(99)
    # valuedatas[99] = 1
    actions = np.zeros(99)
    tmpvalues = np.zeros(99)
    tmpvalues = copy.deepcopy(valuedatas)
    # print(valuedatas)
    for j in np.arange(0, 200, 1):
        for i in np.arange(1, 100, 1):
            tmpvalues[i-1] = getmaxdata(i, valuedatas, actions)
        valuedatas = copy.deepcopy(tmpvalues)
    print(valuedatas)
    print(actions)

    # for i in np.arange(1, 100, 1):
    #     tmpvalues[i-1] = getmaxdata(i, valuedatas, actions)
    # valuedatas = copy.deepcopy(tmpvalues)
    # print(valuedatas)
        # print(actions)