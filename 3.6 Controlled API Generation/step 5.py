
# step 5：Generate silicon samples in batches
data = pd.read_excel(INPUT_FILE).reset_index(drop=True)
results = []

for sample_index, row in data.iterrows():
    row_result = process_one_row(sample_index, row)
    results.append(row_result)
