from setuptools import setup, find_packages, dist
import sys
class BinaryDistribution(dist.Distribution):
    def has_ext_modules(self):
        return True
# 현재 파이썬 버전 문자열 만들기 (예: '3.12')
current_version = f"{sys.version_info.major}.{sys.version_info.minor}"
setup(
    name="libcalab",
    description="library for character animation",
    packages=find_packages(),
    #package_dir={"": "libcalab"},
    python_requires=f"=={current_version}.*",  
    include_package_data = True,
    package_data={
        "libcalab": ["*.so", "*.dylib", "*.dll", "*.pyd","*.py", "Resource/*"],  # wheel 안에 포함할 파일
    },
    distclass=BinaryDistribution, 
)


