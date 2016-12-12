"""Given a string, returns True or False depending on whether that
string has balanced parentheses.

>>> has_balanced_parens("()")
True

>>> has_balanced_parens("(Oh Noes!)(")
False

>>> has_balanced_parens("((There's a bonus open paren here.)")
False

>>> has_balanced_parens(")")
False

>>> has_balanced_parens("(")
False

If you receive a string with no parentheses, consider it balanced:

>>> has_balanced_parens("Hey...there are no parens here!")
True

"""


def has_balanced_parens(mystr):
  """Given a string, returns True or False depending on whether that
  string has balanced parentheses.
  """

  curr = []

  for char in mystr:
    if char == '(':
      curr.append(char)
    if char == ')':
      if not curr or curr[-1] != '(':
        return False
      curr.pop()

  if not curr:
    return True
  else:
    return False



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n"


# LEARNED FROM SOLUTION:
# Thought this was a clever way to return True/False without the if statement.

# return len(tracker) == 0




