N = int(input().strip())
w={input().strip() for _ in range(N)}

def sorting_key(word):
    return (len(word), word)

sorted_w = sorted(w, key=sorting_key)

for word in sorted_w:
    print(word)