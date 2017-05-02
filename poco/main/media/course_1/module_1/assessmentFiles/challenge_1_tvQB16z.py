#Module 1

#Challenge 1

'''
one = 1
two = 2
three = 3
'''

#Mock data goes first

#No mock data for this challenge.

try:
    # paste user code here
    &&&  
except Exception as e:
    print('err:' , e)
else:
    try:
        check = (one == 1)
    except NameError as e:
        print('nameerr:' , e)
    except Exception as e:
        print('err:' , e)
    else:
        if not check:
            print('valuebug:' + str(one))
    try:
        check = (two == 2)
    except NameError as e:
        print('nameerr:' , e)
    except Exception as e:
        print('err:' , e)
    else:
        if not check:
            print('valuebug:' + str(two))
    try:
        check = (three == 3)
    except NameError as e:
        print('nameerr:' , e)
    except Exception as e:
        print('err:' , e)
    else:
        if not check:
            print('valuebug:' + str(three))		
