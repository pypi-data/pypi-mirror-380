# DSF AML SDK

**Reduce ML training data requirements by 70-90% through adaptive evaluation and knowledge distillation. Train surrogate models 10-100x faster than traditional approaches.**

## Why DSF AML?

Traditional ML requires thousands of labeled examples and hours of training. DSF AML uses **adaptive formula evaluation** combined with **knowledge distillation** to create fast, lightweight models from domain expertise with minimal data requirements.

---

## Core Concepts

Define weighted evaluation rules based on domain knowledge. The system learns from your data patterns (Enterprise) and can distill this knowledge into ultra-fast surrogate models (Premium). Ideal for scenarios requiring real-time predictions or resource-constrained environments.

---

## Installation

```bash
pip install dsf-aml-sdk
```

---

## Configuration (Environment Variables)

Professional and Enterprise tiers require license validation:

```bash
# Linux/macOS
export SUPABASE_URL="your_provided_url"
export SUPABASE_ANON_KEY="your_provided_key"

# Windows PowerShell
$env:SUPABASE_URL="your_provided_url"
$env:SUPABASE_ANON_KEY="your_provided_key"
```

**Local Development**: Create `.env` file:
```
SUPABASE_URL="your_provided_url"
SUPABASE_ANON_KEY="your_provided_key"
```

Load with `python-dotenv`:
```python
from dotenv import load_dotenv
load_dotenv()

from dsf_aml_sdk import AMLSDK
```

---

## Quick Start

### Community Edition

```python
from dsf_aml_sdk import AMLSDK

sdk = AMLSDK()

# Define domain rules
config = (sdk.create_config()
    .add_field('model_accuracy', default=0.95, weight=2.5, criticality=2.0)
    .add_field('training_epochs', default=100, weight=1.8, criticality=1.5)
    .add_field('validation_loss', default=0.05, weight=2.2, criticality=2.5)
)

# Evaluate ML experiment
experiment_data = {
    'model_accuracy': 0.96,
    'training_epochs': 105,
    'validation_loss': 0.048
}

result = sdk.evaluate(experiment_data, config)
print(f"Score: {result.score:.3f}")
```

### Professional Edition

```python
sdk = AMLSDK(license_key='PRO-2026-12-31-XXXX', tier='professional')

# Batch evaluation
experiments = [
    {'model_accuracy': 0.92, 'epochs': 50},
    {'model_accuracy': 0.95, 'epochs': 100},
    {'model_accuracy': 0.97, 'epochs': 150}
]

results = sdk.batch_evaluate(experiments, config)
metrics = sdk.get_metrics()
```

### Enterprise Edition - Knowledge Distillation

```python
sdk = AMLSDK(license_key='ENT-2026-12-31-XXXX', tier='enterprise')

# Define configuration
config = {
    'feature_importance': {'default': 0.8, 'weight': 2.0, 'criticality': 1.5},
    'correlation_score': {'default': 0.7, 'weight': 1.8, 'criticality': 1.3}
}

# Step 1: Train surrogate model (lightweight, fast)
distill_result = sdk.distill_train(
    config=config,
    samples=1000,  # Synthetic samples for distillation
    seed=42
)
print(f"Training loss: {distill_result.loss:.6f}")
print(f"Total samples seen: {distill_result.total_seen}")

# Step 2: Export trained model
export_data = sdk.distill_export(config=config)
print(f"Model persisted: {export_data.get('persisted')}")
if export_data.get('metrics'):
    print(f"Holdout MAE: {export_data['metrics']['mae']:.6f}")

# Step 3: Fast inference with surrogate
score = sdk.distill_predict(
    data={'feature_importance': 0.85, 'correlation_score': 0.72},
    config=config
)
print(f"Surrogate prediction: {score:.6f}")
# 10-100x faster than full evaluation
```

---

## Knowledge Distillation Workflow

```python
sdk = AMLSDK(license_key='ENT-...', tier='enterprise')

# 1. Define your domain rules
config = {
    'precision': {'default': 0.90, 'weight': 2.5},
    'recall': {'default': 0.85, 'weight': 2.3},
    'f1_score': {'default': 0.87, 'weight': 2.8}
}

# 2. Train surrogate (creates lightweight linear model)
result = sdk.distill_train(config=config, samples=2000)

# 3. Continuous training (incremental learning)
for batch_id in range(10):
    result = sdk.distill_train(config=config, samples=500, seed=batch_id)
    print(f"Batch {batch_id}: Loss={result.loss:.6f}")

# 4. Export with validation metrics
export = sdk.distill_export(config=config)
print(f"MAE: {export['metrics']['mae']:.4f}")
print(f"Within 1%: {export['metrics']['within_1pt']:.2%}")

# 5. Production inference
for new_data in production_stream:
    score = sdk.distill_predict(data=new_data, config=config)
    if score > 0.8:
        accept_model(new_data)
```

---

## Context Manager Pattern

```python
with AMLSDK(license_key='...', tier='enterprise') as sdk:
    result = sdk.evaluate(data, config)
    distill_result = sdk.distill_train(config, samples=1000)
    # Automatic cleanup
```

---

## Error Handling

```python
from dsf_aml_sdk import AMLSDK, LicenseError, ValidationError

try:
    sdk = AMLSDK(license_key='invalid', tier='enterprise')
    result = sdk.distill_train(config, samples=1000)
    
except LicenseError:
    print("Invalid license - distillation requires premium tier")
    sdk = AMLSDK()  # Fallback to community
    
except ValidationError as e:
    print(f"Invalid config: {e}")
```

---

## Tier Comparison

