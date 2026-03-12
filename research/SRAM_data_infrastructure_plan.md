# SRAM LLC — Modern Data Infrastructure & AI Architecture Plan
**Prepared:** March 2026
**Scope:** AWS-native centralized data lakehouse, ERP/CRM modernization, and AI/ML adoption roadmap
**Audience:** SRAM C-suite and technology leadership
**Confidence:** `Confirmed` = explicit source evidence | `Inference` = reasoned synthesis | `Speculative` = plausible but not verified

---

## Executive Summary

SRAM LLC operates a $1B+ multi-brand portfolio spanning nine distinct product lines — from AXS wireless drivetrains and RockShox suspension to Hammerhead cycling computers and Quarq power meters — across manufacturing facilities in Taiwan, Portugal, and China, with R&D centers in Chicago, Colorado Springs, Bloomington, and Spearfish. Despite this complexity, SRAM's current data infrastructure almost certainly resembles the industry norm for private manufacturers of its era: siloed ERP systems per brand or region, manual demand planning, disconnected customer service platforms, and no unified data foundation capable of supporting modern AI and machine learning workloads. This fragmentation is not merely an operational inconvenience — it is a strategic liability. SRAM sits atop one of the most valuable untapped telemetry datasets in consumer hardware: millions of AXS components in the field continuously transmitting shift counts, battery state, error codes, and performance signatures; Quarq crank sensors capturing rider power and cadence; RockShox AXS shocks reporting suspension travel and sag; and Hammerhead Karoo computers stitching it all together with GPS, terrain, and environmental context. Without a unified data platform, this asset generates no intelligence.

This plan proposes a purpose-built, AWS-native modern data architecture centered on a three-layer lakehouse (Bronze/Silver/Gold on Amazon S3 with Delta Lake), SAP S/4HANA Cloud via RISE with SAP as the consolidated ERP backbone, Salesforce as the CRM and dealer/warranty management platform, and Databricks on AWS as the unified analytics and machine learning engine. The architecture is designed around SRAM's specific operational reality: a greenfield opportunity in the new 100,000 m² Taichung mega-factory, an AXS telemetry network that no competitor can replicate, a documented customer service crisis that AI can resolve, and a supply chain exposed to Taiwan concentration risk that demands AI-driven scenario modeling. The total three-year investment is estimated at $39–58M against a combined cost reduction and revenue expansion opportunity of $147M+ — a roughly 3× return driven by manufacturing quality AI, demand forecasting, AXS Intelligence Platform subscriptions, and warranty automation. The window to establish an unassailable data and AI moat in the cycling industry is now; Shimano has no comparable connected ecosystem, but that advantage expires the moment a competitor decides to build one.

---

## 1. Strategic Context: Why SRAM Needs This Now

### 1.1 The AXS Telemetry Opportunity

`Inference` — SRAM's AXS ecosystem generates a dataset that no bicycle component company possesses at scale. Every AXS component in the field transmits:

| Source | Data Generated |
|---|---|
| **AXS Drivetrain** (RED/Force/Rival/Eagle) | Gear position, shift counts, actuation events, battery state, firmware version, error codes |
| **Quarq Power Meters** | Power (watts), cadence, torque, crank angle — timestamped per pedal stroke |
| **RockShox AXS** (Reverb, Super Deluxe, Pike) | Suspension travel, sag position, compression/rebound settings, actuation counts |
| **Hammerhead Karoo 3** | GPS track, elevation, gradient, speed, temperature, route data, third-party integrations (Strava, TrainingPeaks) |

Combined, this is the most complete picture of bicycle performance ever collected from the field. Without a unified data platform, it sits siloed in app databases with no cross-brand intelligence layer.

### 1.2 The Operational Gap

`Inference` — SRAM's current likely state based on company age, private ownership, and acquisition history:

- **ERP:** Multiple legacy systems across brands and geographies, possibly including SAP ECC (pre-S/4HANA), Oracle, or custom systems per acquired brand (Hammerhead, Zipp, Quarq each joined with their own tech stacks)
- **Demand planning:** Spreadsheet-heavy or basic ERP MRP; structurally unable to incorporate external signals (OEM build schedules, POS data, cycling participation trends)
- **Customer service:** Likely fragmented across Zendesk instances or similar per brand — no unified warranty database, no AI triage, no telemetry-informed warranty assessment
- **Data warehouse:** Likely absent or rudimentary; no unified Gold layer serving BI and ML

### 1.3 The Greenfield Moment

Three SRAM-specific circumstances make now the optimal time to build:

1. **Taiwan mega-factory under construction** — The new 100,000 m² Taichung facility is a greenfield deployment opportunity. Installing IoT sensor infrastructure, AI quality control systems, and MES/ERP integrations during construction is 3–5× cheaper than retrofitting an operational facility.
2. **AXS installed base reaching scale** — The AXS ecosystem has enough active users (estimated 500K–1.5M globally) to generate statistically significant ML training data and to justify a subscription monetization layer on top of the free AXS app.
3. **Competitive window** — Shimano has no native cycling computer, no native power meter brand, and no suspension brand. SRAM's multi-sensor ecosystem advantage exists today; it does not exist permanently.

---

## 2. Cloud Foundation: AWS

AWS is confirmed in SRAM's existing engineering tooling (job postings reference AWS explicitly — `Confirmed` [S11]) and is the recommended primary cloud provider for this architecture.

