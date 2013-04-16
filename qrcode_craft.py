#! /usr/bin/python

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.connection as connection
import qrcode

def qrify(sx,sy,sz,msg,mc):
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=2,
	)
	qr.add_data(msg)
	qr.make(fit=True)
	
	# print sx+x, sy+y, data[x][y]

	mc.setBlock(0,4,0,block.STONE.id)

	data = qr.getMatrix()

	for x in range(0,len(data)):
		for y in range(0,len(data[x])):
			if(data[x][y]):
				mc.setBlock(sx+x,sy+y,sz,block.WOOL.id,15)
			else:
				mc.setBlock(sx+x,sy+y,sz,block.WOOL.id,0)

if __name__ == "__main__":
	mc = minecraft.Minecraft.create("192.168.1.100")
	mc.postToChat("Prepare yourself for a QR Code!")
	qrify(30,10,0,"It's the end of the world as we know it, and I feel fine.",mc)
