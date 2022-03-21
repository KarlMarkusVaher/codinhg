from tkinter import *
root = Tk(); root.geometry( "6000x4000" )
c = Canvas( root, width = 8000, height = 4000, bg = "white" ); c.pack()

class MainFrame:
    """Class to move an image on a Canvas screen ( Python 2.5 )"""
    def __init__( self, image0, image1 ):
        self.__image0 = image0
        self.__image1 = image1
        self.__x, self.__y = 250,250
        self.__picture0 = c.create_image( self.__x, self.__y,
                                          image =  self.__image0 )
        self.__picture1 = c.create_image( self.__x, self.__y,
                                          image =  self.__image1 )
        c.create_polygon((0, 100, 50, 0, 100, 100), fill="#4eccde")
        self.__move = False
        c.bind( "<Button-1>", self.startMovement )
        c.bind( "<ButtonRelease-1>", self.stopMovement )
        c.bind( "<Motion>", self.movement )

    def startMovement( self, event ):
        self.__move = True
        self.initi_x = c.canvasx(event.x) #Translate mouse x screen coordinate to canvas coordinate
        self.initi_y = c.canvasy(event.y) #Translate mouse y screen coordinate to canvas coordinate
        print('startMovement init', self.initi_x, self.initi_y)
        self.movingimage = c.find_closest(self.initi_x, self.initi_y, halo=5) # get canvas object ID of where mouse pointer is 
        print(self.movingimage)
        print(c.find_all()) # get all canvas objects ID 

    def stopMovement( self, event ):
        self.__move = False

    def movement( self, event ):
        if self.__move:
            end_x = c.canvasx(event.x) #Translate mouse x screen coordinate to canvas coordinate
            end_y = c.canvasy(event.y) #Translate mouse y screen coordinate to canvas coordinate
            print('movement end', end_x, end_y)
            deltax = end_x - self.initi_x #Find the difference
            deltay = end_y - self.initi_y
            print('movement delta', deltax, deltay)
            self.initi_x = end_x #Update previous current with new location
            self.initi_y = end_y
            print('movement init', self.initi_x, self.initi_y)
            c.move(self.movingimage, deltax, deltay) # move object

if __name__ == "__main__":      
    im0 = PhotoImage( file = "c:/Users/Karl-Markus/Pictures/Haug/Haug.png" )
    im1 = PhotoImage( file = "c:/Users/Karl-Markus/Pictures/Haug/wall.png" )
#     im2 = PhotoImage( file = "giphy.gif" )
    m = MainFrame( im0, im1)
    mainloop()