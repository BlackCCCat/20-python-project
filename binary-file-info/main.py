import os

# Size constants
KB = 1000
MB = KB * 1000
GB = MB * 1000

# Initial bytes for filetypes
pdf = bytes.fromhex('25 50 44 46')
gif = bytes.fromhex('47 49 46')
png = bytes.fromhex('89 50 4E 47 0D 0A 1A 0A')
jpeg_start = bytes.fromhex('FF D8')
jpeg_end = bytes.fromhex('FF D9')
utf8_bom = bytes.fromhex('EF BB BF')

def file_size(filename):
    file_size_in_bytes = os.stat(filename).st_size  # returns file size in bytes
    # Write the functionality to check the file size and convert it to their respective KB, MB or GB
    if file_size_in_bytes // 1000000000 > 0:
        file_size = round(file_size_in_bytes / 1000000000, 2)
        return f'{file_size} GB'
    elif file_size_in_bytes // 1000000 > 0:
        file_size = round(file_size_in_bytes / 1000000, 2)
        return f'{file_size} MB'
    else:
        file_size = round(file_size_in_bytes/1000, 2)
        return f'{file_size} KB'
        
def file_type(filename):
    with open(filename, 'rb') as f:
        filecontent = f.read()
    if filecontent.startswith(pdf):
        return 'PDF'
    if filecontent.startswith(gif):
        return 'GIF'
    if filecontent.startswith(png):
        return 'PNG'
    if filecontent.startswith(jpeg_start) and filecontent.endswith(jpeg_end):
        return 'JPEG'
    if filecontent.startswith(utf8_bom):
        return 'UTF-8'
        

def file_info(filename):
    if not os.path.isfile(filename):
        return f"Error: File [{filename}] does not exist"
    else:
        file_name = f'{filename}'
        file_size1 = file_size(filename)
        file_type1 = file_type(filename)
        file_info = f'File Statistics:\nFile Name: {file_name}\nFile Size: {file_size1}\nFile Type: {file_type1}'
        return file_info


# Run the fileinfo function on a provided filename
def main():
    filename = input("Enter a file name please: ")
    print(file_info(filename))

if __name__ == "__main__":
    main()
