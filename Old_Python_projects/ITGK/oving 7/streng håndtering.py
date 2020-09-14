def check_equal(str1,str2):
    return str1==str2

def check_equals(str1,str2):
    if len(str1)!=len(str2):
        return False
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            return False
        else:
            return True

def reverse_words(str1):
    reversedstring=[]
    for s in (str1.split(" ")):
        reversedstring.append(s[::-1])
    return (str(reversedstring))

def string_reverse(str1):
    return str1[::-1]
print(string_reverse("morna jens"))

def is_palindorme(str1):
    return str1==str1[::-1]
print(is_palindorme("abba"))

def contains_str(str1,str2):
    return str2.find(str1)
print(contains_str("test","est"))