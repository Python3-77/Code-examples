#!/usr/bin/env python3

#Didn't have to subclass this, but did just for example

from minedetector import MineField, stdout
from random import randrange as rr

class AutoGrid(MineField):

            def __init__(self, y, x, debug ):
                
                self.g ={}
                self.map = {}
                
                super(AutoGrid, self).__init__( x, y, debug )
               
            def make_grid(self):
                
                g = self.g

                for  i in  range(1,self.y+1):
                    
                    dots = ['.' for _ in range(self.x)]
            
                    g [i] = dots
                    
                if self.debug == 1 or self.debug == 2:
                    
                            self.show(self.g)    

            def add_random(self):
                
                m=self.map
                 
                for i in range(1,self.y+1):
                     
                     random_number = self.random_numbers()
                     m[i]=random_number
                     
                if self.debug ==  2:
                    
                            self.show(self.map)
                            
            def conf_grid(self):
                
                mine_location = self.random_mine_num_filtered()

                for row, location in self.map.items():
                            
                            data = [ '*' if char in mine_location else '.' for char in location ]
     
                            self.grid[row] = data
                            
                if self.debug  == 2:
                    
                            self.show(self.grid)
                                       
            def random_numbers(self):
                    
                    R = random_Row = []
                    
                    for _ in range ( self.x):
                        
                        random_number1 = rr ( self.x )
                        R.append(str(random_number1))
                        
                    return R
                
            def random_mine_num_filtered (self):
                
                    g = self.g

                    M = random_Mine = []
                    
                    for i in range( int (self.x/2)):
                        
                        random_number2 = rr ( self.x)
                        
                        if random_number2  not in M :
                        
                            M.append (str(random_number2))
                            
                    if self.debug is  2:
                        
                        stdout.write('\nRandom Mine Locations = : ')
                        
                        for i in M:
                            
                            stdout.write('{}, '.format(i))
                            
                        stdout.write('\n')
                        
                    return M

            
                             
           















