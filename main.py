from time import sleep
from rich.traceback import install; install()
print("Hello World")
print("Mike B was here")
print("Hello class")
print("Andrew")
print("does replit actually work?")


def blam(name: str = "?") -> str:
    """
    Function to blamify something

    Args:
        name (str, optional): Thing to blamify. Defaults to "?".

    Returns:
        str: Status of blamification
    """
    
    print(f"Blamming {name}...")
    sleep(3)
    
    
    return f"{name} has been blammed!"



print("Hello World")
print(blam("Python"))

print(blam.__doc__)


try:
  if int(input()) == 1:
    print("Correct!")
  else:
    print("das da rong numba")
except:
  print("Invalid value")
  #Noah has been here


#Somachi: Test Comment