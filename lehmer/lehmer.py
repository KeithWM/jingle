# class Permutation:
#     def __init__(self, k0, k1):
#         self.k0 = k0
#         self.k1 = k1


def swap_last_bit(perm):
    new_perm = perm.copy()
    new_perm[-1] = 1 - new_perm[-1]
    return new_perm


def roundabout(path, a, b):
    n = len(path)
    i_a = 0
    for i, p in enumerate(path):
        if a == p:
            i_a = i
    d = -1 if path[i_a + 1 % n] == b else 1
    return [path[(i_a + d*j) % n] for j in range(n)]


def app(path, bit):
    return [a + [bit, ] for a in path]


def flip(path):
    return [[1-aa for aa in a] for a in path]


def find_path(k0, k1):
    print(k0, k1)
    # even - one
    if k0 % 2 == 0 and k1 == 1:
        return flip(find_path(k1, k0))
    # one - even
    if k0 == 1 and k1 % 2 == 0:
        js = [-j % (k1 + 1) for j in range(k1 + 1)]
        return [[1, ] * j + [0, ] + [1, ] * (k1 - j) for j in js]

    # odd - one
    if k0 % 2 == 1 and k1 == 1:
        return flip(find_path(k1, k0))
    # one - odd
    if k0 == 1 and k1 % 2 == 1:
        return [[1, ] * (k1 - j) + [0, ] + [1, ] * j for j in range(k1 + 1)]

    # even - odd
    if k0 % 2 == 0 and k1 % 2 == 1:
        return flip(find_path(k1, k0))
    # odd - even
    if k0 % 2 == 1 and k1 % 2 == 0:
        path_0 = find_path(k0, k1 - 1)
        path_1 = find_path(k0 - 1, k1)
        a = path_0[0]
        b = path_0[-2]
        c = path_0[-1]
        d = swap_last_bit(b)
        e = swap_last_bit(c)
        return app(path_0[:-1], 1) + app(roundabout(path_1, d, e), 0) + app(path_0[-1:], 1)
    if k0 % 2 == 0 and k1 % 2 == 0:
        path_0 = find_path(k0, k1 - 1)
        path_1 = find_path(k0 - 1, k1)
        a = path_0[0]
        b = path_0[1]
        c = path_0[-1]
        d = path_1[0]
        e = path_1[-2]
        f = path_1[-1]
        return app(path_0, 1) + app(path_1, 0)

    if k0 == 2 and k1 == 2:
        return [[0, 0, 1, 1],
                [0, 1, 1, 0],
                [0, 1, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 0, 1, 0]]
    if k0 == 3 and k1 == 1:
        return [[0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [1, 0, 0, 0]]


def test_path_or_cycle(path, cycle=False):
    i_start = 0 if cycle else 1
    for i, a in enumerate(path[i_start:]):
        b = path[i-1]
        assert all(aa in (0, 1) for aa in a)
        assert all(bb in (0, 1) for bb in b)
        assert sum(aa - bb == 1 for (aa, bb) in zip(a, b)) == 1
        assert sum(aa - bb == -1 for (aa, bb) in zip(a, b)) == 1
        sums = [sum(t[i] for t in path) for i, _ in enumerate(path[0])]
        assert all(s == sums[0] for s in sums)


# test_path_or_cycle(find_path(2, 2), cycle=True)
# test_path_or_cycle(find_path(3, 1))
test_path_or_cycle(find_path(3, 2))
