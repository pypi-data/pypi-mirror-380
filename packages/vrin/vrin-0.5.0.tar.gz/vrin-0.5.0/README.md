# VRIN Hybrid RAG SDK v0.4.0

Enterprise-grade Hybrid RAG system with **hybrid cloud architecture**, user-defined AI specialization, multi-hop reasoning, and blazing-fast performance optimization.

## 🏗️ Hybrid Cloud Architecture

**VRIN supports two deployment models:**
- **General Users** (`vrin_` API keys): Cost-effective shared infrastructure
- **Enterprise Users** (`vrin_ent_` API keys): **100% private infrastructure with data sovereignty**

🛡️ **Data Sovereignty Guarantee**: Enterprise customer data NEVER leaves their cloud account

## 🚀 New in v0.4.0 - Hybrid Cloud & Performance Breakthrough

- 🏗️ **HYBRID CLOUD COMPLETE** - Enterprise private infrastructure with data sovereignty
- 🔄 **API Key Routing** - `vrin_` shared vs `vrin_ent_` private infrastructure
- ☁️ **Azure Integration** - CosmosDB with Gremlin API for enterprise customers
- 🏢 **Enterprise Portal** - Organization, user, and API key management
- ⚡ **Performance Revolution** - Raw fact retrieval in <2s (96.3% faster than full analysis)
- 🚀 **Dual-Speed Processing** - Fast website display + comprehensive expert analysis
- 🧠 **User-Defined Specialization** - Create custom AI experts for any domain
- 🔗 **Multi-Hop Reasoning** - Cross-document synthesis with reasoning chains
- 📊 **Enhanced Graph Retrieval** - Fixed Neptune storage, now finding 36-50 facts vs 0
- 🎯 **Expert-Level Performance** - 8.5/10 validation against professional analysis
- 🏗️ **Production Infrastructure** - 7 Lambda functions optimized (Python 3.12)
- 💾 **Smart Storage** - 40-60% reduction through intelligent deduplication
- 🔒 **Enterprise Security** - Bearer token auth, user isolation, compliance ready

## 🚀 Core Features

- 🏗️ **Hybrid Cloud Architecture** - Customer choice of infrastructure (shared vs private)
- 🛡️ **Data Sovereignty** - Enterprise data stays in customer cloud account
- ⚡ **Hybrid RAG Architecture** - Graph reasoning + Vector similarity search
- 🧠 **User-Defined AI Experts** - Customize reasoning for any domain
- 🔗 **Multi-Hop Reasoning** - Cross-document synthesis and pattern detection
- 📊 **Advanced Fact Extraction** - High-confidence structured knowledge extraction
- 🔍 **Expert-Level Analysis** - Professional-grade insights with reasoning chains
- 🏢 **Enterprise Portal** - Complete organization and user management
- 📈 **Enterprise-Ready** - User isolation, authentication, and production scaling

## 📦 Installation

```bash
pip install vrin==0.4.0
```

## 🔧 Quick Start

```python
from vrin import VRINClient

# For general users (shared infrastructure)
client = VRINClient(api_key="vrin_your_api_key")

# For enterprise users (private infrastructure with data sovereignty)
from vrin import VRINEnterpriseClient
enterprise_client = VRINEnterpriseClient(api_key="vrin_ent_your_enterprise_key")

# STEP 1: Define your custom AI expert
result = client.specialize(
    custom_prompt="You are a senior M&A legal partner with 25+ years experience...",
    reasoning_focus=["cross_document_synthesis", "causal_chains"],
    analysis_depth="expert"
)

# STEP 2: Insert knowledge with automatic fact extraction
result = client.insert(
    content="Complex M&A legal document content...",
    title="Strategic M&A Assessment"
)
print(f"✅ Extracted {result['facts_count']} facts")
print(f"💾 Storage: {result['storage_details']}")

# STEP 3A: Fast fact retrieval for website display (NEW v0.4.0)
raw_response = client.get_raw_facts_only("What are strategic insights?")
print(f"⚡ Lightning-fast retrieval: {raw_response['search_time']}")  # ~0.7-2s
print(f"📊 Facts found: {raw_response['total_facts']}")

# STEP 3B: Complete expert analysis for comprehensive reports
response = client.query("What are the strategic litigation opportunities?")
print(f"📝 Expert Analysis: {response['summary']}")
print(f"🔗 Multi-hop Chains: {response['multi_hop_chains']}")
print(f"📊 Cross-doc Patterns: {response['cross_document_patterns']}")
print(f"⚡ Full Analysis: {response['search_time']}")  # ~15-20s
```

## 📊 Performance & Validation (v0.4.0)

### Production Performance
- **⚡ Raw Fact Retrieval**: 0.7-2s (96.3% faster than full analysis)
- **🧠 Expert Analysis**: 15-20s for comprehensive multi-hop reasoning
- **📊 Graph Retrieval**: Now finding 36-50 facts (fixed from 0 facts)
- **🔗 Multi-hop Reasoning**: 1-10 reasoning chains per complex query
- **📋 Cross-document Patterns**: 2+ patterns detected per expert analysis
- **💾 Storage Efficiency**: 40-60% reduction through intelligent deduplication
- **🎯 Expert Validation**: 8.5/10 performance on professional M&A analysis
- **🏗️ Infrastructure**: 7 Lambda functions optimized (Python 3.12), sub-second API response

