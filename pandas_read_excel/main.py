import pandas as pd
import openpyxl
import glob

out_data = []
in_file = pd.ExcelFile("./data/test_items.xlsx")

in_file = pd.ExcelFile("./data/test_items.xlsx")
print(in_file.sheet_names)

for sheet_name in in_file.sheet_names:
    # exclude sheet made by numbers app.
    if sheet_name != '書き出しの概要':
        sheet = pd.read_excel("./data/test_items.xlsx", sheet_name)
        # print(sheet)
        for index, raw in sheet.iterrows():
            data = []
            data.append(sheet_name)
            data.append(raw["No."])
            data.append(raw["テスト関数"])
            # print(data)
            out_data.append(data)

df = pd.DataFrame(out_data,
                  columns=['sheet_name', 'test_number', 'test_func'])
print(df)

test_serde1_lines = df[df["test_func"] == "test_serde1"]
print(test_serde1_lines)

# str.contains() can't get Nan.
# ---------------------------------------------------------------
# ValueError: cannot index with vector containing NA / NaN values
# ---------------------------------------------------------------
# So it must be set "na" value for Nan.
test_special2_lines = df[df["test_func"].str.contains("test_special2", na=False)]
print(test_special2_lines)

# Pick up only NaN line.
test_nan_lines = df[df["test_func"].isnull()]
print(test_nan_lines)

