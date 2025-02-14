from module.utils import controlScreen as cc

mError = 'caracter invalid'            

def validateInt(msg: str)-> int:        
    while True:
        try:
            return int(input(msg))      
        except ValueError:
            print(mError)              
            
            cc.LLScreen()
def validatefloat(msg:str) -> float:   
    while True:
        try:
            return float(input(msg))    
        except ValueError:
            print(mError)              
            cc.LLScreen()