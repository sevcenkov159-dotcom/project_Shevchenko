"""Извлеките ключи ["name", "salary"] из sample_dict."""
sample_dict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}
keys_to_extract = ["name", "salary"]

extracted_values = [sample_dict[key] for key in keys_to_extract if key in sample_dict]
print(extracted_values)