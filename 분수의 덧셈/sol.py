def solution(numer1, denom1, numer2, denom2):
    
    # denom2가 denom1의 약수고, 어느 분모도 1이 아닌 경우
    if denom1 % denom2 == 0 and denom1 != 1  and denom2 != 1:
        new_denom1 = denom2 * (denom1 // denom2)
        new_numer1 = numer2 * (denom1 // denom2) + numer1
        new_frac1 = [new_numer1, new_denom1]
        return new_frac1

    # denom1이 denom2의 약수고, 어느 분모도 1이 아닌 경우
    elif denom2 % denom1 == 0 and denom1 != 1  and denom2 != 1:
        new_denom2 = denom1 * (denom2 // denom1)
        new_numer2 = numer1 * (denom2 // denom1) + numer2
        new_frac2 = [new_numer2, new_denom2]
        return new_frac2
    
    # denom1이 denom2의 약수고, denom2가 1인 경우
    elif denom2 % denom1 == 0 and denom1 != 1 and denom2 == 1:
        new_denom3 = denom2 * denom1
        new_numer3 = numer2 * denom1 + numer1
        new_frac3 = [new_numer3, new_denom3]
        return new_frac3
    
    
    # denom1이 denom2의 약수고, denom1이 1인 경우
    elif denom2 % denom1 == 0 and denom1 == 1 and denom2 != 1:
        new_denom4 = denom2 * denom1
        new_numer4 = numer1 * denom2 + numer2
        new_frac4 = [new_numer4, new_denom4]
        return new_frac4
    
    # 어느 분모도 서로의 약수가 아닌 경우
    elif denom1 % denom2 != 0 or denom2 % denom1 != 0:
        new_denom5 = denom1 * denom2
        new_numer5 = numer1 * denom2 + numer2 * denom1
        new_frac5 = [new_numer5, new_denom5]
        return new_frac5
    
    # 두 분자의 분모가 모두 1인 경우
    elif denom1 == 1 and denom2 == 1:
        new_frac6 = [numer1 + numer2, 1]
        return new_frac6
        

# 오류 이유 추정
# denom1과 numer1, denom2와 numer2가 각각 약분되는 경우를 고려하지 않음.