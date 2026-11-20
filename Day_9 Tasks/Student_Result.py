class Result:
    # Default parameter sub3 supports both 2 and 3 subjects
    def calculate_result(self, sub1, sub2, sub3=None):
        if sub3 is not None:
            total = sub1 + sub2 + sub3
            avg = total / 3
            print(f"3 Subjects -> Total: {total}, Average: {avg:.2f}")
        else:
            total = sub1 + sub2
            avg = total / 2
            print(f"2 Subjects -> Total: {total}, Average: {avg:.2f}")

res = Result()
res.calculate_result(85, 90)      # 2 subjects
res.calculate_result(85, 90, 95)  # 3 subjects