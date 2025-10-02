from setuptools import setup, find_packages

setup(
    name="meowmod",
    version="3.0.0.7",
    author="小孫孫",
    author_email="sun1000526@gmail.com",
    description="Battle Cats Save File Editor - 修改器套件",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "meowmod": [
            "files/*",              # files 資料夾下的檔案
            "files/locale/*",       # 語言檔
            "files/game_data/*",    # 遊戲資料
        ],
    },
    install_requires=[
        "colored==1.4.4",
        "pyyaml==6.0.2",
        "requests==2.32.3",
        "python-dateutil"
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "meowmod = meowmod.__main__:main",
        ],
    },
)
