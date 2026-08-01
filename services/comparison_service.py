from core.excel_reader import ExcelReader


class ComparisonService:

    def __init__(self, old_file, new_file):

        self.old_file = old_file
        self.new_file = new_file

    def load_files(self):

        old = ExcelReader(self.old_file)
        new = ExcelReader(self.new_file)

        old_df = old.read_first_sheet()
        new_df = new.read_first_sheet()

        return old_df, new_df