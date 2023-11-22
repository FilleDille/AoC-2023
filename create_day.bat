@echo off
setlocal enabledelayedexpansion

set /p "day=Enter day (n): "

set "numeric=true"
for /f "delims=0123456789" %%i in ("!day!") do set "numeric=false"
if %numeric% == false (
    echo Invalid input. Please enter a numeric value with at most 2 digits.
    exit /b 1
)

if not "%day%" EQU "!day:~0,1!!day:~1,1!" (
    echo Invalid input. Please enter a numeric value with at most 2 digits.
    exit /b 1
)

if "!day:~1,1!" EQU "" (
    set "day_formatted=0!day!"
) else (
    set "day_formatted=!day!"
)

if not exist day\ (
	mkdir day\
)

if not exist template\ (
	mkdir template\
)

if not exist day\%day_formatted%\ (
	mkdir day\%day_formatted%\
)

if not exist day\%day_formatted%\src\ (
	mkdir day\%day_formatted%\src\
)

if not exist day\%day_formatted%\input\ (
	mkdir day\%day_formatted%\input\
)

if not exist day\%day_formatted%\input\test.txt (
	break>day\%day_formatted%\input\test.txt
)

if not exist day\%day_formatted%\input\input.txt (
	break>day\%day_formatted%\input\input.txt
)

if not exist .\src\%day_formatted%\main.py (
	echo F|xcopy /S /Q /Y /F .\template\main.py  day\%day_formatted%\main.py
)

if not exist day\%day_formatted%\src\part_1.py (
	echo F|xcopy /S /Q /Y /F .\template\part_1.py  day\%day_formatted%\src\part_1.py
)

if not exist day\%day_formatted%\src\part_2.py (
	echo F|xcopy /S /Q /Y /F .\template\part_2.py  day\%day_formatted%\src\part_2.py
)

if not exist day\%day_formatted%\src\__init__.py (
	echo F|xcopy /S /Q /Y /F .\template\__init__.py  day\%day_formatted%\src\__init__.py
)
