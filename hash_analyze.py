import hashlib
import re
import itertools


def check(inputdata):

    reg = re.fullmatch(r"[0-9a-f]{32}",inputdata)

    if reg != None:
        hash_type = "md5"

        return hash_type

    reg = re.fullmatch(r"[0-9a-f]{40}",inputdata)

    if reg != None:
        
        hash_type = "sha1"

        return hash_type
    
    reg = re.fullmatch(r"[0-9a-f]{56}",inputdata)

    if reg != None:
        
        hash_type = "sha224"

        return hash_type

    reg = re.fullmatch(r"[0-9a-f]{64}",inputdata)

    if reg != None:
        
        hash_type = "sha256"
    
        return hash_type

    reg = re.fullmatch(r"[0-9a-f]{128}",inputdata)

    if reg != None:

        hash_type = "sha512"
        
        return hash_type


def compare(inputdata,hash_type,policy):
    
    for x in range(0,65):

        if policy == "1":

            char = itertools.product("abcdefghijklmnopqrstuvwxyz",repeat=x)
    
        if policy == "2":

            char = itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",repeat=x)

        if policy == "3":

            char = itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",repeat=x)

        if policy == "4":

            char = itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&@",repeat=x)
        
        if policy == "5":

            char = itertools.product("0123456789",repeat=x)
    


        for pin in char:
            pinready = "".join(pin)

            if hash_type == "md5":
            
                cmpvalue = hashlib.md5(pinready.encode()).hexdigest()
                
            if hash_type == "sha1":

                cmpvalue = hashlib.sha1(pinready.encode()).hexdigest()

            if hash_type == "sha224":

                cmpvalue = hashlib.sha224(pinready.encode()).hexdigest()

            if hash_type == "sha256":

                cmpvalue = hashlib.sha256(pinready.encode()).hexdigest()

            if hash_type == "sha512":

                cmpvalue = hashlib.sha512(pinready.encode()).hexdigest()


                
            print(f"[+]Encrypting: {pinready}::::{cmpvalue}",end="\r")

            if cmpvalue == inputdata:

                print("[+]Found!!!!")
                print(f"[+]RawValue: {pinready}")
                print(f"[+]SameHash: {cmpvalue}")


