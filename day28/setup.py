from setuptools import setup
DATA_FILES = ['tomato.png', 'sunset_countdown_timer.mp3' ]
OPTIONS = {'includes': ['pynput']}

setup(
    app=["main.py"],
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=["py2app"],
)

#run python3 setup.py py2app       