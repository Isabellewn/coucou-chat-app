import mongobd_oparations as db

global socket
global c_address

# Utility functions
def recive_from_client():
    message = socket.recv(1024).decode('utf-8')
    
    print(f"{c_address} Message \"{message}\" recived")
    
    return message

def send_to_client(message):
    print(f'{c_address} Message \"{message}\" sent')
    
    socket.send(message.encode('utf-8'))
    
    
def register_menu():
    username = recive_from_client()
    password = recive_from_client()
    # mongobd_oparations.register(username, password)
    # msg = "You have successfully registered.\nYour username is " + username + ", and your password is " + password + "."
    msg = db.register(username, password)
    send_to_client(msg)
    print(username)
    print(password)

        
        
      
def Login_menu():
    userName = recive_from_client()
    password = recive_from_client()
    
def Exit_menu():
    pass
    
def Menu():
    userInput = recive_from_client()
    if userInput == "1":
        register_menu()
    elif userInput == "2":
        Login_menu()
    elif userInput == "3":
        Exit_menu()

### APP
def app(client_socket, client_address):
    global socket
    global c_address
    socket = client_socket
    c_address = client_address
    
    while True:
        Menu()