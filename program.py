

def remove_stars(s: str):

    while s.count("*") != -1:
        starIndex = s.index("*")
        for i in range(0,starIndex):
            if(s[starIndex-1].equals("*")):
                s.pop(starIndex-1)
            s.pop(starIndex)
    return s

            
    


def main():
    pass

print(remove_stars("***aa*b**c*jj(*Djdhh*dniu)"))