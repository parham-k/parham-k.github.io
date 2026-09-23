---
layout: default
title: CV
slug: /cv
---

<span class="print-button"><a href="javascript:window.print();"><i class="fa-solid fa-print"></i> Print</a></span>
<br>

<div class="cv-header">

<h1>PARHAM KAZEMI</h1>

<div class="contact-info">
  <span>Vancouver, BC</span>
  <a href="mailto:pkazemi3@gmail.com">pkazemi3@gmail.com</a>
  <span>+1 (604) 727-1834</span>
</div>

<div class="contact-info">
  <a href="https://parham-k.github.io">parham-k.github.io</a>
  <a href="https://github.com/parham-k">github.com/parham-k</a>
  <a href="https://linkedin.com/in/p-kazemi">linkedin.com/in/p-kazemi</a>
</div>

</div>

<div class="cv" markdown="1">

<div style="text-align: justify;"  markdown="1">

**Machine Learning Engineer and Software Developer** specializing in deep learning (**Python/PyTorch**) and high-performance computing (**C++**). Experienced in integrating large-scale computational models into highly optimized, production-grade software. Proven track record of training CNN/Transformer models on GPU clusters and designing efficient bioinformatics algorithms for 100GB+ to **terabyte-scale** datasets (**4 first-author papers, 1 patent**).

</div>

# CORE SKILLS

**Programming Languages:** C++, Python, Java, SQL, Bash

**ML & AI:** PyTorch/libtorch, HuggingFace, RL, Self-Supervised Learning, Quantization, ONNX

**Software Engineering:** Django, REST APIs, PostgreSQL, Docker, Nginx, Git, CI/CD, CMake, pybind11

**High-Performance Computing:** OpenMP, SIMD Vectorization, Memory Optimization, CUDA, SLURM, Valgrind

**Domain & Data Specialties:** NLP, Bioinformatics, Unstructured Data, Sequence Analysis, Signal Processing

# EXPERIENCE

## Graduate Research Assistant
### BC Cancer Research Institute (September 2021 - Present)

- Architect and manage the full software development lifecycle of **4 open-source** genomic libraries and pipelines.
- Develop high-performance C++ pipelines with multi-threading (**OpenMP**) and memory optimization to accelerate sequence analysis for **100GB+ datasets**.
- Ship Python bindings via **pybind11** and automated **CI/CD** with package release pipelines (Bioconda).
- Train **self-supervised** CNN and Transformer models on **terabyte-scale** signal datasets using **FlashAttention**, **CUDA**, and **SLURM**-managed GPU clusters.

## Backend Developer and System Administrator
### University of Isfahan (September 2018 - September 2021)

- Built an Alumni Social platform in **Django** with **PostgreSQL** serving **100,000+** alumni, including a credential verification engine with institutional syncing.
- Administered the production stack on **Linux (Ubuntu)** using **Nginx** and **uWSGI** on the university's networking platform that remains in active production today.
- Developed a ticketing system integrating **SMS APIs** and **payment gateways** for event registration.

## Course Instructor and Teaching Assistant
### University of Isfahan (September 2016 - June 2020)

- Instructed **Python** and **Django** courses for the ACM Student Chapter (~20 students per cohort).
- Assisted across 12 sections of 9 courses (~30 students each) including **AI**, **Algorithm Design**, **Data Structures**, and **Advanced Programming** in Java and C++.
- Built an automated grading platform from scratch using **Python**, **socket programming**, and **Tkinter**, with **C++** and **Java** interfaces for student AI project submissions.

# EDUCATION

## PhD in Bioinformatics
### University of British Columbia (September 2021 - Expected 2026)

- Thesis: Computational Representations for Nanopore Basecalling and Assembly Polishing
- Supervisor: [Dr. Inanc Birol](https://www.birollab.ca/)

## MSc in Computer Engineering
### University of Isfahan (September 2019 - June 2021)

- Thesis: Deep Reinforcement Learning for Training Intelligent Agents in Natural Language Environments
- GPA: 18.42/20 (highest in cohort)

## BSc in Computer Engineering
### University of Isfahan (September 2015 - June 2019)

- Thesis: Predicting Persian Twitter Users' MBTI Personality Using Text Mining Methods
- GPA: 18.25/20 (highest in cohort)
- Finalist, National Computer Engineering Olympiad (2019); ACM-ICPC West Asia Regional contestant (2016, 2017); RoboCup IranOpen 2D Soccer Simulation competitor (2017)

# PROJECTS AND PUBLICATIONS

## Myrid: Self-Supervised Deep Learning for Raw Signal Processing
### Provisional U.S. patent filed in 2026

- Architected a self-supervised sequence model trained directly on raw nanopore signals without labeled data, eliminating chemistry-dependent model retraining.
- Presented model benchmarks and architecture as a poster at *RECOMB 2026* (Thessaloniki, Greece).

## AIEdit: Alignment-Free ML-Based Genome Assembly Correction

### GitHub: [BirolLab/AIEdit](https://github.com/BirolLab/AIEdit) - PLOS CB: [10.1371/journal.pcbi.1014245](https://doi.org/10.1371/journal.pcbi.1014245)

- Engineered deep learning sequence models in PyTorch and compiled them directly into C++ using TorchScript and pybind11 for low-latency inference.
- Achieved **58% error reduction vs. 21%** for prior methods, dropping run times **from days to 2.7 hours** using **3× less memory** on human-scale data.

## ntStat: Toolkit for Statistical Analysis of K-mer Frequency and Depth

### GitHub: [BirolLab/ntStat](https://github.com/BirolLab/ntStat) - PLOS CB: [10.1371/journal.pcbi.1014158](https://doi.org/10.1371/journal.pcbi.1014158)

- Tracks k-mer/n-gram count and depth *de novo* using Bloom filter data structures, maintaining 99.5-99.9% accuracy at reduced memory usage.
- Components written in Python and C++, integrated together with pybind11.

## ntHash2: High-Throughput Rolling Hash Algorithm

### GitHub: [BirolLab/ntHash](https://github.com/BirolLab/ntHash) - Bioinformatics: [10.1093/bioinformatics/btac564](https://doi.org/10.1093/bioinformatics/btac564)

- Up to **2.1× faster** than ntHash 1 and **3.8× faster** than conventional algorithms at hashing spaced seeds.
- Written in C++, Python wrappers provided by SWIG.

## Fuzzy Word Sense Induction and Disambiguation

### IEEE Transactions on Fuzzy Systems: [10.1109/tfuzz.2021.3133905](https://doi.org/10.1109/tfuzz.2021.3133905)

- Uses fuzzy clustering on word embeddings to disambiguate meanings based on surrounding context.
- Achieves F-scores of 0.58 and 0.62 on SemEval 2010 and 2013, respectively.

# SELECTED TALKS

- TEDx University of Isfahan: [Not So Artificial Intelligence](https://www.ted.com/talks/parham_kazemi_not_so_artificial_intelligence)
- Vancouver Bioinformatics User Group (VanBUG): [Modelling k-mer profiles with evolutionary algorithms](https://www.vanbug.org/archive/2025/2025-02-20/)

# VOLUNTEER EXPERIENCE

**Student Mentor & Conference Adjudicator** — UBC (2024 - 2025)
- Mentored 5 students through UBC's Undergraduate Research Opportunities program.
- Adjudicated undergraduate research posters at UBC's Multidisciplinary Undergraduate Research Conference.

**Volunteer Organizer** — Vancouver Bioinformatics User Group, VanBUG (2023 - 2024)
- Coordinated community engagement for seminars by local and international bioinformatics researchers.

</div>
