from conan.packager import ConanMultiPackager
import os

if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86"], args="--build ogg")
    builder.add_common_builds(pure_c=True)
    builder.run()
