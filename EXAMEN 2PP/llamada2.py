#!/usr/bin/python
# coding: utf-8

class Node( object ):
	def __init__( self, end_node = False ):
		self.end_node = end_node
		self.prefix_count = 0
		self.children = {}
	


class Trie( object ):
	def __init__( self ):
		self.root = Node()
	
	def insert( self, key ):
		current = self.root
		for k in key:
			if k not in current.children:
				current.children[k] = Node()
			current = current.children[k]
			current.prefix_count += 1
		current.end_node = True

	def enumerate( self, key ):
		current = self.root
		for k in key:
			if k not in current.children:
				return []
			current = current.children[k]
		
		return self._walk( current, key )	

	def _walk( self, root, prefix ):
		out = []
		if root.end_node:
			out.append( prefix )
		
		for ch in root.children:
			if isinstance( prefix, tuple ):
				tmp = self._walk( root.children[ch], prefix + (ch,) )
			elif isinstance( prefix, list ):
				tmp = self._walk( root.children[ch], prefix + [ch] )
			else:
				tmp = self._walk( root.children[ch], prefix + ch )
			out.extend( tmp )
		return out


n = int(input())
for x in range(n):
	numP = Trie()
	conts = {}
	numCont = int(input())
	for y in range(1,numCont+1):
		nom, num = input().split()
		conts [str(num)] = y
		numP.insert((str(num)))
	numM = input()
	resp = sorted(numP.enumerate((str(numM))))
	if resp == []:
		print("Activado")
	else:
		print(" ".join( [ str(conts.get(x)) for x in resp ] ))
	print(conts)


