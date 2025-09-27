'''Pydantic Example'''
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    '''User model with validation'''
    name: str
    email: EmailStr
    age: int

def main(name="Alessander S. Goulart", email="sander@unixwork.com.br", age=50):
    '''Main function to create and display a User instance'''
    user = User(name=name, email=email, age=age)
    print(user.name)
    print(user.email)
    print(user.age)

if __name__ == "__main__":
    main()
