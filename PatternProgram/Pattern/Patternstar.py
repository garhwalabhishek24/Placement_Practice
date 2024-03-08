n=int(input("enter some nmber :"))
for i in range(n):
    print(" "*i+"* "*(n-i))
for i in range(n-1):
    print(" "*(n-2-i)+"* "*(i+2)) 
     
#enter some nmber :5
#* * * * * 
# * * * * 
#  * * * 
#   * * 
#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * *        