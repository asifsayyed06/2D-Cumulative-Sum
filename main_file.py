arr=[
    [2,3,4],
    [5,6,7],
    [8,9,0]
]
rows=len(arr)
cols=len(arr[0])
prefix=[[0]*cols for _ in range(rows)]
for i in range(rows):
  for j in range (cols):
    prefix[i][j]=arr[i][j]
    if i>0:
      prefix [i][j]+=prefix[i-1][j]
    if j>0:
        prefix[i][j]+=prefix[i][j-1]
    if i>0 and j>0:
          prefix[i][j]-=prefix[i-1][j-1]
print("orginal arr")
for rows in arr:
  print(rows)
print("prefix sum",)
for rows in prefix:
  print(rows)
