import logging
import collections

################################# README ######################################
#
# Python dictionnary are used as a base for the nodes for fast child retrieval
# through arbitrary char-based key.
# The keys are one character only
#
# The current implementation is very efficient in retriaval, but the memory
# usage is not really optimized, as the path in the tree are fully developed.
#
################################# README ######################################

class NULL(object):
	'''
	Specific object to mark construction
	nodes that do not hold true ``value``

	'''
	pass

class TrieNode(object):

	__slots__ = ('value','children')

	def __init__(self, value=NULL):
		self.value = value
		self.children = dict()

	def __len__(self):
		'''
		Return the number of keys in the subtree rooted at this node.

		'''
		return (
			int(self.value is not NULL) +
			sum(len(child) for child in self.children.itervalues())
			)
				
	def __copy__(self):
		copy = self.__class__(self.value)
		copy_children = clone.children
		for key, value in self.children.iteritems():
			clone_children[key]= value.__copy__()
		return copy

	def __getstate__(self):
		return (self.value, self.children)

	def __setstate__(self, state):
		self.value, self.children = state

def _generator(node,parts):
	'''
	A generator function to go through the trie
	from a node with an iterator

	'''
	if node.value is not NULL:
		yield (''.join(parts), node.value)
	for part, child in node.children.iteritems():
		parts.append(part)
		for subresult in _generator(child,parts):
			yield subresult
		del parts[-1]


class Trie(collections.MutableMapping):
	'''
	A Trie implementation that can be used as a dictionnary

	'''

	# ______________ MutableMapping API __________________

	def __init__(self,*args, **kwargs):
		self._root = TrieNode()
		self.update(*args, **kwargs)

	def __len__(self):
		return len(self._root)

	def __setitem__(self,key,value):
		'''
		Put an item in the trie

		'''
		node = self._root
		for part in key:
			next = node.children.get(part)
			if next is None:
				node = node.children.setdefault(part, TrieNode())
			else:
				node = next
		node.value = value

	def __getitem__(self,key):
		node = self._root
		for part in key:
			node = node.children.get(part)
			if node is None:
				break

		if node is None or node.value is NULL:
			raise KeyError('%s is not in the trie' % str(key))

		return node.value

	def __delitem__(self,key):
		path = []
		node = self._root
		for part in key:
			path.append(node,part)
			node = node.children.get(part)
			if node is None:
				break
		if node is None or node.value is NULL:
			raise KeyError
		node.value = NULL

		# Removing all uneccessary nodes along the way
		while node.value is NULL and not node.children and path:
			node,part = path.pop()
			del node.children[part]		

	def __iter__(self):
		return self.iteritems()

	# _________________ Iterability API __________________


	def iteritems(self):
		'''
		Return an iterator over the trie's item 
		(``(key,value)`` tuples)

		'''
		parts = []
		return _generator(self._root,parts)

	def iterkeys(self):
		'''
		Return an iterator over this trie's keys.

		'''
		return (key for key,value in self.iteritems(prefix))

	def itervalues(self):
		'''
		Return an iterator over this trie's values.

		'''
		return (value for key,value in self.iteritems(prefix))

	# _________________ Trie specific func __________________


	def prefix(self,prefix):
		'''
		Return a list of key that have the given prefix

		'''
		if prefix is None:
			return []
		
		parts = []
		node = self._root
		for part in prefix:
			parts.append(part)
			node = node.children.get(part)
			if node is None:
				return []

		return _generator(node,parts)



if __name__ == '__main__':
	trie = Trie()
	trie['bla'] = 32
	trie['blabla'] = 12
	trie['blab'] = 40
	print len(trie)
	print trie['blab']
	test = [(key,value) for key,value in trie.prefix('bla')]
	print test
