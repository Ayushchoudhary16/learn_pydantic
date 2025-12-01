from pydantic import validate_call,StrictInt,PositiveInt


@validate_call
def sum(a:StrictInt,b:PositiveInt):
    return a+b



res=sum(2,1)
print(res)
