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


def append(path, bit):
    return [a + [bit, ] for a in path]


def flip(path):
    return [[1-aa for aa in a] for a in path]


def create_path(powers):
    result = []
    for j, power in enumerate(powers):
        result = result + [j % 2, ] * power
    return result


def zip_paths(path, apps):
    return [perm + app for i, perm in enumerate(path) for app in apps[::1-(2 * (i % 2))]]


def find_path(k0, k1):
    print(k0, k1)
    # zero - any
    if k0 == 0:
        path = [[1, ] * k1]
        return path
    # any - zero
    if k1 == 0:
        return flip(find_path(k1, k0))

    # one - even
    if k0 == 1 and k1 % 2 == 0:
        path = [[1, ] * j + [0, ] + [1, ] * (k1 - j) for j in range(k1 + 1)]
        return path + path[1:2]
    # even - one
    if k0 % 2 == 0 and k1 == 1:
        return flip(find_path(k1, k0))

    # one - odd
    if k0 == 1 and k1 % 2 == 1:
        return [[1, ] * (k1 - j) + [0, ] + [1, ] * j for j in range(k1 + 1)]
    # odd - one
    if k0 % 2 == 1 and k1 == 1:
        return flip(find_path(k1, k0))

    # even - odd
    if k0 % 2 == 0 and k1 % 2 == 1:
        return flip(find_path(k1, k0))
    # odd - even
    if k0 % 2 == 1 and k1 % 2 == 0:
        path_0 = find_path(k0, k1 - 1)
        path_1 = find_path(k0 - 1, k1)
        # a = path_0[0]
        b = path_0[-2]
        c = path_0[-1]
        d = swap_last_bit(b)
        e = swap_last_bit(c)
        return append(path_0[:-1], 1) + append(roundabout(path_1, d, e), 0) + append(path_0[-1:], 1)
    # even - even
    if k0 % 2 == 0 and k1 % 2 == 0:
        path_0 = find_path(k0, k1 - 1)
        path_1 = find_path(k0 - 1, k1)
        a = path_0[0]
        b = path_0[1]
        c = path_0[-1]
        d = path_1[0]
        e = path_1[-2]
        f = path_1[-1]
        return append(path_0, 1) + append(path_1, 0)
    # odd - odd
    if k0 % 2 == 1 and k1 % 2 == 1:
        path_0 = find_path(k0, k1 - 2)
        path_1 = find_path(k0 - 1, k1 - 1)
        path_3 = find_path(k0 - 2, k1)
        path_12 = zip_paths(path_1, ([0, 1], [1, 0]))
        a = path_0[0]
        b = path_0[-1]
        return None
    else:
        raise ValueError


def test_path_or_cycle(path, cycle=False, stutter=True):
    i_start = 0 if cycle else 1
    for i, _ in enumerate(path[i_start:]):
        a = path[i]
        b = path[i-1]
        assert all(aa in (0, 1) for aa in a), 'Non-binary nodes'
        assert all(bb in (0, 1) for bb in b), 'Non-binary nodes'
        assert sum(aa - bb == 1 for (aa, bb) in zip(a, b)) == 1, 'More than one switch from 0 to 1'
        assert sum(aa - bb == -1 for (aa, bb) in zip(a, b)) == 1, 'More than one switch fro 1 to 0'
        sums = [sum(t[i] for t in path) for i, _ in enumerate(path[0])]
        if stutter:
            assert all(s == sums[0] for s in sums), 'Some nodes revisited'
        else:
            assert all(s == sums[0] for s in sums), 'Some nodes revisited'


test_path_or_cycle(find_path(3, 0))
test_path_or_cycle(find_path(0, 2))
test_path_or_cycle(zip_paths(find_path(2, 2), ([0, 1], [1, 0])), cycle=True)


test_path_or_cycle(zip_paths(find_path(2, 0), ([1, 1, 0, 1], [1, 1, 1, 0])), cycle=True)
test_path_or_cycle(zip_paths(find_path(0, 2), ([0, 0, 0, 1], [0, 0, 1, 0])), cycle=True)

test_path_or_cycle(find_path(2, 2), cycle=True)

test_path_or_cycle(find_path(3, 3))
test_path_or_cycle(find_path(2, 2), cycle=True)
test_path_or_cycle(find_path(3, 1))
test_path_or_cycle(find_path(3, 2))
