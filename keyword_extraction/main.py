import os
import csv
import glob

PATH_RUST = "./rust/test/*.rs"
PATH_CSV = "./out.csv"
header = ["No.", "file", "test_func", "feature1", "feature2", "feature3"]
feature_list = []
test_lines = []

def extract_test_fnc(rust_file_path, count):

    basename_rust = os.path.basename(rust_file_path)

    with open(rust_file_path) as f:
        lines = f.readlines()
        with open(PATH_CSV, "a") as fc:
            writer = csv.writer(fc, quoting=csv.QUOTE_NONE)
            for i, line in enumerate(lines):
                if ("#[test]" in line):
                    test_lines.append(i)
                elif ("#[cfg(feature =" in line):
                    feature_name = line.strip().replace("#[cfg(feature = \"", "").replace("\")]", "")
                    feature_list.append(feature_name)
                elif ("pub fn" in line):
                    feature_list.clear()
                elif ("fn " in line) and ( (i-1 in test_lines) or (i-2 in test_lines) ):
                    func_name = line.strip().replace("fn ", "").replace(" {", "")
                    feature_cnt = len(feature_list)
                    count = count + 1
                    if (feature_cnt == 0):
                        writer.writerow([count, basename_rust, func_name, "", "", ""])
                    elif (feature_cnt == 1):
                        writer.writerow([count, basename_rust, func_name, feature_list[0], "", ""])
                    elif (feature_cnt == 2):
                        writer.writerow([count, basename_rust, func_name, feature_list[0], feature_list[1], ""])
                    elif (feature_cnt == 3):
                        writer.writerow([count, basename_rust, func_name, feature_list[0], feature_list[1], feature_list[2]])
                    else:
                        print("Unsupported Format!! ", basename_rust, line)
                    feature_list.clear()
    return count

def main():
    print("List up rust test function in[", PATH_RUST, "]")

    cnt = 0
    os.remove(PATH_CSV)
    with open(PATH_CSV, "a") as fc:
        writer = csv.writer(fc, quoting=csv.QUOTE_NONE)
        writer.writerow(header)
    files = glob.glob(PATH_RUST)
    for file in files:
        ret = extract_test_fnc(file, cnt)
        cnt = cnt + ret
    print("Completed...")
    print("CSV file[", PATH_CSV, "].")
    print("Total ", cnt ," functions are listed.")

if __name__ == "__main__":
    main()
