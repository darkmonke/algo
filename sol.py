def solution(hp):
    
     Ngen = hp // 5
     Lhp1 = hp % 5
     
     Nsol = Lhp1 // 3
     Lhp2 = Lhp1 % 3
     
     Nant= Lhp2
     
     total = Ngen + Nsol + Nant
     
     return total