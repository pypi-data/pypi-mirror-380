"""
Hallucination Detection Module

This module provides the core HallucinationDetector class that implements
confidence-aware routing for LLM reliability enhancement using a multi-signal approach.
"""

import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Dict, Union
import warnings

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
)

# Import FlagEmbedding for BGE-M3
try:
    from FlagEmbedding import BGEM3FlagModel
    BGE_M3_AVAILABLE = True
except ImportError:
    BGE_M3_AVAILABLE = False
    warnings.warn(
        "FlagEmbedding not available. Install with: pip install -U FlagEmbedding",
        ImportWarning
    )

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)


class ProjectionHead(nn.Module):
    """
    Projection head for mapping LLM hidden states to embedding space.
    
    This component learns to project internal LLM representations to align
    with reference embeddings from BGE-M3 for confidence estimation.
    """
    
    def __init__(self, input_dim: int, output_dim: int, hidden_dim: int = 1024):
        """
        Initialize projection head.
        
        Args:
            input_dim: Dimension of input LLM hidden states
            output_dim: Dimension of target embedding space
            hidden_dim: Hidden layer dimension
        """
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, output_dim),
            nn.LayerNorm(output_dim),
        )

    def forward(self, x):
        """Forward pass through projection network."""
        return self.net(x)


def get_pooled_embeddings(
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    texts: List[str],
    device: str,
    max_length: int = 512,
):
    """
    Extract pooled embeddings from LLM.
    
    Args:
        model: The LLM model
        tokenizer: Associated tokenizer
        texts: List of input texts
        device: Computing device
        max_length: Maximum sequence length
        
    Returns:
        Pooled embeddings tensor
    """
    model.eval()
    inputs = tokenizer(
        texts,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=max_length,
    ).to(device)
    
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
    
    last_hidden = outputs.hidden_states[-1]
    mask = inputs.attention_mask.unsqueeze(-1)
    pooled = (last_hidden * mask).sum(dim=1) / mask.sum(dim=1)
    
    # Ensure output is on the specified device
    return pooled.to(device)


