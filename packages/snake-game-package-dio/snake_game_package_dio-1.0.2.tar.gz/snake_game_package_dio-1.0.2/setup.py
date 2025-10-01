from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="snake_game_package_dio",
    version="1.0.2",
    author="Isaias Oliveira",
    author_email="isaiaswebnet@gmail.com",
    description="O clássico jogo da Cobrinha foi recriado em estilo Synthwave Cyberpunk.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skynetsites/snake_game_package",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "snake_game": ["assets/sounds/*.wav"],
        "": ["docs/*.gif"],
    },
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "snake-game = snake_game.game:main"
        ]
    },
)
