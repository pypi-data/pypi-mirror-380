from setuptools import setup, find_packages, dist
class BinaryDistribution(dist.Distribution):
    def has_ext_modules(self):
        return True

setup(
    name="libcalab",
    version="0.0.1",
    description="library for character animation",
    packages=find_packages(),
    #package_dir={"": "libcalab"},
    python_requires=">=3.7",
    include_package_data = True,
    package_data={
        "libcalab": ["*.so", "*.dylib", "*.dll", "*.pyd","*.py", "Resource/*"],  # wheel 안에 포함할 파일
    },
    distclass=BinaryDistribution, 
)