class HallucinationDetector:
    """
    Confidence-aware hallucination detector using Llama-3.2-3B + BGE-M3.
    
    This class implements the multi-signal confidence estimation approach described
    in the research paper, combining semantic alignment measurement, internal 
    convergence analysis, and learned confidence estimation.
    """
    
    def __init__(
        self,
        model_path: str = None,
        llm_model_id: str = "unsloth/Llama-3.2-3B-Instruct",
        embed_model_id: str = "BAAI/bge-m3",
        device: str = None,
        max_length: int = 512,
        bge_max_length: int = 512,
        use_fp16: bool = True,
        load_llm: bool = True,
        enable_inference: bool = False,
    ):
        """
        Initialize the hallucination detector.
        
        Args:
            model_path: Path to trained model checkpoint. If None, downloads pre-trained model.
            llm_model_id: Hugging Face model ID for the LLM
            embed_model_id: Hugging Face model ID for the embedding model
            device: Computing device ('cuda' or 'cpu')
            max_length: Maximum sequence length for LLM
            bge_max_length: Maximum sequence length for BGE-M3
            use_fp16: Whether to use FP16 precision
            load_llm: Whether to load the LLM (set False if only using for projection/embedding)
            enable_inference: Whether to enable LLM inference capabilities
        """
        if not BGE_M3_AVAILABLE:
            raise ImportError(
                "FlagEmbedding is required for BGE-M3. "
                "Install with: pip install -U FlagEmbedding"
            )
        
        # Auto-detect device if not specified
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
        self.max_length = max_length
        self.bge_max_length = bge_max_length
        self.use_fp16 = use_fp16
        self.load_llm = load_llm
        self.enable_inference = enable_inference
        
        print(f"🚀 Loading models on {self.device}...")
        
        # Download model if path not provided
        if model_path is None:
            from .utils import download_model
            model_path = download_model()
        
        # Load checkpoint with proper device mapping
        checkpoint = torch.load(model_path, map_location=self.device, weights_only=False)
        self.config = checkpoint['config']
        
        # Conditionally load LLM
        self.llm = None
        self.tokenizer = None
        
        if self.load_llm:
            print("📥 Loading Llama-3.2-3B-Instruct...")
            self.tokenizer = AutoTokenizer.from_pretrained(llm_model_id)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            
            model_dtype = torch.float16 if (use_fp16 and self.device == "cuda") else torch.float32
            self.llm = AutoModelForCausalLM.from_pretrained(
                llm_model_id,
                torch_dtype=model_dtype,
                device_map="auto" if self.device == "cuda" else None,
            )
            
            # Ensure LLM is on the correct device
            if self.device == "cpu":
                self.llm = self.llm.to(self.device)
        else:
            print("⏩ Skipping LLM loading (load_llm=False)")
            # Create a dummy tokenizer for cases where we need basic tokenization
            self.tokenizer = AutoTokenizer.from_pretrained(llm_model_id)
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Load BGE-M3
        print("📥 Loading BGE-M3...")
        # Disable FP16 for BGE-M3 when using CPU
        bge_use_fp16 = use_fp16 and (self.device == "cuda")
        self.embed_model = BGEM3FlagModel(embed_model_id, use_fp16=bge_use_fp16)
        
        # Load projection head
        print("📥 Loading projection head...")
        self.projector = ProjectionHead(
            self.config['llm_hidden_size'],
            self.config['embedding_dim'],
            hidden_dim=1536,
        ).to(self.device)
        
        self.projector.load_state_dict(checkpoint['projector_state'])
        self.projector.eval()
        
        # Ensure projection head is on same device as LLM (if loaded)
        if self.llm and hasattr(self.llm, 'device'):
            llm_device = next(self.llm.parameters()).device
            if str(llm_device) != str(self.device):
                print(f"⚠️ Moving projection head from {self.device} to {llm_device}")
                self.device = str(llm_device)
                self.projector = self.projector.to(self.device)
        
        print(f"✅ Model loaded successfully!")
        print(f"   LLM Hidden Size: {self.config['llm_hidden_size']}")
        print(f"   Embedding Dimension: {self.config['embedding_dim']}")
        if 'best_val_loss' in checkpoint:
            print(f"   Best Validation Loss: {checkpoint['best_val_loss']:.4f}")
    
    def predict(self, texts: Union[str, List[str]], query_context_pairs: List[Dict] = None) -> Dict:
        """
        Predict hallucination confidence scores for given texts.
        
        This method implements the core confidence estimation approach by:
        1. Computing semantic alignment between LLM and reference embeddings
        2. Analyzing internal convergence patterns
        3. Using learned confidence estimation
        
        Args:
            texts: Input text(s) to analyze
            query_context_pairs: Optional list of dicts with 'query' and 'context' keys for enhanced embedding
            
        Returns:
            Dictionary with predictions, confidence scores, and interpretations
        """
        if isinstance(texts, str):
            texts = [texts]
        
        # Prepare texts for embedding based on context
        embedding_texts = texts
        if query_context_pairs:
            # Format with specific prompt structure for better accuracy
            embedding_texts = []
            for i, text in enumerate(texts):
                if i < len(query_context_pairs) and query_context_pairs[i]:
                    pair = query_context_pairs[i]
                    formatted_text = f"query: {pair.get('query', text)}\ncontext: {pair.get('context', '')}"
                    embedding_texts.append(formatted_text)
                else:
                    embedding_texts.append(text)
        
        # Check if LLM is loaded for embedding computation
        if not self.load_llm or self.llm is None:
            raise RuntimeError("LLM not loaded. Set load_llm=True for hallucination detection.")
        
        # Get LLM embeddings and ensure they're on correct device
        # For projection model, use only query part for better similarity comparison
        projection_texts = texts
        if query_context_pairs:
            projection_texts = [pair.get('query', text) if i < len(query_context_pairs) and query_context_pairs[i] else text 
                             for i, (text, pair) in enumerate(zip(texts, query_context_pairs + [None] * len(texts)))]
        
        llm_embeddings = get_pooled_embeddings(
            self.llm,
            self.tokenizer,
            projection_texts,
            self.device,
            self.max_length,
        ).to(self.device)
        
        # Get BGE-M3 reference embeddings with formatted texts
        bge_outputs = self.embed_model.encode(
            embedding_texts,
            batch_size=len(embedding_texts),
            max_length=self.bge_max_length,
            return_dense=True,
            return_sparse=False,
            return_colbert_vecs=False,
        )
        
        ref_embeddings = torch.tensor(
            bge_outputs['dense_vecs'], 
            dtype=torch.float32,
            device=self.device
        )
        
        # Project LLM embeddings and compute similarity
        with torch.no_grad():
            # Ensure all tensors are on the same device and correct dtype
            llm_embeddings = llm_embeddings.float().to(self.device)
            ref_embeddings = ref_embeddings.to(self.device)
            
            projected = self.projector(llm_embeddings)
            similarities = F.cosine_similarity(projected, ref_embeddings, dim=1)
            confidence_scores = torch.sigmoid(similarities)
        
        # Convert to numpy for easier handling
        confidence_scores = confidence_scores.cpu().numpy()
        similarities = similarities.cpu().numpy()
        
        # Interpret results according to confidence-aware routing strategy
        results = []
        for i, (text, conf_score, sim_score) in enumerate(zip(texts, confidence_scores, similarities)):
            if conf_score >= 0.65:
                interpretation = "HIGH_CONFIDENCE"
                risk_level = "LOW_RISK"
                routing_action = "LOCAL_GENERATION"
                description = "This response appears to be factual and reliable."
            elif conf_score >= 0.60:
                interpretation = "MEDIUM_CONFIDENCE"
                risk_level = "MEDIUM_RISK"
                routing_action = "RAG_RETRIEVAL"
                description = "This response may contain uncertainties. Consider retrieval augmentation."
            elif conf_score >= 0.4:
                interpretation = "LOW_CONFIDENCE"
                risk_level = "HIGH_RISK"
                routing_action = "LARGER_MODEL"
                description = "This response is likely unreliable. Route to larger model."
            else:
                interpretation = "VERY_LOW_CONFIDENCE"
                risk_level = "VERY_HIGH_RISK"
                routing_action = "HUMAN_REVIEW"
                description = "This response appears to be highly unreliable. Human review required."
            
            results.append({
                "text": text,
                "confidence_score": float(conf_score),
                "similarity_score": float(sim_score),
                "interpretation": interpretation,
                "risk_level": risk_level,
                "routing_action": routing_action,
                "description": description,
            })
        
        return {
            "predictions": results,
            "summary": {
                "total_texts": len(texts),
                "avg_confidence": float(confidence_scores.mean()),
                "high_confidence_count": sum(1 for score in confidence_scores if score >= 0.65),
                "medium_confidence_count": sum(1 for score in confidence_scores if 0.60 <= score < 0.65),
                "low_confidence_count": sum(1 for score in confidence_scores if 0.4 <= score < 0.6),
                "very_low_confidence_count": sum(1 for score in confidence_scores if score < 0.4),
            }
        }
    
    def batch_predict(self, texts: List[str], batch_size: int = 16) -> Dict:
        """
        Process large batches of texts efficiently.
        
        Args:
            texts: List of texts to analyze
            batch_size: Batch size for processing
            
        Returns:
            Combined results dictionary
        """
        all_results = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_results = self.predict(batch)
            all_results.extend(batch_results["predictions"])
        
        # Compute overall summary
        confidence_scores = [r["confidence_score"] for r in all_results]
        
        return {
            "predictions": all_results,
            "summary": {
                "total_texts": len(texts),
                "avg_confidence": sum(confidence_scores) / len(confidence_scores),
                "high_confidence_count": sum(1 for score in confidence_scores if score >= 0.65),
                "medium_confidence_count": sum(1 for score in confidence_scores if 0.60 <= score < 0.65),
                "low_confidence_count": sum(1 for score in confidence_scores if 0.4 <= score < 0.6),
                "very_low_confidence_count": sum(1 for score in confidence_scores if score < 0.4),
            }
        }
    
    def evaluate_routing_strategy(self, texts: List[str]) -> Dict:
        """
        Evaluate the confidence-aware routing strategy for given texts.
        
        Args:
            texts: List of texts to analyze
            
        Returns:
            Routing strategy analysis
        """
        results = self.predict(texts)
        routing_counts = {}
        
        for pred in results["predictions"]:
            action = pred["routing_action"]
            routing_counts[action] = routing_counts.get(action, 0) + 1
        
        return {
            "routing_distribution": routing_counts,
            "computational_efficiency": {
                "local_generation_percentage": routing_counts.get("LOCAL_GENERATION", 0) / len(texts) * 100,
                "expensive_operations_percentage": (
                    routing_counts.get("RAG_RETRIEVAL", 0) + 
                    routing_counts.get("LARGER_MODEL", 0)
                ) / len(texts) * 100,
                "human_review_percentage": routing_counts.get("HUMAN_REVIEW", 0) / len(texts) * 100,
            },
            "summary": results["summary"]
        }
    
    def predict_with_query_context(self, query_context_pairs: List[Dict]) -> Dict:
        """
        Convenience method for predicting with query-context pairs.
        
        Args:
            query_context_pairs: List of dicts with 'query' and 'context' keys
            
        Returns:
            Dictionary with predictions, confidence scores, and interpretations
        """
        texts = [pair.get('query', '') for pair in query_context_pairs]
        return self.predict(texts, query_context_pairs=query_context_pairs)
    
    @classmethod
    def for_embedding_only(
        cls,
        model_path: str = None,
        embed_model_id: str = "BAAI/bge-m3",
        device: str = None,
        bge_max_length: int = 512,
        use_fp16: bool = True,
    ):
        """
        Create detector instance optimized for embedding-only usage (no LLM loading).
        
        Args:
            model_path: Path to trained model checkpoint
            embed_model_id: Hugging Face model ID for the embedding model
            device: Computing device ('cuda' or 'cpu')
            bge_max_length: Maximum sequence length for BGE-M3
            use_fp16: Whether to use FP16 precision
            
        Returns:
            HallucinationDetector instance with LLM disabled
        """
        return cls(
            model_path=model_path,
            embed_model_id=embed_model_id,
            device=device,
            bge_max_length=bge_max_length,
            use_fp16=use_fp16,
            load_llm=False,
            enable_inference=False,
        )