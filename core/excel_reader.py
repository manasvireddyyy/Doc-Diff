import pandas as pd


class ExcelReader:
    """
    Reads Excel files and returns pandas DataFrames.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def read_first_sheet(self):
        """
        Reads the first sheet.
        """

        return pd.read_excel(self.file_path)

    def read_all_sheets(self):
        """
        Returns all sheets as a dictionary.
        """

        return pd.read_excel(
            self.file_path,
            sheet_name=None
        )

    def get_sheet_names(self):
        """
        Returns sheet names.
        """

        excel = pd.ExcelFile(self.file_path)

        return excel.sheet_names