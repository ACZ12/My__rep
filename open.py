try:
    with open("pyhmd.txt","a") as f:
        print(f.write("sdddddddsdsds"))
except FileNotFoundError:
    print("f n f")
finally:
    print("end")