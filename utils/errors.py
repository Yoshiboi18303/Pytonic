def refer_err(bad_reference):
  raise ReferenceError(f"You didn't define {str(bad_reference)}!")
def type_err(correct_type):
  raise TypeError(f"Pytonic raised an error:\nTypeError: {correct_type} should be the right type, not what you have entered.")