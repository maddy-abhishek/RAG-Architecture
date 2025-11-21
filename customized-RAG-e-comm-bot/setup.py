from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="maddy-abhishek",
    author_email="abhishekraj16.12.2002@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain_google_genai','datasets','pypdf','python-dotenv','flask','langchain_huggingface','sentence_transformers']
)