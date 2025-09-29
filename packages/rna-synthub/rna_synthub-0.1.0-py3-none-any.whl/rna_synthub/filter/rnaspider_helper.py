import os
import time
from typing import Optional

import tqdm
import pandas as pd
import numpy as np

from rna_synthub.filter.predict_abstract import PredictAbstract
from rna_synthub.filter.rnaspider_utils import predict_rnaspider


class RNASpiderHelper(PredictAbstract):
    def __init__(self):
        super().__init__("rnaspider")

    def predict_single_file(self, rna_path: str) -> float:
        try:
            out = predict_rnaspider(rna_path)
        except IndexError:
            out = None
        if out is None:
            score = np.nan
        else:
            score = len(out.get("entanglements", []))
        return score

    def predict_files(self, in_dir_path: str, out_path: str,
                      out_time_path: Optional[str] = None):
       """
       Given a directory of RNAs, it will predict the scoring function
       If out_path already exists, it will add to the file
       :return:
       """
       if os.path.exists(out_path):
           out = pd.read_csv(out_path)
       else:
           out = pd.DataFrame({"rna": [], self.name: [] })
       if os.path.exists(out_time_path):
           out_time = pd.read_csv(out_time_path)
       else:
           out_time = pd.DataFrame({"rna": [], "time": []})
       out["rna"] = out["rna"].map(lambda x: x.replace("/cp", "_cp"))
       out_time["rna"] = out_time["rna"].map(lambda x: x.replace("/cp", "_cp"))
       rnas = [name for name in os.listdir(in_dir_path) if name not in out["rna"].values]
       index = 0
       for rna in tqdm.tqdm(rnas):
           index+=1
           rna_path = os.path.join(in_dir_path, rna)
           time_b = time.time()
           scores = self.predict_single_file(rna_path)
           c_time = time.time() - time_b
           c_rna = rna.replace("_cppc", "/cppc")
           out.loc[len(out)] = [c_rna, scores]
           out_time.loc[len(out_time)] = [c_rna, c_time]
           if index % 10 == 0:
               c_out = out.set_index("rna")
               c_out.to_csv(out_path)
               c_out_time = out_time.set_index("rna")
               c_out_time.to_csv(out_time_path)
       out = out.set_index("rna")
       out.to_csv(out_path)
       out_time = out_time.set_index("rna")
       out_time.to_csv(out_time_path)