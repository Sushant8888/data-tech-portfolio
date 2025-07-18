def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
        
    return i == len(s)

print(isSubsequence("abc", "ahbgdc"))  # Output: True
print(isSubsequence("axc", "ahbgdc"))  # Output: False
