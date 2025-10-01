import logging
import tkinter as tk
from tkinter import ttk
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from imagedatasetanalyzer import ImageDataset

import json

from segdan.utils.constants import LabelFormat
from segdan.training.training import model_training
from segdan.reduction.reduction import reduce_dataset 
from segdan.clustering.clustering import cluster_images, get_embeddings
from segdan.converters.converterfactory import ConverterFactory
from segdan.analysis.analysis import analyze_data
from segdan.forms.wizard import Wizard
from segdan.datasets.traindataset import TrainingDataset
from segdan.utils.imagelabelutils import ImageLabelUtils

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="tensorflow")

def create_logger():
   logger = logging.getLogger("SegmentationPipeline")
   logger.setLevel(logging.INFO)

   if not logger.hasHandlers():
      handler = logging.StreamHandler()
      formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M')
      handler.setFormatter(formatter)
      logger.addHandler(handler)
   
   return logger

if __name__ == "__main__":

   def print_config_data(config_data):
        config_json = json.dumps(config_data, indent=4)
        print(config_json)

   app = Wizard()
   app.mainloop()

   config_dict = app.final_dict

   app.destroy()

   if len(config_dict) == 0:
      sys.exit()

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
   height_mode, width_mode = None, None
    
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

      embeddings = np.load(r"C:\Users\joortif\Desktop\datasets\Grid\embeddings_camvid.npy")
      embeddings_dict = {
        img_name: emb for img_name, emb in zip(image_dataset.image_files, embeddings)
      }
      #embeddings = np.array(list(embeddings_dict.values()))

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
   model_data = config_dict["model_data"]
   hold_out = split_data["split_method"]
   model_output_path = os.path.join(output_path, "models")

   if height_mode is None and width_mode is None:
      img_dataset = ImageDataset(general_data["image_path"])
      height_mode, width_mode = img_dataset.image_sizes()

   model_training(model_data=model_data, general_data=general_data, split_path=split_output_path, 
                  model_output_path=model_output_path, hold_out=hold_out, classes=classes, 
                  mode_height=height_mode, mode_width=width_mode)