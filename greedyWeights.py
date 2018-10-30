import sorting
import logging,sys
logging.basicConfig(stream=sys.stderr,level=logging.WARNING)
def mineffort1(weights):
	G=[]
	cumulative_weight=0
	sorting.quick_sort(weights,0,n-1)
	for i in range(len(weights)):
		cumulative_weight+=weights[i][1]
		G.append(cumulative_weight)
		print("Floor(",i,") : Adding w[",weights[i][0],"] = ",weights[i][1]," to bag. G[",i,"] = ",cumulative_weight)
		print("Total Effort = ",sum(G))
"""
Here, the weights are sorted and took according to increasing weights.
w(i)<w(j) for floor i<j
if we are taking a weight such that it is not the minimum weight available,
then that weight should be carried through each floor. So cumulative weight
will be more than optimum value. Hence this approach will minimize total effort.
"""
def min_heapify(A,i):
	l=i*2+1#left child
	r=i*2+2#right child
	smallest=i
	if l<=extract_min.heap_size and A[i][1]>A[l][1]:
		smallest=l
	if r<=extract_min .heap_size and A[r][1]<A[smallest][1]:
		smallest=r
	if smallest!=i:
		A[i],A[smallest]=A[smallest],A[i]
		min_heapify(A,smallest)
def build_min_heap(A):
	for i in range((len(A)-1)//2,-1,-1):
		min_heapify(A,i)
		logging.debug("build_min_heap : "+str(A))
	logging.debug("min_heap : "+str(A))

def extract_min(A):
	if extract_min.heap_size<0:
		return "!"
	minimum=A[0]
	A[0]=A[extract_min.heap_size]
	del A[-1]
	extract_min.heap_size-=1
	min_heapify(A,0)
	return minimum
def heap_insert(A,item):
	A.append(item)
	extract_min.heap_size+=1#heap size is stored in extract_min function
	logging.debug("heap_insert: heap_size= "+str(extract_min.heap_size))
	i=extract_min.heap_size
	while i>=1 and A[(i-1)//2][1]>A[i][1]:#compare with parent
		A[(i-1)//2],A[i]=A[i],A[(i-1)//2]
		i=(i-1)//2
def mineffort2(weights,floors):
	extract_min.heap_size=len(weights)-1
	cumulative_weight=0
	#weight is list of weights in format[floor,weight,'W' or 'G']
	build_min_heap(weights)
	#initially take the weight
	taken1=extract_min(weights)
	newItem=[0,taken1[1],'G']
	print("Floor(0) : Adding w[",taken1[0],"] = ",taken1[-1]," to bag, G[ 0 ]=",newItem[1])
	cumulative_weight+=newItem[1]
	heap_insert(weights,newItem)
	logging.debug("floor1"+str(weights))
	for i in range(1,floors):
		print("Floor("+str(i)+") : ",end="")
		logging.debug("before taking : "+str(weights))
		taken1=extract_min(weights)
		taken2=extract_min(weights)

		deposited=0
		if (taken1[-1]=='G' and taken1[0]==i-1) or (taken2[-1]=='G' and taken2[0]==i-1):
			deposited=0#G from previous floor is not deposited
		else:
			print("Depositing G["+str(i-1)+"] = "+str(newItem[1]))
			deposited=1
		print("Adding ",end="")
		if deposited==0:
			if taken1[-1]=='G' and taken1[0]==i-1:
				print(taken2[-1],"[",taken2[0],"] = ",taken2[1],end=" ")
			else:
				print(taken1[-1],"[",taken1[0],"] = ",taken1[1],end=" ")
		else:
			print(taken1[-1],"[",taken1[0],"] = ",taken1[1],end=", ")
			print(taken2[-1],"[",taken2[0],"] = ",taken2[1],end=" ")
		newItem=[i,taken1[1]+taken2[1],'G']
		heap_insert(weights,newItem)
		cumulative_weight+=newItem[1]
		print(" to bag, G[",i,"] = ",newItem[1])
	print("Total Effort = "+str(cumulative_weight))

if __name__=='__main__':
	n=int(input("Enter number of floors: "))
	print("Enter the weights : ")
	weights=[]
	for i in range(1,n+1):
	    temp=int(input())
	    weights.append([i,temp,'W'])
	print("\n######Part 1######")
	mineffort1(weights)
	print("\n######Part 2######")
	mineffort2(weights,len(weights))
