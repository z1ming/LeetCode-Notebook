# 比较两个版本号 version1 和 version2。
# 如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
#
# 你可以假设版本字符串非空，并且只包含数字和 . 字符。
#
#  . 字符不代表小数点，而是用于分隔数字序列。
#
# 例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。
#
# 你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
#  
#
# 示例 1:
#
# 输入: version1 = "0.1", version2 = "1.1"
# 输出: -1

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) > len(v2):
            v2 = v2 + [0]*(len(v1) - len(v2))
        elif len(v2) > len(v1):
            v1 = v1 + [0] * (len(v2) - len(v1))
        i = 0
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1
        return 0
