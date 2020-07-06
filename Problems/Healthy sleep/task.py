A = int(input())
B = int(input())
H = int(input())
if H > B:
    print("Excess")
if H < A:
    print("Deficiency")
if B >= H >= A:
    print("Normal")
