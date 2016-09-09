from conan.packager import ConanMultiPackager
import os

if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86"], visual_versions=[14], args="--build ogg vorbis")
    builder.add_common_builds(shared_option_name="vorbis:shared", pure_c=True)
    builder.run()
