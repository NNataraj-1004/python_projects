database = {"malini": "123456", "sweet": "654321"}
username = input("Enter Your Username : ")
while True:
 for i in database.keys():
    if username == i:
        flag=1
        break
    else:
        flag=0
        
 if flag==1:
        password =input("Enter Your Password : ")
        while password!=database.get(i):
            print("your password is incorrect")
            password=input( "Re enter  your password:")
        print("Verified")
        break

            
 else:
      username=input("No data found : Re enter you name :")

