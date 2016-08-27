# Only building shared library, since the static library would not work
from conans import ConanFile, CMake, os

class VorbisConan(ConanFile):
    name = "vorbis"
    version = "1.3.5"
    ZIP_FOLDER_NAME = "%s-%s" % (name, version)
    generators = "txt"
    settings = "os", "arch", "build_type", "compiler"
    url="http://github.com/coding3d/conan-vorbis"
    requires = ""
    license="BSD"
    exports = "*"
    
    def configure(self):
        del self.settings.compiler.libcxx 
                
    def build(self):
        self.system_requirements()
        cmake = CMake(self.settings)

        try:
            if self.settings.os == "Windows":
                self.run("rd /s /q _build")
            else:
                self.run("rm -rf _build")
        except:
            pass

        self.run("mkdir _build")
        self.run("cp -rf %s _build/" % self.ZIP_FOLDER_NAME)
        cd_build = "cd _build/%s" % self.ZIP_FOLDER_NAME
        self.run("%s && ./configure" % cd_build)
        self.run("%s && make" % cd_build)

    def package(self):
        self.copy("FindVorbis.cmake", ".", ".")
        self.copy("include/vorbis/*", ".", "%s" % (self.ZIP_FOLDER_NAME), keep_path=True)

        if self.settings.os == "Windows":
            self.copy(pattern="*.dll", dst="bin", src=self.ZIP_FOLDER_NAME, keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src=self.ZIP_FOLDER_NAME, keep_path=False)
        else:
            if self.settings.os == "Macos":
                # .a is more flexible so we'll only be using that for now
                #self.copy(pattern="*.dylib", dst="lib", keep_path=False)
                self.copy(pattern="*.a", dst="lib", keep_path=False)
            else:
                self.copy(pattern="*.so*", dst="lib", src=self.ZIP_FOLDER_NAME, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['vorbis']