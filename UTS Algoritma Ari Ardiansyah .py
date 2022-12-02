a = 5
for b in range(1, a+1):
   print(((a-b+1) * "* ") + ((b-1) * "  ") + ((b-1) * "  ") + (a-b+1) * "* ")

a = 5
for b in range(1, a+1):
    print((b * "* ") + (((a-b+1)-1) * "  ") + (((a-b+1)-1) * "  ") + (b * "* "))

a = 5
for b in range(1, a+1):
   print(((a-b+1) * "  ") + ((b-1) * "* ") + (b * "* ") + (a-b+1) * "  ")

a = 5
for b in range(1, a+1):
    print((b * "  ") + ((a-b+1) * "* ") + (((a-b+1)-1) * "* ") + (b * "  "))