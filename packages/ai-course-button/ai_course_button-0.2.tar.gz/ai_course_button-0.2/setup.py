from setuptools import setup, find_packages

setup(
    name="ai-course-button",
    version="0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
    "lms.djangoapp": [
        "ai_course_button = ai_course_button.apps:AICourseButtonConfig",
    ],
    "cms.djangoapp": [
        "ai_course_button = ai_course_button.apps:AICourseButtonConfig",
    ],
    },
)

