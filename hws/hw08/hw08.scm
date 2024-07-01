(define (rle s)
  (define (helper s n)
    (if (null? s)
      nil
      (if (null? (cdr-stream s))
        (cons-stream (list (car s) n) nil)
        (if (= (car (cdr-stream s)) (car s))
          (helper (cdr-stream s) (+ n 1))
          (cons-stream (list (car s) n) (helper (cdr-stream s) 1))))))
  (helper s 1)
)



(define (group-by-nondecreasing s)
  (define (group-helper curr-seq curr-stream)
    (if (null? curr-stream)
        nil
        (let ((next-value (car curr-stream))
               (next-stream (cdr-stream curr-stream)))
          (if (or (null? curr-seq) (<= (car curr-seq) next-value))
              (group-helper (append curr-seq (list next-value)) next-stream)
              (cons-stream curr-seq (group-helper (list next-value) next-stream))))))
  (group-helper '() s)
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

