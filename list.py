def addtwonumbers(l1,l2):
    newl1 = l1.reverse()
    newl2 = l2.reverse()
    outcome = []
    for i in range(len())
    for elem in newl1, newl2:
        el = newl1.elem[i] + newl2.elem[i]
        if el[i] > 10:
            el[i] = el[i] % pow(10, i)
            el[i+1] = el[i] // pow(10,i)
            outcome.append(el)
        else:
            outcome.append(el)
            return outcome.reverse()

print(addtwonumbers([2, 4, 3], [5, 6, 4]))

