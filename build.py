from conan.packager import ConanMultiPackager
import os

if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86"])
    builder.add_common_builds(pure_c=True)
    builder.run()
