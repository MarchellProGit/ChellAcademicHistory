# Blockchain Technology (Semester 9)
> **Author**: Marchell Adi Pratama & Nova

---

## Domain Overview & Technical Specifications

A full-stack Web3 Decentralized Autonomous Organization (DAO) platform featuring Solidity smart contracts managed via Foundry and a responsive React + Vite + TailwindCSS dApp interface.

### Pipeline Architecture

```text
Semester-9/Blockchain/
 NexusDAO-Web3/
 foundry.toml # Foundry Compiler & Testnet Configuration
 src/
 NexusDAO.sol # Governance & Voting Smart Contract
 SimpleStorage.sol # State Storage Smart Contract
 script/
 Deploy.s.sol # Anvil Local Deployment Script
 test/
 NexusDAO.t.sol # Unit Tests (Voting & Proposal Execution)
 app/ # React + Vite + Tailwind Frontend
 src/
 App.tsx # Web3 UI Dashboard
 lib/ethereum.ts # Ethers/Viem Provider Integration
 package.json
 Crypto-Lab/ # Cryptographic Digest & Signature Scripts
```

---

## Build & Deployment Quickstart

### 1. Smart Contract Compilation & Verification (Foundry)
```bash
cd Semester-9/Blockchain/NexusDAO-Web3
forge build
forge test -vvv
```

### 2. Launching React Web3 Frontend
```bash
cd Semester-9/Blockchain/NexusDAO-Web3/app
npm install
npm run dev
```
