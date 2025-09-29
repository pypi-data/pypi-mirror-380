from setuptools import setup, find_packages

setup(
    name="timelib-jack",
    version="1.0.0",
    author="Jack",
    description="مكتبة توقيت متقدمة، Async + Cron + Retry + Priority + Pause/Resume + Monitoring + Time protection",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
)