# Factoreally

**Generate realistic test data from your actual production data patterns**

Factoreally automatically analyzes your real data to create intelligent factories that generate statistically accurate test data. Instead of manually crafting test fixtures or using random data that doesn't reflect reality, leverage the patterns hidden in your production datasets to build better tests, faster development cycles, and more reliable systems.

## Why Factoreally?

### 🎯 **Production-Grade Realism**
- **Data-driven accuracy**: Learns from your actual data patterns instead of generating random noise
- **Statistical fidelity**: Preserves field distributions, value frequencies, and structural relationships
- **Pattern recognition**: Automatically detects UUIDs, timestamps, email formats, and custom patterns
- **Relationship preservation**: Maintains correlations between nested fields and optional data
- **Pydantic model support**: Uses dictionary type annotations to identify dynamic object fields

### ⚡ **Accelerated Development**
- **Zero configuration**: Point at your data, get a working factory instantly
- **Type-safe integration**: Works seamlessly with Pydantic models and data classes
- **Flexible generation**: Create single objects, batches, or infinite streams
- **Override capabilities**: Customize specific fields while preserving realistic defaults

### 🔧 **Testing Excellence**
- **Comprehensive coverage**: Generate edge cases and realistic data distributions automatically
- **Consistent reproducibility**: Deterministic generation for reliable test suites
- **Performance at scale**: Generate thousands of realistic records efficiently
- **Integration ready**: Drop-in replacement for manual fixture creation

### 📊 **Business Impact**
- **Risk reduction**: Catch data-related bugs before they reach production
- **Time savings**: Eliminate hours of manual test data creation and maintenance
- **Quality assurance**: Test against realistic data scenarios, not toy examples
- **Compliance confidence**: Generate test data that mirrors production complexity without exposing sensitive information

## Quick Start

### 1. Generate a factory specification from your data

```bash
# Basic spec generation
factoreally create --in real_user_payloads.json --out user.spec.json

# With Pydantic model for dynamic field detection
factoreally create \
  --in user_payloads.json \
  --out user.spec.json \
  --model myapp.models.UserModel
```

### 2. Create intelligent factories

```python
from factoreally import Factory

# From saved specification file
user_factory = Factory("user.spec.json")

# Or directly from spec dictionary
user_factory = Factory(spec)

# Or with overrides built-in
admin_factory = Factory(spec, role="admin", permissions__level="high")
```

### 3. Generate realistic test data

```python
# Single realistic user
user_data = user_factory.build()

# Batch generation for performance tests
users = user_factory[:1000]

# Infinite stream for stress testing
for user in user_factory:
    process_user(user)
```

### 4. Integrate with your models

```python
# Works with Pydantic, dataclasses, or any validation library
user = UserModel.model_validate(user_factory.build())
users = [UserModel.model_validate(u) for u in user_factory[:100]]
```

### 5. Customize while preserving realism

```python
# Override specific fields
admin_factory = user_factory.copy(role="admin", permissions__level="high")

# Per-generation overrides
user = admin_factory.build(email="specific@example.com")

# Nested field overrides
user = user_factory.build(address__country="US", profile__verified=True)

# Array field overrides (applies to all array elements)
users = user_factory.build(actions__data__patient__id="fixed-id")

# Array element overrides (target specific array indices)
user = user_factory.build(items__0__name="first_item", items__1__value=999)
```

### Dynamic Overrides with Callables

Override values can be callables for dynamic, context-aware customization:

```python
# No arguments - static value generator
user = user_factory.build(id=lambda: str(uuid.uuid4()))

# One argument (factoreally's generated field value) - transform existing value
user = user_factory.build(name=lambda value: value.upper())

# Two arguments (field value, entire object) - complex logic
user = user_factory.build(
    display_name=lambda value, obj: f"{value} ({obj['role']})"
)

# Keyword-only arguments for clarity
user = user_factory.build(
    full_name=lambda *, obj: f"{obj['first_name']} {obj['last_name']}"
)

# Mixed callable and static overrides
user = user_factory.build(
    name=lambda value: value.title(),  # Callable
    email="admin@example.com",         # Static
    created_at=lambda: datetime.now()  # Callable
)
```

## Pydantic Model Integration

Factoreally's Pydantic integration helps identify dynamic dictionary fields in your data structure. By providing your Pydantic model, Factoreally can distinguish between static nested objects and dynamic dictionaries.


```python
from pydantic import BaseModel
from datetime import datetime
from typing import Dict, List, Optional

class UserEvent(BaseModel):
    user_id: str
    event_type: str
    metadata: Dict[str, str]  # Factoreally knows this is a dynamic dictionary
    profiles: List[UserProfile]  # Array of objects (no special handling)
    created_at: datetime
    settings: Optional[Dict[str, int]] = None  # Dynamic dict (Optional ignored)

# Without model: Factoreally guesses from data patterns
spec_basic = create_spec(sample_events)

# With model: Factoreally knows which fields are dynamic dictionaries
spec_enhanced = create_spec(sample_events, model=UserEvent)
```

