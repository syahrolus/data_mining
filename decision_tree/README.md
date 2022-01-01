# Decision Tree

## install :

```bash
pip install pandas
pip install numpy
git clone https://github.com/syahrolus/data_mining.git
# cd data_mining/decision_tree
```

thanks to https://www.kaggle.com/fedesoriano/stroke-prediction-dataset for the dataset

description:

1. `healthcare-dataset-stroke-data.csv` & `healthcare-dataset-stroke-data.xlsx`, dataset (both are same, just differ in extension)
2. `klasifikasi.py`, you must change according to your need for better proccess
3. `stroke_classified.xlsx`, result after running the `klasifikasi.py` 
4. `decision_tree.py`, main program
5. `decision_tree.txt`, decisions after running the main program, just to illustrate
6. `hasil_prediksi.xlsx`, result prediction
7. `tmp.xlsx`, just a temporary need, you can delete it

running:

1. first, you have to make sure to classify your attributes first (you can use `klasifikasi.py` and change them according to your needs), and change NaN (if any) to `other` attributes or other names manually.
2. ```python3 klasifikasi.py``` 