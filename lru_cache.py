# LRU (Least Recently Used) Cache Replacement Algorithm

capacity = 3
access_sequence = [4, 2, 1, 4, 3, 2, 5, 4]

cache = []
hits = 0
misses = 0

print("LRU Cache Replacement Algorithm")
print("-" * 65)
print(f"{'Block':<10}{'Status':<12}{'Removed':<12}{'Cache Contents'}")
print("-" * 65)

for block in access_sequence:

    removed = "-"

    if block in cache:
        # Cache hit: update the recent usage
        hits += 1
        cache.remove(block)
        cache.append(block)
        status = "HIT"

    else:
        # Cache miss
        misses += 1
        status = "MISS"

        if len(cache) == capacity:
            # Remove the least recently used block
            removed = cache.pop(0)

        cache.append(block)

    print(f"{block:<10}{status:<12}{str(removed):<12}{cache}")

print("-" * 65)

total_accesses = len(access_sequence)
hit_ratio = hits / total_accesses

print("Total accesses:", total_accesses)
print("Total hits:", hits)
print("Total misses:", misses)
print(f"Hit ratio: {hit_ratio:.4f}")
print(f"Hit ratio percentage: {hit_ratio * 100:.2f}%")