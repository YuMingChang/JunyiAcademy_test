reverse_string = lambda s:s[::-1]
print('f(\"{}\") == \"{}\"'.format('junyiacademy', reverse_string('junyiacademy')))

reverse_word = lambda s:' '.join(w[::-1] for w in s.split())
ms = 'flipped class room is important'
print('f(\"{}\") == \"{}\"'.format(ms, reverse_word(ms)))