| Feature                      |  Community | Professional | Enterprise |
|------------------------------|------------|--------------|------------|
| **Single evaluation**        | ✅        | ✅           | ✅         |
| **Batch evaluation**         | ❌        | ✅           | ✅         |
| **Adaptive thresholds**      | ❌        | ✅           | ✅         |
| **Performance metrics**      | ❌        | ✅           | ✅ Enhanced|
| **Weight auto-calibration**  | ❌        | ❌           | ✅         |
| **Knowledge distillation**   | ❌        | ❌           | ✅         |
| **Surrogate models**         | ❌        | ❌           | ✅         |
| **Model export**             | ❌        | ❌           | ✅         |
| **Support**                  | Community  | Email        | Priority SLA|

---

## Enterprise Features

### Knowledge Distillation

Create lightweight surrogate models from your evaluation logic:

```python
# Teacher: Complex adaptive formula (slow, accurate)
# Student: Linear surrogate model (fast, approximates teacher)

sdk = AMLSDK(license_key='ENT-...', tier='enterprise')

# Distill knowledge
distill_result = sdk.distill_train(
    config=complex_config,
    samples=5000,  # More samples = better approximation
    seed=42
)

# Performance comparison
import time

# Full evaluation
start = time.time()
score_full = sdk.evaluate(data, config)
full_time = time.time() - start

# Surrogate prediction
start = time.time()
score_surrogate = sdk.distill_predict(data, config)
surrogate_time = time.time() - start

print(f"Full: {full_time:.4f}s, Surrogate: {surrogate_time:.6f}s")
print(f"Speedup: {full_time/surrogate_time:.1f}x")
```

### Adaptive Learning

```python
sdk = AMLSDK(tier='enterprise', mode='temporal_forgetting')

# System learns from evaluation patterns
for batch in data_batches:
    results = sdk.batch_evaluate(batch, config)
    
# View adaptations
metrics = sdk.get_metrics()
print(f"Weight changes: {metrics['weight_changes']}")
```

---

## API Reference

### AMLSDK

**Initialization:**
```python
AMLSDK(tier='community', license_key=None, mode='standard')
```

**Evaluation Methods:**
- `evaluate(data, config)` - Single evaluation
- `batch_evaluate(data_points, config)` - Batch processing (Pro/Enterprise)
- `get_metrics()` - Performance stats (Pro/Enterprise)

**Distillation Methods (Enterprise only):**
- `distill_train(config, samples=1000, seed=42)` - Train surrogate model
- `distill_export(config=None)` - Export with validation metrics
- `distill_predict(data, config)` - Fast inference with surrogate

### DistillationResult

```python
@dataclass
class DistillationResult:
    trained_on: int      # Samples in this training batch
    total_seen: int      # Total samples across all training
    loss: float          # Current MSE loss
    model_version: str   # Model architecture version
```

---

## Use Cases

### ML Experiment Tracking

```python
config = {
    'train_accuracy': {'default': 0.92, 'weight': 2.0},
    'val_accuracy': {'default': 0.88, 'weight': 2.5},
    'train_loss': {'default': 0.1, 'weight': 1.8},
    'overfitting_gap': {'default': 0.04, 'weight': 2.2}
}

# Score experiment quality
result = sdk.evaluate(experiment_metrics, config)
```

### Hyperparameter Optimization

```python
config = {
    'learning_rate': {'default': 0.001, 'weight': 2.0},
    'batch_size': {'default': 32, 'weight': 1.5},
    'dropout_rate': {'default': 0.3, 'weight': 1.8}
}

# Evaluate hyperparameter sets
for hp_set in hyperparameter_grid:
    score = sdk.evaluate(hp_set, config)
    if score > best_score:
        best_params = hp_set
```

### Model Selection

```python
config = {
    'accuracy': {'default': 0.90, 'weight': 2.5},
    'inference_time_ms': {'default': 100, 'weight': 2.0},
    'model_size_mb': {'default': 50, 'weight': 1.5},
    'memory_usage_mb': {'default': 200, 'weight': 1.8}
}

# Compare models
candidates = [resnet_metrics, mobilenet_metrics, efficientnet_metrics]
scores = sdk.batch_evaluate(candidates, config)
```

---

## Performance Benefits

### Data Efficiency
- Traditional ML: Requires 10,000+ labeled examples
- DSF AML: Effective with 100-1,000 examples + domain rules

### Training Speed
- Full evaluation: ~10-50ms per sample
- Surrogate model: ~0.1-0.5ms per sample (10-100x faster)

### Deployment Size
- Traditional models: 100MB-10GB
- Surrogate models: <1KB (weights + bias)

---

## FAQ

**Q: How accurate are surrogate models?**  
A: Typical MAE of 0.01-0.05 on normalized scores. Quality improves with more training samples.

**Q: Can I export models for edge devices?**  
A: Yes. Export provides JSON with weights/bias. Implement linear prediction in any language.

**Q: How does distillation work?**  
A: Generates synthetic samples, evaluates with teacher (adaptive formula), trains student (linear model) to match outputs.

**Q: When should I retrain?**  
A: When data distribution changes significantly or loss increases on validation set.

---

## Support

- **Documentation:** https://docs.dsf-aml.ai
- **Issues:** https://github.com/dsf-aml/sdk/issues
- **Enterprise Support:** contacto@softwarefinanzas.com.co

---

## Licensing

**Professional:** $299/month or $2,999/year
**Enterprise:** Custom pricing (includes distillation)

Contact: contacto@softwarefinanzas.com.co

**License format:**
- `PRO-YYYY-MM-DD-XXXX-XXXX`
- `ENT-YYYY-MM-DD-XXXX-XXXX`

---

## License

MIT for Community Edition. Professional/Enterprise subject to commercial terms.

© 2025 DSF AML SDK. Adaptive ML powered by Knowledge Distillation.