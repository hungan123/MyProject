class ChallengeClass:
    def FindTalent(self, A, B, C, D, E, F):
        group_A = list(map(int, A.split(',')))
        group_B = list(map(int, B.split(',')))
        group_C = list(map(int, C.split(',')))
        group_D = list(map(int, D.split(',')))
        group_E = list(map(int, E.split(',')))
        group_F = list(map(int, F.split(',')))

        group_A = self.screening1(group_A, group_B, group_C)
        group_D = self.screening1(group_D, group_E, group_F)

        group_A = self.screening2(group_A)
        group_B = self.screening2(group_B)
        group_C = self.screening2(group_C)
        group_D = self.screening2(group_D)
        group_E = self.screening2(group_E)
        group_F = self.screening2(group_F)

        group_ABC = group_A + group_B + group_C
        group_DEF = group_D + group_E + group_F
        group_ABC = self.screening3(group_ABC)
        group_DEF = self.screening3(group_DEF)

        final_group = set(group_ABC + group_DEF)
        return len(final_group)

    def screening1(self, group1, group2, group3):
        # Loại bỏ số đăng ký nhỏ nhất trong mỗi nhóm theo từng lượt 3 sinh viên một lần
        new_group1 = []
        for i in range(0, len(group1), 3):
            students = [group1[i], group2[i], group3[i]]
            min_value = min(students)
            if students[0] != min_value:
                new_group1.append(group1[i])
            if i + 1 < len(group1) and students[1] != min_value:
                new_group1.append(group1[i + 1])
            if i + 2 < len(group1) and students[2] != min_value:
                new_group1.append(group1[i + 2])
        return new_group1

    def screening2(self, group):
        min_value = min(group)
        max_value = max(group)
        product = 1
        for num in group:
            product *= num
        if product % (max_value - min_value) != 0:
            group.remove(min_value)
            group.remove(max_value)
        return group

    def screening3(self, group):
        counts = {}
        for num in group:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        new_group = [num for num in group if counts[num] != 3]
        return new_group


challenge = ChallengeClass()
result = challenge.FindTalent(
    "55,59,73,65,56,52,71,70,72,57,64,74,66,61,53,50,60,62,51,69,63,68,58,67,54",
    "60,51,69,53,74,73,61,66,70,55,72,71,54,56,65,58,63,68,64,59,50,52,67,62,57",
    "51,55,70,50,53,52,67,64,65,61,60,57,62,69,63,74,56,54,71,58,68,73,59,72,66",
    "70,74,63,58,55,54,61,68,52,56,59,66,65,62,53,60,51,72,64,50,57,73,71,67,69",
    "51,72,50,70,63,60,68,71,61,67,55,69,66,59,52,74,54,53,64,56,62,57,73,65,58",
    "67,71,51,62,56,55,64,57,70,52,66,74,69,50,59,65,58,73,72,53,63,54,68,61,60"
)
print(result)  # Kết quả sẽ là số lượng các số đăng ký khác nhau sau khi sàng lọc
