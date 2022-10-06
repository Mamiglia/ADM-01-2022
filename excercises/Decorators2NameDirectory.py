

def person_lister(f):
    def inner(people):
        for p in people:
            p[2] = int(p[2])
        people.sort(key=operator.itemgetter(2))
        return [f(p) for p in people]
    return inner

