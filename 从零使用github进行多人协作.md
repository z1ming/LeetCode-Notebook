# 从零开始 Github 多人协作

### 前言

在 GitHub 上进行协同合作是每一位编程的小伙伴的必备技能，但是对于一些火热的开源项目，我们往往不知道该做何贡献，也对自己贡献的代码能否被采用感到信心不足，因此门槛较高。而在这里通过贡献自己的力扣代码，从普通的 pull request 开始参与协作，让每一位童鞋都能参与其中。操作简单门槛低，一起开始吧！

### 准备工作

1. [注册 github 账号](https://github.com/)

2. [安装版本控制工具 Git](https://git-scm.com/)

### 具体步骤

1. 进入习题集 [仓库](https://github.com/ML-ZimingMeng/LeetCode-Python3)，点击右上角 Fork，将仓库拉取 Fork 到自己的仓库内；

2. 先点击 Branch:master 按钮，再点击 english 按钮，将分支切换到 leetcoder 分支；

3. 点击 Clone or Download，然后在下拉列表中点击链接右侧的按钮，这时复制了仓库的链接；
   
4. 在本地目录（自己选择，比如桌面）右键，点击 Git Bash Here，输入 `git clone https://github.com/xxx(粘贴刚才复制的链接)`，回车；

5. 这时开始将仓库拉取到本地，当完成时就可以对本地文件进行修改了，比如增加代码、删除文件等；

6. 当对本地仓库文件修改完毕时，再次打开 Git Bash Here，输入以下行内容：（文字为解释，不要输入文字部分）

```c
git add .        // 将文件更新
git commit -m "original commit"   // 提交到分支，并添加说明
git push -u origin master leetcoder  // 将更新内容推送到分支 leetcoder 上
```

7. 回到自己 Fork 的仓库，切换到 leetcoder 分支上，点击 Branch:master 按钮右边的 New pull request，之后添加说明之后点击确定就可以等待作者是否接受您的更改啦！
