def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    c = ''
    for i in range(len(s)+1):
        for a in range(len(s)+1):
            print(i,a)
            if i < a:
                new_str = s[i:a]
                d = ''
                for b in new_str[::-1]:
                    d = d + b
                if new_str == d and len(new_str) > len(c):
                    c = new_str
    print(c)



longestPalindrome('aababacd')