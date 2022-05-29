#...TTOWG!
# input statements

nx = int(input('Input the amount of blocks in x-axis'))
ny = int(input('Input the amount of blocks in y-axis'))
nz = int(input('Input the amount of blocks in z-axis'))
N = float(input('What is the initial value of oil in-place STOIIP in each block'))
Boi = float(input('What is the initial value of oil FVF'))
Pb = float(input('What is the value of bubble point pressure'))
Bob = float(input('What is the value of oil FVF at bubble point pressure'))
Co = float(input('What is the value of oil compressibility'))
Ce = float(input('What is the value of effective compressibility'))

# initializing output value
total_np = 0
# the 'for' loops
for k in range(1,nz+1):
    for j in range(1,ny+1):
         for i in range(1,nx+1):
             block_n_order = ((k-1)*nx*ny) + ((nx*(j-1)) + i)
             Pi = float(input('What is the initial value of reservoir in layer {0}'.format(k)))
             Bo = float(input('What is the current value of FVF in layer {0}'.format(k)))
             PNow = float(input('The value of pressure for Block {0}'.format(block_n_order)))
             block_np = (N*Boi*Ce*(Pi - PNow))/Bo
             total_np = total_np + block_np
             print('The amount of oil produced from Block {0} is {1:.2f} STB'.format(block_n_order, block_np))
# displaying the results.
print('The total amount of oil produced from the entire reservoir is {0:.2f} STB'.format(total_np))                       

       
   
      
