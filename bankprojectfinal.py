d={'sudeep':1234,'yash':2345,'darshan':3456,'puneeth':4567}
dr={'sudeep':104500,'yash':79000,'darshan':34500,'puneeth':136000}
dnum={'sudeep':9902347424,'yash':9481159578,'puneeth':9448530493}
dn=['sudeep','yash','puneeth','darshan']



import sl4a
v=sl4a.Android()
def test():
  title = 'Welcome to PES banking:-)'
  message = ('Select your choice :')
  v.dialogCreateAlert(title, message)
  v.dialogSetPositiveButtonText('login')
  v.dialogSetNegativeButtonText('create mobile banking')
  v.dialogShow()
  global response
  response = v.dialogGetResponse().result
test()


if(response['which']=='negative'):
 u1=input('enter username :')
 if u1 in dn:
  p1=int(input('create a new pin:'))
  d[u1]=p1
  n1=int(input('enter mobile number:'))
  dnum[u1]=n1
  print("******************************************")
 else: 
  print('invalid username')
  
  
  
def transaction():
    to=input('enter the name of person to whom you want to tranfer money :')
    if to in dn:
      am=int(input('enter the amount to transfer:'))
      if am<dr[u]:
        dr[u]=dr[u]-am
        dr[to]=dr[to]+am
        print('your transaction is complete')
        print('your current balance is',dr[u])
      else:
        print('insufficient account balance')
    else:
      print('invalid name !')
      
      
def balance():
    print('your account balance is',dr[u])
    
    
    
def enter(u):
    print('select what you want to do :')
    print('a.Make a transaction')
    print('b.Check the balance')
    print('c.exit')
    ch=input('enter your choice:')
    if ch=='a':
      transaction()
    elif ch=='b':
      balance()
    elif ch=='c':
      exit()
    else:
      print('invalid choice')
      
     
     
def check():
 if u in d: 
    if int(p)==d[u]:
      print()
      enter(u)
    else:
      print("pin is incorrect")
      ask=input("do you want to reset your pin(y/n) :")
      if ask=='y':
         send()
      elif ask=='n':
         password()
      else:
         print('wrong input')     
 else:
    print("invalid username")
    
    
    
def user():
   global u
   u=input("enter username :")
   return(u)
   
   
def password():
   global p
   p=input("enter the pin :")
   check()

   
   
def send():
   import sl4a,random
   a=sl4a.Android()
   ans=str(dnum[u])
   tosend=str(random.randint(1000,9999))
   a.smsSend(ans,tosend)
   print('an OTP is sent to your mobile number')
   ch=input('enter the OTP received :')
   if(tosend==ch):
     np1=int(input('enter a new pin:'))
     np2=int(input('re enter the new pin:'))
     if(np1==np2):
       print('your pin is updated')
       d[u]=np1
       password()
       check()
     else:
       print('re entered pin does not match')
   else:
     print('entered OTP is wrong')
     
     
     
user()
password()
check()

   
      
  