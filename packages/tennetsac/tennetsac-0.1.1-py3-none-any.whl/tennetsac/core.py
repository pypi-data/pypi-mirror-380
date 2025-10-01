# === Standard Library ===
import os
import warnings

# === Computing & Visualization ===
import torch
import pandas as pd
import numpy as np

# === Warning Suppression ===
from tqdm import TqdmWarning
warnings.simplefilter("ignore", category=TqdmWarning)
warnings.filterwarnings("ignore", message="TypedStorage is deprecated")
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message="Some weights of RobertaModel were not initialized")
from transformers.utils import logging
logging.set_verbosity_error()

# === Model Architectures ===
from .models.Emb2Profile import SigmaProfileGenerator
from .models.Emb2Geometry import GeometryGenerator
from .models.Prf2Gamma import Prf_to_Seg_Model

# === Model Loading ===
from .utils.model_io import load_model, load_all_Gamma_models

# === Embedding Extraction ===

from .utils.embedding import ChemBERTaEmbedder, SMITEDEmbedder

# === Computation ===
from .utils.property import get_sigma_profile, calc_ln_gamma, ensemble_segac, calc_ln_gamma_binary

# === Embedding models ===
cb_emb = ChemBERTaEmbedder()
st_emb = SMITEDEmbedder()

# === Load checkpoints ===
here = os.path.dirname(__file__)  
ckpt_path = os.path.join(here, "ckpt_files")

prf_model = load_model(SigmaProfileGenerator(), os.path.join(ckpt_path, "prf.ckpt"))
geometry_model = load_model(GeometryGenerator(), os.path.join(ckpt_path, "geo.ckpt"))
Gamma_base_model = load_model(Prf_to_Seg_Model(), os.path.join(ckpt_path, "base.ckpt"))

Gamma_finetuned_models = load_all_Gamma_models(Prf_to_Seg_Model, os.path.join(ckpt_path, "fine-tuned"))

# === Define functions ===
def sigma_profile_wrapper(smiles):
    return get_sigma_profile(smiles, prf_model, geometry_model, cb_emb, st_emb)

def single_model_predictor(sigma, temperature):
    return Gamma_base_model(sigma, torch.tensor([temperature]))[1]

def ensemble_predictor(sigma, temperature):
    return ensemble_segac(Gamma_finetuned_models, sigma, temperature)

def select_gamma_predictor(model_type: str):
    if model_type == "base":
        return single_model_predictor
    elif model_type == "tuned":
        return ensemble_predictor
    else:
        raise ValueError("Invalid model_type. Choose 'base' or 'tuned'.")

def profile(smiles):
    return sigma_profile_wrapper(smiles)

def binary_lng(smiles:list, temperature:float, molefraction:list):
    gamma_predictor = select_gamma_predictor("tuned")
    
    ln_gamma_1, ln_gamma_2 = calc_ln_gamma_binary(smiles[0], smiles[1], molefraction, temperature,
                         gamma_predictor=gamma_predictor,
                         get_sigma_profile_fn=sigma_profile_wrapper)
    return ln_gamma_1.tolist(), ln_gamma_2.tolist()

def multi_lng(smiles:list, temperature:float, composition:list):
    gamma_predictor = select_gamma_predictor("tuned")
    
    lng_array = calc_ln_gamma(
    smiles,
    composition,
    temperature,
    gamma_predictor=gamma_predictor,
    get_sigma_profile_fn=sigma_profile_wrapper
    )
    
    return lng_array