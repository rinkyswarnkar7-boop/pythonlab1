print('\t\t\t BAI Calculator')
print('\t\t\t By priyanshi')
print('\n Hello, this is a BAI Calculator!')
n=int(input("how many respond?"))
unit=str(input('do you widh to enter metric unit or imperial units:'))
for i in range(1,n+1):
    if unit=='metric':
        GND = str(input('please enter your gender input string(Women or Men):'))
        AGE = int(input('please enter your age input interger(whole number):'))
        HM = float(input('please enter your hight input meters(decimals):'))
        HC = int(input('please enter your hip circumference input centimetres:'))
        BAI = ((HC/((HM)**(1.5))))-18
        if GND =='Women':
            if(BAI<21 and 20<= AGE<=39) or (BAI<23 and 40<=AGE<=59) or ( BAI<25 and 60<=age<=79):
                print('your BAI is ',BAI,'which means you are underweight.')
            elif(21<=BAI <=33 and 20<=AGE<=39) or(23<=BAI<=35 and 40<=AGE<=59) or (25<=BAI<=38 and 60<=AGE<=79):
                print('your BAI is', BAI,'which means you are healthy.')
            elif(33<BAI<=39 and 20<=AGE<=39) or (35<BAI<=41 and 40<=AGE<=59) or (38<BAI<=43 and 60<=AGE<=70):
                print('your BAI is',BAI,'which means you are overweight.')
            elif(BAI>39 and 20<=AGE<=39) or (BAI>41 and 40<=AGE<=59) or (BAI>43 and 60<=AGE<=79):
                print('your BAI is',BAI,'which means you are abese.')
            else:
               print('there is an error with your input')
        elif GND=='MEN':
            if(BAI<8 and 20<=AGE<=39) or (BAI<11 and 40<=AGE<=59) or (BAI<13 and 60<=AGE<=79):
                print('your BAI is ',BAI,'which means you are underweight.')
            elif(8<=BAI <=21 and 20<=AGE<=39) or(11<=BAI<=23 and 40<=AGE<=59) or (13<=BAI<=25 and 60<=AGE<=79):
                print('your BAI is', BAI,'which means you are healthy.')
            elif(21<BAI<=26 and 20<=AGE<=39) or(23<BAI<=29 and 40<=AGE<=59) or (25<=BAI<=31 and 60<=AGE<=79):
                print('your BAI is',BAI,'which means you are overweight.')
            elif(BAI>26 and 20<=AGE<=39) or (BAI>29 and 40<=AGE<=59) or (BAI>31 and 60<=AGE<=79):
                print('your BAI is',BAI,'which means you are abese.')
            else:
                print('there is an error with your input')
        else:
            print("there is an error")
    elif unit=='imperial':
        GND = str(input('please enter your gender input string(Women or Men):'))
        AGE = int(input('please enter your age input interger(whole number):'))
        HM = float(input('please enter your hight input meters(decimals):'))
        HC = int(input('please enter your hip circumference input centimetres:'))
        BAIn = ((HC/((HM)**(1.5))))-18
        if GND =='Women':
            if(BAIn<21 and 20<= AGE<=39) or (BAIn<23 and 40<=AGE <=59) or (BAIn<25 and 60<=age<=79):
                print('your BAIn is ',BAIn,'which means you are underweight.')
            elif(21<=BAIn <=33 and 20<=AGE<=39) or(23<=BAIn<=35 and 40<=AGE<=59) or (25<=BAIn<=38 and 60<=AGE<=79):
                print('your BAIn is', BAIn,'which means you are healthy.')
            elif(33<BAIn<=39 and 20<=AGE<=39) or (35<BAIn<=41 and 40<=AGE<=59) or (38<BAIn<=43 and 60<=AGE<=70):
                print('your BAI is',BAI,'which means you are overweight.')
            elif(BAIn>39 and 20<=AGE<=39) or (BAIn>41 and 40<=AGE<=59) or (BAIn>43 and 60<=AGE<=79):
                print('your BAIn is',BAIn,'which means you are abese.')
            else:
               print('there is an error with your input')
        elif GND=='MEN':
            if(BAIn<8 and 20<=AGE<=39) or (BAIn<11 and 40<=AGE<=59) or (BAIn<13 and 60<=AGE<=79):
                print('your BAIn is ',BAIn,'which means you are underweight.')
            elif(8<=BAIn <=21 and 20<=AGE<=39) or(11<=BAIn<=23 and 40<=AGE<=59) or (13<=BAIn<=25 and 60<=AGE<=79):
                print('your BAIn is', BAIn,'which means you are healthy.')
            elif(21<BAIn<=26 and 20<=AGE<=39) or(23<BAIn<=29 and 40<=AGE<=59) or (25<=BAIn<=31 and 60<=AGE<=79):
                print('your BAIn is',BAIn,'which means you are overweight.')
            elif(BAIn>26 and 20<=AGE<=39) or (BAIn>29 and 40<=AGE<=59) or (BAIn>31 and 60<=AGE<=79):
                print('your BAIn is',BAIn,'which means you are abese.')
            else:
                print('there is an error with your input')
        else:
            print("there is an error")
    else:
         print("there is an error")
                
            
