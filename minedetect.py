#!/usr/bin/env python3

from sys import stdout

class MineField (object):
    
    ''' Maps the proximity of '*'s in grid '''

    def __init__ ( self, y,x, debug = 0 ) :
        
        self.x = x
        self.y = y
        self.debug=debug
        self.grid={}
        self.gridX={}
        self.gridY={}
        self.gridZ={}
        
        self.pause_q = lambda: input ( '''\n Press Enter To Continue,
        or Enter "q" To Quit........''')
        
        self.pause = lambda: input(' \nPress Enter to continue........')
        
        if self.debug and self.debug != 3:
            
            self.populate(self.grid)
            self.prep(self.grid)
            self.scan()
            
    def populate(self,cont):
        
        ''' populate grid'''
        
        if self.debug != 3:
            
            ap=input('Auto-Populate? y/n > ')
            
            if ap =="y" :
                
                            self.auto_populate()
            else:
                
                            rc=row_count=1
                            stdout.write('\n')
                            
                            while len(cont) != self.y:
                                
                                        data =input('Row {} '.format(rc))

                                        if data == "q":
                                            break
                                        
                                        if len(data) > self.x or len(data) < self.x :
                                            
                                                    stdout.write('Enter correct Column size\n')
                                                    continue
                                                
                                        data=[ '.' if char != '*' else char for char in data]
                                        contList=cont[rc]=data
                                        
                                        if self.debug == 1:
                                            print(contList)
                                        
                                        rc+=1
                                        
                            if data=='q':
                                
                                quit()
            
    def auto_populate(self):
        
        ''' Calls Sub-class AutoGrid's methods '''

        self.make_grid()
        self.add_random()
        self.conf_grid()

    def prep(self, cont):
        
        ''' Change dots to zeros '''
        
        if self.debug and self.debug!=3:
            stdout.write('\nPrepare grid')
        
        for key,value in cont.items():
            
                k,v=key,value
                for ch in v:
                        
                        if isinstance(v[0],list):
                            
                            zeros=[ i.replace ('.', '0') for i in v[0]]
                        else:
                            zeros=['0' if index =='.' else index for index in v ]
                            
                        self.gridX [k]=zeros
            
        if self.debug != 3:
             
            self.show(self.gridX)
            p=self.pause_q()
        
            if p  == 'q' :
                
                quit()

    def show(self,cont):
        
                    ''' Write container content to console'''
                    
                    stdout.write('\n')
                    space = '    '
                
                    for row, string in cont.items():
                        
                        for ch in string:
                            
                            if isinstance(ch,list):
                                
                                for i in ch:
                                    
                                    stdout.write('{}{}'.format(i,space))
                                    
                            else:
                                stdout.write('{}{}'.format(ch,space))
                            
                        stdout.write('\n')
            
    def scan(self):

            '''Scan grid'''
            
            gx=self.gridX
            gy=self.gridY
            gz=self.gridZ
            
            def X_Yscan(cont):
                
                ''' Scan x-horizontal axis'''
                
                if self.debug and self.debug!=3:
                    stdout.write('\nX-Y scan\n')
                
                for k,v in cont.items():
                    
                    c=0
                    
                    for ch in v:

                            #scan left side
                                        
                            if ch == '*' and c==0 and cont[k][c+1] != '*':
                                
                                if self.debug == 2:
                                    stdout.write('left\n')
                               
                                nvls=int(cont[k][c+1])
                                nvls+=1
                                cont[k][c+1]=str(nvls)
                        
                            #scan middle
                        
                            if ch == '*' and c != 0 and c != len(v)-1:
                                
                                    if self.debug == 2:
                                        stdout.write('middle\n')

                                    if cont[k][c-1] != '*':
                            
                                        nvr = int(cont[k][c-1])
                                        nvr +=1
                                        
                                        cont[k][c-1] = str(nvr)
                                
                                    if cont[k][c+1] != '*':
                         
                                        nvf = int(cont[k][c+1])
                                        nvf +=1

                                        cont[k][c+1] = str(nvf)
                                    
                            #scan right side
                                
                            if ch =='*' and c == len(v)-1 and cont[k][c-1] != '*':
                                if self.debug == 2:
                                    stdout.write('right\n')
                               
                                nvrs = int(cont[k][c-1])
                                nvrs +=1
                                
                                cont[k][c-1] = str(nvrs)
                                
                            c+=1
                            
                if self.debug and self.debug!=3:
                    
                    self.show(cont)
                    p=self.pause()
                    
                    if p  == 'q' :
                        quit()

            def Zscan(cont):
                
                '''Scan z-diagonal axis from all points'''
                
                if self.debug and self.debug!=3:                
                    stdout.write('\nZ-scan\n')
                
                for k,v in cont.items():
                    
                    c=0
                    
                    for ch in v:
                                     
                            #z-csan top-left corner
                        
                            if ch =='*' and k ==1 and c==0 and cont[k+1][c+1] !='*':
                                
                                if self.debug==2:
                                    
                                    stdout.write('top-left\n ')                                                                                             
                                
                                ndfLtL=int(cont[k+1][c+1])
                                ndfLtL+=1
                                
                                cont[k+1][c+1]=str(ndfLtL)
                                
                            #z-csan top
                                    
                            elif ch =='*' and k == 1 and c!= 0 and c !=len(v)-1:
                                
                                if self.debug == 2:
                                    stdout.write('top\n ')
                                
                                if cont[k+1][c-1] != '*':
                                   
                                    ndtrt = int(cont[k+1][c-1])
                                    ndtrt+=1
                                    
                                    cont[k+1][c-1]=str(ndtrt)

                                if cont[k+1][c+1]!='*':
                               
                                    ndtft=int(cont[k+1][c+1])
                                    ndtft+=1
                                    
                                    cont[k+1][c+1]=str(ndtft)
                                
                            #z-scan top right corner
                                
                            elif ch =='*' and k ==1 and c ==len(v)-1 \
                                 and cont[k+1][c-1] != '*':
                                
                                if self.debug == 2:
                                    stdout.write('top-right\n')
                                
                                ndrLtr=int(cont[k+1][c-1])
                                ndrLtr+=1
                                
                                cont[k+1][c-1]=str(ndrLtr)
                            
                            #d-csan left side
                                
                            elif ch =='*' and k !=1 and k != len(cont) and c==0:
                                
                                if self.debug == 2:
                                    stdout.write('left-side\n')
                                
                                if cont[k-1][c+1]!='*':
                               
                                    ndfuLs=int(cont[k-1][c+1])
                                    ndfuLs+=1
                                    
                                    cont[k-1][c+1]=str(ndfuLs)
                                
                                if cont[k+1][c+1]!='*':
                                   
                                    ndfLLs=int(cont[k+1][c+1])
                                    ndfLLs+=1

                                    cont[k+1][c+1]=str(ndfLLs)
                                    
                            #z-scan center
                                    
                            elif ch =='*' and k !=1 and k != len(cont) and c!=0 \
                                 and c !=len(v)-1:
                                
                                if self.debug == 2:
                                    stdout.write('center\n')
                                
                                if cont[k+1][c+1]!='*':
                                    
                                    if self.debug == 2:
                                        stdout.write("1c- lower-right\n")
                                    
                                    ndfL=int(cont[k+1][c+1])
                                    ndfL+=1
                                    
                                    cont[k+1][c+1]=str(ndfL)

                                if cont[k+1][c-1]!='*':
                                    
                                    if self.debug == 2:
                                        stdout.write("2c- lower-left\n")
                                    
                                    ndrL=int(cont[k+1][c-1])
                                    ndrL+=1
                                    
                                    cont[k+1][c-1]=str(ndrL)

                                if cont[k-1][c+1]!='*':
                                    
                                    if self.debug == 2:
                                        stdout.write("3c- upper-right\n")
                                    
                                    ndfu=int(cont[k-1][c+1])
                                    ndfu+=1
                                
                                    cont[k-1][c+1]=str(ndfu) 

                                if cont[k-1][c-1]!='*':
                                    
                                    if self.debug == 2:
                                        stdout.write("4c- upper-left\n")
                                    
                                    ndru=int(cont[k-1][c-1])
                                    ndru+=1
                                
                                    cont[k-1][c-1]=str(ndru)

                            #z-scan right side
                                    
                            elif ch =='*' and k !=1 and k != len(cont) and c ==len(v)-1:
                                
                                if self.debug == 2:
                                    
                                    stdout.write('right-side\n')
                                
                                if cont[k-1][c-1]!='*':
                             
                                    ndrurs=int(cont[k-1][c-1])
                                    ndrurs+=1
                                
                                    cont[k-1][c-1]=str(ndrurs)
                                
                                if cont[k+1][c-1]!='*':
                               
                                    ndrLrs=int(cont[k+1][c-1])
                                    ndrLrs+=1
                        
                                    cont[k+1][c-1]=str(ndrLrs)
                                    
                            #z-csan lower right corner
                                
                            elif ch =='*' and k == len(cont) and c ==len(v)-1 \
                                 and cont[k-1][c-1] != '*':
                                
                                if self.debug == 2:
                                    stdout.write('lower-right\n')
                                
                                ndrur=int(cont[k-1][c-1])
                                ndrur +=1
                                
                                cont[k-1][c-1]=str(ndrur)
                               
                            #z-csan bottom
                                    
                            elif ch =='*' and k == len(cont) and c != 0 and c !=len(v)-1:
                                
                                if self.debug == 2:
                                    stdout.write('bottom\n')
                                
                                if cont[k-1][c-1]!='*':
                                    
                                    ndbr=int(cont[k-1][c-1])
                                    ndbr+=1
                                    
                                    cont[k-1][c-1]=str(ndbr)

                                if cont[k-1][c+1]!='*':
                             
                                    ndbf=int(cont[k-1][c+1])
                                    ndbf+=1
                                
                                    cont[k-1][c+1]=str(ndbf)
                                    
                            #z-scan lower left corner
                                
                            elif ch =='*' and k == len(cont) and c==0 \
                                 and cont[k-1][c+1] != '*':
                                
                                if self.debug == 2:
                                    stdout.write('lower-left\n')                                                                                          
                                
                                ndfur=int(cont[k-1][c+1])
                                ndfur+=1
                                
                                cont[k-1][c+1]=str(ndfur)

                            c+=1
                                      
            def re_ordery():
                
                ''' Swap x / y '''

                if self.debug and self.debug!=3:
                    stdout.write('\nRe-order-to-y')
                
                c=0    
                while c < self.x:
                    swap=[]
                    
                    r=1
                 
                    while r <=self.y :
                        
                            swap.append(gx[r][c])
                            
                            r+=1
                            
                    gy[c+1]=swap
                    
                    c+=1
                    
                if self.debug and self.debug!=3:
                    
                    self.show(gy)
                    p=self.pause()
                    
                    if p  == 'q' :
                        
                        quit()
                        
            def re_orderxz():
                
                ''' Swap y / x '''

                if self.debug and self.debug!=3:
                    stdout.write('\nRe-order-to-x\n')
                    
                c=0
                
                while c < self.y:
                    swap=[]
                    
                    r=1
                 
                    while r <= self.x :
                        
                            swap.append(gy[r][c])
                            
                            r+=1
                            
                    gz[c+1]=swap
                    c+=1
                    
                if self.debug and self.debug!=3:
                    
                    self.show(gz)
                    
                    CP=self.pause()
                    
                    if CP  == 'q' :
                        quit()
                   
            X_Yscan(gx)
    
            re_ordery()
            X_Yscan(gy)
            
            re_orderxz()
            Zscan(gz)
            
            if self.debug != 3:
                self.show(gz)
            
# uncomment  following lines on Windows CMD, not sure if CMD will close after execution

##            if self.debug :
##               self.pause()






















                
