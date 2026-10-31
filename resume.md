---
layout: default
title: Resume
slug: /resume
---

<span class="print-button"><a href="javascript:window.print();"><i class="fa-solid fa-print"></i> Print</a></span>
<br>

<div class="cv-header">

<h1>PARHAM KAZEMI</h1>

<div class="contact-info">
  <a href="mailto:pkazemi3@gmail.com">pkazemi3@gmail.com</a>
  <span>+1 604-727-1834</span>
  <a href="https://github.com/parham-k">github.com/parham-k</a>
  <a href="https://www.linkedin.com/in/p-kazemi">linkedin.com/in/p-kazemi</a>
</div>

</div>

<div class="cv" markdown="1">

<div style="text-align: justify;"  markdown="1">

Machine Learning Software Engineer specializing in natural language processing, representation learning, and large-scale data pipelines. Proven track record of designing self-supervised models and multithreaded C++/PyTorch pipelines for terabyte-scale, long-context sequential data. Experienced in bridging research and engineering to deploy models into scalable, real-time ML systems.

</div>

# EXPERIENCE

## Machine Learning Software Engineer (PhD)
### BC Cancer Research Institute | September 2021 – Present

- Train 100M+ parameter **Transformers** on **TB-scale**, long-context (>10k tokens) **multimodal** data (**PyTorch**).
- Design and scale **self-supervised** representation learning models for **high-dimensional**, terabyte-scale data.
- Engineer **C++** inference engines (**libtorch**, **OpenMP**), cutting runtime from days to 2.7h and RAM usage by 3x.
- Quantize models and train on multiple GPUs to improve throughput by an order of magnitude (**CUDA**, **SLURM**).
- Architect and maintain the full software development lifecycle for open-source **C++** tools (10,000+ downloads).
- Ship production-ready **pybind11** and **libtorch** bindings with automated **CI/CD** release pipelines (**Docker**, **Azure**).
- Spearhead core ML R&D, yielding a provisional U.S. patent, 4 first-author papers, and grant funding.

## Machine Learning Researcher (Part-Time)
### University of Isfahan | September 2016 – September 2021

- Engineered an end-to-end ML pipeline for **user modeling**, predicting user traits from social media text data.
- Trained **deep reinforcement learning** agents in **NLP** environments utilizing **NLTK** and fuzzy logic.
- Instructed **ML**, **NLP**, **Python**, and **Django** courses for the ACM Student Chapter (~20 students per cohort).
- Built an automated grading platform (**Python**) using sockets, with **C++** and **Java** interfaces for project evaluation.

## Software Engineer (Contract)
### University of Isfahan | September 2018 – September 2019

- Built a **Django** + **PostgreSQL** social platform for **100,000+ users** with an automated credential verification engine.
- Administered the production **Linux (Ubuntu)**, **Nginx**, and **uWSGI** stack, ensuring high availability for daily traffic.

# SKILLS

**ML/AI:** Recommender Systems • User Modeling • Search & Ranking • Representation Learning • NLP • RL • LLMs<br>
**Languages/Frameworks:** Python • C++ • PyTorch • libtorch • Django • PostgreSQL<br>
**Systems/Inference:** CUDA • OpenMP • pybind11 • TorchScript • Model Quantization • Memory Optimization • SLURM<br>
**Developer Tools:** Cursor / GitHub Copilot • Docker • Git • CMake • CI/CD • Linux

# EDUCATION

## PhD in Bioinformatics
### University of British Columbia | September 2021 – November 2026

- Focus: Multimodal Machine Learning, Inference Optimization, and Sequence Modelling (PI: [Dr. Inanc Birol](https://www.birollab.ca/))

## M.Sc. in Computer Engineering
### University of Isfahan | September 2019 – June 2021

- Focus: Deep Learning, Language Modelling, Reinforcement Learning, and Natural Language Processing

## B.Sc. in Computer Engineering
### University of Isfahan | September 2015 – June 2019

- Competitions: RoboCup 2D Soccer Simulation, ACM-ICPC West Asia Regionals, Computer Engineering Olympiad

# PROJECTS

## Myrid: Self-Supervised Deep Learning for Large-Scale Signal Data Processing
### Provisional U.S. patent filed in 2026 | PoC presented at RECOMB 2026

- Built an end-to-end data processing pipeline and representation learning system for **TB-scale** temporal data.
- Trained a **self-supervised** model, using **quantization** for memory- and compute-efficient inference.

## Fuzzy Word Sense Induction and Disambiguation

### Paper: [10.1109/tfuzz.2021.3133905](https://doi.org/10.1109/tfuzz.2021.3133905)

- Designed a context-aware semantic classifier using fuzzy clustering on word embeddings (**BERT**, **word2vec**).
- Validated the architecture against standard natural language processing benchmarks (SemEval 2010 and 2013).

## AIEdit: Deep Learning for Alignment-Free CER Improvement

### GitHub: [BirolLab/AIEdit](https://github.com/BirolLab/AIEdit) | Paper: [10.1371/journal.pcbi.1014245](https://doi.org/10.1371/journal.pcbi.1014245)

- Engineered a production-grade inference engine, compiling **PyTorch** to **C++** via **TorchScript** and **pybind11**.
- Achieved a 58% error reduction, outperforming the next-best baseline while strictly optimizing latency.

## ntStat: Toolkit for Statistical Analysis of Sequence Data

### GitHub: [BirolLab/ntStat](https://github.com/BirolLab/ntStat) | Paper: [10.1371/journal.pcbi.1014158](https://doi.org/10.1371/journal.pcbi.1014158)

- Implemented n-gram counting via Bloom filters in **C++** (**pybind11**), with 99.5% accuracy at reduced memory usage.
- Applied differential evolution and BFGS optimization to accurately model token count histograms.

## ntHash2: High-Throughput Rolling Hash Algorithm for Pattern Matching

### GitHub: [BirolLab/ntHash](https://github.com/BirolLab/ntHash) | Paper: [10.1093/bioinformatics/btac564](https://doi.org/10.1093/bioinformatics/btac564)

- Implemented an optimized algorithm in **C++** and shipped high-performance **Python** bindings via **SWIG**.
- Accelerates hashing throughput by 3.8× over conventional algorithms for pattern matching (spaced seeds).

# SELECTED TALKS

- TEDx University of Isfahan: [Not So Artificial Intelligence](https://www.ted.com/talks/parham_kazemi_not_so_artificial_intelligence)
- Vancouver Bioinformatics User Group (VanBUG): [Modelling k-mer profiles with evolutionary algorithms](https://www.vanbug.org/archive/2025/2025-02-20/)

# VOLUNTEER EXPERIENCE

**Student Mentor & Conference Adjudicator** | UBC | 2024 – 2025
- Mentored 5 students through UBC's Undergraduate Research Opportunities program.
- Adjudicated undergraduate research posters at UBC's Multidisciplinary Undergraduate Research Conference.

**Volunteer Organizer** | Vancouver Bioinformatics User Group, VanBUG | 2023 – 2024
- Coordinated community engagement for seminars by local and international researchers.

</div>
