n = input()
arr = input()
arr = [int(s) for s in arr.split()] 
ans = []
for i in range(len(arr) - 1):
    if arr[i+1] == 1:
        ans.append(arr[i])
    else:
        if arr[i] > arr[i+1]:
            ans.append(arr[i])
ans.append(arr[-1])            
print(len(ans))
print(' '.join([str(i) for i in ans]))