# function decorator
def password(func):
    pwd = "3Tenfour"

    def wrapper(**kwargs):
        assert(kwargs["pwd"] == pwd), "Incorrect password."
        func(**kwargs)
    return wrapper


@password
def bank_account(**kwargs):
    print(f'Welcome, {kwargs["user_name"]}')


# bank_account(pwd="3Tenfour", user_name="Tokyo")

# class decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        try:
             assert(self.num_calls == 0 )  , "Line is busy"    
             self.func(*args, **kwargs)
             self.num_calls += 1
        except Exception as e:
            print(f'Error, {e}')




@CountCalls
def answerCall():
    print("FreeCodeCamp, how can we help you ?")


# answerCall()
# answerCall()
