#
#

def genericMain(
        *args,
        **kwargs,
):
    print(f"genericMain(Args):")
    print(f"{args}")
    print(f"genericMain(KWArgs):")
    print(f"{kwargs}")

    for key, value in kwargs.items():
      print(key, "->", value)
    print(f"In moduleMain")