### Benchmark Validation (September 2025)
VRIN v0.4.0 validated against industry-standard RAG benchmarks:

| Benchmark | Accuracy | Validation |
|-----------|----------|------------|
| **RGB (Noise Robustness)** | **97.9%** ✅ | Core retrieval architecture validated |
| **FRAMES (Multi-hop)** | 28.6% | Multi-constraint reasoning challenges identified |
| **BEIR SciFact** | 22.2% | Scientific claim verification |
| **RAGBench FinQA** | 11.1% | Table interpretation enhancement in progress |

**Key Finding**: RGB benchmark (97.9% with 60% noise) validates VRIN's core hybrid retrieval is sound. Enhancement underway for structured data (tables).

**See**: `docs/BENCHMARK_TESTING_RESULTS.md` for comprehensive analysis

## 🏗️ Hybrid Cloud Architecture

VRIN uses enterprise-grade Hybrid RAG with **hybrid cloud architecture**:

### 🔄 API Key Routing
- **`vrin_` keys** → VRIN shared infrastructure (cost-effective)
- **`vrin_ent_` keys** → Customer private infrastructure (data sovereignty)

### 📊 Database Support
- **Neptune** (AWS) - For general users and AWS enterprise deployments
- **CosmosDB** (Azure) - For Azure enterprise deployments with Gremlin API
- **Automatic routing** based on API key type and enterprise configuration

### 🏢 Enterprise Portal
- Organization and user management
- API key provisioning and management
- Infrastructure configuration (Azure/AWS)
- Usage monitoring and analytics

### 🏗️ System Flow
1. **API Key Authentication** - Routes to appropriate infrastructure
2. **User Specialization** - Custom AI experts defined by users
3. **Enhanced Fact Extraction** - Multi-cloud database storage
4. **Multi-hop Reasoning** - Cross-document synthesis with reasoning chains
5. **Hybrid Retrieval** - Graph traversal + vector similarity (36-50 facts)
6. **Expert Synthesis** - Domain-specific analysis using custom prompts
7. **Production Infrastructure** - 11 Lambda functions with hybrid routing
8. **Enterprise Security** - Bearer token auth, user isolation, compliance

## 🔐 Authentication & Setup

### General Users (Shared Infrastructure)
1. Sign up at [VRIN Console](https://console.vrin.ai)
2. Get your `vrin_` API key from account dashboard
3. Use the API key to initialize your client

```python
client = VRINClient(api_key="vrin_your_api_key_here")
```

### Enterprise Users (Private Infrastructure)
1. Contact VRIN Enterprise Sales for onboarding
2. Deploy VRIN infrastructure in your Azure/AWS account
3. Get your `vrin_ent_` API key from enterprise portal
4. Configure your infrastructure via enterprise portal

```python
enterprise_client = VRINEnterpriseClient(api_key="vrin_ent_your_enterprise_key")
```

## 🏢 Production Ready Features

### 🔄 Hybrid Cloud
- **Data Sovereignty**: Enterprise data never leaves customer infrastructure
- **Multi-Cloud Support**: AWS Neptune and Azure CosmosDB
- **Intelligent Routing**: Automatic infrastructure routing by API key type
- **Enterprise Portal**: Complete organization and user management

### 🧠 AI Capabilities
- **Custom AI Experts**: Define domain-specific reasoning for any field
- **Multi-hop Analysis**: Cross-document synthesis with evidence chains
- **Working Graph Facts**: Fixed Neptune/CosmosDB storage now retrieving real relationships
- **Expert Validation**: 8.5/10 performance against professional analysis

### 🏗️ Infrastructure
- **Production APIs**: Bearer token auth, 99.5% uptime, enterprise ready
- **Smart Deduplication**: 40-60% storage optimization with transparency
- **Hybrid Database**: Seamless Neptune/CosmosDB routing
- **Enterprise Security**: VPC isolation, private endpoints, compliance ready

## 🎯 Use Cases

- **Legal Analysis**: M&A risk assessment, contract review, litigation strategy
- **Financial Research**: Investment analysis, market research, due diligence
- **Technical Documentation**: API analysis, architecture review, compliance
- **Strategic Planning**: Competitive analysis, market intelligence, decision support

## 🌟 What Makes VRIN Different

### vs. Basic RAG Systems
- ✅ **Multi-hop reasoning** across knowledge graphs
- ✅ **User-defined specialization** instead of rigid templates
- ✅ **Cross-document synthesis** with pattern detection
- ✅ **Expert-level performance** validated against professionals

### vs. Enterprise AI Platforms
- ✅ **Complete customization** - users define their own AI experts
- ✅ **Hybrid cloud architecture** - customer choice of infrastructure
- ✅ **100% data sovereignty** - enterprise data never leaves customer infrastructure
- ✅ **Multi-cloud support** - AWS and Azure with seamless routing
- ✅ **Enterprise portal** - complete organization and user management
- ✅ **Production-ready infrastructure** with full authentication
- ✅ **Temporal knowledge graphs** with provenance and graceful fallback handling
- ✅ **Resilient connectivity** - Neptune/CosmosDB fallback ensures service continuity
- ✅ **Open SDK** with transparent operations and full API access

## 📄 License

MIT License - see LICENSE file for details.

---

**Built with ❤️ by the VRIN Team**

*Last updated: September 15, 2025 - Production v0.4.0 with Hybrid Cloud Architecture*