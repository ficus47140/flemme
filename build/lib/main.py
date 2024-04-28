from cryptography.fernet import Fernet
import sys

def main():
  arg = sys.argv[1:]
  if len(arg) != 3:
    return 1
  key = Fernet(arg[0].encode("utf-8"))
  open(arg[2], "w").write(key.encrypt(arg[1]))
  return 0


if __name__ == "__main__":
  main()
