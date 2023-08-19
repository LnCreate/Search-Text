# Search-Text
一个用来帮助我的考研朋友在某文件夹下的所有文件中搜索指定关键词的python项目

- 该项目目前可以在根目录的所有文件中寻找多个关键词，支持的文件格式有txt，docx，pptx，pdf

- 对于PDF，在以上功能基础上，可以实现对含关键词的页面的截取和关键词高亮，并将其存储在临时文件夹中，临时文件夹会在程序运行结束后自动删除

### 文件项目
```text
D:\GIT_PROJECT\SEARCH-TEXT
│  app_logic.py
│  main.py
│  Ui_search.py
│
├─dist
│      main.exe
│
└─UI
      search.ui

其中, app_logic.py为代码运行逻辑
Ui_search.py为QT5生成的设计界面
main.py为主程序，将设计界面和代码进行关联绑定
dist\main.exe为pyinstaller生成的可执行文件
```
### 使用介绍

1.  输入关键词（多个关键词以","分隔），然后点击“选择文件夹”按钮选择搜索根目录

  <img src="https://github.com/LnCreate/Search-Text/assets/80500908/aa112dbc-687b-4849-8a9d-da6e3d364cbd" alt="image" style="zoom:50%;" />

2.  获得搜索结果，格式为”{文件路径} 包含关键词 {关键词1,关键词2......}

  <img src="https://github.com/LnCreate/Search-Text/assets/80500908/6e8d9636-3286-43bd-b15c-de38c7707bfa" alt="image" style="zoom:50%;" />

3. 选择要打开的文件，若“是否打开pdf并高亮”没有勾选，点按“显示内容”按钮，在下方文本框中显示检索到的含有关键词的文本

   <img src="https://github.com/LnCreate/Search-Text/assets/80500908/5da9e28e-245a-442d-9a6d-61c26432750d" alt="image" style="zoom:50%;" />

4. 若点按”显示内容“时，已勾选“是否打开pdf并高亮”，则会创建临时文件以获取PDF中的含关键词页面并高亮关键词（目前只针对pdf，对其他格式文件勾选项无用，都会按3执行）

   <img src="https://github.com/LnCreate/Search-Text/assets/80500908/189e6c56-f360-4bca-9d59-c9f3e0dbd155" alt="image" style="zoom:50%;" />

   <img src="https://github.com/LnCreate/Search-Text/assets/80500908/c7bed238-4282-4c65-9083-ddcf92117a58" alt="image" style="zoom:50%;" />

### 更新
