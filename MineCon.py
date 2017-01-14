#!/usr/bin/env python3

from autogrids import AutoGrid,stdout

def process(cont):

            ''' populate and display grid '''

            m.populate(cont)
            m.prep(cont)
            show_prox()
            
def show_prox ():

            ''' process grid '''
          
            m.scan()
            
            if not m.debug :
                
                    pause = input ( '''\n Press Enter To Continue, \n\t or Enter "q" To Quit........''')

                    if pause  == 'q':
                            
                            quit()
            
def bugs():

            db =100
            while db > 3 :
                
                    try:
                    
                        db = input('Selection? -> ')# re-asign db
                        stdout.write('\n')
                        
                        if db == 'rules':
                            
                                rules()

                        if db == 'q' :
                            
                                break
                            
                        if db in ('0','1','2','3',):# from this point db is an integer
                            
                            db=int(db)

                        if db==1 or db ==2:
                            
                            stdout.write(' \n\t<<===<<DEBUG>>===>>\n ')
                            
                        if db > 3:
                        
                            stdout.write(' \tThat\'s not one of the choices')
                            
                        if db ==3:
                            
                            stdout.write(' \n\t<<===<<TEST>>===>> \n')
                            
                            test()
                            stdout.write('')
                           
                    except:
                        
                        if (ValueError,TypeError):
                            
                            stdout.write('\n\tThat\'s not a number....')
                            db =100
                                   
            return db

def test():#import and run test

            from unittest import TextTestRunner, makeSuite
            from mineTest import Grids
          
            mine_detector = TextTestRunner()
            r=result = mine_detector.run(makeSuite(Grids))
            
            if r.errors :
                        
                for log in r.errors:
                    stdout.write(log)
            
            if r.failures :
                
                for log in r.failures:
                    stdout.write(log)
                    
if __name__ == '__main__' :

    rules=lambda: stdout.write('''

@Expected input :
\nType "rules" or "q" (quit) at any prompt.
\n\t "*" = Mine
\t "." = Blank-space
\n Output will show number of mines surounding "Blank" grid locations.
 Select "y" @ "Auto-Populate" to render a random grid with provided dimensions.
\n@ Selection Prompt;
 \n\t 0. Normal
\t 1. Debug 1 : Grid Manipulation
\t 2. Debug 2 : Grid Manipulation and Index Locations
\t 3. Test
    ''')
    test()
    rules()
    
    col = 0
    db=0

    while not col or db==0:

        stdout.write('\n     Grid Size : :')

        try:

            r = input('\nRows? -> ')
            
            if r is 'q':
                
                break
            
            if r == 'rules':
                
                rules()
                
            if not r:
                rows= 3
            else:
                rows = int(r)
            
            c = input('Columns? -> ')
            
            if c is 'q':
                
                break
            
            if c == 'rules':
                
                rules()
            else:
                    col = int(c)
            db=bugs()
            m = AutoGrid(col, rows,db)
            
            m.debug=db
                      
            if not m.debug :
                
                process(m.grid)
            
        except(ValueError):
                        
            stdout.write('\tThat\'s not a number, e.g(0,1,2,3,4,5...)')
                    

            




             
