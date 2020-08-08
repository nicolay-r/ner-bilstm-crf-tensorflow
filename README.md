# Additional Flask wrapper for DeepNER (Named Entity Recognition)

In this repo is a [flask](http://flask.pocoo.org/) wrapper over neural network
architectures for named entity recognition (NER) from the paper "_Application
of a Hybrid Bi-LSTM-CRF model to the task of Russian Named Entity Recognition_"
https://arxiv.org/pdf/1709.09686.pdf, which is inspired by LSTM+CRF
architecture from https://arxiv.org/pdf/1603.01360.pdf.

[Original](https://github.com/deepmipt/ner) repository.

### Changes

- Added support of Tensorflow-gpu 1.14.0
- Fixed problem with RTX cards (RTX-2070)

#### Dependencies

* Python 3.6

#### Library installation

```
pip install .
```

#### Using as a 

Install [Flask](http://flask.pocoo.org/), and start server as follows:
```
$ python3 start.py
```
