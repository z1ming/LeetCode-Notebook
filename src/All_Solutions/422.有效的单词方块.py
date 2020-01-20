# 给你一个单词序列，判断其是否形成了一个有效的单词方块。
#
# 有效的单词方块是指此由单词序列组成的文字方块的 第 k 行 和 第 k 列 (0 ≤ k < max(行数, 列数)) 所显示的字符串完全相同。
#
# 注意：
#
# 给定的单词数大于等于 1 且不超过 500。
# 单词长度大于等于 1 且不超过 500。
# 每个单词只包含小写英文字母 a-z。

/ **
* @ param
{string[]}
words
* @ return {boolean}
* /
var
validWordSquare = function(words)
{

// 1
x1
是有效方块
if (words.length === 1 & & words[0] == = "")
return true;
if (words.length === 1 & & words[0].length == = 1) return true;

// 第一行不等于第一列
不是有效方块
if (words.map(x= > x[0]).join('') !== words[0]) return false;

// 切除第一行和第一列
words = words.slice(1).map(x= > x.slice(1));

// 递归
return validWordSquare(words);
};