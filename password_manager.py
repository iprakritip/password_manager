master_pwd = input("Whar is the master password? ")

def view():
    pass

view();

def add():
    name = input("Account name: ")
    pwd=input("Password: ")



while True:
  mode= input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
  if mode == 'q':
    break
  elif mode=='view':
    pass
  elif mode=='add':
    pass
  else:
    print("Invalid mode.") 
    continue
