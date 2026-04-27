(defun area-of-circle (r)
  (let ((area (* 3.1416 r r)))
    (format t "Area of circle = ~f~%" area)))

(defun area ()
  (format t "Enter radius: ")
  (let ((radius (read)))
    (area-of-circle radius)))

(area)