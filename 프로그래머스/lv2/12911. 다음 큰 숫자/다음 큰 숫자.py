def solution(n):
    
    num = str(bin(n)[2:]).count('1')
    
    for i in range(n + 1, 1000000):
        if str(bin(i)[2:]).count('1') == num:
            return i
        
