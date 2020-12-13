import os
import sys
import art
import hash_analyze


def init():

    art.tprint("Brute4",font="cyber")

init()

print("[+]Enter Hash")

prompt    = "brute4@hshcrker:~$ "
inputdata = input(prompt)

banner = """

+--------------------+
|                    |
|1) [a-z]            |
|                    |
|2) [a-zA-Z]         |
|                    |
|3) [a-zA-Z0-9]]     |
|                    |
|4) [a-zA-Z0-9!#$%&@]|
|                    |
|5) [0-9]            |
|                    |
+--------------------+

[+]select policy 

"""
print(banner)

policy = input(prompt)

hash_type = hash_analyze.check(inputdata)

print(f"[+]HashType is {hash_type}")

print(f"[+]InputedHashValue---> {inputdata}")

hash_compare = hash_analyze.compare(inputdata,hash_type,policy)
