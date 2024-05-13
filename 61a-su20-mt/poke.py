def copycat(lst1, lst2):
    """
    >>> copycat(['a', 'b', 'c'], [1, -1, 3])
    ['c', 'c', 'c']
    """
    new_lst = []
    def helper(index):
        while index < min(len(lst1), len(lst2)):
            if lst2[index] > 0:
                for _ in range(lst2[index]):
                    new_lst.append(lst1[index])
                index += 1
            elif lst2[index] == 0:
                index += 1
            else:
                for _ in range(abs(lst2[index])):
                    new_lst.pop()
                index += 1
        return new_lst
    return helper(0)



