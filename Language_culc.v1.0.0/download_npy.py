import gdown

def download_from_gdrive(file_id, output_name):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_name, quiet=False)

if __name__ == "__main__":
    FILE_ID = "18A0xlwxpVx5kBrojYGW6izSo-_Q0ipEf"  # Google Drive のファイルID
    OUTPUT_NAME = "language_dateset3a.model.vectors.npy"  # 保存するファイル名

    download_from_gdrive(FILE_ID, OUTPUT_NAME)
