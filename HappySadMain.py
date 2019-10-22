 #Main   
import HappySad as HsControll
import sys

def main():
    
    while True:
        try:
            userInput = input("Enter a number:")
            num = int(userInput)
            if num > 0:
                response = HsControll.isHappySadNumber(num)
                if(response):  
                    print(str(num) + " is a happy number")
                else:   
                    print(str(num) + " is not a happy number"); 
                    
            else:
                print("Number should be greater than 0")
        except:
            print("That's not a valid option!")
  

if __name__ == "__main__":
    main()
