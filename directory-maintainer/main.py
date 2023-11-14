# Directory Maintainer
# Organizes the files within a directory
# Usage: python3 main.py [path/to/directory] [option1] [option2]

import click

from actions import *


# 定义主命令
@click.command()
# 定义必要的参数，这里是你文件路径
@click.argument('path', type=click.Path(exists=True))
@click.option('--organize', is_flag=True, help='Organize the files.')
@click.option('--log-separate', is_flag=True, help='Separate log files.')
@click.option('--delete-log', is_flag=True, help='Delete log files.')
@click.option('--days', type=int, help='The number of days for old log files.')
@click.option('--include-large-file', is_flag=True, help='Organize large files.')
@click.option('--size', type=int, help='The size threshold in bytes for large files.')
def main(path, organize, include_large_file, size, delete_log, days, log_separate):
    """处理文件和日志的简单脚本"""
    click.echo(f'Path to files: {path}')
    
    if include_large_file and not organize:
        raise click.UsageError('--organize option must be provided when using --include-large-files')

    if organize:
        organize_files(path)
        if size and not include_large_file:
            raise click.UsageError('--include-large-files option must be provided when using --size')
        if include_large_file:
            organize_large_files(path, size)

    if log_separate:
        separate_logs(path)


    if days and not delete_log:
        raise click.UsageError('--delete-log option must be provided when using --days')
    
    if delete_log and not days:
        days = 3
    if delete_log and days:
        delete_logs(path, days)

    click.echo('Operation completed.')

# 如果是直接运行此脚本，则调用 main() 函数
if __name__ == "__main__":
    main()



