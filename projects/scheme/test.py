from scheme import *

env = create_global_frame()
env.define("x", 0)
breakpoint()
do_or_form(
    read_line(
        "((begin(define x(+ x 1))  #f) (begin(define x(+ x 10))  #f) (begin(define x(+ x 100))  #f) (begin(define x(+ x 1000))  #f))"
    ), env)
