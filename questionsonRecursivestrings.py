# Questions on Subsets, subsequence and string using recursion.

# Q.1) Skip a character in a string. Eg: baccad , skip char 'a', ans = bccd. 
# --> 

def SkipChar(char, s, ans = ""):
    a = ans
    if len(s) == 0:
        return a
    if s[0] == char:
        s1 = s[1:]
        return SkipChar(char, s1, a)
    else:
        s1 = s[1:]
        a = a + s[0]
        return SkipChar(char, s1, a)


# print(SkipChar('c', 'baccad'))

# Q.2) Skip a string in a String. Eg: bccappled, skip apple, ans = bccd
# --> 

def Skipstring(skip_s, s, ans = ""):
    a = ans
    l = len(skip_s)
    if len(s) == 0:
        return a
    if len(s) < l:
        a = a + s
        s1 = ""
        return SkipChar(skip_s, s1, a)
    if s[0:l] == skip_s:
        s1 = s[l:]
        return Skipstring(skip_s, s1, a)
    else:
        s1 = s[1:]
        a = a + s[0]
        return Skipstring(skip_s, s1, a)
    
print(Skipstring("apple", "applebccdd"))

## Subset or subsequence problems.

# Q.3) Print all the subsequence of a given string.
# --> 

def SubSeq(pr, unpr):  # pr == processed string and unpr = unprocessed string (unpr/pr)
    if len(unpr) == 0:
        print(pr + ", ", end = "")
        return
    else:
        ch = unpr[0]
        unpr1 = unpr[1:]
        # Take the ch in string pr
        pr1 = pr + ch
        SubSeq(pr1, unpr1)
        # Skip the ch in string pr
        SubSeq(pr, unpr1)

# Returning a List of the above answer, by creating list in the body itself.
def SubSeqRet(pr, unpr):  # pr == processed string and unpr = unprocessed string (unpr/pr)
    if len(unpr) == 0:
        list = [pr]
        return list
    else:
        ch = unpr[0]
        unpr1 = unpr[1:]
        # Take the ch in string pr
        pr1 = pr + ch
        left = SubSeqRet(pr1, unpr1)
        # Skip the ch in string pr
        right = SubSeqRet(pr, unpr1)

        main = left + right
        return main

# print(SubSeqRet("", "abc"))

# Q.4) Permutations of a string using subset problem.
# -->

def Premute(pr, unpr):
    if len(unpr) == 0:
        print(pr + " ", end = "")
        return
    else:
        ch = unpr[0]
        unpr1 = unpr[1:]
        for i in range(0, len(pr)+1):
            f = pr[:i]
            s = pr[i:]
            pr1 = f + ch + s
            Premute(pr1, unpr1)
    
def Premute_LRet(pr, unpr):  # List Return 
    if len(unpr) == 0:
        list = [pr]
        return list
    else:
        ch = unpr[0]
        unpr1 = unpr[1:]
        main = []
        for i in range(0, len(pr)+1):
            f = pr[:i]
            s = pr[i:]
            pr1 = f + ch + s
            main = main + Premute_LRet(pr1, unpr1)

        return main
    
Premute("", "abc")
print()
print(Premute_LRet("", "abc"))

# Q.4) Letter combinations of phone numbers (VVIP Questions, asked in Google.)
# -->
letterdict = {1: [],                   2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 
              4: ['g', 'h', 'i'],      5: ['j', 'k', 'l'], 6:['m', 'n', 'o'],
              7: ['p', 'q' ,'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

ans = []
def Lettercombi(pr, unpr):
    if len(unpr) == 0:
        # print(pr + ", ", end = "")
        ans.append(pr)
        return
    else:
        ch = unpr[0]
        unpr1 = unpr[1:]
        for i in letterdict[int(ch)]:
            pr1 = pr + i
            Lettercombi(pr1, unpr1)
        
Lettercombi("", "23")
print(ans)

# Q.5) Dice Rolls for a given Target value. (VVIP , Amazon question)
# -->
t = 4
def Dicerolls(pr, unpr):
    if unpr == 0:
        list = [pr]
        return list
    else:
        main = []
        for i in range(1, unpr + 1):
            if i <= 6:
                unpr1 = unpr - i
                pr1 = pr + " " + str(i)
                main = main + Dicerolls(pr1, unpr1)
        
        return main

print(Dicerolls("", t))
