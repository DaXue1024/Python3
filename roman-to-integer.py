class Solution:
    def romanToInt(self, s: str) -> int:
        list1=['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
        list2=['1','5','10','50','100','500','1000','4','9','40','90','400','900']
        spectial_list=['IV','IX','XL','XC','CD','CM']
        dict1=dict(zip(list1,list2))
        sum1 = 0
        for i in range(0,len(s)):
            if s[i:i+2] in spectial_list:
                a = int((dict1[s[i:i+2]])) - int((dict1[s[i+1]]))
            else:
                a = int(dict1[s[i]])
            sum1 = sum1 + a
        return (sum1)