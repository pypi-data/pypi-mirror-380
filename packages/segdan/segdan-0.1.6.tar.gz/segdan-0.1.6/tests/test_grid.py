import logging
import tkinter as tk
from tkinter import ttk
import sys
import os
import itertools
import copy
import numpy as np



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from imagedatasetanalyzer import ImageDataset

import json
import glob

from segdan.reduction.reduction import reduce_dataset 
from segdan.clustering.clustering import cluster_images, get_embeddings
from segdan.converters.converterfactory import ConverterFactory
from segdan.analysis.analysis import analyze_data
from segdan.forms.wizard import Wizard
from segdan.datasets.traindataset import TrainingDataset
from segdan.training.partition import dataset_split
from segdan.utils.imagelabelutils import ImageLabelUtils
from segdan.utils.constants import LabelFormat



def create_logger():
   logger = logging.getLogger("SegmentationPipeline")
   logger.setLevel(logging.INFO)

   if not logger.hasHandlers():
      handler = logging.StreamHandler()
      formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M')
      handler.setFormatter(formatter)
      logger.addHandler(handler)
   
   return logger

def general_pipeline(config_dict, logger):
    transformer = ConverterFactory()
    logger = create_logger()

    general_data = config_dict["general_data"]
    output_path = general_data["output_path"]
    verbose = general_data["verbose"]
    class_map = general_data["class_mapping"]
    image_path = general_data["image_path"]
    label_path = general_data["label_path"]
    label_format = general_data["label_format"]
    background = general_data["background"]
    
    embeddings_dict = None
    clustering_results=None
    height_mode = None 
    width_mode = None 
        
    if general_data["class_mapping"]:
        classes = list(general_data["class_mapping"].values())

    # Dataset analysis 
    if config_dict["analyze"]:
        height_mode, width_mode = analyze_data(general_data, transformer, output_path, class_map, verbose)
        classes = ImageLabelUtils.get_classes_from_csv(os.path.join(output_path, "analysis", "metrics.csv"), background)

    # Embedding clustering
    if config_dict["cluster_images"]:
        clustering_data = config_dict["clustering_data"]
        image_dataset = ImageDataset(image_path)

        #embeddings_dict = get_embeddings(clustering_data, image_dataset, verbose, logger)
        #np.savez(r"C:\Users\joortif\Desktop\datasets\Grid\embeddings_dict_busi.npz", filenames=np.array(list(embeddings_dict.keys())), embeddings=np.array(list(embeddings_dict.values())))
        
        data = np.load(r"C:\Users\joortif\Desktop\datasets\Grid\embeddings_dict_busi.npz")
        filenames = data["filenames"]
        embeddings = data["embeddings"]

        embeddings_dict = dict(zip(filenames, embeddings))
        
        embeddings = np.array(list(embeddings_dict.values()))
        #np.save(r"C:\Users\joortif\Desktop\datasets\Grid\embeddings_kvasir.npy", embeddings)
        #embeddings = np.load(r"C:\Users\joortif\Desktop\datasets\Grid\embeddings_camvid.npy")

        clustering_results = None
        clustering_results = cluster_images(clustering_data, image_dataset, embeddings, output_path, verbose, logger)
        

    # Dataset reduction
    if config_dict["reduce_images"]:
        if not embeddings_dict:
            clustering_data = config_dict["clustering_data"] #CAMBIAR
            image_dataset = ImageDataset(image_path)
            embeddings_dict = get_embeddings(clustering_data, image_dataset, verbose, logger)
            embeddings = np.array(list(embeddings_dict.values()))
            
        evaluation_metric = clustering_data.get("clustering_metric")
        reduction_data = config_dict.get("reduction_data")

        reduction_path = reduce_dataset(reduction_data, clustering_results, evaluation_metric, image_dataset, label_path, 
                                            embeddings_dict, output_path, verbose, logger)
        if reduction_data["use_reduced"]:
            image_path = os.path.join(reduction_path, "images")
            label_path = os.path.join(reduction_path, "labels")

    multilabel_transformation_path = os.path.join(output_path, "transformations", LabelFormat.MASK.value)
    if not os.path.exists(multilabel_transformation_path):
        multilabel_transformation_path = label_path
    
    # Dataset split 
    split_output_path = os.path.join(output_path, "split")
    split_data= config_dict["split_data"]
    dataset = TrainingDataset(image_path, multilabel_transformation_path, split_output_path, label_format, label_path)
    dataset.split(general_data, split_data)
    
    # Model training
    #model_data = config_dict["model_data"]
    #hold_out = split_data["split_method"]
    #model_output_path = os.path.join(output_path, "models")

    #model_training(model_data, general_data, split_output_path, model_output_path, multilabel_transformation_path, hold_out=hold_out, classes=classes)

def grid_search(config_dict, 
                logger,
                reduction_methods=["representative", "diverse", "random", "vote_k"], 
                reduction_percentages=[1.0, 0.75, 0.50, 0.25, 0.10], 
                stratification_methods=["nostrat", "pixels", "objects", "pixel_to_object_ratio"]):  
    
    base_output_path = config_dict["general_data"]["output_path"]

    all_combinations = list(itertools.product(reduction_methods, reduction_percentages, stratification_methods))

    filtered_combinations = []
    full_seen_strats = set()

    for reduction_type, retention_percentage, strat_method in all_combinations:
        if retention_percentage == 1.0:
            if strat_method not in full_seen_strats:
                filtered_combinations.append((reduction_type, retention_percentage, strat_method))
                full_seen_strats.add(strat_method)
            continue
        filtered_combinations.append((reduction_type, retention_percentage, strat_method))

    for reduction_type, retention_percentage, strat_method in filtered_combinations:
        config_copy = copy.deepcopy(config_dict)
        #config_copy["split_data"]["split_method"] = True

        is_full = retention_percentage == 1.0

        config_copy["general_data"]["output_path"] = os.path.join(
            base_output_path,
            os.path.join("full", strat_method) if is_full else os.path.join(reduction_type, strat_method, str(retention_percentage))
        )

        os.makedirs(config_copy["general_data"]["output_path"], exist_ok=True)

        if strat_method == "nostrat":
            config_copy["split_data"]["stratification"] = False
        else:
            config_copy["split_data"]["stratification"] = True
            config_copy["split_data"]["stratification_type"] = strat_method

        if is_full:
            config_copy["cluster_images"] = False
            config_copy["reduce_images"] = False
        else:
            config_copy["cluster_images"] = True
            config_copy["reduce_images"] = True
            config_copy["reduction_data"]["reduction_type"] = reduction_type
            config_copy["reduction_data"]["retention_percentage"] = retention_percentage

        print(f"Ejecutando combinación → Reducción: {reduction_type}, Porcentaje: {retention_percentage}, Estratificación: {strat_method}")
        general_pipeline(config_copy, logger=logger)


if __name__ == "__main__":

    app = Wizard()
    app.mainloop()

    config_dict = app.final_dict

    app.destroy()

    if len(config_dict) == 0:
        sys.exit()
    
    logger = create_logger()

    grid_search(config_dict, logger, reduction_methods=["representative", "diverse", "random", "vote_k"], 
                reduction_percentages=[1.0, 0.75, 0.50, 0.25, 0.10], 
                stratification_methods=["nostrat"])




   