def insert_into_all(item, nested_list):
    """Assuming that nested_list is a list of lists, return a new list
    consisting of all the lists in nested_list, but with item added to
    the front of each.

    >>> nl = [[], [1, 2], [3]]
    >>> insert_into_all(0, nl)
    [[0], [0, 1, 2], [0, 3]]
    """
    new_nested_lst = []
    for lst in nested_list:
        new = lst.copy()
        new.insert(0, item)
        new_nested_lst.append(new)
    return new_nested_lst

def subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists). The subsequences can appear in any order.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    # observe that the subsequence can be classify into several type
    # 1. empty
    # 2. sequence that begin with a paricular number in the order of S continually increase length in the list of output
    # -------------------------------------------------
    # subseqs([1, 2]) include subseqs([1]), subseqs([2]), S itself
    # subseqs([1, 2, 3]) include subseqs([1]), subseqs([2]), subseqs([3]), subseqs([1, 2]), subseqs([1, 3]), S itself
    # How to simplify the problem subseqs(s) if len(s) > 1
    # -------------------------------------------------
    # insert_into_all(1, [[], [2], [2, 3], [3]]) return [[1], [1, 2], [1, 2, 3], [1, 3]]
    # insert_into_all(2, [[], [3]] return [[2], [2, 3]]
    # insert_into_all(3, [[]]] return [[3]]
    # iteration version
#    result = [[]]
#    for i in s[::-1]:
#        result = result + insert_into_all(i, result)
#    return result
    # recursion version
    if not s:
        return [[]]
    else:
        subseqs_but_not_first = s[1:]
        # example: insert_into_all(1, [[], [2], [2, 3], [3]]) return [[1], [1, 2], [1, 2, 3], [1, 3]]
        return insert_into_all(s[0], subseqs(s_but_not_first)) + subseqs(s_but_not_first)


def inc_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

    >>> seqs = inc_subseqs([1, 3, 2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> inc_subseqs([])
    [[]]
    >>> seqs2 = inc_subseqs([1, 1, 2])
    >>> sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    # why it would appear descend subsequence?
    # In recursion call, for example, there would be a insert_into_all(3, subseqs(s_but_not_first)) and subseqs(s_but_not_first) include a [2], so it produce [3, 2] a descend sub sequence.
    # undertanding prev:
    # I should only include an element if it is greater than or equal to the last included element in the subsequence
    # so, prev = last included element
    # Because I reduce the problem by s[1:], removing first element from begin to end, the prev is going from begin to end
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            # skip the current element
            return subseq_helper(s[1:], prev) # I'm not insert anything. So, prev remain the same.
        else:
            a = subseq_helper(s[1:], prev) # all subsequences that can be formed withous including s[0]
            b = subseq_helper(s[1:], s[0]) # all subsequences that include s[0], updating the prev to s[0]
            return insert_into_all(s[0], b) + a # combine two part
    return subseq_helper(s, -1) # intially any element can be taken


def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.

    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    # computation model:
    # if one total > another, switch added object
    # if deal, exchange by using slice assignment
    m, n = 1, 1 # I assume it's the index
    # condition checking function
    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    # if it's possible that one's index reach the end but its sum is still less than another?
    # it won't rise IndexError
    while not equal_prefix() and not (m >= len(first) and n >= len(second)):
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1

    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m] # nice switch statement
        return 'Deal!'
    else:
        return 'No deal!'


def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    "*** YOUR CODE HERE ***"
    # iteration start from the end to begin, take the last to insert into the begin
    i = 0
    for e in lst[::-1]: # lst here has already been evaluated. So, it will not change as the lst is mutated
        lst[i] = e
        i += 1


cs61a = {
    "Homework": 2,
    "Lab": 1,
    "Exam": 50,
    "Final": 80,
    "PJ1": 20,
    "PJ2": 15,
    "PJ3": 25,
    "PJ4": 30,
    "Extra credit": 0
}

def make_glookup(class_assignments):
    """ Returns a function which calculates and returns the current
    grade out of what assignments have been entered so far.

    >>> student1 = make_glookup(cs61a) # cs61a is the above dictionary
    >>> student1("Homework", 1.5)
    0.75
    >>> student1("Lab", 1)
    0.8333333333333334
    >>> student1("PJ1", 18)
    0.8913043478260869
    """
    "*** YOUR CODE HERE ***"
    # mutate dict, a non-local variable inside make_glookup
    def glookup(assignment_keyword, points):
        nonlocal class_assignments
        for keyword, points in class_assignments.items():
            if assignment_keyword == keyword:
                class_assignments[assignment_keyword] = points
        return sum(class_assignments.values()) # I don't know how to calculate the grade based on a particular assignment with the points earned
    return glookup



def num_trees(n):
    """How many full binary trees have exactly n leaves? E.g.,

    1   2        3       3    ...
    *   *        *       *
       / \      / \     / \
      *   *    *   *   *   *
              / \         / \
             *   *       *   *

    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429

    """
    # try to create trees that have exact n leaves and at the meantime count the valid trees
    # Observe that if is_leaf(tree): num_leaves += 1; and if branches(tree): num_leaves += 2
    # First thing I need to do is generating a number of likely qualified tree
    # And then I filter them by if count_leaves(tree) == n
    # Now the problem is how to define the "likely qualified"?
    # In the process of drawing a tree, I need choose if a node is a leaf or branch. 
    # Let t is nonlocal variable
#    def gen_tree(choice):
#    """generate a tree, return True if it's valid"""
#    nonlocal num_leaves
#    if choice == 0: # stand for leaf
#        num_leaves += 1
#        verify()
#        jump_to_another_node(node) # if any exist
#    elif choice == 1: # stand for branches
#        # I have two node. I need to make two choices.
#        !
#        gen_tree(choice)
#        gen_tree(choice)
#
#    def jump_to_another_node(node):
#        # it seems impossible to jump to another node without store another node in advanse
#        # So, I need store another node as a local state
#        nonlocal node
#        # rebind node
#        !
#        node = another_node
#    # varifying if the condition is met at the current node
#    def varify()
#    if num_leaves == n:
#        return True
#
#    # initialization
#    trees = []
#    t = None
#    node = None # current node
#    # Generate all trees confined on a range of "likely qualified", and if it is valid, append it to trees
#    for _ in range(10000):
#        num_leaves = 0
#        # if I choose randomly, it won't generate a "likely qualified" tree
#        if gen_tree(choice):
#            trees.append(t)
#        # reset
#        t = None
#        node = None
#    return len(trees)

    # I think I could acquire a lot of inspire from fib_tree(n)
    # I want to construct a tree whose label is the number of total leaves
    def gen_tree(n):
        """Return a tree whose label is the number of total leaves and which have the n number of leaves"""
        if n == 1:
            return tree(1) 
        elif n == 2:
            return tree(2, [tree(1), tree(1)])
        else:
            return tree(n, [tree(i), tree(j)]) # i + j = n It's a partition problem

def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    ________________
    def ____________(__________):
        ________________
        def ____________(__________):
            ________________
            "*** YOUR CODE HERE ***"
            # as many lines as you want
        ________________
    ________________

