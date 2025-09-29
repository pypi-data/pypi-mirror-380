from setuptools import setup, find_packages

setup(
    name='KElbowFinder',
    version='0.1.0',
    description='Automatically find the optimal number of clusters (k) for KMeans using the Elbow Method and visualize the result.',
    author='Mohamed Adan, Sara Iidle, Nasteha Nor',
    author_email='zaaraxikmahiidle388@gmail.com',
    url='https://github.com/Zahraaxikmah123/kmeans_elbow_finder.git',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'matplotlib',
        'pandas',
        'numpy',
        'kneed'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)