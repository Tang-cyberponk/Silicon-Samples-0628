
# step 6：Aggregate and save the generated results
result_df = pd.DataFrame(results)

# Sort the results according to the original sample order in the input data
result_df = result_df.sort_values("sample_index").reset_index(drop=True)

# Write the results to an Excel file
result_df.to_excel(LLM_OUTPUT_FILE, index=False)

print("Silicon-sample generation completed. Output file:", LLM_OUTPUT_FILE)

