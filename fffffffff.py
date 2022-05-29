#...TTOWG!
# input statements

nx = int(input('How many blocks there are in x-axis?'))
ny = int(input('How many blocks there are in y-axis?'))
nz = int(input('How many blocks there are in z-axis?'))
N = float(input('What is the value of initial oil in-place STOIIP in each block?'))
boi = float(input('What is the value of initial oil FVF?'))
Pb = float(input('What is the value of bubble point pressure?'))
bob = float(input('What is the value of oil FVF at bubble point pressure?'))
co = float(input('What is the value of oil compressibility?'))
ce = float(input('What is the value of effective compressibility?'))

# initializing output variable
total_np = 0
# the 'for' loops
for k in range (1,nz+1):
    for j in range(1,ny+1):
         for i in range(1,nx+1):
             block_n_order = ((k-1)*nx*ny) + (nx*(j-1)) + 1)
             Pi = float(input('what is the initial value of reservoir in layer {0}'.format(k)))
             Bo = float(input('what is the current value of FVF in layer {0}'.format(k)))
             Pnow = float(input('What is the current value of pressure for Block {0}?'.format(block_n_order)))
             block_np = (N*boi*ce*(Pi - Pnow))/bo
             total_np = total_np + block_np
             print('The cummulative oil produced from Block {0} is {1:.2f} STB'.format(block_n_order, block_np))
# displaying the results.
print('The total cummulative oil produced from the entire reservoir is {0:.2f} STB'.format(total_np))                       




        
   
