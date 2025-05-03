submitted = [int(input()) for _ in range(28)]  
all_students = set(range(1, 31))                
not_submitted = list(all_students - set(submitted)) 
not_submitted.sort()                          

print(not_submitted[0])
print(not_submitted[1])