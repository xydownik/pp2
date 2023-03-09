from time import sleep
def delay(func, ms, *args):
  sleep(ms / 1000)
  return func(*args)

a = int(input())
b= int(input())

print(f"Square root of {a} after {b} miliseconds is", delay(lambda x: pow(x, 0.5) , b , a))
