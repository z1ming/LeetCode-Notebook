# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment):
            """
            Check if the current segment is valid:
            1. less or equal to 255
            2. the first character could be '0'
                only if the segment is equal to '0'
            """
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):
            """
            Append the current list of segments
            to the list of solutions
            """
            # cur_pos 是指当前指针
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            """
            prev_pos:the position of the previously placed dot
            dots:number of dots to place
            """
            # 当前'.'可以加的位置curr_pos是上一个'.'的位置prev_pos+1到prev_pos + 4的位置
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)
                    # 如果所有3个.都放了
                    if dots - 1 == 0:
                        update_output(curr_pos)  # 添加到结果中
                    else:
                        backtrack(curr_pos, dots - 1)
                    segments.pop()  # 移除最后放的.

        n = len(s)
        output, segments = [], []
        backtrack()
        return output