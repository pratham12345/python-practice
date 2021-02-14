def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('python'))
print(string_both_ends('py'))
print(string_both_ends('w'))
