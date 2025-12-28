import kagglehub

# Download latest version
path = kagglehub.dataset_download("parvmodi/cgpa-vs-package-in-lpa")

print("Path to dataset files:", path)