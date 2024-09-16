nx=int(input('Enter number of rows: '))
ny=int(input('Enter number of columns: '))
nz=int(input('Enter number of layers: '))
no=float(input('Enter N: '))
pb=float(input('Enter Pb: '))
bob=float(input('Enter Bob: '))
ce=float(input('Enter effective compressibility: '))
for k in range(1,nz+1):
    pi=float(input('Enter Pi for layer {0}: '.format(k)))
    boi=float(input('Enter Boi for layer {0}: '.format(k)))
    for j in range(1,ny+1):
        for i in range(1,nx+1):
            vc =((k-1)*nx*ny)+((j-1)*nx)+i
            pnow=float(input('Enter current reservoir pressure for Block {0}: '.format(vc)))
            BO=(bob)*(1-ce*(pnow-pb))
            NP=(no*boi*ce*(pi-pnow))/(BO)
            print('The cumulative amount of oil produced in the block is {0:.2f}'.format(NP))

        
    
            
            
        
        
        
