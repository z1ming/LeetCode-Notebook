# 从零开始 Github 多人协作

### 前言

在 GitHub 上进行协同合作是每一位编程的小伙伴的必备技能，但是对于一些火热的开源项目，我们往往不知道该做何贡献，也对自己贡献的代码能否被采用感到信心不足，因此门槛较高。而在这里通过贡献自己的力扣代码，从普通的 pull request 开始参与协作，让每一位童鞋都能参与其中。操作简单门槛低，一起开始吧！

### 准备工作

1. [注册 github 账号](https://github.com/)

2. [安装版本控制工具 Git](https://git-scm.com/)

> 如果无法下载 Git，请百度或者联系作者。

### 具体步骤

1. 进入习题集 [仓库](https://github.com/ML-ZimingMeng/LeetCode-Python3)，点击右上角 Fork，将仓库 Fork 到自己的仓库内；

![fig 1](https://i.loli.net/2020/03/01/UXNo8uv3VBnSqOz.png)

2. 先点击 Branch:master 按钮，在下拉列表中填写分支名称，并切换到该分支；

![fig 2](https://i.loli.net/2020/03/01/2gzZR4qeplMaGTJ.png)

在这里，创建了 newbranch 分支，如下图：

![fig 3](https://i.loli.net/2020/03/01/yq7CzYx8hdOuMfi.png)

3. 点击 Clone or Download，然后在下拉列表中点击链接右侧的按钮，这时复制了仓库的链接；
   
![fig 4](https://i.loli.net/2020/03/01/n53Q1AeWM6wuByI.png)

4. 在本地目录（自己选择，比如桌面）右键，点击 Git Bash Here：
   
![fig 5](https://i.loli.net/2020/03/01/z3CIZVyoSO14c5R.png)

输入 `git clone https://github.com/xxx(粘贴刚才复制的链接)`，回车：

![fig 6](https://i.loli.net/2020/03/01/8vSmycrT4h52E3B.png)

1. 这时开始将仓库拉取到本地，当完成时就可以对本地文件进行修改了，比如增加代码等；

2. 当对本地仓库文件修改完毕时，再次打开 Git Bash Here，输入以下行内容：（文字为解释，不要输入文字部分）

```c
git add .        // 将文件更新
git commit -m "original commit"   // 提交到分支，并添加说明
git push -u origin master english  // 将更新内容推送到分支 english 上
```

7. 回到自己 Fork 的仓库，切换到刚刚创建的分支上，点击 Branch:master 按钮右边的 New pull request：

![fig 7](https://i.loli.net/2020/03/01/LWef9CASuozI4Bx.png) 
 
之后添加说明之后点击确定就成功完成了一次您的提交！

### 接下来的工作

接下来可以在仓库的 issue 选项卡中进行提交是否符合规范等方面的讨论，事实上，有任何问题都可以在此进行讨论！

如果您的提交没有任何问题，您的提交将被合并！您将成为一名 contributor！