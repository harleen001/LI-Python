for num in range(0,2001):
  sum=0
  fixing=num
  while fixing>0:
      n_num=fixing%10
      sum=sum+n_num**3
      fixing=fixing//10
      if num==sum:
         print(sum)