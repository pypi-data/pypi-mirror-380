import os
import re
import subprocess
import time

import inquirer
import pkg_resources
import requests
from packaging.version import parse


update_source = [
    inquirer.List(
        'source',
        message='Please choose the source to update',
        choices=['清华源(推荐)', '北京外国语', 'PyPI'],
    ),
]


def check_for_updates():
    print('Checking for updates...')
    # 获取本地autowsgr版本号
    local_version = get_local_version()
    assert local_version is not None, 'Failed to get the local version'

    # 发送 GET 请求获取库的元数据信息
    response = requests.get('https://mirrors.pku.edu.cn/pypi/web/json/autowsgr', timeout=5)
    data = response.json()

    # 提取最新版本号
    latest_version = data['info']['version']
    # 比较版本号
    if parse(local_version) < parse(latest_version):
        update_questions = [
            inquirer.List(
                'source',
                message=f'New version {latest_version} is available.Your version is {local_version}. Do you want to update?',
                choices=['Yes', 'No'],
            ),
        ]
        result = get_user_choice(update_questions)
        if result == 'Yes':
            # 选择使用哪个源更新,输出按钮回车选择
            choice = get_user_choice(update_source)
            update_library(choice)
            recent_updates = get_recent_updates_from_pypi(latest_version)
            print('更新内容:\n' + recent_updates)

            print('更新完成，稍后将自动退出，请重新启动脚本')
            time.sleep(5)
            os._exit(0)  # 更新成功后退出脚本
    else:
        print('You are using the latest version of the library.')


def get_local_version():
    # 使用pkg_resources获取本地库的版本号
    try:
        return pkg_resources.get_distribution('autowsgr').version
    except Exception as e:
        print(f'Failed to get the local version.Error: {e}')
        return None


def get_user_choice(questions):
    answers = inquirer.prompt(questions)
    assert answers is not None, 'User did not make a choice'
    return answers['source']


def update_library(choice='PyPI'):
    choice_list = {
        'PyPI': [
            'pip',
            'install',
            '--upgrade',
            '--index-url',
            'https://pypi.org/simple',
            'autowsgr',
        ],
        '北京外国语': [
            'pip',
            'install',
            '--index-url',
            'https://mirrors.bfsu.edu.cn/pypi/web/simple/',
            '--upgrade',
            'autowsgr',
        ],
        '清华源(推荐)': [
            'pip',
            'install',
            '--index-url',
            'https://pypi.tuna.tsinghua.edu.cn/simple',
            '--upgrade',
            'autowsgr',
        ],
    }
    subprocess.run(choice_list[choice])


def get_recent_updates_from_pypi(latest_version):
    url = f'https://pypi.org/project/autowsgr/{latest_version}/#description'
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        readme_content = response.text
        updates_section = re.search(
            r'<h2>近期更新</h2>(.*?)</ul>',
            readme_content,
            re.DOTALL,
        )

        if updates_section:
            updates = updates_section.group(1).strip()
            # 提取所有 <li> 标签中的内容
            updates_list = re.findall(r'<li>(.*?)</li>', updates, re.DOTALL)
            # 合并为一个字符串，每行前面加上一个 ·
            return '\n'.join(
                [f'· {re.sub(r"<.*?>", "", update).strip()}' for update in updates_list],
            )
        return '未找到近期更新部分。'
    return f'无法获取更新内容，状态码: {response.status_code}'


# if __name__ == "__main__":
#     check_for_updates()
