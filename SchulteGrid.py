from email import header
import random
# import prettytable
from prettytable import PrettyTable, MSWORD_FRIENDLY, ALL


class SchulteGrid():
    def __init__(self) -> None:
        pass

    def GenNumbers(self, size_):
        theGrid = ""
        self.size_ = size_
        self.max_ = size_*size_
        numbers_ = list(range(1, self.max_+1))
        random.shuffle(numbers_)
        print('-' * 25)
        print(numbers_)
        return numbers_

    def DrawTableSingle(self, thenumbers_):
        print('-' * 25)
        table_ = PrettyTable(border=True, header=False, hrules=ALL)
        # table_.set_style(MSWORD_FRIENDLY)
        i = 0
        while i < self.max_:
            table_.add_row(thenumbers_[i: i+self.size_])
            i += self.size_
        print(table_)


if __name__ == '__main__':
    thegrid_ = SchulteGrid()
    thegrid_.DrawTableSingle(thegrid_.GenNumbers(4))
    thegrid_.DrawTableSingle(thegrid_.GenNumbers(5))

# JS 生成舒尔特方格？ 