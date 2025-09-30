# HalluNox

**Confidence-Aware Routing for Large Language Model Reliability Enhancement**

A Python package implementing a multi-signal approach to pre-generation hallucination mitigation for Large Language Models. HalluNox combines semantic alignment measurement, internal convergence analysis, and learned confidence estimation to produce unified confidence scores for proactive routing decisions.

## Features

- **🎯 Pre-generation Hallucination Detection**: Assess model reliability before generation begins
- **🔄 Confidence-Aware Routing**: Automatically route queries based on estimated confidence
- **🧠 Multi-Signal Approach**: Combines semantic alignment, internal convergence, and learned confidence
- **⚡ Optimized for Llama Models**: Default support for Llama-3.2-3B-Instruct architecture
- **📊 Comprehensive Evaluation**: Built-in metrics and routing strategy analysis
- **🚀 Easy Integration**: Simple API for both training and inference

## Research Foundation

Based on the research paper "Confidence-Aware Routing for Large Language Model Reliability Enhancement: A Multi-Signal Approach to Pre-Generation Hallucination Mitigation" by Nandakishor M (Convai Innovations).

The approach implements deterministic routing to appropriate response pathways:
- **High Confidence (≥0.8)**: Local generation  
- **Medium Confidence (0.6-0.8)**: Retrieval-augmented generation
- **Low Confidence (0.4-0.6)**: Route to larger models
- **Very Low Confidence (<0.4)**: Human review required

## Installation

### Requirements

- Python 3.8+
- PyTorch 1.13+
- CUDA-compatible GPU (recommended)
- At least 8GB GPU memory for training

### Install from PyPI

```bash
pip install hallunox
```

### Install from Source

```bash
git clone https://github.com/convai-innovations/hallunox.git
cd hallunox
pip install -e .
```

### Dependencies

HalluNox automatically installs the following dependencies:

- `torch>=1.13.0` - PyTorch framework
- `transformers>=4.21.0` - Hugging Face Transformers
- `FlagEmbedding>=1.2.0` - BGE-M3 embedding model
- `datasets>=2.0.0` - Dataset loading utilities
- `scikit-learn>=1.0.0` - Evaluation metrics
- `numpy>=1.21.0` - Numerical computations
- `tqdm>=4.64.0` - Progress bars

## Quick Start

### Using Pre-trained Model

```python
from hallunox import HallucinationDetector

# Initialize detector (downloads pre-trained model automatically)
detector = HallucinationDetector()

# Analyze text for hallucination risk
results = detector.predict([
    "The capital of France is Paris.",  # High confidence
    "Your password is 12345678.",       # Low confidence  
    "The Moon is made of cheese."       # Very low confidence
])

# View results
for pred in results["predictions"]:
    print(f"Text: {pred['text']}")
    print(f"Confidence: {pred['confidence_score']:.3f}")
    print(f"Risk Level: {pred['risk_level']}")
    print(f"Routing Action: {pred['routing_action']}")
    print()
```

### Command Line Interface

#### Interactive Mode
```bash
hallunox-infer --interactive
```

#### Batch Processing
```bash
hallunox-infer --input_file texts.txt --output_file results.json
```

#### Demo Mode
```bash
hallunox-infer --demo --show_routing
```

### Training Your Own Model

```python
from hallunox import Trainer, TrainingConfig

# Configure training
config = TrainingConfig(
    batch_size=8,
    learning_rate=5e-4,
    max_epochs=6,
    output_dir="./models/my_hallucination_model"
)

# Train model
trainer = Trainer(config)
trainer.train()
```

Or using the command line:

```bash
hallunox-train --batch_size 8 --learning_rate 5e-4 --max_epochs 6
```

## Model Architecture

HalluNox uses a hybrid architecture combining:

1. **LLM Component**: Llama-3.2-3B-Instruct (default)
   - Extracts internal hidden representations
   - Supports any Llama-architecture model
   
2. **Embedding Model**: BGE-M3 (fixed)
   - Provides reference semantic embeddings
   - 1024-dimensional dense vectors

3. **Projection Network**: 
   - Maps LLM hidden states (3072D) to embedding space (1024D)
   - 3-layer MLP with ReLU activations and dropout

## Configuration

### Model Configuration

```python
from hallunox import HallucinationDetector

detector = HallucinationDetector(
    model_path="path/to/trained/model.pt",           # Optional: uses pre-trained if None
    llm_model_id="unsloth/Llama-3.2-3B-Instruct",  # Any Llama model
    embed_model_id="BAAI/bge-m3",                    # Fixed embedding model
    device="cuda",                                   # cuda or cpu
    max_length=512,                                  # LLM sequence length
    bge_max_length=512,                             # BGE-M3 sequence length
    use_fp16=True                                    # Mixed precision
)
```

### Training Configuration

