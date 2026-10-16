class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = []
        dict1 = {}
        res = []
        for s in strs:
            list1.append("".join(sorted(s)))
        
        for i, s in enumerate(list1):
            if s not in dict1:
                dict1[s] = [i]
            elif s in dict1:
                dict1[s].append(i)
        
        for key, value in dict1.items():
            temp_list = []
            for i in value:
                temp_list.append(strs[i])

            res.append(temp_list)

        return res
        # for s in strs:
        #     temp_list = []
        #     for t in strs:
        #         if "".join(sorted(s)) == "".join(sorted(t)):
        #             temp_list.append(t)

        #     list1.append(temp_list)

        # return list1
