from setuptools import setup, find_packages

setup(
    name="tkurses",
    version="0.2.6",
    author="Freeboardtortoise",
    author_email="Freeboardtortoise@gmail.com",
    description="Tkinter-like themed UI framework for curses... New aditions to 0.2.5: default theme file if theme=None",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://not-aplicable.com",
    packages=find_packages(),
    python_requires='>=3.6',
)
