#FROM rocm/tensorflow:latest
FROM rocm/tensorflow:rocm6.4.2-py3.10-tf2.18-dev

WORKDIR /workspace

RUN pip install --no-cache-dir matplotlib seaborn pillow scikit-learn pandas


CMD ["python", "GalaxyMLmodel.py"]
#CMD ["bash"]
