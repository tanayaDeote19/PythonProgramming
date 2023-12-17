def info(fx):
  def mfx(*args, **kwargs):
    print("Enter Your Info")
    fx(*args, **kwargs)
    print("Thanks for entering your info")
  return mfx

@info
def details(name,id,age):
    print(f"Hey.\nI am {name}.My id no. is {id} and I am {age} yrs old\n")


details("Tanaya",12,20)