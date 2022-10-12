@REM a) Create the directory "shell_test" (and changing directory)
cd C:\Users\Vaccari\Desktop
md shell_test
cd shell_test

@REM b) Create the file "test_print.py" with a simple print into the directory
echo print('You did it!') > test_print.py

@REM c) Rename the file to "new_test_print.py"
ren test_print.py new_test_print.py

@REM d) List what is in the directory "shell_test" including their file permissions
dir 
icacls new_test_print.py

@REM e) Execute the Python file and call the simple print
python new_test_print.py

@REM f) Remove the directory "shell_test" with its content
cd ..
rmdir /s shell_test
