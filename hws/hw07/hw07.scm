(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond 
    ((< num 0) -1)
    ((= num 0) 0)
    ((> num 0) 1)
  )
)


(define (square x) (* x x))

(define (pow x y)
    (if (= y 1) x
        (if (even? y) 
            (square (pow x (/ y 2)))
            (* x (square (pow x (floor (/ y 2)))))
        )
    )
)

(define (in ele lst)
  (cond
  ((null? lst) #f)
  ((null? (car lst)) #f)
  ((eq? ele (car lst)) #t)
  (else (in ele (cdr lst)))
  )
)

(define (unique s)
  (define (helper s memo)
    (cond
    ((null? s) memo)
    ((in (car s) memo)
      (helper (cdr s) memo))
    (else
      (helper (cdr s) (append memo (cons (car s) nil))))
    )
  )
  (helper s nil)
)

(define (replicate x n)
  (define (helper n s)
    (if (= n 0) s
      (helper (- n 1) (cons x s)))
  )
  (helper n nil)
)


(define (accumulate combiner start n term)
  (define (helper num result)
    (if (> num n) result
      (helper (+ num 1) (combiner result (term num))) 
    )
  )
  (helper 1 start)
)


(define (accumulate-tail combiner start n term)
  (define (helper num result)
    (if (> num n) result
      (helper (+ num 1) (combiner result (term num))) 
    )
  )
  (helper 1 start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  ;(map (lambda (var) map-expr) lst)
  ;(filter (lambda (var) filter-expr) lst)
  ;(map (lambda (var) map-expr) (filter (lambda (var) (filter-expr)) lst))
  (list 'map (list 'lambda (list var) map-expr) (list 'filter (list 'lambda (list var) filter-expr) lst))
)

