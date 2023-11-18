# CSED
The Corpus &amp; Code for the paper ["CSED: A Chinese Semantic Error Diagnosis Corpus"](https://arxiv.org/pdf/2305.05183.pdf).

## CSED-R
The CSED-R task is a binary classification task to judge whether a sentence contains semantic errors.

| Dataset| #Sentence | Avg.Length | Error Ratio |
| :---: | :---: | :---: | :---: |
| Train |  45,248 | 50.4 | 74.6% |
| Dev |  2,160 | 52.6 | 50.0% |
| Test |  2,000 | 54.5 | 50.0% |

## CSED-C
The CSED-C task is a natural language generation task that translates incorrect semantic sentences into correct ones.

| Dataset| #Sentence | Avg.Length | Avg.Edit | Avg.Refernce |
| :---: | :---: | :---: | :---: | :---: |
| Train |  8,682 | 52.1 | 4.0 |1.31|
| Dev |  970 | 51.6 | 4.2 |1.03|
| Test |  1,000 | 52.1 | 4.1 |1.00|
