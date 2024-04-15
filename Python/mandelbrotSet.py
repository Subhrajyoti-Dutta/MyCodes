import numpy as np
from PIL import Image

class Mandelbrot():
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.center = (-0.5,0)
		self.ratio = self.height / self.width
		self.xLength = 3
		self.yLength = 3 * self.ratio
		self._computeLimits()
		
	def _computeLimits(self):
		self.xRange = (self.center[0] - self.xLength / 2, self.center[0] + self.xLength / 2)
		self.yRange = (self.center[1] - self.yLength / 2, self.center[1] + self.yLength / 2)

	def changeCenter(self, center):
		self.center = center
		self._computeLimits()

	def changeLength(self, xLength = None, yLength = None):
		assert ((xLength is None) ^ (yLength is None))
		if xLength is not None:
			self.xLength = xLength
			self.yLength = xLength * self.ratio
		else:
			self.yLength = yLength
			self.xLength = xLength / self.ratio
		self._computeLimits()

	def changeRange(self, xRange = None, yRange = None):
		print("Not Recommended")
		if xRange is not None:
			self.xRange = xRange
		if yRange is not None:
			self.xRange = yRange
		self.center = ((self.xRange[0] + self.xRange[1]) / 2, (self.yRange[0] + self.yRange[1]) / 2)
		self.xLength = self.xRange[1] - self.xRange[0]
		self.yLength = self.yRange[1] - self.yRange[0]
		self.ratio = self.yLength / self.xLength

	def defaultSetting(self):
		self.center = (-0.5,0)
		self.xLength = 3
		self.yLength = 3 * self.height / self.width
		self._computeLimits()

	def initialize(self):
		xAxis = np.linspace(self.xRange[0], self.xRange[1], self.width ).reshape(1,-1)
		yAxis = np.linspace(self.yRange[1], self.yRange[0], self.height).reshape(-1,1)
		self.c = xAxis + yAxis * 1j
		self.z = self.c.copy()
		self.prevNotLargerThan2 = np.full(self.z.shape, fill_value = True, dtype = np.bool)
		self.divIter = np.zeros(self.z.shape, dtype = np.uint8)
		# print(self.z.shape)

	def execute(self, iter):
		for i in range(iter):
			self.z[self.prevNotLargerThan2] = self.z[self.prevNotLargerThan2]**2 + self.c[self.prevNotLargerThan2]
			largerThan2 = np.abs(self.z) > 2
			self.divIter[largerThan2 & self.prevNotLargerThan2] = i
			self.prevNotLargerThan2 = ~largerThan2

	def createImage(self, imageName, location = ""):
		RGB = [self.divIter % 4 * 64, self.divIter % 8 * 32, self.divIter % 16 * 16]
		self.img = np.stack(RGB, 2)
		print(self.img.dtype)
		img = Image.fromarray(self.img)
		img.save(location + imageName)
		# print(self.img.shape)



if __name__ == '__main__':
	mandelbrotSet = Mandelbrot(1000,1000)
	mandelbrotSet.initialize()
	mandelbrotSet.execute(iter = 100)
	mandelbrotSet.createImage(imageName = "img.png")