# p3_koroglu.py
# Problem 3 - Duplicated Substrings


# ---------- part a) ----------

def find_dup_str(s, n):
    

    if n <= 0:
        return ""

    for i in range(0, len(s) - n + 1):
        candidate = s[i:i + n]

        
        for j in range(i + n, len(s) - n + 1):
            if candidate == s[j:j + n]:
                return candidate

    return ""


s = input("Enter a string: ")
n = int(input("Enter the length of the substring: "))

answer = find_dup_str(s, n)

if answer == "":
    print("There is no duplicated substring of length", n)
else:
    print("The first duplicated substring of length", n, "is:", answer)


# ---------- part b) ----------

def find_max_dup(s):
    
    for n in range(len(s) // 2, 0, -1):
        answer = find_dup_str(s, n)
        if answer != "":
            return answer

    return ""



s = input("Enter a string: ")

answer = find_max_dup(s)

if answer == "":
    print("There is no duplicated substring in", s)
else:
    print("The longest duplicated substring is:", answer)