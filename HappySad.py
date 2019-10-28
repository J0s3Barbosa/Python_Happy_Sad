
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
        return True;
    #Sad number ends in a cycle of repeating numbers which contain 4    
    elif(result == 4):    
        return False;

def fun(num1):  
    Result = {}  
    if num1 > 0:
        response = isHappySadNumber(num1)
        if(response):  
            happyResult = str(num1) + " is a happy number"
            Result = { 'string': '{}!'.format(happyResult),
                'bool': response
            } 
            return Result
        else:   
            sadResult = str(num1) + " is not a happy number"
            Result = {
                'string': '{}!'.format(sadResult),
                'bool': response
            } 
            return Result
    else:
        return "Number should be bigger than 0"
