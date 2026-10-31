#!/usr/bin/env python3
"""Audit keluaran referensi Bab 10 tanpa mengunduh dataset dan tanpa melatih ulang model."""
from pathlib import Path
import json
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, precision_recall_fscore_support

ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'results'
FAIL=[]

def require(condition, message):
    if not condition: FAIL.append(message)

m=json.loads((RES/'Metadata_Eksperimen.json').read_text(encoding='utf-8'))
require(m['raw_rows']==3810 and m['rows_analyzed']==3810 and m['duplicate_rows_removed']==0,'audit dataset')
require(m['train_rows']==3048 and m['test_rows']==762 and m['random_state']==42,'split dan seed')
require(m['selected_model_from_training_cv']=='Logistic Regression','model terpilih')
require(m['sha256_arff']=='1af97883100c89de2ea2972f7a28d428f4f1c14711a61defc0b0569e9eb65665','hash UCI')
cv=pd.read_csv(RES/'Tabel_10_4_Hasil_Validasi_Silang.csv')
require(cv.loc[cv.CV_Macro_F1_Mean.idxmax(),'Model']=='Logistic Regression','peringkat CV')
require(abs(float(cv.loc[cv.Model=='Logistic Regression','CV_Macro_F1_Mean'].iloc[0])-0.9316705423614721)<1e-10,'nilai CV')
test=pd.read_csv(RES/'Tabel_10_5_Perbandingan_Model_Test.csv')
pred=pd.read_csv(RES/'Prediksi_Pengujian.csv')
labels=['Cammeo','Osmancik']
require(len(pred)==762,'jumlah prediksi test')
for _,r in test.iterrows():
    name=r['Model'];y=pred['actual'];p=pred[name]
    require(abs(accuracy_score(y,p)-r['Accuracy'])<1e-12, 'accuracy '+name)
    require(abs(f1_score(y,p,average='macro')-r['Macro_F1'])<1e-12,'Macro-F1 '+name)
    require(int((y!=p).sum())==int(r['Jumlah_Salah']),'kesalahan '+name)
cm=confusion_matrix(pred.actual,pred['Logistic Regression'],labels=labels)
require(cm.tolist()==[[288,38],[26,410]],'confusion matrix buku')
pr,rc,f1,support=precision_recall_fscore_support(pred.actual,pred['Logistic Regression'],labels=labels,zero_division=0)
per=pd.read_csv(RES/'Tabel_10_6_Metrik_Per_Kelas.csv')
require(per['Kelas'].tolist()==labels+['Rata-rata macro'],'urutan label per kelas')
for key,arr in [('Precision',pr),('Recall',rc),('F1',f1),('Support',support)]:
    require(max(abs(per[key].to_numpy()[:2]-arr))<1e-10,'metrik per kelas '+key)
require(len(pd.read_csv(RES/'Tabel_10_1_Deskripsi_Fitur.csv'))==8,'Tabel 10.1 termasuk target')
require(int(pd.read_csv(RES/'Tabel_10_3_Pembagian_Data.csv').iloc[-1]['Observasi'])==3810,'total Tabel 10.3')
require(abs(per.loc[2,'F1']-f1.mean())<1e-10,'baris macro Tabel 10.6')
for i in range(1,7):
    require(len(list(RES.glob(f'Tabel_10_{i}_*.csv')))==1,f'berkas Tabel 10.{i}')
for i in range(1,6):
    require(len(list((ROOT/'figures').glob(f'Gambar_10_{i}_*.png')))==1,f'berkas Gambar 10.{i}')
nb=json.loads((ROOT/'notebooks'/'Bab10_Rice_Statistical_ML.ipynb').read_text(encoding='utf-8'))
source='\n'.join(''.join(c['source']) for c in nb['cells'])
require('StratifiedKFold(n_splits=5,shuffle=True,random_state=SEED)' in source,'konfigurasi CV notebook')
require('test_size=0.2,stratify=y,random_state=SEED' in source,'pembagian notebook')
require('Gambar_10_4_Validasi_Silang.png' in source and 'Gambar_10_5_Confusion_Matrix.png' in source,'nomor gambar notebook')
require('Tabel_10_6_Metrik_Per_Kelas.csv' in source,'tabel 10.6 notebook')
require(all(c['cell_type']!='code' or c['execution_count'] is None for c in nb['cells']),'notebook harus bersih dari output lama')
if FAIL:
    print('GAGAL:', '; '.join(FAIL));raise SystemExit(1)
print('LULUS: dataset, CV, prediksi individu, metrik 3 model, 6 tabel, 5 gambar, struktur notebook.')
print('Ringkasan:',m['rows_analyzed'],'baris;',m['selected_model_from_training_cv'],
      '; accuracy %.4f'%accuracy_score(pred.actual,pred['Logistic Regression']),
      '; kesalahan',int((pred.actual!=pred['Logistic Regression']).sum()))
print('Catatan: ini validasi hasil yang disimpan, bukan eksekusi ulang data UCI asli.')
