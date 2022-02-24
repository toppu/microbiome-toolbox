import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="microbiome-toolbox", 
    version="1.0.2",
    author="Jelena Banjac, Shaillay Kumar Dogra, Norbert Sprenger",
    author_email="msjelenabanjac@gmail.com, ShaillayKumar.Dogra@rd.nestle.com, norbert.sprenger@rdls.nestle.com",
    maintainer="Jelena Banjac",
    maintainer_email="msjelenabanjac@gmail.com",
    description="Microbiome Toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JelenaBanjac/microbiome-toolbox",
    packages=setuptools.find_packages(include=['microbiome', 'microbiome.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "seaborn",
        "ipyvolume",
        "xgboost",
        "certifi",
        "cycler",
        "matplotlib",  #==2.2.2
        "pyparsing",
        "ipykernel",
        "ipython",
        "ipython_genutils",
        "jedi",
        "joblib",
        "jupyter_client",
        "jupyter_core",
        "numpy",
        "pandas",
        "parso",
        "pickleshare",
        "pip",
        "prompt-toolkit",
        "pygments",
        "python-dateutil",
        "scikit-learn",
        #"scikit-bio",
        "scipy",
        "setuptools",
        "six",
        "threadpoolctl",
        "tornado",
        "traitlets",
        "wheel",
        "dash==2.0.0",
        "diskcache",
        "multiprocess",
        "psutil",
        "dash-renderer",
        "dash-table",
        "dash-uploader",
        "dash-extensions",
        "plotly",
        "flask-caching",
        # "catboost",
        "statsmodels",
        "numpy",
        "shap",
        "tk",
        "gunicorn",
        "diskcache",
        "python-dotenv",
        "psutil",
        "diskcache",
        "multiprocess",
        "natsort",
        "umap-learn",
        "black",
        "isort",
        #"flake8",
    ]
)
