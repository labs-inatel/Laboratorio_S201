(defun apply-function (lst)
  (mapcar (lambda (x)
            (if (>= x 4)
                (* x 2)
                (/ x 2)))
          lst))

(let ((list1 '(1 2 3))
      (list2 '(4 5 6)))
  (format t "Resultado: ~a~%"
          (append (apply-function list1)
                  (apply-function list2))))
