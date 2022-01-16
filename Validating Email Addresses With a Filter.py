def fun(s):
    try:
        user, url = s.split('@')
        web,ext = url.split('.')
    except ValueError:
        return False
    
    if user.replace('-','').replace('_','').isalnum() is False:
        return False
    
    elif web.isalnum() is False:
        return False
    
    elif len(ext) > 3:
        return False
    
    else :
        return True
