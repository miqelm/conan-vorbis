from conan.packager import ConanMultiPackager
import os

if __name__ == "__main__":
    builder = ConanMultiPackager(visual_versions=[14])
    builder.add_common_builds(pure_c=True)
    builder.run()