```python
from hallunox import TrainingConfig

config = TrainingConfig(
    # Model settings
    model_id="unsloth/Llama-3.2-3B-Instruct",
    embed_model_id="BAAI/bge-m3",
    
    # Training hyperparameters  
    batch_size=8,
    learning_rate=5e-4,
    max_epochs=6,
    warmup_steps=300,
    
    # Dataset configuration
    use_truthfulqa=True,
    use_halueval=True,
    use_fever=True,
    max_samples_per_dataset=3000,
    
    # Confidence thresholds
    high_confidence_threshold=0.9,
    medium_confidence_threshold=0.7,
    low_confidence_threshold=0.3,
)
```

## Pre-trained Model

A pre-trained model is available for immediate use:

```python
from hallunox.utils import download_model

# Automatically downloads from https://storage.googleapis.com/courseai/best_model_hl.pt
model_path = download_model()
```

The model was trained on a combination of:
- TruthfulQA
- HaluEval  
- FEVER
- XSum Factuality
- SQuAD v2
- Natural Questions
- Synthetic examples

## API Reference

### HallucinationDetector

#### Methods

- `predict(texts)`: Analyze texts for hallucination confidence
- `batch_predict(texts, batch_size=16)`: Process large batches efficiently  
- `evaluate_routing_strategy(texts)`: Analyze routing decisions

#### Returns

```python
{
    "predictions": [
        {
            "text": "input text",
            "confidence_score": 0.85,
            "similarity_score": 0.92,
            "interpretation": "HIGH_CONFIDENCE", 
            "risk_level": "LOW_RISK",
            "routing_action": "LOCAL_GENERATION",
            "description": "This response appears to be factual and reliable."
        }
    ],
    "summary": {
        "total_texts": 1,
        "avg_confidence": 0.85,
        "high_confidence_count": 1,
        "medium_confidence_count": 0,
        "low_confidence_count": 0,
        "very_low_confidence_count": 0
    }
}
```

### Training Classes

- `TrainingConfig`: Configuration dataclass for training parameters
- `Trainer`: Main training class with dataset loading and model training
- `MultiDatasetLoader`: Loads and combines multiple hallucination detection datasets

### Utility Functions

- `download_model()`: Download pre-trained model
- `setup_logging()`: Configure logging
- `check_gpu_availability()`: Check CUDA compatibility
- `validate_model_requirements()`: Verify dependencies

## Performance

Our confidence-aware routing system demonstrates:

- **74% hallucination detection rate** (vs 42% baseline)
- **9% false positive rate** (vs 15% baseline)  
- **40% reduction in computational cost** vs post-hoc methods
- **1.6x cost multiplier** vs always using expensive operations (4.2x)

## Hardware Requirements

### Minimum Requirements (Inference Only)
- **CPU**: Modern multi-core processor
- **RAM**: 12GB system memory minimum
- **GPU**: 8GB VRAM minimum (NVIDIA RTX 3070, RTX 4060 Ti, or better)
- **Storage**: 10GB free disk space for models
- **OS**: Python 3.8+ compatible operating system

### Recommended Requirements (Inference)
- **CPU**: Intel i7/AMD Ryzen 7 or better
- **RAM**: 16GB+ system memory  
- **GPU**: NVIDIA GPU with 12GB+ VRAM (RTX 4070, RTX 3080, or better)
- **Storage**: NVMe SSD with 15GB+ free space
- **CUDA**: 11.8+ compatible GPU driver

### Training Requirements
- **CPU**: High-performance multi-core processor (Intel i9/AMD Ryzen 9)
- **RAM**: 32GB+ system memory (64GB recommended)
- **GPU**: NVIDIA GPU with 24GB+ VRAM (RTX 4090, A100, H100, or better)
- **Storage**: 150GB+ free disk space (NVMe SSD strongly recommended)
  - Model checkpoints: ~5GB per epoch
  - Training datasets: ~20GB
  - Intermediate outputs: ~50GB
  - Logs and metrics: ~10GB
- **Network**: High-speed internet for dataset downloads

### CPU-Only Mode
- **RAM**: 16GB minimum (32GB recommended)
- **Storage**: 15GB free disk space
- **Note**: CPU inference is 10-50x slower than GPU inference

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

## Citation

If you use HalluNox in your research, please cite:

```bibtex
@article{nandakishor2024hallunox,
    title={Confidence-Aware Routing for Large Language Model Reliability Enhancement: A Multi-Signal Approach to Pre-Generation Hallucination Mitigation},
    author={Nandakishor M},
    journal={AI Safety Research},
    year={2024},
    organization={Convai Innovations}
}
```

## Contributing

We welcome contributions! Please see our contributing guidelines and submit pull requests to our repository.

## Support

For technical support and questions:
- Email: support@convaiinnovations.com  
- Issues: [GitHub Issues](https://github.com/convai-innovations/hallunox/issues)

## Author

**Nandakishor M**  
AI Safety Research  
Convai Innovations Pvt. Ltd.  
Email: support@convaiinnovations.com