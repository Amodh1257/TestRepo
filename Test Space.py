from time import sleep
from rich.traceback import install; install()
print("a")

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



try:
  if int(input()) == 1:
    print("Correct!")
  else:
    print("das da rong numba")
except:
  print("das not even a numba...")
