- #### 创建仓库🙈🙉🙊

  选中目标文件夹，右键选择[Git Bash Here]() 而后输入

  **`git init`**

  目标结果：

  ```
  daichuan@DESKTOP-7VGEU18 MINGW64 /e/Python_projects/应用软件课程设计
  $ git init
  Initialized empty Git repository in E:/Python_projects/应用软件课程设计/.git/
  ```

- #### 添加与提交

  Git命令行中输入

  **`git add readme.txt`**  添加单个文件

  **`git add -A`**  添加全部文件

  **`git commit -m "版本名称"`**  提交添加的文件

  ```git
  daichuan@DESKTOP-7VGEU18 MINGW64 /e/Python_projects/应用软件课程设计 (master)
  $ git add -A
  The file will have its original line endings in your working directory
  
  daichuan@DESKTOP-7VGEU18 MINGW64 /e/Python_projects/应用软件课程设计 (master)
  $ git commit -m "git仓库搭建尝试1"
  [master (root-commit) 03f8d0b] git仓库搭建尝试1
   7 files changed, 52 insertions(+)
  ```

- #### 辅助命令：status、diff掌握仓库状态

  - 时刻掌握仓库当前的状态

  `git status`

  输出表示，`readme.txt`被修改过了，但还没有准备提交的修改。

  ```
  $ git status
  On branch master
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)
  
  	modified:   readme.txt
  
  no changes added to commit (use "git add" and/or "git commit -a")
  ```

  - 查看具体修改的内容

  `git diff`

































