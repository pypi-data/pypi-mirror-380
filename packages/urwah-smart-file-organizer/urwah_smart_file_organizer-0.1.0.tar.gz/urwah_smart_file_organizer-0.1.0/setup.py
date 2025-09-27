from setuptools import setup, find_packages

setup(
    name="urwah-smart-file-organizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "pillow",
        "imagehash"
        "click"
    ],
    entry_points={
        "console_scripts": [
            "smart-file-organizer=smart_file_organizer.cli:main"
        ]
    }
)
