# CCS-MMS dataset
A dataset designed to tackle the Combined Complementary Supplementary Multi-Modal Summarization (CCS-MMS) problem proposed in 'Multi-Modal Supplementary-Complementary Summarization using Multi-Objective Optimization'.

Since the developed dataset is an extension of the [MMS dataset](http://www.nlpr.ia.ac.cn/cip/ZhangPublications/emnlp_en.htm) proposed by Li. et al [2], we've provided the steps to obtain our dataset.

Steps to follow to obtain the dataset:
* Step-1: Obtain the MMS dataset by filling up the application form provided at http://www.nlpr.ia.ac.cn/cip/ZhangPublications/emnlp_en.htm.
* Step-2: Run the `convert_nomenclature.py` file by using the following command:
```
python3 /path/to/mms_data/zip/file /path/to/new/data/directory
```
* Step-3: Refer to the `labels.csv` file containing the outputs extracted by annotation process described in [1]. 

If you use this dataset, we appreciate that you can cite our paper as well as the original paper by Li et al. [2].
```
@inproceedings{10.1145/3404835.3462877,
author = {Jangra, Anubhav and Saha, Sriparna and Jatowt, Adam and Hasanuzzaman, Mohammed},
title = {Multi-Modal Supplementary-Complementary Summarization Using Multi-Objective Optimization},
year = {2021},
isbn = {9781450380379},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3404835.3462877},
doi = {10.1145/3404835.3462877},
booktitle = {Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval},
pages = {818–828},
numpages = {11},
keywords = {multi-objective optimization, data driven summarization, multi-modal summarization, grey wolf optimizer},
location = {Virtual Event, Canada},
series = {SIGIR '21}
}

```

Feel free to contact us (anubhav0603 at gmail.com) if you have any suggestions or questions.


## References
1. Multi-Modal Supplementary-Complementary Summarization using Multi-Objective Optimization. Anubhav Jangra, Sriparna Saha, Adam Jatowt, Mohammed Hasanuzzaman. 44rd International ACM SIGIR Conference on Research and Development in Information Retrieval, 2021.

2. Multi-modal summarization for asynchronous collection of text, image, audio and video. Haoran Li, Junnan Zhu, Cong Ma, Jiajun Zhang, Chengqing Zong. Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing. 

