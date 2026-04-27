(defun palindrome-check (str)
  (let ((rev (reverse (coerce str 'list))))
    (if (equal (coerce str 'list) rev)
        (format t "The given string is a palindrome.~%")
        (format t "The given string is NOT a palindrome.~%"))))

(defun main ()
  (format t "Enter a string: ")
  (let ((input (read-line)))
    (palindrome-check input)))

(main)