Note: The actual key generation and pattern detection works the same
regardless of whether you provide a model or not

**⚡ Command Line Usage**
```bash
# Basic analysis
factoreally create --in api_logs.json --out api.spec.json

# With Pydantic model for dynamic field detection
factoreally create \
  --in api_logs.json \
  --out api.spec.json \
  --model myproject.schemas.APILogEvent

# Works with any importable Pydantic model
factoreally create \
  --in user_data.json \
  --out user.spec.json \
  --model backend.models.user.UserAccount
```

### Real-World Example: E-commerce Events

```python
from pydantic import BaseModel
from datetime import datetime
from typing import Dict, List, Optional
from decimal import Decimal

class ProductMetrics(BaseModel):
    views: int
    clicks: int
    conversions: float

class EcommerceEvent(BaseModel):
    event_id: str  # UUID pattern
    user_id: str   # UUID pattern
    session_id: str  # Different ID pattern

    # Dynamic object - product IDs as keys
    product_metrics: Dict[str, ProductMetrics]

    # Dynamic object - feature flags
    experiments: Dict[str, bool]

    # Static nested structure
    user_profile: UserProfile

    # Optional dynamic fields
    custom_attributes: Optional[Dict[str, str]] = None
    ab_tests: Optional[Dict[str, str]] = None

    timestamp: datetime
    revenue: Optional[Decimal] = None

# Sample data
sample_data = [
    {
        "event_id": "550e8400-e29b-41d4-a716-446655440000",
        "user_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
        "session_id": "sess_abc123xyz789",
        "product_metrics": {
            "prod_1": {"views": 45, "clicks": 12, "conversions": 0.27},
            "prod_2": {"views": 33, "clicks": 8, "conversions": 0.24}
        },
        "experiments": {
            "new_checkout": True,
            "recommended_products": False
        },
        "user_profile": {"tier": "premium", "region": "US"},
        "custom_attributes": {"source": "mobile", "campaign": "summer_sale"},
        "timestamp": "2024-01-15T10:30:00Z",
        "revenue": "125.99"
    }
]

# Create spec with model intelligence
spec = create_spec(sample_data, model=EcommerceEvent)
factory = Factory(spec)

# Generate realistic test events
event = factory.build()
# ✅ Realistic UUIDs for event_id, user_id
# ✅ Session ID following pattern sess_*
# ✅ Dynamic product_metrics with varied product IDs
# ✅ Realistic experiment flag combinations
# ✅ Consistent user_profile structure
# ✅ Optional fields respect original probabilities
```

## Advanced Features

### Pattern Recognition
Factoreally automatically detects and generates:
- **Temporal patterns**: ISO timestamps, durations, date formats
- **Structured identifiers**: UUIDs, Auth0 IDs, MAC addresses
- **Semantic patterns**: Email formats, phone numbers, custom schemas
- **Numerical distributions**: Maintains statistical properties of your data

### Dynamic Object Support
- **Automatic detection**: Recognizes dynamic dict fields vs static nested objects
- **Key pattern analysis**: Learns from UUID keys, date keys, or custom patterns
- **Flexible generation**: Creates realistic dynamic keys while preserving value patterns
- **Pydantic integration**: Use `Dict[K, V]` type annotations to identify dynamic fields

### Smart Null Handling
- Preserves optional field probabilities from your data
- Maintains conditional presence (nested objects appear when parents exist)
- Respects field interdependencies
- Gracefully handles None values in array overrides

### Performance Optimized
- Lazy evaluation for memory efficiency
- Batch generation capabilities
- Streaming interfaces for large datasets
- Minimal overhead factory creation

## Real-World Applications

**API Testing with Pydantic Models**: Generate test payloads with realistic data patterns. Use Pydantic model validation to ensure generated data matches your schemas.

**Load Testing**: Generate millions of realistic user profiles that stress-test your system with production-like data patterns.

**Integration Testing**: Create test data that matches your data patterns automatically. Generated data can be validated against your Pydantic models.

**Development Environments**: Populate local databases with realistic data for feature development without production data access.

**Compliance Testing**: Generate test datasets that mirror production complexity while maintaining data privacy.

**Performance Benchmarking**: Test with realistic data distributions instead of uniform random data that doesn't reflect actual usage patterns, leveraging your domain models for accuracy.

**Microservices Testing**: Generate consistent, realistic test data for distributed system testing using shared data patterns.
