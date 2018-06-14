def is_isogram(argument):
  word_seen=set()
  if type(argument) != str:
    raise TypeError('Argument should be a string')
  elif argument==" " :
    return(argument,False)
    argument.lower()
  for letter in argument:
      if letter in word_seen:
        return(argument,False)
      word_seen.add(letter)
  return (argument,True)
