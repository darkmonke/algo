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
        

# 1. denom1과 denom2를 같은 수로 만들기 위한 과정이 있어야 함(통분).
# 분모의 두 수를 곱하면 통분이 가능하지만 이럴 경우 약분하는 과정이 있어야 함.

# if문 여러 개 사용하기

# 두 가지 경우로 분리하기
# - 만약 한 분모가 다른 분모의 약수라면(코드:
# if denom2 % denom1 or denom1 % denom2 == 0:),
# 그 몫만큼 분모와 분자에 곱해라
# (denom1 * (denom2 // denom1)) or (denom2 * (denom1 // denom2) ==> 분자에 곱하는 과정도 있어야 함. 지금은 분모만 통분했음.

# - 두 수가 맞아떨어지지 않는다면 두 분모를 곱한 수로 통분해라(코드: 한 분모를 다른 분모로 나눈 나머지가 0이 아니라면)

# 2. 각 분모에 곱한 수를 분자에도 곱해야 함.

# 3. 그 후 기약 분수의 분모, 분자를 리스트에 넣어야 함.