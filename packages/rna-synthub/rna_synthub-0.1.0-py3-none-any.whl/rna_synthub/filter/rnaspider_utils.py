#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Maciej Antczak
import argparse
import time
import json

import requests

ENGINE_CONFIG = {
    "mode": 1,
    "homo": "Y",
    "hetero": "Y",
    "heteroElements": "N",
    "deleteIsolatedBps": "Y",
    "removeDuplicates": "N",
    "orders": "Y Y Y Y Y",
    "minLimits": "4 4 4 4 4",
    "maxLimits": "30 30 30 30 30",
    "strandPoints": "P C4'",
    "majorElementPoints": "C4' P",
    "minorElementPoints": "B",
    "rMin": 7,
    "LiMax": 100,
    "BONDSMAX": "2.00",
}

def predict_rnaspider(pdb_file: str):
    response = requests.post(
        "https://rnaspider.cs.put.poznan.pl/api/new-request",
        data={"engine_config": ENGINE_CONFIG, "split_policy": "first"},
        files={"model_3d_0": open(pdb_file, "rb")},
    )
    response.raise_for_status()
    response_json = response.json()

    if response_json["success"] != True:
        return None

    request_id = response_json["request_id"]
    counter = 0
    while counter < 5:
        response = requests.get(
            f"https://rnaspider.cs.put.poznan.pl/api/{request_id}/status"
        )
        response.raise_for_status()
        response_json = response.json()

        if response_json["tasks"][0]["report"]:
            break

        time.sleep(1)
        counter+=1

    response = requests.get(
        f"https://rnaspider.cs.put.poznan.pl/api/{request_id}/0/report"
    )
    response.raise_for_status()
    output = response.text.strip("'")
    output = json.loads(output)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdb")
    args = parser.parse_args()

    response = requests.post(
        "https://rnaspider.cs.put.poznan.pl/api/new-request",
        data={"engine_config": ENGINE_CONFIG, "split_policy": "first"},
        files={"model_3d_0": open(args.pdb, "rb")},
    )
    response.raise_for_status()
    response_json = response.json()

    if response_json["success"] != True:
        print(response_json["message"])
        exit(1)

    request_id = response_json["request_id"]

    while True:
        response = requests.get(
            f"https://rnaspider.cs.put.poznan.pl/api/{request_id}/status"
        )
        response.raise_for_status()
        response_json = response.json()

        if response_json["tasks"][0]["report"]:
            break

        time.sleep(1)

    response = requests.get(
        f"https://rnaspider.cs.put.poznan.pl/api/{request_id}/0/report"
    )
    response.raise_for_status()
    print(response.text)
