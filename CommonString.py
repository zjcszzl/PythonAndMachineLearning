import collections


def countVowel(str):
    vowels = set("AEIOUaeiou")
    res = 0
    for c in str:
        if c in vowels:
            res += 1
    return res


def reverseStr(str):
    stack = []
    for c in str:
        stack.append(c)
    res = ""
    while stack:
        res += stack.pop()
    return res


def reverseWord(str):
    l = str.split()
    stack = []
    for word in l:
        stack.append(word)
    res = ""
    while stack:
        res += stack.pop() + " "
    return res.strip()


def isRotation(strA, strB):
    if len(strB) == 0:
        return True
    if len(strA) == 0:
        return False
    temp = strA + strA
    loc = temp.index(strB[0])
    if temp[loc:loc+len(strB)] == strB:
        return True
    return False


def removeDuplicate(str):
    res = ""
    seen = set()
    for c in str:
        if c in seen:
            continue
        seen.add(c)
        res += c
    return res


def mostFrequenc(str):
    count = collections.Counter(str)
    return count.most_common(1)[0][0]


def captilizeWord(str):
    l = str.split()
    res = ""
    for val in l:
        res += val.capitalize() + " "
    return res.strip()


def isAnagram(strA, strB):
    count = collections.Counter(strA)
    for c in strB:
        if c in count:
            count[c] -= 1
        else:
            return False
    for k, v in count.items():
        if v != 0:
            return False
    return True


def isPalind(str):
    return str == str[::-1]


if __name__ == "__main__":
    print(countVowel("helloHELLO"))
    print(reverseStr("hello"))
    print(reverseWord("   Trees    are beautiful    "))
    print(isRotation("ABCD", "ADBC"))
    print(removeDuplicate("Helllllloooo!!!"))
    print(mostFrequenc("Hellllllllooo!!!!!!!!!!!!"))
    print(captilizeWord("      trees      are       beautiful!    "))
    print(isAnagram("abcde", "adbceee"))
    print(isPalind("abca"))
