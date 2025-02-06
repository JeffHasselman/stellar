

<div align="center">
  
  [![Website](https://img.shields.io/badge/🌐_Visit_Our_Website-stellargateway.com-2ea44f?style=for-the-badge)](https://stellargateway.com)
  [![Twitter](https://img.shields.io/badge/Follow_Us-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/Stellar_Loom)
  
  <h1>Weaving Precision into Decentralization</h1>
  <p>Stellar Loom is an AI-driven decentralized oracle platform, meticulously designed to bridge the vast cosmos of real-world data with the precision of blockchain ecosystems. Leveraging cutting-edge artificial intelligence and a decentralized validator network, Stellar Loom ensures unrivaled data integrity, security, and scalability for the next era of decentralized finance (DeFi)</p>
</div>

<p align="center">
  <a href="#why-stellar">Why Stellar Loom?</a> •
  <a href="#core-features">Features</a> •
  <a href="#quick-tour">Demos</a> •
  <a href="#get-started-in-5-minutes">Quick Start</a> •
  <a href="#advanced-usage">Advanced</a>
</p>

## ✨ Why Stellar Loom?

- AI-driven, trustless, and highly secure decentralized oracles.
- Ultra-fast, real-time data feeds for DeFi applications.
- Seamless cross-chain interoperability across multiple blockchains.
- Decentralized validation ensures accuracy and eliminates manipulation.
- Adaptive AI optimization for minimal latency and maximum efficiency.

## 🚀 Core Features

- AI-Powered Data Aggregation – Cleans, verifies, and refines data from multiple sources.
- Decentralized Validation – Eliminates single points of failure and ensures trustless security.
- Ultra-Low Latency – High-speed data feeds optimized for DeFi and automated trading.
- Multi-Chain Compatibility – Seamless data integration across Ethereum, Solana, and more.
- Advanced Security Framework – AI-driven anomaly detection and cryptographic safeguards.

## 🎯 Quick Tour

Check out what's possible:
- 🌤️ [Weather Bot](demo/weather_forecast/README.md) - Live weather data integration
- 🏥 [Insurance Helper](demo/insurance_agent/README.md) - Policy management and claims
- 🔧 [Network Assistant](demo/network_agent/README.md) - Network monitoring and control
- 💱 [Currency Exchange](demo/currency_exchange/README.md) - Real-time forex rates
- 🤖 [LLM Router](demo/llm_routing/README.md) - Multi-model management

## Get Started in 5 Minutes

1. Grab the tools:
   ```bash
   # You'll need these
   docker compose version 2.29+
   python 3.12+
   ```

2. Install stellar:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install server/ #make sure you're in the stellar directory
   ```

3. Create your first agent:
   ```yaml
   # config.yaml
   version: v0.1
   listener:
     address: 0.0.0.0
     port: 10000
     message_format: huggingface
     connect_timeout: 0.005s
   
   llm_providers:
     - name: gpt-4
       provider: openai
       access_key: $OPENAI_API_KEY
   
   prompt_guards:
     input_guards:
       jailbreak:
         on_exception:
           message: Request blocked for security
   ```

4. Launch:
   ```bash
   stellargw up config.yaml
   ```

5. Start chatting:
   ```bash
   curl localhost:10000/v1/chat/completions \
     -H 'Content-Type: application/json' \
     -d '{"messages":[{"role":"user","content":"Hello!"}]}'
   ```

## 🛠️ Advanced Usage

### 🔄 LLM Routing
Switch between models on the fly:
```bash
curl -H 'x-stellar-llm-provider-hint: gpt-4' localhost:10000/v1/chat/completions
```

### ⚡️ Function Calling
Connect to your APIs:
```yaml
prompt_targets:
  - name: get_weather
    endpoint:
      name: weather_api
      path: /v1/current
```

### 🛡️ Security Features
Built-in protection against:
- 🚫 Prompt injection
- 🔒 Jailbreak attempts
- 🔑 Token theft
- ⚡️ Rate abuse

## 📊 Watch It Work

Monitor everything in real-time:
```mermaid
graph LR
    A[Your App] --> B[stellar Gateway]
    B --> C[AI Models]
    B --> D[Your APIs]
    B --> E[Metrics]
```

- 📈 Performance metrics: http://localhost:19901/stats
- 🎯 Visual dashboards: http://localhost:3000/
- 🔍 Request tracing: http://localhost:16686/

## 🌟 Community & Support

<div align="center">
  
  [![GitHub Stars](https://img.shields.io/github/stars/stellarlaboratory/stellar?style=social)](https://github.com/stellarlaboratory/stellar)
  [![Twitter Follow](https://img.shields.io/twitter/follow/stellargateway?style=social)](https://twitter.com/stellargateway)
  
</div>

- 🐦 [Twitter Updates](https://twitter.com/stellargateway)
- 📧 [Email Support](mailto:support@stellargateway.com)

---

<div align="center">
  <sub>Built with ❤️ by the stellar team</sub>
</div>
