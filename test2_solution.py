# ... to the only wise God


#     Function average_poro
def average_poro(pay_list, poro_list): # 0.5 marks for def; 0.5 marks for arguments
    numerator_sum = 0 # 0.5 marks
    denominator_sum = 0  # 0.5 marks
    for i in range(len(pay_list)):   # 1 mark
        numerator = poro_list[i] * pay_list[i]  # 1 mark
        numerator_sum = numerator_sum + numerator     # 0.5 marks
        denominator = pay_list[i]             
        denominator_sum = denominator_sum + denominator     # 0.5 marks
    avg_poro = round((numerator_sum/denominator_sum),4)        # 1 mark
    for j in range(len(poro_list)): # 0.5 marks (extra-point question)
        poro_list[j]  = avg_poro   # 0.5 marks (extra-point question)
    print(poro_list)
    return avg_poro                   # 1 mark



        

        

          

                       
