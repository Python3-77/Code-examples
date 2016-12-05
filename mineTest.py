#!/usr/bin/env python3

from unittest import TestCase as TC, main as MM
from Mine.randgrid import MineField as MF, AutoGrid

class Grids(TC):

            Test_input ={
                
                        1:['*','*','*'],
                        2:['*','.','*'],
                        3:['*','*','*']
            }

            Test_grids ={
        
                        1 : {1:['*','*','*'],2:['*','0','*'],3:['*','*','*']},#prep(grid)-- '.'  to '0'
                        2 : {1:['*','*','*'],2:['*','2','*'],3:['*','*','*']},#scan(gridX)
                        3 : {1:['*','*','*'],2:['*','4','*'],3:['*','*','*']},#scan(gridY)
                        4 : {1:['*','*','*'],2:['*','8','*'],3:['*','*','*']},#scan(gridZ)

            }
            
           
                                        
            m=MF(3,3,3)
            n = AutoGrid(3,3,3)#there is no way for me to create an assertion case, the output is random
            
            Tg=Test_grids
            Ti = Test_input
            m.d=Ti
            
            def test_Auto_grid(self):
                 
                 self.n.make_grid()
                 self.n.add_random()
                 self.n.conf_grid()                
                 self.n.show(self.n.grid)#passes if it runs through methods without error
                        
            def test_Prep(self):
                    '''Prepares grid for integers'''

                    self.m.prep(self.m.d)
                    self.assertEqual(self.m.gridX,self.Tg[1])
                    
            def test_Scanner(self):
                
                self.m.scan()#4 functions called, one repeated  
                #Grids X Y Z Processed, Check results
                
             
            def test_XScan_grid(self):
                                            
                                            ''' X-Scan'''
                                                                                                
                                            self.assertEqual(self.m.gridX,self.Tg[2])
                                            
            def test_YScan_grid(self):
                      
                                            ''' Y-Scan'''
                                                        
                                            self.assertEqual(self.m.gridY,self.Tg[3])
                                            
            def test_ZScan_grid(self):
                      
                                            ''' Z-Scan'''
                                            
                                            self.assertEqual(self.m.gridZ,self.Tg[4])
                            
if __name__=='__main__':

                        MM()
                    
                                        

            

                    
