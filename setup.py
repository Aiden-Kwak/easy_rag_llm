from setuptools import setup, find_packages

setup(
    name="easy-rag",
    version="1.0.0",
    description="Easily implement RAG workflows with pre-built modules.",
    author="Aiden-Kwak",
    author_email="duckracoon@gist.ac.kr",
    packages=find_packages(),
    install_requires=[
        "faiss-cpu",
        "numpy",
        "tqdm",
        "PyPDF2",
        "openai",
        "requests",
        "python-dotenv",
    ],
    python_requires=">=3.8",
)
