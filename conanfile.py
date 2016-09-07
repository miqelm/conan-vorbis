from conans import ConanFile, CMake, os, ConfigureEnvironment
from conans.tools import download, unzip, replace_in_file

class VorbisConan(ConanFile):
    name = "vorbis"
    version = "1.3.5"
    ZIP_FOLDER_NAME = "lib%s-%s" % (name, version)
    generators = "txt"
    settings = "os", "arch", "build_type", "compiler"
    url="http://github.com/coding3d/conan-vorbis"
    requires = "ogg/1.3.2@coding3d/stable"
    license="BSD"
    exports = "*"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        try:
            if self.settings.os == "Windows":
                self.run("rd /s /q %s" % self.ZIP_FOLDER_NAME)
            else:
                self.run("rm -rf %s" % self.ZIP_FOLDER_NAME)
        except:
            pass

        zip_name = "%s.tar.gz" % self.ZIP_FOLDER_NAME

        download("http://downloads.xiph.org/releases/vorbis/%s" % zip_name, zip_name)
        unzip(zip_name)

    def build(self):
        env = ConfigureEnvironment(self.deps_cpp_info, self.settings)

        if self.settings.os == "Windows":
            libdirs="<AdditionalLibraryDirectories>"
            libdirs_ext="<AdditionalLibraryDirectories>$(LIB);"
            replace_in_file("%s\win32\VS2010\libvorbis\libvorbis_dynamic.vcxproj" % self.ZIP_FOLDER_NAME, libdirs, libdirs_ext)
            replace_in_file("%s\win32\VS2010\libvorbisfile\libvorbisfile_dynamic.vcxproj" % self.ZIP_FOLDER_NAME, libdirs, libdirs_ext)
            replace_in_file("%s\win32\VS2010\libvorbisdec\libvorbisdec_dynamic.vcxproj" % self.ZIP_FOLDER_NAME, libdirs, libdirs_ext)
            replace_in_file("%s\win32\VS2010\libvorbisenc\libvorbisenc_dynamic.vcxproj" % self.ZIP_FOLDER_NAME, libdirs, libdirs_ext)
            cd_build = "cd %s\win32\VS2010" % self.ZIP_FOLDER_NAME
            self.run("%s & devenv vorbis_dynamic.sln /upgrade" % cd_build)
            self.run("%s & %s & msbuild vorbis_dynamic.sln" % (cd_build, env.command_line))
        else:
            cd_build = "cd %s" % self.ZIP_FOLDER_NAME
            self.run("%s && chmod +x ./configure && %s ./configure" % (cd_build, env.command_line))
            self.run("%s && make" % cd_build)

    def package(self):
        self.copy("FindVORBIS.cmake", ".", ".")
        self.copy("include/vorbis/*", ".", "%s" % (self.ZIP_FOLDER_NAME), keep_path=True)

        if self.settings.os == "Windows":
            self.copy(pattern="*.dll", dst="bin", keep_path=False)
            self.copy(pattern="*.lib", dst="lib", keep_path=False)
        else:
            if self.settings.os == "Macos":
                # .a is more flexible so we'll only be using that for now
                #self.copy(pattern="*.dylib", dst="lib", keep_path=False)
                self.copy(pattern="*.a", dst="lib", keep_path=False)
            else:
                self.copy(pattern="*.so*", dst="lib", keep_path=False)
                self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.os == "Windows":
            self.cpp_info.libs = ['libvorbis', 'libvorbisfile']
        else:
            self.cpp_info.libs = ['vorbis', 'vorbisfile']
