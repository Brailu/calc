"""
memory.py

Represents a file memory.
"""


class Memory():
    
    def write(self, line):
        f = open("results", "a")
        template = f"{line}\n"
        f.write(template)
        f.close()
