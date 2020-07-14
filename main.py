def solution(number):
    numberlist=[]
    for num in range (number):
        if num%3==0:
            numberlist.append(num)
            num+=1
        elif num%5==0:
            numberlist.append(num)
            num+=1          
            
    return  print(f"solution({number})", sum(numberlist))


number=int(input('give a number :'))
solution(number)
