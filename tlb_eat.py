# Program to calculate Effective Access Time (EAT) using TLB

# Given values
tlb_time = 10          # TLB lookup time in nanoseconds
memory_time = 80       # Main memory access time in nanoseconds

# Display the given values
print("Effective Access Time (EAT) Using TLB")
print("-" * 40)
print("TLB lookup time:", tlb_time, "ns")
print("Main memory access time:", memory_time, "ns")

# Calculate EAT for TLB hit ratio = 0.90
h1 = 0.90

eat1 = h1 * (tlb_time + memory_time) + \
       (1 - h1) * (tlb_time + 2 * memory_time)

print("\nFor TLB hit ratio =", h1)
print("Effective Access Time:", eat1, "ns")

# Calculate EAT for TLB hit ratio = 0.75
h2 = 0.75

eat2 = h2 * (tlb_time + memory_time) + \
       (1 - h2) * (tlb_time + 2 * memory_time)

print("\nFor TLB hit ratio =", h2)
print("Effective Access Time:", eat2, "ns")

# Compare both results
print("\nComparison")
if eat1 < eat2:
    print("Hit ratio 0.90 provides better performance.")
elif eat2 < eat1:
    print("Hit ratio 0.75 provides better performance.")
else:
    print("Both have the same effective access time.")