(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (if (null? rests)
    nil
    (cons (cons first (car rests)) (cons-all first (cdr rests)))
  )
)

(define (zip pairs)
  (list (map car pairs) (map cadr pairs)))

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (helper n s) 
    (if (null? s)
      nil
      (cons (list n (car s)) (helper (+ n 1) (cdr s)))
    )
  )
  (define n 0)
  (helper n s)
)
; not tail recursive though
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (if (= total (car denoms))
    (if (null? (cdr denoms))
      (cons (list (car denoms)) nil)
      (append (cons (list (car denoms)) nil)
              (list-change total (cdr denoms))))
    (if (< (car denoms) total)
      (if (null? (cdr denoms))
        (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
        (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
                (list-change total (cdr denoms))))
      (if (null? (cdr denoms))
        nil
        (list-change total (cdr denoms))))))
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         `(quote ,(cadr expr))
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (append (list form params) (map let-to-lambda body))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (cons (append `(lambda ,(car (zip values))) (map let-to-lambda body)) (map let-to-lambda (cadr (zip values))))
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         (let ((operator (car expr))
               (operands (cdr expr)))
           (cons operator (map let-to-lambda operands)))
         ; END PROBLEM 18
         )))
