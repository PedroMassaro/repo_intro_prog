#!/usr/bin/env python3

import re

text = """CEN0336 é a
        melhor disciplina"""

line = text.rstrip()

print(line)

print(re.search(r'é amelhor', line))
