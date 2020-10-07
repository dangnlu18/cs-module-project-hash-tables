from collections import OrderedDict

def no_dups(s):
    # Your code here
    s.lower()
    words = s.split(' ')
    word_hash = {}
    result = ''

    if len(s) ==0:
        return ""

    for word in words:
        if word in word_hash:
            word_hash[word] +=1
        else:
            word_hash[word] = 1
            result = result + f'{word} '
    
    return result.strip() 


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))