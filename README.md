# LINDA - (Lazy INtelligent Distributed Agents)
Currently, this is just a trading engine.
- We use Alpaca API, Schwab API to source market data and submit trades.
- Currently using Conditional Normalizing Flows to predict some market trends

The hope is that we will eventually transition over to using AI agents to source these trends for us.

## Getting Started
While most of this was built from first principles ground up, some the resulting fruit can be seen deployed from Google Cloud Batch Run

[https://linda-1022869032774.us-central1.run.app](https://linda-1022869032774.us-central1.run.app)

## Project Directory Structure

```
├── Dockerfile
├── README.md
├── engine/
│   ├── pom.xml
│   ├── README.md
│   ├── src/
│   │   ├── main/
│   │   │   └── java/
│   │   │       └── com/
├── pengine/
│   ├── engine.py
│   ├── helper.py
│   ├── main.py
│   ├── requirements.txt
│   ├── server.py
│   └── strategies/
│       ├── AbstractStrategy.py
├── research/
│   ├── cnf/
```
