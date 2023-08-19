import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
import atexit
from app_logic import Logic

from Ui_search import Ui_Dialog 

class SearchApp(QDialog):
    def __init__(self):
        try:
            ### 使用search.ui
            # super(SearchApp, self).__init__()
            # uic.loadUi('UI\search.ui', self)  # 用正确的路径替换 'path_to_search.ui'

            ### 使用Ui_search.py
            super().__init__()
            # 初始化 UI
            self.ui = Ui_Dialog()  # 使用导入的 Ui_MainWindow 类
            self.ui.setupUi(self)  # 设置 UI
            self.logic = Logic()

            # 连接按钮的点击事件到相应的槽函数
            self.ui.folderButton.clicked.connect(self.choose_folder)
            self.ui.showcontentButton.clicked.connect(self.show_content)
        except Exception as e:
            print(f"Init Error: {e}")

    @pyqtSlot()
    def choose_folder(self):
        """
        处理选择文件夹按钮的点击事件。
        """
        # 定义获取关键词的函数
        def get_keywords():
            return self.ui.textEdit.toPlainText().split(',')
        # 定义搜索文件的函数
        def search_files(keywords):
            # 返回文件列表，每个元素是一个元组 (file_path, keyword_list)
            # return [(file_path,keyword_list)]
            return self.logic.search_files(self.folder_path, keywords)
        # 定义显示搜索结果的函数
        def show_result(found_files):
            self.ui.result_list.clear()
            for file in found_files:
                self.ui.result_list.addItem(str(file[0])+"  包含关键词  "+ ' , '.join(file[1]))

        try:
            # 获取用户选择的文件夹路径
            folder_path = self.get_folder_path()
            if folder_path:
                self.folder_path = folder_path
                # 获取关键词
                self.keywords = get_keywords()

                # 关键词获取成功，查找含有关键词的文件
                if not self.keywords:
                    self.show_message("错误", "请输入关键词")
                    return
                self.found_files = search_files(self.keywords)

                # 文件查找成功，输出结果
                if not self.found_files:
                    self.show_message("结果", "未找到包含关键词的文件")
                    return
                show_result(self.found_files)

            else:
                self.show_message("错误", "请选择文件夹")
                return
        except Exception as e:
            print(f"Error Choose Folder: {e}")
            return []
        

    @pyqtSlot()
    def show_content(self):
        """
        处理显示内容按钮的点击事件。
        """
        # 定义高亮关键词的函数
        def highlight_pdf(path,keywords):
            self.logic.highlight_keywords(path, keywords)
        def highlight_docx(path,keywords):
            self.logic.highlight_keywords_in_docx(path, keywords)
        # 定义显示文本内容的函数
        def show_text(path,keywords):
            lines_with_keywords = self.logic.search_keywords_in_file(path, keywords)
            self.ui.textBrowser.clear()
            for line_num, line in lines_with_keywords:
                self.ui.textBrowser.append(f"{line_num}: {line}")

        # try:
        # 获取用户选中的结果索引
        selected_index = self.ui.result_list.currentRow()
        if selected_index<0:
            return
    
        selected_path = self.found_files[selected_index][0]
        selected_keywords = self.found_files[selected_index][1]

        # 根据是否勾选选择，已勾选，高亮并打开临时文件
        # 否则，直接显示文本内容
        if self.ui.checkBox.isChecked() and selected_path.endswith('.pdf'):
            highlight_pdf(selected_path, selected_keywords)
        # elif self.ui.checkBox.isChecked() and selected_path.endswith('.docx'):
        #     highlight_docx(selected_path, selected_keywords)
        else:
            show_text(selected_path, selected_keywords)
        # except Exception as e:
        #     print(f"Error Show Content: {e}")
        #     return []


    def get_folder_path(self):
        return QFileDialog.getExistingDirectory(self, "选择文件夹")

    def show_message(self, title, message):
        """
        显示消息框。
        """
        QMessageBox.warning(self, title, message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    search_app = SearchApp()
    search_app.show()
    atexit.register(search_app.logic.cleanup_temp_folder) # 清理临时文件夹
    sys.exit(app.exec_())
