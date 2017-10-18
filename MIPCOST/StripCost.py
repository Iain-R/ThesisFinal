from MIPBlock import Block
import json
from DraglineClass import Dragline
class Strip:
	def __init__(self,Mine,Spoil,Dragline):
		self.Mine = Mine
		self.Spoil = Spoil
		self.Dragline = Dragline
		self.Blk = Block(self.Mine,self.Spoil,self.Dragline)
		self.dict = {}
		self.count = 0

	def BlockSettings(self,spoilcap,swell,expand):
		self.Blk.set_spoilvals(spoilcap,swell,expand)

	def DP(self,position,end,spoil):
		self.count +=1
		print("Resource Constrained Dynamic Program \t Called:\t",self.count,'  times')
		print("Distance Remainging  :\t" ,end-position)
		if position>end-self.Dragline.get_minBlock():
			return (10000000000000000000000000,0,[])

		if position == end:
			return (0,0,[])
		# if end <= position:
			# self.dict[position,end,str(spoil)] = 100000000
			# return self.dict[position,end,str(spoil)]
		if (position,end,str(spoil)) not in self.dict:
			self.dict[position,end,str(spoil)] = min((10000+self.Blk.BlockCost(position,position+Action,spoil)[0]+
				self.DP(position+Action,end,self.Blk.BlockCost(position,position+Action,spoil)[1])[0]
				,Action,self.Blk.BlockCost(position,position+Action,spoil)[1])
			for Action in range(self.Dragline.get_minBlock(),self.Dragline.get_maxBlock()))
		return self.dict[position,end,str(spoil)]

	def GetDict(self):
		return self.dict
	def SaveDict(self,filename='RCDP_Out.txt'):
		json.dump(self.dict, open(filename,'w'))

	def LoadDict(self,filename='RCDP_Out.txt'):
		self.dict = json.load(open(filename))

	def ReturnOptimalSolution(self):
		return None 

	def printRange(self):
		print(self.Dragline.get_minBlock(),self.Dragline.get_maxBlock())




