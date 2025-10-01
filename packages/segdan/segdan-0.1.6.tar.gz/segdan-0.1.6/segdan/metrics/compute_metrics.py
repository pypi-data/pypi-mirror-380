import torch
import re

from segdan.metrics.segmentationmetrics import accuracy, iou_score, dice_score, precision, recall, f1_score
from segdan.metrics.custom_metric import custom_metric

metric_functions = {
    "accuracy": accuracy,
    "iou": iou_score,
    "dice": dice_score,
    "precision": precision,
    "recall": recall,
    "f1": f1_score,
}

def compute_metrics(results, metrics, classes, stage="train"):
    tp = torch.cat([x["tp"] for x in results])
    fp = torch.cat([x["fp"] for x in results])
    fn = torch.cat([x["fn"] for x in results])
    tn = torch.cat([x["tn"] for x in results])

    results = {}

    for metric in metrics:
        metric_fn = metric_functions[metric]

        score_global = custom_metric(tp, fp, fn, tn, metric_fn, reduction="micro")
        results[f"{metric}_{stage}"] = score_global.item() if torch.is_tensor(score_global) else score_global

        score_none = custom_metric(tp, fp, fn, tn, metric_fn, reduction="none")
        score_per_class = score_none.mean(dim=0)  

        for class_idx, class_score in enumerate(score_per_class):
            class_name = classes[class_idx]
            results[f"{metric}_{stage}_class_{class_name}"] = class_score.item()

    return results
