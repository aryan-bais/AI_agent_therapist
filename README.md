# AI_agent_therapist

# Med Asking Agent

A **Medical Asking Agent** is an AI-powered conversational agent designed to **ask safe, structured, and medically relevant questions** to users in order to understand symptoms, collect health context, and guide next steps—**without providing diagnosis or treatment**.

This agent is optimized for **intake, triage support, and medical information gathering**, acting as the *first layer* in a healthcare workflow.

---

## 🩺 What Is a Med Asking Agent?

Unlike a medical chatbot that gives answers, a **Med Asking Agent primarily asks questions**.

Its goal is to:

* Collect accurate symptom and history data
* Reduce ambiguity before clinician interaction
* Guide users to appropriate care pathways
* Ensure safety through escalation and guardrails

> ⚠️ **Important:** This agent does **not** diagnose conditions or recommend treatments. It supports decision-making by gathering information.

---

## 🎯 Core Responsibilities

### 1. Symptom Inquiry

* Asks adaptive follow-up questions
* Covers onset, duration, severity, triggers, and progression
* Uses medically accepted frameworks (e.g., OPQRST, SOCRATES)

### 2. Medical History Collection

* Chronic conditions
* Medications and allergies
* Recent procedures or hospitalizations
* Relevant family history

### 3. Risk & Red-Flag Detection

* Identifies emergency warning signs
* Immediately escalates high-risk cases
* Encourages urgent care when appropriate

### 4. Structured Output

* Produces clinician-ready summaries
* Converts free text into structured data (JSON / FHIR-ready)

---

## 🧠 How the Agent Thinks

**Conversation Flow:**

1. Start with the user’s main concern
2. Ask high-yield clarifying questions
3. Narrow uncertainty safely
4. Detect red flags
5. Summarize findings
6. Escalate or hand off

```
User → Med Asking Agent → Structured Medical Summary → Clinician / System
```

---

## 🔐 Safety & Guardrails

* No diagnosis or treatment claims
* Mandatory medical disclaimers
* Emergency detection & escalation logic
* Refusal to answer unsafe or speculative requests
* Bias and hallucination mitigation

---

## 🛠️ Example Question Types

* "When did the symptom first start?"
* "Is the pain constant or intermittent?"
* "On a
