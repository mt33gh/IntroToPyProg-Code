#4.1 Conditional Statements

# Run the following code:

p = 8      # or 4
q = 100
for i in range(20):    # i=0 to 19
    if p < 5:
        p += 5
        q -= 10
    print("i = ", i, "   p = ", p, "   q = ", q)
    p = p - 1
print("range(20)=",list(range(20)))

#time = 70
