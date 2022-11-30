from setuptools import setup

setup(name="envkey",
      version="2.1.1",
      description="EnvKey's Python library. Protect API keys and credentials. Keep configuration in sync.",
      url="https://github.com/envkey/envkey-python",
      keywords=["security", "secrets management", "configuration management", "environment variables", "configuration", "python"],
      author="EnvKey",
      author_email="support@envkey.com",
      license="MIT",
      packages=["envkey"],
      package_data={"envkey": ["ext/?/*"]},
      include_package_data=True,
      install_requires=[],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
      ],
      zip_safe=False)