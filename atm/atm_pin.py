import time, os, pickle,re
import atm_binary
try:
   pin=5054
   amount=15000
   list1=['amount is 15000']
   i=3
   os.system('color 70')
   os.system('cls')
   print('Swipe your Card')
   #if possible provide some advertisements
   time.sleep(2)
   os.system('cls')
   print(f'''              
                           ATM Services
         ===================================================
         1--Balance Enquiry           Transaction History--4
         2--Cash Withdrawl                     Pin Change--5           
         3--Deposit
         ''')
   print()
   

   choice=eval(input('Enter Your choice:  '))
   if choice==1 or choice=='Balance Enquiry' or choice=='balance enquiry' or choice=='Balance enquiry' or choice=='balance Enquiry':
      print('=================BALANCE ENQUIRY==================')
      while i>0:
         
         pin1=int(input('Enter your Pin:  '))
         if pin1==pin:
            os.system('cls')
            print(f'Your available Balance is {amount}')
            break
         else:
            os.system('cls')
            print(f'you have {i} more chances')
            i-=1
      else:
         print('''        you have exceeded maximum limits, 
                        wait for 48 hours''')
   elif choice==2 or choice=='cash withdrawl' or choice=='cash Withdrawl' or choice=='Cash withdrawl' or choice=='Cash Withdrawl':
      while i>0:
         os.system('cls')
         pin2=int(input('Enter your Pin:  '))
         if pin2==pin:
            os.system('cls')
            withdrawl=int(input('Please Enter Withdrawl Amount : '))
            if withdrawl>amount:
               os.system('cls')
               print("""         Your Bank Balance is Low 
                              Please check the Balance and withdrawl your Amount""")
               break
            else:
               os.system('cls')
               amount-=withdrawl
               print(f"""Please collect the cash""")
               list1.append(f'withdrawl is {withdrawl} , balance is {amount}')
               break
         else:
            os.system('cls')
            print(f'you have {i} more chances')
            i-=1   
      else:
         os.system('cls')
         print('''        you have exceeded maximum limits, 
                        wait for 48 hours''')
   elif choice==3 or choice=='deposit' or choice=='Deposit' :
      while i>0:
         os.system('cls')
         pin3=int(input('Enter your Pin:  '))
         if pin3==pin:
            os.system('cls')
            deposit=int(input('Please Enter the deposit Amount ')) #the deposit amount is calculated on the basis of the cash 
            #here we entering the amount 
            amount+=deposit
            os.system('cls')
            list1.append(f'deposited amount is {deposit}, balance is {amount}')
            print(f'''You have deposited {deposit}
Your available Balance is {amount}''')
            time.sleep(10)
            break
         else:
            os.system('cls')
            print(f'you have {i} more chances')
            i-=1
      else:
         os.system('cls')
         print('''        you have exceeded maximum limits, 
                        wait for 48 hours''')
   elif choice==4 or choice=='transaction History' or choice=='Transaction history' or choice=='Transaction History' or choice=='transaction history' :
      while i>0:
         pin4=int(input('Enter your Pin:  '))
         if pin4==pin:
            os.system('cls')
            print('=========Transaction History===========')
            for i in list1:print(i)
            break
         else:
            os.system('cls')
            print(f'you have {i} more chances')
            i-=1
      else:
         os.system('cls')
         print('''        you have exceeded maximum limits, 
                        wait for 48 hours''')
   elif choice==5 or choice=='Pin Change' or choice=='Pin change' or choice=='pin Change' or choice=='pin change':
      os.system('cls')
      print('==========Pin Change============')
      con=input('If you confirm to change pin ( y/n ): ')
      if con=='y'or con=='Y':
         while i>0:
            pin5=int(input('Enter you Pin'))
            if pin==pin5:
               pin=int(input('Enter the New Pin : '))
            else:
               os.system('cls')
            print(f'you have {i} more chances')
            i-=1
         else:
            os.system('cls')
         print('''        you have exceeded maximum limits, 
                        wait for 48 hours''')
except (RuntimeError,SyntaxError) as e:
   print(e)
finally:
   print()
   print('THANK YOU FOR USING OUR ATM')
   