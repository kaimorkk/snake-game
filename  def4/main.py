def stick(*arg):
    args = [args for args in args if isinstance(args, str)]
    result = '#'.join(args)
    return result


print(stick('sport', 'summer'))
print(stick(3, 4, 7))
print(stick(False,'true', True, 'workout', [],'gym'))