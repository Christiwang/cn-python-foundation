"""
Intro to Python Project 1, Task 0

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
"""


"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0: 
what is the first record of texts and what is the last record of calls
Print messages: 
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

## Key: extract the according data from list
incoming_number0 = texts(0)
answering_number0 = texts(1)
time0 = texts(2)
print("First record of texts, {0} texts {1} at time {2}".format(incoming_number0,answering_number0,time0))

incoming_number1 = calls(-4)
answering_number1 = calls(-3)
time1 = calls(-2)
during = calls(-1)
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(incoming_number1,answering_number1,time1,during))


