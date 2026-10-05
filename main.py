from sentences import get_sentence
from typing_test import start_test
from result import show_result

print("================================")
print("        TYPING TESTER")
print("================================")

sentence = get_sentence()

time_taken, wpm, accuracy, errors = start_test(sentence)

show_result(time_taken, wpm, accuracy, errors)
