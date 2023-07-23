# -*- coding=utf-8 -*-
#!/usr/bin/env python3

import string
from email import header
import math
import random
import labels
import os
from reportlab.graphics import shapes
# import prettytable
from prettytable import PrettyTable, MSWORD_FRIENDLY, ALL
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont


class SchulteGrid():
    def __init__(self) -> None:
        pass

    def GenNumbers(self, size_):
        "生成数字随机序列"
        self.size_ = abs(size_)
        self.max_ = size_ * size_
        numbers_ = list(range(1, self.max_ + 1))
        random.shuffle(numbers_)
        print('-' * 25)
        print(numbers_)
        return numbers_

    def GenCharacters(self, size_):
        characters = []
        self.size_ = abs(size_)
        # 6阶以上统一定制为五阶
        if size_ > 5:
            size_ = 5
            self.size_ = 5
        self.max_ = size_ * size_
        characters = list(string.ascii_lowercase)
        characters.append(' ')
        random.shuffle(characters)
        return characters[0:self.max_]

    def DrawTableSingle(self, thenumbers_):
        "绘制方格"
        print('-' * 25)
        table_ = PrettyTable(border=True, header=False, hrules=ALL)
        i = 0
        while i < self.max_:
            table_.add_row(thenumbers_[i: i + self.size_])
            i += self.size_
        res_ = table_.get_string()
        print(res_)
        return res_

    def GenGridPdf(self, data: list):
        "生成PDF 文件"
        # Create an A4 portrait (210mm x 297mm) sheets with 2 columns and 3 rows of labels. Each label is 80mm x 80mm with a 1mm rounded corner. The margins are automatically calculated.
        # 创建A4 页面 ，一页最大布局8个舒尔特方格
        specs = labels.Specification(210, 297, 2, 4, 72, 72, corner_radius=1)
        # 设置字体 为楷体后能美化展示
        base_path = os.path.dirname(__file__)
        registerFont(TTFont('kaiti', os.path.join(base_path, 'simkai.ttf')))
        registerFont(TTFont('misans', os.path.join(
            base_path, 'MiSans-Normal.ttf')))
        # Create a function to draw each label. This will be given the ReportLab drawing  object to draw on, the dimensions (NB. these will be in points, the unit  ReportLab uses) of the label, and the object to render.

        def draw_grids(label, width, height, obj):
            "逐行添加舒尔特方格"
            data_ = str(obj).split('\n')
            lines_ = len(data_)
            # 为不同大小的方格设置格式
            if lines_ - 1 == 4:  # 2*2
                for index, i_ in enumerate(data_, 1):
                    s = shapes.String(2, height - 32 * index, i_,
                                      fontSize=36, fontName="kaiti")
                    label.add(s)
            elif lines_ - 1 == 6:  # 3*3
                for index, i_ in enumerate(data_, 1):
                    s = shapes.String(2, height - 24 * index, i_,
                                      fontSize=22, fontName="kaiti")
                    label.add(s)
            elif lines_ - 1 == 8:  # 4*4
                for index, i_ in enumerate(data_, 1):
                    s = shapes.String(2, height - 20 * index, i_,
                                      fontSize=18, fontName="kaiti")
                    label.add(s)
            elif lines_ - 1 == 10:  # 5*5
                for index, i_ in enumerate(data_, 1):
                    s = shapes.String(2, height - 5 - 16 * index,
                                      i_, fontSize=14, fontName="kaiti")
                    label.add(s)
            elif lines_ - 1 == 12:  # 6*6
                for index, i_ in enumerate(data_, 1):
                    s = shapes.String(2, height - 10 - 12 * index,
                                      i_, fontSize=12, fontName="kaiti")
                    label.add(s)
        # Create the sheet.
        sheet = labels.Sheet(specs, draw_grids, border=True)
        # sheet.partial_page(1, ((1, 1), (2, 2), (4, 2)))
        # sheet.partial_page(2, ((2, 1), (3, 1)))
        # sheet.add_labels(range(3, 10))
        for i in data:
            sheet.add_label(i, 1)
        # 输出文件时间戳
        from datetime import datetime
        t = datetime.now()
        tString = t.strftime('%Y-%m-%d-%H-%M-%S')
        # 输出PDF文件
        sheet.save(f'SchuiteGrid_lable_{tString}.pdf')


if __name__ == '__main__':
    thegrid_ = SchulteGrid()
    # thegrid_.DrawTableSingle(thegrid_.GenNumbers(4))
    a = []
    # 一页最大8个舒尔特方格,规格设置2-6行宫格
    # 2 - 6 表示宫格大小 , 一页最多放8个
    # 第一页
    def page_too_easy():
        print_grid_list = [3, 3, 2, 2, 3, 3, 2, 2]
        for i in print_grid_list:
            a.append(thegrid_.DrawTableSingle(thegrid_.GenNumbers(i)))

    def page_easy():
        print_grid_list = [3, 3, 4, 4, 3, 3, 4, 4]
        for i in print_grid_list:
            a.append(thegrid_.DrawTableSingle(thegrid_.GenNumbers(i)))

    def page_normal():
        print_grid_list = [3, 3, 4, 4, 5, 5, 4, 4]
        for i in print_grid_list:
            a.append(thegrid_.DrawTableSingle(thegrid_.GenNumbers(i)))

    def page_challenge():
        print_grid_list = [3, 3, 4, 4, 5, 5, 4, 4]
        for i in print_grid_list:
            a.append(thegrid_.DrawTableSingle(thegrid_.GenNumbers(i)))

    # 第二页

    def page_test():
        test_grids = [2, 3, 4, 5, 6]
        for i in test_grids:
            a.append(thegrid_.DrawTableSingle(thegrid_.GenNumbers(i)))

    # 使用字母来做舒尔特方格
    # 6阶以上统一定制为五阶
    def test_page_chars():
        test_grids = [2, 3, 4, 5, 6]
        for i in test_grids:
            a.append(thegrid_.DrawTableSingle(thegrid_.GenCharacters(i)))

    def page_chars():
        test_grids = [3, 3, 4, 4, 5, 5]
        for i in test_grids:
            a.append(thegrid_.DrawTableSingle(thegrid_.GenCharacters(i)))

    page_normal()

    thegrid_.GenGridPdf(a)


# JS 生成舒尔特方格？
