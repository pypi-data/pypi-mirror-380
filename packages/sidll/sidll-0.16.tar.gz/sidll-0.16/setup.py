from skbuild import setup
setup(
    name="SIDLL",
    version="0.14",
    cmake_install_dir=".",
    py_modules=["sidll"],
    cmake_args=["-DCMAKE_GENERATOR_PLATFORM=x64"],
    platforms=["win_amd64"]
)