from linked_list_69 import LinkedList
from linked_list_69 import CircularList


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

	list3 = CircularList([1, 2, 3, 3, 4, 5])
	print(list3)
	#list3.circularListReverse()
	#print(list3)

"""def addAtEnd
def testIndexOutBoundsDoesNothing

def testAddToEmptyAList:
	# have an empt
	#"""