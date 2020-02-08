from cryptography.fernet import Fernet
import os

def changeKey():
    key=Fernet.generate_key()
    _file=open('credentials','wb')
    _file.flush()
    _file.write(key)
    _file.close()
    return key
    
def changePass(id=None,pswd=None):
    changeKey()
    if pswd:
        _file=open('credentials','rb')
        key=_file.readline()  
        f=Fernet(key)
        _file.close()
        _file=open('credentials','ab')
        encid=f.encrypt(id.encode())
        encpass=f.encrypt(pswd.encode())
        _file.write("\n".encode()+encid)
        _file.write("\n".encode()+encpass)
        _file.close()

def getPass():
    _file=open('credentials','rb')
    lines=_file.readlines()
    _file.close()
    f=Fernet(lines[0])
    return f.decrypt(lines[2]).decode()

def getId():
    _file=open('credentials','rb')
    lines=_file.readlines()
    _file.close()
    f=Fernet(lines[0])
    return f.decrypt(lines[1]).decode()

if __name__ == "__main__":
    #if not initialized
    if not os.path.exists("credentials"):
        open('credentials','x')
        print("Enter id")
        id=input()
        print("Enter password")
        pswd=input()
        changePass(id,pswd)
    #if already initialized ask for reset/change
    else:
        print("Do you want to reset the password(Y/N):")
        ans=input().lower()
        if ans in ['y','yes']:
            os.remove('credentials')
            open('credentials','x')
            print("Enter new id")
            id=input()
            print("Enter new password")
            pswd=input()
            changePass(id,pswd)