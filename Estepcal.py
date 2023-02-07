import time
import sys

def main():
    instruction()
    # get the remaining Value
    try:
        extruded = float(input("\nWhat's the remaining Value: ")) 
    except ValueError:
        sys.exit("Not a Valid number")
        
    # get what have been extruded
    
    extruded = 120 - extruded
    print("\n To get the old e-step:\n  ► Go to control/motion/step/Estep")   
     
    # get what's the old input
    try:
        old = float(input("\nWhat's the value of E-step? "))
    except ValueError:
        sys.exit("Not a Valid number")
        
    # Little math 
    new = old * 100 / extruded
    
    # Answer
    print(f"\n You're new E-step value is {new:.4f}\n\n")
    
    
def instruction():
    print("\n\n  ----E-step calibration calculator----")
    time.sleep(0.5)
    print("\nPlease mark your fillament at 120mm from your Extruder")
    print("\n")
    print("  ► Go in the Control and Temperature and set it to desire one.")
    time.sleep(0.5)
    print("  ► Go to control/move axis/extruder/move 10mm and set it to 100mm")
    time.sleep(0.5)
if __name__ =="__main__":
    main()   
