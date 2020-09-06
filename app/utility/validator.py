def validate_name(name):

    num = {"1","2","3","4","5","6","7","8","9","0"}
    spe ={"!","@","#","$"}
    spea =" "
    is_spea = spea in name
    if is_spea :
        return False
    if name =="" :
        return False
    
    for char in name:
        is_num = char in num
        is_spe = char in spe
         
        if  is_num or is_spe or char ==""  : 
            return False
    return True


def validate_id(id):
    return True


def validate_phone_number(phone_number):
    return True
