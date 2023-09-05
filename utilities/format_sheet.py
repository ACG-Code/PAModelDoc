import pandas as pd
import xlsxwriter.utility


class Format:
    """
    Class to format Excel sheet to specifications
    """

    @staticmethod
    def format_sheet(df: pd.DataFrame, writer: pd.ExcelWriter, sheet_name: str, merge: bool, merge_object: str or None,
                     filter: bool):
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        worksheet.hide_gridlines(2)

        # Define Formats
        merge_format = workbook.add_format({'align': 'left', 'valign': ' vCenter'})
        header_format = workbook.add_format({'bold': True, 'bg_color': '#BFBFBF', 'border': 1})
        body_format = workbook.add_format({'border': 1})
        clear_format = workbook.add_format({'border': 0})

        # Clear Exiting Formats
        for col_num, value in enumerate(df):
            worksheet.write(1, col_num + 1, value, clear_format)

        # Set Header Style
        worksheet.conditional_format(xlsxwriter.utility.xl_range(1, 1, 1, len(df.columns)),
                                     {'type': 'no_errors', 'format': header_format})

        # Set Body Style
        worksheet.conditional_format(xlsxwriter.utility.xl_range(2, 1, len(df) + 1, len(df.columns)),
                                     {'type': 'no_errors', 'format': body_format})

        # Merge if needed
        if merge:
            for obj in df[merge_object].unique():
                rows = df.loc[df[merge_object] == obj].index.values + 2
                worksheet.merge_range(rows[0], 1, rows[-1], 1, df.loc[rows[0] - 2, merge_object], merge_format)

        # Size Columns
        worksheet.set_column(0, 0, 2)
        worksheet.set_row_pixels(0, 6)
        idx_max = max([len(str(s)) for s in df.index.values] + [len(str(df.index.name))])
        idx_max = [idx_max] + [max([len(str(s)) for s in df[col].values] + [len(col)]) for col in df.columns]

        for x in range(len(idx_max)):
            if x > 0:
                worksheet.set_column(x, x, idx_max[x] * 1.25)

        # Auto Filtering Logic
        if filter:
            worksheet.autofilter(1, 1, df.shape[0], df.shape[1])