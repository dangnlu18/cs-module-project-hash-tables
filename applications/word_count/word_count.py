def word_count(s):
    # Your code here
    lower = s.lower()
    words = lower.split(' ')
    word_hash = {}

    for word in words:
        if word in word_hash:
            word_hash[word] +=1
        else:
            word_hash.update({word: 1})
    print(word_hash)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))