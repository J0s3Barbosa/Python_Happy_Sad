
#Para saber se um número é feliz,
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #você deve obter o quadrado de cada dígito deste número,
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
        
def isHappySadNumber(num):    
    result = num;    
    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    
        
    #Happy number always ends with 1    
    if(result == 1): 
        print(str(num) + " is a happy number");    
        return True;
    #Sad number ends in a cycle of repeating numbers which contain 4    
    elif(result == 4):    
        print(str(num) + " is not a happy number");   
        return False;


