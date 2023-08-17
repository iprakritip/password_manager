master_pwd = input("Whar is the master password? ")

def view():
    pass

view();

def add():
    name = input("Account name: ")
    pwd=input("Password: ")

    # open the password.txt file, append to it and close it. 
    # a is a mode called append. others are w-write, r-read.
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | '+ pwd + "\n")

while True:
  mode= input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
  if mode == 'q':
    break
  elif mode=='view':
    view();
  elif mode=='add':
    add();
  else:
    print("Invalid mode.") 
    continue
