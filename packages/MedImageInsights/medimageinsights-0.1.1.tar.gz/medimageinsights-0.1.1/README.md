# 🩺 MedImageInsights

MedImageInsights is a package streamlined of the original HuggingFace repository mantained by the Lion-AI team available [here](https://huggingface.co/lion-ai/MedImageInsights). Its purpose is to make it easier to integrate the medical image embedding model **MedImageInsight** in Python projects by removing unecessary modules, simplifying dependencies and offering a clean `pip install` interface. 

The official guide to download and use the model belongs to Microsoft and it is defined as open-source though the installation process is quite complicated. Moreover, the model version of Lion-AI requires the cloning of the repository and the use of a package manager.

Thus, in this work we present an easy to use `pip` library for the model **MedImageInsight**. By packaging and simplifying some of the code in the repository owned by Lion-AI we are able to make it even easier to use the model, without needing to use Microsoft Azure services or downloading the whole code from the HuggingFace repo. On the contrary, the user can simply install the library **MedImageInsights** via `PyPi` in order to use the model for tasks such as zero-shot classification or embedding generation. 

## 💿 Installation 

As mentioned above, the library can easily installed via pip:

```python
pip install medimageinsights
```

## 📝 Tutorials

Once you have installed the library on your environment, you can test it by running this example [script](https://github.com/joortif/MedImageInsights/blob/main/tests/example.py).

A python notebook is also provided, that can be either run on your device or in Google Colab. You may preview the notebook [here](https://github.com/joortif/MedImageInsights/blob/main/tests/MedImageInsights_Tutorial.ipynb) or directly run it on Colab [here](https://colab.research.google.com/github/joortif/MedImageInsights/blob/main/tests/MedImageInsights_Tutorial.ipynb
).

## 🌟 Acknowledgements

Both the original Lion-AI repo and this package are based on the work described in the paper "MedImageInsight: An Open-Source Embedding Model for General Domain Medical Imaging" by Noel C. F. Codella et al ([arXiv:2410.06542](https://arxiv.org/abs/2410.06542)).

Most of the implementation is inherited from the Lion-AI repository. Credit is due to Noel C. F. Codella et al., and the Lion-AI team for designing, training, and publishing the original model and code.