def currency():

    while True:
        print("\n == Currency Converter == \n")

        quest0 = input ("Enter your currency \n"
                         "a) Dollars\n"
                         "b) Dirhams\n"
                         "c) Rubl\n>>> ")
        if quest0 == "a":
        
            quest1 = input(' == enter the currency you what to change == \n '
            
            "Choose:\n"
            "a) Dollars\n"
            "b) Dirhams\n"
            "c) Rubl\n>>> " )

            if quest1 == "a":
            
                print ('Sorry sir, unfortunately, you can not conver dollars to dollars')
                
                print (quest1)
                
    
                
            elif quest1 == 'b':
            
                amount = float(input("Enter the amount >>> "))
                
                task = int(amount * 3.672)
             
                print(task, 'dirhams')
                
                
        
            elif quest1 == "c": 
            
               amount = float(input("Enter the amount >>> ")) 
            
               task = int(amount * 80)
         
               print (task, "rubls")
            
            else:
                
                print ('You can only choose a , b or c options')
                
                continue
               
            quest3 = input ('\nDo you want to convert any other currency, yes/ no >>>')
               
            if quest3 == "yes" :
                   
                   continue
            else :
                  
                   print ("The currency successfully changed"
                          "\Thank you for working with us 😇")
                   break
        
        elif quest0 == "b":
        
            quest1 = input(' == enter the currency you what to change == \n '
            
            "Choose:\n"
            "a) Dollars\n"
            "b) Dirhams\n"
            "c) Rubl\n>>> " )

            if quest1 == "a":
            
                amount = float(input("Enter the amount >>> "))
            
                task = int(amount / 3.672)
         
                print(task, 'dollars')    
    
            elif quest1 == 'b':
            
                print ('Sorry sir, unfortunately, you can not convert dirhams to dirhams')
                    
                print (quest1)
                
                
        
            elif quest1 == "c": 
            
               amount = float(input("Enter the amount >>> ")) 
            
               task = amount * 22
         
               print (task, "rubls")
            
            else:
                
                print ('You can only choose a , b or c options')
                
                continue
               
            quest3 = input ('Do you want to convert any other currency, yes/ no >>>')
               
            if quest3 == "yes" :
                   
                   continue
            else :
                  
                   print ("The currency successfully changed"
                          "\Thank you for working with us 😇")
                   break
        
        elif quest0 == "c":
        
            quest1 = input(' == enter the currency you what to change == \n '
            
            "Choose:\n"
            "a) Dollars\n"
            "b) Dirhams\n"
            "c) Rubl\n>>> " )

            if quest1 == "a":
            
                amount = float(input("Enter the amount >>> "))
            
                task = amount / 0.045
         
                print(task, 'dollars')    
            
             
            elif quest1 == 'b':
            
                amount = float(input("Enter the amount >>> "))
            
                task = amount / 80
         
                print(task, 'dirhams')
                
        
            elif quest1 == "c": 
            
               print ('Sorry sir, unfortunately, you can not convert rubls to rubls')
                       
               print (quest1)
                   
            else:
                
                print ('You can only choose a , b or c options')
                
                continue
               
            quest3 = input ('Do you want to convert any other currency, yes/ no >>>')
               
            if quest3 == "yes" :
                   
                   continue
            else :
                  
                   print ("The currency successfully changed"
                          "\Thank you for working with us 😇")
                   break
        else:
           
            print ('You can only choose a , b or c options')
            
            continue
            
        
currency()