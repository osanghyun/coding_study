# opcode rD rA rB
# opcode rD rA #C
n = int(input())
inputs = [input().split() for _ in range(n)]

d = {
    'ADD': '00000',
    'ADDC': '00001',
    'SUB': '00010',
    'SUBC': '00011',
    'MOV': '00100',
    'MOVC': '00101',
    'AND': '00110',
    'ANDC': '00111',
    'OR': '01000',
    'ORC': '01001',
    'NOT': '01010',
    'MULT': '01100',
    'MULTC': '01101',
    'LSFTL': '01110',
    'LSFTLC': '01111',
    'LSFTR': '10000',
    'LSFTRC': '10001',
    'ASFTR': '10010',
    'ASFTRC': '10011',
    'RL': '10100',
    'RLC': '10101',
    'RR': '10110',
    'RRC': '10111'
}


def dec_to_bin(num: int, length: int) -> str:
    ret: str = ''
    while num != 0:
        ret = ret + str(num % 2)
        num //= 2
    ret = ret[::-1]

    while len(ret) < length:
        ret = '0' + ret

    return ret


answers = []

for inp in inputs:
    op = inp[0]
    rd = dec_to_bin(int(inp[1]), 3)
    if 'MOV' in op or op == 'NOT':
        ra = '000'
    else:
        ra = dec_to_bin(int(inp[2]), 3)

    if 'C' in op:
        rb = dec_to_bin(int(inp[3]), 4)
    else:
        rb = dec_to_bin(int(inp[3]), 3)
        rb = rb + '0'

    answers.append(d[op] + '0' + rd + ra + rb)

for answer in answers:
    print(answer)