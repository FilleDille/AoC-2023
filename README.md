# Advent of Code Calendar Project
## Overview

Welcome to my Advent of Code repo. Starting this year, i'll try to be a bit more organized with the structure and testing. This repo provides both a bash and batch script to automate the setup process of a new day, including the creation of necessary directories and copying template files.

## Setup
#### Bash
`bash create_day.sh`

#### Batch
`.create_day.bat`

A prompt asking for day appears in both scripts. Write the number of the day, e.g. 1. The script will add a 0 before single digits, so 1 becomes 01. 

If attempting to re-create an existing day, only missing folders and files will be added. E.g. if part_1.py gets deleted, a fresh new template copy of that file will be added.

## Project Structure

The project structure is organized as follows:

    .
    `-- root/
        |-- create_day.bat
        |-- create_day.sh
        |-- template/
        |   |-- __init__.py
        |   |-- main.py
        |   |-- part_1.py
        |   `-- part_2.py
        `-- day/
            |-- 01/
            |   |-- main.py
            |   |-- src/
            |   |   |-- part_1.py
            |   |   `-- part_2.py
            |   `-- input/
            |       |-- input.txt
            |       `-- test.txt

             ...

            `-- 25/
                |-- main.py
                |-- src/
                |   |-- part_1.py
                |   `-- part_2.py
                `-- input/
                    |-- input.txt
                    `-- test.txt

### template folder
The files in this folder will be copied to each new day-folder. A change here will only affect new days created after this point.

### day folder naming
Each day will be named with two unsigned integers between 01-99. If anything else than two unsigned integers are used in the creation of a new day will result in the script aborting.

### day folder structure
Each day is built as a project. The idea is to run the main.py with the use of flags and sys arguments, and write the logic in the part_n.py. main.py will call the part_n scripts which in turn will return the result to main.py.

## Usage
Run the main.py followed by which part to run as an argument. Optional --test flag can be included followed by the value to assert. If --test flag is used, the script will read test.txt as input and compare the result with the value provided. If no --test flag is used, the script will read input.txt, which should contain the actual input.

`python main.py <part> [--test <test-value>]`

### Example usage real input

`python main.py 1`

will return the result of part 1 run on input.txt

### Example usage with test

`python main.py 2 --test 12345`

will either yield Assertion successful or raise AssertionError.

### Debug usage

The code contains a block that is commented out per default and is used for debugging in an IDE. Uncomment to run the code in an IDE without the need to provide sys arguments.

    ############################ v DEBUG BLOCK v ############################

    #input_path = os.path.join(script_dir, 'input', 'input.txt')
    #input_raw = read_input(input_path)
    #result = part_1.run(input_raw)
    #sys.exit()

    ############################ ^ DEBUG BLOCK ^ ############################
