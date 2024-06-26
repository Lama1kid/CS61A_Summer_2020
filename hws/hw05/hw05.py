def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message == "deposit":
            balance += amount
            return balance
        elif message == "withdraw":
            if amount > balance:
                return "Insufficient funds"
            else:
                balance -= amount
                return balance
        else:
            return "Invalid message"
    return bank


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Too many incorrect attempts. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Too many incorrect attempts. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    attempts = [] # attempts of input_password
    def withdraw(amount, input_password):
        nonlocal balance, password, attempts
        # check if the account is locked
        if len(attempts) >= 3:
            return f"Too many incorrect attempts. Attempts: {attempts}"
        if input_password == password:
            if amount > balance:
                return "Insufficient funds"
            else:
                balance -= amount
                return balance
        else:
            attempts.append(input_password)
            return "Incorrect password"
    return withdraw


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> lst = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst, 2)
    9
    >>> lst2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    times_appears_in_row = 1
    # initial pre_e = the first element and advance the position forward one step
    pre_e = next(t)
    for e in t: # it's supposed to start with 9 
        if e == pre_e:
            times_appears_in_row += 1
        else:
            pre_e = e
            # reset
            times_appears_in_row = 1
        if times_appears_in_row == k: # met the condition
            return e
    


def merge(incr_a, incr_b):
    """Yield the elements of strictly increasing iterables incr_a and incr_b, removing
    repeats. Assume that incr_a and incr_b have no repeats. incr_a or incr_b may be infinite
    sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    iter_a, iter_b = iter(incr_a), iter(incr_b)
    next_a, next_b = next(iter_a, None), next(iter_b, None)
    "*** YOUR CODE HERE ***"
    # for example
    # 0 < 0, false
    # remain the first 0
    # two iterables move forward 
    # [0]
    # 2 < 3, True
    # remain the 2
    # the first iterable move forward
    # observe that the iterable move forward of which elements remain except that two elements are equal
    # but how to access the values in the position of a iterator without advancing it forward
    # I can use assignment to remain a sort of local state, and I compare with variable instead of calling next() again
    while next_a != None and next_b != None:
        if next_a < next_b:
            yield next_a
            next_a = next(iter_a, None)
        elif next_a > next_b:
            yield next_b
            next_b = next(iter_b, None)
        else:
            yield next_a
            next_a = next(iter_a, None)
            next_b = next(iter_b, None)
    # If One iterable already reached the end
    if next_a == None and next_b != None:
        yield next_b
        yield from iter_b
    elif next_b == None and next_a != None:
        yield next_a
        yield from iter_a

def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    # how to make two account jointed, which means two account have access to the same balance
    # assignment different name to the same function, sothey have the same value
    # But I add a password conversion mechanism
    # how to verify old_pass?
    verification = withdraw(0, old_pass)
    if type(verification) is str:
        return verification
    def jointed_w(amount, password):
        if password == new_pass:
            password = old_pass
        return withdraw(amount, password)
    return jointed_w


def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.
    i = n % m
    n = natural * m + i
    n is a series of number that the generator produce

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def make_gen(remainder):
        """Nested generator function that captures the current remainder."""
        if remainder == 0:
            n = 1
        else:
            n = 0
        while True:
            yield n * m + remainder
            n += 1

    for i in range(m):
        yield make_gen(i)

def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

