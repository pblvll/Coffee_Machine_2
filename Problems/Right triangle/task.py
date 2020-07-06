class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
    # calculate the area here

    def get_area(self):
        return (0.5 * self.a) * self.b


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]
triangle = RightTriangle(input_c, input_a, input_b)
# write your code here
if input_a ** 2 + input_b ** 2 == input_c ** 2:
    print(RightTriangle.get_area(triangle))
else:
    print("Not right")
