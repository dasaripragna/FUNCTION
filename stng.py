# def a(n):
#     i=0
#     while i<len(n):
#         if len(n)>1 and n[0]==n[-1]:
#             i=i+1
#         return i
# print (a(["abc","xyz","aba",1221]))
def match_words(words):
    ctr = 0	
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
        return ctr
print(match_words(['abc', 'xyz', 'aba', '1221']))