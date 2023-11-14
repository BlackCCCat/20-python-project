from pathlib import Path
import shutil

def organize_files(path):
    p = Path(path)
    file_suffixs = set()
    for item in p.iterdir():
        if item.is_file():
            file_suffix = item.suffix
        
            if file_suffix:
                file_suffixs.add(file_suffix)
    
    if file_suffixs:
        print(f'all kinds of files: {file_suffixs}')
    
        
        for file_suffix in file_suffixs:
            file_dir = p / f'{file_suffix[1:]}-files'
            file_dir.mkdir(exist_ok=True)

            files = list(p.glob(f'*{file_suffix}'))
            for file in files:
                shutil.move(file, file_dir)
        
        print('all files organized successfully')
    
    else:
        print('no files found')


def organize_large_files(path, size):
    p = Path(path)
    large_file_dir = p / 'large-files'
    files_list = list(p.glob('**/*'))
    all_large_files_list = []
    for item in files_list:
        if item.is_file():
            # 文件大小可能是0，也需要参与比较，用is not None合适
            if item.stat().st_size is not None and size is not None and item.stat().st_size >= size and item.suffix:
                all_large_files_list.append(item)

    large_files_list = [file for file in all_large_files_list if large_file_dir not in file.parents]

    if large_files_list:
        print(f'large files: {large_files_list}')
        large_file_dir.mkdir(exist_ok=True)
        for item in large_files_list:
            shutil.move(item, large_file_dir)
        print('large files organized successfully')
    else:
        print('no large files found')
            


def delete_logs(path, days):
    # Implement the directory cleaning functionality here
    # You might need to add other parameters as a result of the program requirements
    import time
    p = Path(path)
    log_files = list(p.glob('**/*.log'))
    
    if log_files:
        del_files = []
        for log_file in log_files:
            if log_file.stat().st_mtime and days and (log_file.stat().st_mtime < (time.time() - days * 24 * 60 * 60)):
                del_files.append(log_file)
        print(len(del_files))
        if del_files:
            for file in del_files:
                file.unlink()
                print(f'{file} deleted!')
            return
        else:
            print('no expired log files found')
            return
    else:
        print('no log files found')


def separate_logs(path):
    p = Path(path)
    clean_log_dir = p / 'clean_logs'
    raw_log_dir = p / 'raw_logs'
    clean_log_dir.mkdir(exist_ok=True)
    raw_log_dir.mkdir(exist_ok=True)

    # 排除已经分离的日志文件
    log_files = [file for file in list(p.glob('**/*.log')) if not file in clean_log_dir.glob('*.log') and not file in raw_log_dir.glob('*.log')]
    # 删除日志文件
    clean_log_files = [file for file in log_files if 'clean' in file.stem]
    # 常规日志文件
    raw_log_files = [file for file in log_files if 'raw' in file.stem]

    if clean_log_files or raw_log_files:
        for file in clean_log_files:
            if (clean_log_dir / file.name).exists():
                (clean_log_dir / file.name).unlink()
            shutil.move(file, clean_log_dir)
        for file in raw_log_files:
            if (raw_log_dir / file.name).exists():
                (raw_log_dir / file.name).unlink()
            shutil.move(file, raw_log_dir)
        print('log files separated successfully')
    else:
        print('no clean or raw log files found')


def main():
    path = Path.home() / 'Desktop'
    # organize_files(path)
    # organize_large_files(path, 10*1024**2)
    # separate_logs(path)



if __name__ == "__main__":
    main()