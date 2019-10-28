
from flask import *  
import HappySad as HsControll

app = Flask(__name__) 

@app.route('/')  
def message(): 
        return render_template('hs_Template.html')

@app.route('/happysadnumber',methods = ['GET'])  
def hs(): 
    try:
        number=request.args.get('number')  
        if number != None or int(number) > 0:  
          result = HsControll.fun(int(number))
          return render_template('hs_Template.html',result=result )  
    except:
        return render_template('hs_Template.html')  


@app.route('/happysadnumber/<int:number>')  
def happysadnumber(number): 
    try:
        return HsControll.fun(number); 
    except Exception as exc:
        return exc
     

if __name__ =='__main__':  
    app.run(debug = True)  

