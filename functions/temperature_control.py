#define function with temperature_value and unit as inputs
#set default unit as C.
#if selected unit is F
#    temperature = (temperature * 9/5) + 32
#    set temperature threshold 
#if selected unit is C or default:
#    temperature = (temperature - 32)*5/9
#    set temp_threshold 
#if temperature < temp_threshold
#    set heat advisory as "cold advisory" 
#if  temperature >= temp_threshold
#    set heat advisory as "Heat alert"
#return heat advisory
#call function
#print function


def get_temp_advisory_control(temperature, temp_threshold, unit = "C"):
    if unit.upper() == "C":
        temperature = (temperature * 9/5) + 32
        temp_threshold = (temp_threshold * 9/5) + 32
    elif unit.upper() == "":
        temperature = (temperature - 32)*5/9
        temp_threshold = (temp_threshold - 32)*5/9
    else:
        raise ValueError("Invalid unit!")
    if temperature < temp_threshold:
        return temperature, "cold advisory"
    elif  temperature >= temp_threshold:
        return temperature, "Heat alert"
    
    
        
        
     
    
        
        
    
     










