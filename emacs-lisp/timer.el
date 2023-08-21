;; Define a function to save the buffer automatically
(defun my-auto-save-buffer ()
  (when (and (buffer-modified-p)
             (buffer-file-name))
    (save-buffer)))

;; Set up a timer to call the function every 9 seconds
(run-with-timer 0 9 'my-auto-save-buffer)
