(define-macro (def func args body)
    `(define ,(cons func args) ,body))


(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define all-three-multiples
  (map-stream (lambda (x) (+ x 3)) (cons-stream 0 all-three-multiples)) 
)


(define (compose-all funcs)
  (define (composed-funcs x)
      (define (apply_funcs funcs x)
        (if (null? (cdr funcs))
            ((car funcs) x)
            (apply_funcs (cdr funcs) ((car funcs) x))))
      (apply_funcs funcs x))
  (if (null? funcs)
    (lambda (x) x)
    composed-funcs)
)


(define (partial-sums stream)
  'YOUR-CODE-HERE
  (helper 0 stream)
)

