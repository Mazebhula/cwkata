def solution(s):
    b = []
    if len(s) % 2 == 0:

        for i in range(0, len(s),2):
            a = s[i:i+2]
            b.append(a)
    
    elif len(s) %2 !=0:
        s = s+"_"
        for i in range(0, len(s),2):
            a = s[i:i+2]
            b.append(a)

    print(b)
    
    return 

solution("hello")