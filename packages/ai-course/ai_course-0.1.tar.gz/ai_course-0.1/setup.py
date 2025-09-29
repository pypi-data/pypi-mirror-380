from setuptools import setup, find_packages

setup(
    name="ai-course",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
    "lms.djangoapp": [
        "ai_course = apps:AICourseButtonConfig",
    ],
    "cms.djangoapp": [
        "ai_course = apps:AICourseButtonConfig",
    ],
    },
)