**Why AWS for SRAM specifically:**
- Already in SRAM's technology footprint — reduces adoption friction
- RISE with SAP on AWS is a validated path (AWS is SAP's preferred hyperscaler for cloud ERP)
- AWS IoT Core + IoT SiteWise purpose-built for factory telemetry collection at the Taichung mega-factory
- Amazon Bedrock provides access to Anthropic Claude (recommended for warranty AI, AXS coaching, and CS chatbot) via private, enterprise-grade endpoints
- SageMaker provides end-to-end ML lifecycle management for AXS component health models

**Multi-account structure (AWS Organizations):**

| Account | Purpose |
|---|---|
| `sram-management` | Billing, governance, IAM Identity Center (SSO) |
| `sram-data-platform` | Lakehouse, Databricks, ML workloads |
| `sram-erp-prod` | SAP S/4HANA workloads |
| `sram-crm-integration` | Salesforce connectors, EventBridge |
| `sram-iot-factory` | IoT Core, IoT SiteWise, factory data |
| `sram-dev` / `sram-staging` | Per-environment sandbox and UAT |

Single AWS region primary: `us-east-1` with cross-region failover to `eu-west-1` (Amsterdam — near SRAM European HQ in Amstelveen) for GDPR data residency compliance on EU rider data.

---

## 3. ERP: SAP S/4HANA Cloud via RISE with SAP on AWS

### 3.1 Recommendation

**SAP S/4HANA Cloud (RISE with SAP), deployed on AWS.**

`Inference` — For a $1B+ multi-brand precision manufacturer with global operations across 10+ countries, complex OEM supply relationships (Brose motor partnership, chain manufacturing, OEM spec contracts with Trek/Specialized/Giant/Canyon), and multi-channel revenue (OEM, IBD, aftermarket), SAP S/4HANA is the appropriate ERP. No other platform handles this combination of manufacturing complexity, multi-entity consolidation, and supply chain depth as well at SRAM's scale.

### 3.2 SRAM-Specific SAP Modules

| SAP Module | SRAM Application |
|---|---|
| **Manufacturing (PP/MF)** | Production planning across Taichung, Coimbra, China facilities; BOMs for multi-brand components |
| **Materials Management (MM)** | Procurement from Brose (motor), chain raw materials, carbon fiber suppliers; MAP policy enforcement |
| **Sales & Distribution (SD)** | OEM contract management (Trek, Specialized, Giant, Canyon); IBD wholesale orders; MAP/pricing rules |
| **Quality Management (QM)** | Defect tracking, recall management (2024 brake lever CPSC recall process), inspection workflows |
| **Plant Maintenance (PM)** | Equipment maintenance scheduling at Taichung mega-factory; integration with predictive maintenance AI |
| **Finance (FI/CO)** | Multi-entity consolidation across SRAM LLC, Zipp, Hammerhead, TIME, Velocio; cost center reporting |
| **Supply Chain Management (SCM)** | Taiwan concentration risk modeling; Coimbra chain supply planning; tariff scenario analysis |
| **Warranty & Service (CS)** | Component serial number tracking; warranty entitlement linked to AXS telemetry; recall management |

### 3.3 Implementation Notes

- **SAP BTP (Business Technology Platform)** — integration middleware connecting SAP to the AWS data platform, Salesforce, and the AXS app backend via REST APIs
- **Phase in by process area:** Finance/procurement first (lowest disruption), then manufacturing, then sales/distribution
- Use **AWS Launch Wizard for SAP** for initial deployment; **AWS Backint Agent** for SAP HANA database backups to S3
- Brand-specific legacy systems (Hammerhead runs its own SaaS infrastructure; Karoo OS is independent) connect via SAP BTP APIs, not direct integration — this preserves Hammerhead's velocity while giving central finance/ops visibility

---

## 4. CRM: Salesforce Sales + Service Cloud

### 4.1 Recommendation

**Salesforce Sales Cloud + Service Cloud + AgentForce**, integrated with SAP via MuleSoft.

### 4.2 SRAM-Specific CRM Architecture

SRAM's channel structure is unusual for a manufacturer: it operates simultaneously in B2B (OEM spec contracts, IBD wholesale), B2B2C (dealer-sold components), and increasingly near-DTC (Hammerhead Karoo direct retail, Velocio apparel). Salesforce handles all three:

| Salesforce Object | SRAM Use Case |
|---|---|
| **Accounts (OEM)** | Trek, Specialized, Giant, Canyon, Santa Cruz, Yeti — spec contract relationships, model year pipeline |
| **Accounts (IBD)** | ~5,000+ independent bike dealers globally; purchase history, service capability rating, region |
| **Accounts (Distributor)** | Rush Sports and regional distributors; territory management |
| **Contacts** | Dealer mechanics, OEM purchasing managers, brand marketing contacts |
| **Opportunities** | OEM spec contract pipeline (e.g., "Trek 2027 Slash spec — Eagle Transmission vs. Shimano XTR") |
| **Cases (Warranty)** | Warranty claims linked to AXS component serial numbers + telemetry; AI-assessed entitlement |
| **Service Contracts** | Per-component warranty periods by SKU; auto-expiry and renewal tracking |
| **Knowledge Base** | AI-indexed service documentation, installation guides, firmware release notes per product line |

### 4.3 Warranty AI — SRAM's Most Urgent CRM Initiative

`Confirmed` — SRAM's Trustpilot score (~1.6/5) and PissedConsumer volume (114 reviews) indicate a systemic warranty and customer service problem. [S48]

The fix is architectural, not just operational. Because AXS components transmit usage telemetry (shift counts, mileage equivalent, battery cycles, error codes) already captured in SRAM's AXS backend, AI can make objective warranty assessments using actual usage data:

```
Warranty Claim Received
        │
        ▼
AXS Telemetry Pull (via SAP CS → AXS API)
        │
  Component registered? → No → Route to registration verification
        │ Yes
        ▼
Usage within warranty parameters?
  • Shift count vs. expected lifespan
  • Environmental exposure (temp/moisture via Karoo GPS)
  • Firmware version at time of failure
  • Error code history
        │
        ▼
Claude (Bedrock) reasons over telemetry + warranty policy
        │
  ┌─────┴─────┐
Auto-approve  Human review  Auto-deny (with explanation)
  (standard)  (edge cases)  (clear out-of-warranty)
```

This simultaneously eliminates unjust denials (rider gets objective telemetry-backed decision) and fraudulent claims (AI flags components with usage patterns inconsistent with claimed failure).

---

## 5. Data Lakehouse Architecture

### 5.1 Core Platform: Databricks on AWS + Amazon S3

`Inference` — Databricks on AWS is the right choice for SRAM because:
- SRAM's highest-value use cases are ML-heavy (AXS component health prediction, demand forecasting, manufacturing QC) — Databricks is ML-native
- Unity Catalog provides cross-brand governance (SRAM brand, RockShox, Zipp, Quarq, Hammerhead data domains — each brand owns its domain, central governance)
- Delta Lake on S3 handles both streaming IoT data (factory sensors, AXS telemetry) and batch ERP/CRM data in one platform
- MLflow (built-in) manages all model versioning and deployment without additional tooling

### 5.2 Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       SOURCE SYSTEMS                            │
│                                                                 │
│  SAP S/4HANA  │  Salesforce  │  AXS Backend  │  Hammerhead     │
│  (ERP/MRP)    │  (CRM/Cases) │  (Telemetry)  │  (Karoo GPS)    │
│                                                                 │
│  Quarq Power  │  RockShox    │  Factory IoT  │  E-Commerce /   │
│  (Ride data)  │  AXS Data    │  (SiteWise)   │  Dealer EDI     │
└───────────────────────────┬─────────────────────────────────────┘
                            │
          ┌─────────────────┼──────────────────┐
          │                 │                  │
     AWS Glue          Amazon MSK          AWS AppFlow
     + Fivetran        (Kafka) via         (Salesforce
     (batch ERP/       Amazon              → S3 sync)
      CRM data)        Kinesis
     AWS Transfer      (AXS                AWS IoT
     Family (EDI)      telemetry           Core → S3
                       stream)             (factory)
          │                 │                  │
          └─────────────────▼──────────────────┘
┌───────────────────────────────────────────────────────────────┐
│              BRONZE LAYER  (Amazon S3 — raw zone)             │
│   Raw ERP extracts │ Raw Salesforce │ Raw AXS telemetry       │
│   Factory sensor streams │ Karoo GPS tracks │ Dealer EDI      │
│   Retention: 7 years │ Format: Delta Lake / Parquet           │
└───────────────────────────┬───────────────────────────────────┘
                            │ AWS Glue / Databricks ETL
┌───────────────────────────▼───────────────────────────────────┐
│             SILVER LAYER  (Amazon S3 — clean zone)            │
│   Cleaned, deduplicated, conformed                            │
│   dim_components │ dim_products │ dim_dealers │ dim_riders     │
│   fct_warranty_claims │ fct_orders │ fct_axs_events           │
│   fct_factory_sensor_readings │ fct_rides (Karoo/Quarq)       │
│   Unity Catalog enforces schema contracts                     │
└───────────────────────────┬───────────────────────────────────┘
                            │ dbt transformations
┌───────────────────────────▼───────────────────────────────────┐
│              GOLD LAYER   (Amazon S3 — governed metrics)      │
│   Business-ready, governed by Unity Catalog                   │
│   Brand P&L rollup │ Dealer performance │ Component health    │
│   Warranty claim rates by SKU │ Demand forecast inputs        │
│   AXS fleet telemetry aggregates │ Factory OEE               │
└───────────────────────────────────────────────────────────────┘
```

### 5.3 Brand Data Domains (Data Mesh Pattern)

SRAM's nine-brand portfolio benefits from a data mesh approach — each brand owns its data domain; central platform team owns infrastructure and governance:

| Data Domain | Owner | Key Data Products |
|---|---|---|
| **SRAM Drivetrain** | SRAM product team | AXS shift telemetry, groupset OEM spec, warranty claims |
| **RockShox** | RockShox product team | Suspension telemetry, fork/shock serial registry, service intervals |
| **Zipp** | Zipp product team | Wheel serial numbers, OEM spec, CFD performance data |
| **Quarq** | Quarq product team | Power meter data, ride metrics, calibration history |
| **Hammerhead** | Hammerhead product team | Karoo GPS tracks, route data, software version telemetry |
| **Supply Chain** | Operations | Factory production data, inventory, supplier lead times |
| **Commercial** | Sales/Finance | OEM contracts, IBD orders, dealer performance, financials |

### 5.4 Orchestration & Semantic Layer

- **Amazon MWAA (Managed Apache Airflow)** — pipeline scheduling; coordinates Glue jobs, Databricks jobs, SageMaker pipelines
- **dbt Cloud** — semantic layer running against Databricks SQL; business analysts query governed `fct_orders`, `dim_products` models, not raw SAP tables
- **Databricks SQL + Genie** — natural language querying of Gold layer for non-technical users

---

## 6. Integration & API Layer

### 6.1 Architecture

| Integration Pattern | AWS Service | SRAM Use Case |
|---|---|---|
| **Event bus** | Amazon EventBridge | SAP order events → Salesforce; AXS firmware update events → warranty eligibility updates |
| **Message queue** | Amazon SQS + SNS | Async warranty claim processing; dealer order notifications |
| **High-throughput streaming** | Amazon MSK (Managed Kafka) | AXS telemetry stream (millions of component events/day) |
| **IoT ingestion** | AWS IoT Core | Factory sensor data (Taichung, Coimbra); AXS component firmware OTA events |
| **File/EDI** | AWS Transfer Family | OEM EDI (Trek/Specialized build schedules); dealer wholesale orders |
| **API management** | Amazon API Gateway | Internal microservices; controlled AXS Developer API (existing licensed API program) |
| **Enterprise iPaaS** | **MuleSoft Anypoint** | SAP S/4HANA ↔ Salesforce bidirectional sync; pre-built connectors save months |

### 6.2 AXS API Integration Note

`Confirmed` — SRAM operates a licensed AXS API developer program [S37]. The data infrastructure must integrate with this existing API layer — the Gold layer's AXS telemetry datasets feed both internal AI models and the licensed developer ecosystem. This is a potential B2B data revenue stream (see Section 8.4).

---

## 7. IoT & Factory Intelligence (Taichung Mega-Factory)

The new 100,000 m² Taichung facility is the most important AI deployment opportunity SRAM has in the near term. Building AI infrastructure into the facility during construction is a multi-million dollar advantage over retrofitting.

### 7.1 Factory Data Stack

| Layer | Technology | SRAM Application |
|---|---|---|
| **Device/Edge** | **AWS IoT Greengrass** | Edge inference on assembly line — detect defects before data hits cloud; reduce latency |
| **IoT Ingestion** | **AWS IoT Core** | MQTT broker for all factory sensor streams (vibration, thermal, current, vision camera feeds) |
| **Industrial Data** | **AWS IoT SiteWise** | Asset hierarchy modeling (CNC machines, assembly cells, test equipment); OEE calculation |
| **Streaming processing** | **Amazon Kinesis Data Streams** | Real-time sensor data processing; anomaly detection triggers |
| **Storage** | **Amazon S3 (Bronze)** | Raw sensor time-series; 7-year retention |
| **ML inference** | **Amazon SageMaker** | Deployed predictive maintenance models; defect classification models |

### 7.2 Quality Control AI Vision

`Confirmed` — The 2024 CPSC recall of 20,000+ shift brake levers for improper threadlock application [CPSC 2024] is the paradigm case for AI vision QC. The assembly defect (excess threadlock creating false torque readings during assembly) is exactly the defect class that AI vision systems catch.

**Deployment at Taichung:**
- **Cognex ViDi** or **Landing AI** vision models trained on SRAM component defect signatures
- Camera stations at: threadlock application, torque verification, final assembly inspection, packaging
- **AWS IoT Greengrass** runs inference at the edge; only exception events sent to cloud for logging
- Integration: defect events → SAP QM module → quality dashboard in Power BI / QuickSight

**Target improvements:**
- Defect detection: 98–99% accuracy vs. 80–85% human inspection
- Recall prevention: 1 prevented recall per 3-year period saves estimated $5–20M
- Inspection throughput: 25–50% faster cycle time

### 7.3 Predictive Maintenance

High-precision CNC machining at Taichung requires scheduled maintenance to prevent unplanned downtime. Estimated cost of unplanned downtime: $10,000–$50,000/hour.

**Sensor deployment:** Vibration (accelerometers), thermal (IR), current draw on spindle motors, acoustic emission on cutting tools
**Platform:** AWS IoT SiteWise → Amazon Kinesis → SageMaker anomaly detection (Random Cut Forest)
**Integration:** SageMaker alert → Amazon SNS → SAP PM work order created automatically

---

## 8. AI/ML Architecture

### 8.1 Foundation Models: Amazon Bedrock

All LLM workloads route through **Amazon Bedrock** — private, enterprise-grade, no data leaves SRAM's AWS environment:

| Model | SRAM Use Case |
|---|---|
| **Anthropic Claude 3.5/3.7** (via Bedrock) | Warranty claim reasoning, AXS coaching insights, CS chatbot, internal knowledge assistant, competitive brief synthesis |
| **Amazon Titan Embeddings** | Vector embeddings for RAG over SRAM knowledge base (product manuals, service docs, firmware changelogs) |
| **Meta Llama 3** (via Bedrock) | Cost-optimized high-volume classification (warranty triage, dealer inquiry routing) |
| **Amazon Nova** | Structured data tasks (generating dealer performance summaries, SAP report narration) |

**Amazon Bedrock Knowledge Bases** — RAG infrastructure indexing:
- All SRAM/RockShox/Zipp/Quarq product manuals
- AXS firmware changelogs (auto-ingested on each release)
- Warranty policy documents by brand and SKU
- IBD training materials and installation guides

### 8.2 ML Platform: Amazon SageMaker

| SageMaker Component | SRAM Application |
|---|---|
| **SageMaker Studio** | Data science IDE for AXS telemetry models, demand forecasting |
| **SageMaker Pipelines** | Automated retraining pipelines for component health models (triggered on new telemetry batches) |
| **SageMaker Feature Store** | Centralized feature registry — `component_age_hours`, `terrain_severity_score`, `power_stress_index` shared across all models |
| **SageMaker Model Registry** | Versioned model catalog; A/B deployment (e.g., compare XGBoost vs. LightGBM for cassette wear prediction) |
| **SageMaker Canvas** | No-code demand forecasting for supply chain planners who don't write Python |
| **SageMaker Clarify** | Bias/fairness checks on warranty AI (ensure no geographic or demographic bias in denial rates) |

### 8.3 Agentic Framework

| Agent | Platform | Capability |
|---|---|---|
| **Warranty Assessment Agent** | Bedrock Agents + Lambda | Pull AXS telemetry, evaluate warranty policy, approve/deny/escalate claim |
| **Dealer Intelligence Agent** | Bedrock Agents + Lambda | Query Salesforce + Gold layer, generate personalized dealer outreach recommendations |
| **Competitive Intelligence Agent** | Bedrock Agents + Crayon API | Monitor Shimano/Fox/Garmin launches; synthesize weekly competitive brief for SRAM leadership |
| **Supply Chain Risk Agent** | Bedrock Agents + SageMaker | Monitor Taiwan geopolitical signals, supplier lead time data; flag risk scenarios and recommend inventory buffers |
| **AgentForce (Salesforce)** | Salesforce native | In-CRM agent for dealer service reps; auto-drafts responses, schedules follow-ups, creates warranty cases |

---

## 9. Specific AI/ML Use Cases for SRAM

### 9.1 AXS Component Health Prediction

**The opportunity:** `Inference` — AXS telemetry contains the signals to predict component wear before riders experience failure. No competitor can build this model because no competitor has the data.

**Model inputs (from Feature Store):**
- Shift count since installation (AXS drivetrain logs every actuation)
- Terrain severity score (Karoo GPS elevation profile + gradient variance)
- Power stress index (Quarq watts × cadence × duration)
- Environmental exposure (temperature/moisture from Karoo sensors, ride geography)
- Component age in hours of riding
- Historical failure rates by SKU and batch

**Model outputs:**
- Estimated remaining component life (hours) with confidence interval
- Recommended service action (lube chain, replace cassette, rebuild shock)
- Probability of mid-ride failure within next 10 hours of riding

**Delivery mechanism:**
- AXS app push notification: *"Your Eagle XX cassette has ~60 hours of life remaining based on your riding patterns. Schedule service or order a replacement."*
- Dealer portal alert: *"3 of your registered customers have drivetrains within 20 hours of predicted service threshold — proactive outreach opportunity."*

**AWS implementation:** SageMaker Pipelines (weekly retraining on new telemetry) + SageMaker Feature Store + Lambda for real-time scoring → AXS app backend via API Gateway

### 9.2 Demand Forecasting

**The problem:** `Confirmed` — The cycling industry experienced extreme demand volatility 2020–2024. SRAM's multi-brand, multi-SKU portfolio (SRAM + RockShox + Zipp + Quarq + Hammerhead + TIME, hundreds of SKUs, across OEM/IBD/aftermarket channels) makes traditional ERP-based MRP forecasting structurally inadequate.

**Data inputs to forecast model:**
- SAP historical orders by SKU × channel × geography (3+ years)
- OEM build schedules via EDI (Trek, Specialized, Giant, Canyon model year commitments)
- Dealer POS data (where available via IBD integration)
- Hammerhead Karoo registration data (geographic cycling activity proxy)
- Macro cycling participation indices (USA Cycling, Strava Year in Sport)
- Product launch calendar (new Eagle Transmission tier releases historically spike cassette demand)
- Tariff and trade policy signals (Taiwan/China supply cost scenarios)

**Platform:** **o9 Solutions** or **Blue Yonder** ML demand planning (best-in-class for complex multi-SKU manufacturing) running on SageMaker-trained base models, outputs feeding SAP S/4HANA MRP directly via EventBridge

**Target:** 20–35% lower forecast error vs. current state; $10–25M working capital release from inventory reduction

### 9.3 Customer Service & Warranty Management

`Confirmed` — Trustpilot ~1.6/5, PissedConsumer 114 reviews, pattern of warranty blame-shifting [S48]. This is SRAM's most publicly visible weakness and the fastest AI win.

**Multi-layer transformation:**

| Layer | Solution | AWS/Salesforce Service |
|---|---|---|
| **Tier 0 — Self-service** | AI chatbot handles: AXS pairing issues, firmware update instructions, compatibility questions (e.g., "Is Force AXS compatible with my 2022 Specialized Tarmac?"), setup guides | Bedrock Knowledge Bases + Claude (RAG over all service docs) + Salesforce Experience Cloud |
| **Tier 1 — Intelligent triage** | AI classifies and routes: technical, warranty, shipping, retail; pre-populates Salesforce case with diagnosed issue | Salesforce Einstein + Bedrock classification |
| **Warranty AI** | Telemetry-backed objective assessment: pull serial number → AXS usage history → Claude reasoning over warranty policy → decision with explanation | Bedrock Agents + Lambda + SAP CS API |
| **Sentiment escalation** | Detect frustrated customers before they post reviews; route to senior agents with full context | Amazon Comprehend (sentiment) + Salesforce escalation rules |
| **RockShox service proactive** | Notify riders when suspension service interval approaches based on actuation count from RockShox AXS data | SageMaker + SNS + AXS app push |

### 9.4 OEM Relationship & Competitive Intelligence

**The stakes:** `Inference` — SRAM's OEM channel (Trek, Specialized, Giant, Canyon spec contracts) likely represents $300–500M of annual revenue. A single OEM model year spec switch (e.g., Trek 2027 Slash moving from Eagle Transmission to Shimano XTR) affects thousands of units across multiple years.

**AI solution stack:**
- **Crayon** (competitive intelligence platform) + **Brandwatch** (social listening) → monitors Shimano/Fox/Garmin product launches, OEM spec announcements, cycling media coverage in real time
- **Bedrock Agent (Claude)** → synthesizes signals into weekly competitive brief: *"Shimano announced GRX RX827 availability on 3 major gravel OEM builds this week. Trek Checkpoint AL 2027 spec sheet was updated. Recommend proactive Trek account team outreach."*
- **Salesforce Einstein** → scores OEM account health; flags accounts with declining order velocity or increased competitive spec inquiries
- **IBD personalization:** Bedrock-generated personalized email sequences to dealers based on their local riding community profile, purchase history, and service cycle timing derived from AXS component data in their geography

### 9.5 Eagle Powertrain AI (E-Bike)

`Confirmed` — SRAM Eagle Powertrain (Brose motor + SRAM drivetrain) is growing OEM adoption (Nukeproof, GASGAS, Transition, Propain). [SRAM company analysis] The AI opportunity is significant and defensible:

- **Terrain-adaptive motor assist:** Karoo GPS detects upcoming climb from route data → pre-stages motor assist 30 seconds before gradient change → smoother power delivery, better battery management
- **AI-auto-shift:** SageMaker model trained on rider power patterns + terrain → auto-shifts drivetrain in coordination with motor assist level, eliminating the cognitive load of simultaneous motor + gear management
- **Battery range prediction:** ML model learns individual rider's effort patterns + terrain preferences → predicts remaining range with high accuracy, far outperforming simple battery-percentage estimates
- **OTA model updates:** All AI models deployed over-the-air via Karoo 3 → continuous improvement without hardware recall

### 9.6 Generative Design for Zipp & RockShox R&D

`Inference` — Zipp's competitive advantage is engineering: a 5g wheel weight saving or 2W aerodynamic improvement justifies premium pricing. RockShox innovation (T-Type compatibility, zero-adjust precision) differentiates SRAM's MTB ecosystem.

**AI-accelerated R&D tools:**

| Tool | Application |
|---|---|
| **Autodesk Fusion Generative Design** | Topology optimization for Zipp rim profiles, Quarq spider arms, RockShox fork crowns — find minimum-material geometries meeting strength/stiffness targets |
| **NVIDIA Modulus** (physics-informed ML) | CFD surrogate models for Zipp wheel aerodynamics — run 100× more wind tunnel simulations in equivalent time |
| **Ansys Discovery** | AI-accelerated FEA for fatigue/impact testing on new suspension linkages |
| **PatSnap AI** | Monitor Shimano, Fox, DT Swiss, Enve patent filings — identify white-space IP opportunities and competitive R&D directions |

---

## 10. BI & Analytics

| Tool | Use Case | Integration |
|---|---|---|
| **Amazon QuickSight** | Executive dashboards (brand P&L, dealer performance, warranty KPIs, factory OEE); embedded in internal portals | Native S3/Redshift/Databricks integration |
| **Power BI** | Finance team reporting (if Microsoft 365 is office suite); connects to Databricks via ODBC | Cloud-agnostic |
| **Databricks SQL + Genie** | Data science and analyst self-service; natural language querying of Gold layer | Databricks native |
| **dbt-governed metrics** | All BI tools query from dbt-defined `fct_orders`, `dim_dealers`, `metric_warranty_rate_by_sku` — not raw tables | dbt Cloud on Databricks |

**Brand-specific dashboards (QuickSight):**
- **RockShox service dashboard:** Service interval compliance rate by geography; seal failure rate by product line and batch
- **Warranty operations dashboard:** Claim volume, AI auto-approval rate, average resolution time, Trustpilot sentiment trend
- **OEM spec dashboard:** SRAM vs. Shimano spec share by bike category and brand; YoY trend
- **AXS fleet dashboard:** Active components by firmware version; component health distribution across installed base; subscription conversion funnel

---

## 11. Governance, Security & Compliance

| Requirement | AWS Service | SRAM Context |
|---|---|---|
| **Identity & access management** | AWS IAM + IAM Identity Center | SSO across 9 brands; role-based access to brand data domains in Unity Catalog |
| **Data encryption** | AWS KMS (customer-managed keys) | Separate encryption keys per brand data domain; AXS rider data encrypted at rest and in transit |
| **Network isolation** | AWS VPC + PrivateLink | SAP and Salesforce traffic via private endpoints; factory IoT on isolated VPC |
| **Audit logging** | AWS CloudTrail + S3 | Immutable audit trail; required for CPSC recall documentation and GDPR data subject requests |
| **GDPR / EU rider data** | AWS eu-west-1 regional data residency | AXS rider telemetry for EU users stored in eu-west-1 (near Amstelveen European HQ); consent management via Salesforce |
| **PII detection** | Amazon Macie | Auto-scan S3 for rider PII; flag unmasked data in Bronze layer before promotion to Silver |
| **Secrets management** | AWS Secrets Manager | Auto-rotate SAP BTP, Salesforce, AXS API credentials; never hardcoded in application code |
| **Factory OT/IT segmentation** | AWS IoT + dedicated VPC | Factory sensor network isolated from corporate IT; data flows one-way via IoT Core → S3 |

---

## 12. Full Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────────────┐
│                          SOURCE SYSTEMS                                  │
│                                                                          │
│  SAP S/4HANA   │  Salesforce   │  AXS App     │  Hammerhead             │
│  (ERP / MRP)   │  (CRM/Cases)  │  Backend     │  Karoo OS               │
│                                                                          │
│  Quarq Power   │  RockShox AXS │  Factory IoT │  OEM EDI / E-Commerce   │
│  (Ride data)   │  Telemetry    │  (SiteWise)  │  Dealer Orders          │
└───────────────────────────────┬──────────────────────────────────────────┘
                                │
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
  AWS Glue +              Amazon MSK              AWS IoT Core
  Fivetran               (Kafka — AXS            + IoT SiteWise
  (batch ERP/CRM)         telemetry stream)      (factory sensors)
  AWS AppFlow             Amazon Kinesis          AWS IoT Greengrass
  (Salesforce)            (streaming)             (edge inference)
       │                        │                        │
       └────────────────────────▼────────────────────────┘
┌───────────────────────────────────────────────────────────────────────────┐
│            LAKEHOUSE  (Amazon S3 + Delta Lake / Apache Iceberg)           │
│                                                                           │
│  Bronze (raw) ──► Silver (conformed) ──► Gold (governed business metrics) │
│                                                                           │
│  Databricks Unity Catalog (cross-brand governance)                       │
│  AWS Lake Formation (fine-grained S3 access control)                     │
│  Amazon Macie (PII detection on Bronze)                                  │
│  dbt Cloud (semantic layer on Gold)                                      │
│  Amazon MWAA — Airflow (pipeline orchestration)                          │
└───────────────┬───────────────────────────────────────────────────────────┘
                │
    ┌───────────┼───────────────────────────────────┐
    │           │                                   │
┌───▼────┐  ┌──▼──────────────────┐  ┌─────────────▼────────────────────────┐
│  BI /  │  │  ANALYTICS          │  │       AI / ML LAYER                  │
│ Quick- │  │  Amazon Redshift    │  │                                      │
│ Sight  │  │  Serverless         │  │  SageMaker: Demand Forecasting       │
│ Power  │  │  Databricks SQL     │  │  SageMaker: AXS Component Health     │
│ BI     │  │  + Genie (NL query) │  │  SageMaker: Factory QC / Pred. Maint │
└────────┘  └─────────────────────┘  │                                      │
                                     │  Amazon Bedrock (Claude, Titan, Nova)│
                                     │  Bedrock Agents: Warranty AI         │
                                     │  Bedrock Agents: Competitive Intel   │
                                     │  Bedrock Knowledge Bases (RAG)       │
                                     │                                      │
                                     │  Salesforce AgentForce (CRM agents)  │
                                     │  IoT SiteWise + Greengrass (factory) │
                                     └──────────────────────────────────────┘
```

---

## 13. Phased Implementation Roadmap

### Phase 1 — Foundation & Quick Wins (Months 1–12, ~$9–16M)

**Priority:** Demonstrate AI ROI quickly; address SRAM's most urgent vulnerability (CS/warranty); build data infrastructure for Phase 2.

| Initiative | Investment | Expected Y1 Benefit |
|---|---|---|
| Engineering AI tools (GitHub Copilot + Claude Code) — all ~300 SRAM engineers | $370K | $8M labor equivalent |
| AI customer service pilot — AXS chatbot + warranty AI on Salesforce | $1M | $2M savings + brand recovery |
| Demand forecasting platform (o9 or Blue Yonder) — implementation | $4M | $7M + $15M WC release |
| SAP S/4HANA design & implementation start (Finance/Procurement first) | $3M | Foundation |
| AWS data platform foundation (S3 Bronze/Silver, Unity Catalog, Airflow) | $2M | Foundation for Phase 2 |
| AXS telemetry pipeline (Kinesis → Bronze → Silver) | $1M | Foundation for Phase 2 |
| Competitive intelligence AI (Crayon + Bedrock synthesis) | $400K | $3M OEM retention value |
| **Phase 1 Total** | **~$11.7M** | **~$20M + $15M WC** |

**Phase 1 — Day 1 deployments:**
- GitHub Copilot Enterprise → all engineers; Week 1; zero integration complexity
- Salesforce Service Cloud → warranty case management; begin CS data consolidation
- Amazon Bedrock access → all internal AI prototypes route through Bedrock from Day 1

### Phase 2 — Core Investment (Months 12–24, ~$15–25M)

**Priority:** Scale successful pilots; launch AXS Intelligence Platform; deploy manufacturing AI at Taichung.

| Initiative | Investment | Expected Y2 Benefit |
|---|---|---|
| Taichung QC vision AI (Cognex/Landing AI on new production lines) | $3M | $5M/yr defect/recall prevention |
| Predictive maintenance — Taichung mega-factory (SiteWise + SageMaker) | $3M | $5M/yr downtime reduction |
| SAP S/4HANA go-live (Manufacturing + SCM modules) | $5M | Operational foundation |
| AXS component health models (SageMaker) + app integration | $3M | $5M incremental parts revenue |
| AXS Premium subscription launch (beta cohort) | $2M | $4M ARR |
| Salesforce OEM pipeline management + Einstein scoring | $2M | $8M OEM retention |
| **Phase 2 Total** | **~$18M** | **~$27M/yr run rate** |

### Phase 3 — Moat Building (Months 24–36, ~$10–18M)

**Priority:** Compound competitive advantages; launch B2B data intelligence; Eagle Powertrain AI.

| Initiative | Investment | Expected Y3 Benefit |
|---|---|---|
| AXS Performance subscription + OEM/dealer data intelligence tier | $3M | $9M ARR |
| Eagle Powertrain AI (terrain-adaptive assist, AI auto-shift) | $4M | OEM differentiation + premium pricing |
| Generative design tools for Zipp + RockShox R&D | $3M | $4M/yr R&D acceleration |
| Full AI warranty lifecycle management across all brands | $2M | $3M/yr + brand recovery |
| IBD personalization engine (Bedrock + Salesforce) | $1M | $3M/yr dealer revenue |
| **Phase 3 Total** | **~$13M** | **~$19M incremental** |

---

## 14. Budget Summary

### Three-Year Investment vs. Return

| | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|
| **Investment** | $11.7M | $18M | $13M | **$42.7M** |
| **Cost Reduction Benefits** | $18M | $28M | $35M | **$81M** |
| **New Revenue (annualized)** | $4M | $13M | $30M | **$47M ARR by Y3** |
| **One-Time WC Release** | $15M | — | — | **$15M** |
| **Cumulative Net Benefit** | $25.3M | $41M | $65M | **$131M** |
| **Net of Investment** | $13.6M | $23M | $52M | **$88.3M** |

**3-Year Blended ROI: ~207%**
**Payback on total investment: ~18–22 months**

### Annual Steady-State Value (Year 3+)

| Category | Annual Value |
|---|---|
| Manufacturing QC cost reduction (defect/recall prevention) | $8–14M |
| Predictive maintenance savings | $5–9M |
| Demand forecasting / supply chain | $7–15M |
| Customer service + warranty efficiency | $3–9M |
| Engineering productivity (AI coding tools) | $8M (labor equivalent) |
| **Total Cost Reduction** | **$31–55M/yr** |
| AXS Premium + Performance subscriptions | $20–35M ARR |
| Incremental parts/accessories (proactive maintenance AI) | $8M |
| OEM/dealer data intelligence (B2B data tier) | $4M |
| R&D acceleration / pricing power | $5–14M |
| **Total Revenue Expansion** | **$37–61M/yr** |
| **Combined Annual Value (Steady State)** | **$68–116M/yr** |

---

## 15. Key Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| **GDPR compliance on AXS rider telemetry** (EU users) | Medium | High | EU data residency in eu-west-1 from Day 1; Salesforce consent management; Amazon Macie PII scanning |
| **AXS subscription rider adoption** | Medium | High | Free tier must remain genuinely valuable; subscription AI features must be demonstrably unique vs. Garmin Connect+/Wahoo |
| **SAP implementation complexity** (multi-brand legacy consolidation) | High | High | Phase by process area; Finance/procurement first; brand tech stacks connect via BTP APIs, not direct migration |
| **Taiwan geopolitical disruption** | Low-Medium | Very High | AI supply chain modeling actually helps — scenario planning and alternative supplier activation is faster with Gold-layer data |
| **Shimano data platform response** | Medium | High | Speed to market matters enormously; first-mover in cycling AI platform has durable advantage |
| **AXS data quality from older components** | Medium | Medium | Bronze-layer data cleaning pipeline; ML models trained only on components with sufficient telemetry history |
| **Factory IoT cybersecurity (OT/IT boundary)** | Medium | High | Strict VPC segmentation; IoT data flows one-way into S3; no inbound access to factory floor from cloud |
| **Brose motor partnership changes for Eagle Powertrain** | Low | High | Secure long-term partnership agreements; AI layer is SRAM-owned IP regardless of motor supplier |

---

## 16. Recommended Vendor Reference

### Manufacturing & Factory AI
| Vendor | Product | SRAM Use Case |
|---|---|---|
| Cognex | ViDi Deep Learning Vision | Assembly QC, threadlock detection, final inspection |
| Landing AI | LandingLens | Custom defect classification model training |
| AWS | IoT Core + IoT SiteWise | Factory telemetry ingestion, asset hierarchy, OEE |
| AWS | IoT Greengrass | Edge inference at Taichung assembly lines |
| IBM | Maximo Application Suite | Predictive maintenance CMMS integration |

### Data Platform
| Vendor | Product | SRAM Use Case |
|---|---|---|
| Databricks | Lakehouse Platform on AWS | Core analytics + ML platform + Unity Catalog |
| AWS | Amazon S3 + Lake Formation | Data lake storage + access governance |
| AWS | Amazon MWAA (Airflow) | Pipeline orchestration |
| dbt Labs | dbt Cloud | Semantic layer on Gold |
| Fivetran | Data connectors | Salesforce, Hammerhead SaaS → Bronze layer |

### ERP & CRM
| Vendor | Product | SRAM Use Case |
|---|---|---|
| SAP | S/4HANA Cloud (RISE on AWS) | Core manufacturing ERP |
| SAP | BTP Integration Suite | SAP ↔ AWS ↔ Salesforce middleware |
| Salesforce | Sales + Service Cloud | OEM pipeline, dealer CRM, warranty management |
| Salesforce | AgentForce | Dealer service AI agents |
| MuleSoft | Anypoint Platform | SAP ↔ Salesforce bidirectional sync |

### AI/ML & Integration
| Vendor | Product | SRAM Use Case |
|---|---|---|
| AWS | Amazon Bedrock (Claude, Titan, Nova) | Warranty AI, AXS coaching, CS chatbot, competitive intel |
| AWS | Amazon SageMaker | Component health models, demand forecasting, QC models |
| Anthropic | Claude API (via Bedrock) | Reasoning-heavy tasks: warranty adjudication, coaching insights |
| o9 Solutions | Demand Planning | Multi-brand demand forecasting + SAP integration |
| Crayon | Competitive Intelligence | Shimano/Fox/Garmin monitoring → Bedrock synthesis |
| GitHub | Copilot Enterprise | AI coding assistant for all ~300 SRAM engineers |

---

## 17. Priority Decision Points

Before implementation begins, SRAM leadership should align on five foundational decisions that drive the rest of the architecture:

1. **SAP vs. Microsoft Dynamics 365** — SAP is recommended given manufacturing complexity, but Dynamics 365 is viable if Microsoft stack integration is a priority. This decision locks in ERP, integration middleware, and implementation partner.

2. **Databricks vs. Snowflake** — Databricks recommended for ML-heavy workloads (AXS component health, factory AI). Snowflake is a valid alternative if SQL-native analytics is the primary use case and ML is secondary.

3. **Build vs. buy for AXS AI features** — AXS component health models should be built on SageMaker (proprietary competitive advantage). Demand forecasting and CS AI should use best-of-breed vendors (o9, Salesforce Einstein) to accelerate time-to-value.

4. **AXS subscription pricing and free tier boundary** — Must be decided before Phase 2 product development. The free tier must remain genuinely useful to protect the AXS installed base; the paid tier must offer AI value that Garmin/Wahoo cannot replicate.

5. **Data residency strategy for EU rider telemetry** — GDPR compliance requires a firm decision on which AXS data is stored in eu-west-1 vs. us-east-1, and what the consent and anonymization framework looks like before any AI modeling on rider data begins.

---

*Analysis compiled from SRAM competitive intelligence, company research, industry AI ROI benchmarks (IBM, Bridgera, Rock-and-River, GitHub/Microsoft, LinearB, 2024–2026), and AWS reference architecture guidance. All SRAM-specific financial figures are estimates based on publicly available data for a private company. Re-verify projections against internal SRAM financials before capital allocation decisions. Confidence labels follow the project convention: `Confirmed` = explicit source evidence; `Inference` = reasoned synthesis from confirmed facts; `Speculative` = plausible but unverified.*
