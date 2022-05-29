#...TTOWG!
# input statements

nx = int(input('Number of blocks in x-axis is'))
ny = int(input('Number of blocks in y-axis is'))
nz = int(input('Number of blocks in z-axis is'))
N = float(input('Initial value of oil in-place STOIIP in each block is'))
boi = float(input('Initial value of oil FVF is'))
Pb = float(input('Value of bubble point pressure is'))
bob = float(input('Value of oil FVF at bubble point pressure is'))
co = float(input('Value of oil compressibility is'))
ce = float(input('Value of effective compressibility is'))

# initializing output variable
total_np = 0
# the 'for' loops
for k in range(1,nz+1):
    for j in range(1,ny+1):
         for i in range(1,nx+1):
             block_n_order = ((k-1)*nx*ny) + ((nx*(j-1)) + i)
             Pi = float(input('What is the initial value of reservoir in layer {0}'.format(k)))
             Bo = float(input('What is the current value of FVF in layer {0}'.format(k)))
             Pnow = float(input('Value of pressure for Block {0}'.format(block_n_order)))
             block_np = (N*boi*ce*(Pi - Pnow))/Bo
             total_np = total_np + block_np
             print('The amount of oil produced from Block {0} is {1:.2f} STB'.format(block_n_order, block_np))
# displaying the results.
print('The total amount of oil produced from the entire reservoir is {0:.2f} STB'.format(total_np))                       

       
   
      
        
