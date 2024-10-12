from linked_list import LinkedList
from linked_list import CircularList


if __name__ == '__main__':

	list1 = LinkedList([1,2,3])
	print(list1)
	list1.add_back(4)
	list1.add_front(0)
	#print(list1.tail.data)
	print(list1)
	list1.remove_link(4)
	print(list1)
	list1.add_link_before(69, 0)
	list1.add_link_before(699, 5)
	print(list1)
	#list2 = LinkedList()
	#print(list2.get_front())
	#print(list2.get_back())
	print(list1.get_front())
	print(list1.get_back())
	#list1.remove_front() good
	#print(list1) good
	list1.remove_back()
	print(list1)
	#list3 = LinkedList()
	#print(list3.is_empty())
	print(list1.is_empty())
	print(list1.contains(3))
	print(list1.contains("rodizios"))
	list1.remove(3)
	print(list1)
	list1.remove_front()
	print(list1)

	#print(list1.tail.data)

	"""list1.remove_front()
	print(list1)
	print(list1.contains(2))

	list2 = LinkedList()
	list2.add_front('A')
	list2.add_front('B')
	list2.add_front('C')
	print(list2)"""

	list3 = CircularList([1, 2, 3,  4, 5])
	print(list3)
	#list3.circularListReverse() goood
	#list3.remove_link(5) # bad
	list3.add_link_before(69,5)
	list3.add_front(6999)
	print(list3)
	#list3.remove_back() good
	#list3.remove_front() # good
	list3.remove_link(7) ##uh hh
	list4 = CircularList()
	print(list3)
	list3.remove(50)
	print(list3)
	list4.add_front(1)
	list4.add_back(2)
	print(list4)
	print(list4.get_back()) # get front get back good
	list4.remove_front()
	print(list4)
	list5 = CircularList()
	print(list5.is_empty())
	print(list4.is_empty())
	print(list3.contains(69))

	"""c1 = CircularList(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
	c1.add_link_before('X', 7)
	print(c1)
	#for i in range(3):
		#print(c1)
		#c1.remove_front()
	#print(c1)"""

	c2 = CircularList(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
	c2.add_front('G')
	print(c2)
	c2.remove('G')
	print(c2)
	print(c2.remove_link(-9))


"""def addAtEnd
def testIndexOutBoundsDoesNothing

def testAddToEmptyAList:
	# have an empt
	#"""