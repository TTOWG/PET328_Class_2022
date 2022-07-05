#...TTOWG!
 
def oilfvf_calc(bob, co, pb, p, step = 100):
    # 1 mark for def and list of arguments
    # 1 mark for defaulting step to 100
                            
    import math # 0.5 mark
    counter  = 0 # 0.5 mark (extra-point question)
    while p > pb: # 1 mark
        bo = bob*(math.exp(co*(pb-p)))
        p = p - step # 0.5 mark
        counter = counter + 1 # 1mark (extra-point question)

    print(bo) # 0.5 mark
    print("Bubble point pressure raeched after {0} iterations".format(counter) ) # 1 mark (extra-point question)
    return bo # 0.5 marks
    
