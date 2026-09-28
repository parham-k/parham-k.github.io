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

**Machine Learning Engineer and Software Developer** specializing in deep learning (**Python/PyTorch**) and high-performance computing (**C++**). Experienced in translating computational research into highly optimized, production-grade software. Proven track record of training CNN/Transformer models on GPU clusters and designing efficient algorithms for 100GB+ to **terabyte-scale** datasets (**4 first-author papers, 1 provisional patent**).

</div>

# SKILLS

**Languages:** C++, Python, Java, SQL, Bash

**ML:** PyTorch, HuggingFace, Self-Supervision, Quantization, TorchScript, RL, NLP, Signal Processing, Linear Algebra

**Systems & HPC:** OpenMP, CUDA, SLURM, Memory Optimization, pybind11, CMake, Valgrind

**Engineering:** Django, PostgreSQL, REST APIs, Docker, Git, CI/CD

# EXPERIENCE

## Graduate Research Assistant
### BC Cancer Research Institute (September 2021 - Present)

- Design and manage the full software development lifecycle of 4 open-source tools and libraries.
- Develop memory-optimized, multithreaded (**OpenMP**) C++ data-processing tools for 100GB+ genomic datasets.
- Ship Python bindings via pybind11 and automated **CI/CD** with package release pipelines (**Bioconda**, **Docker**).
- Train 100M+ parameter CNN/Transformers on **TB-scale** data via multi-GPUs (**FlashAttention**, **CUDA**, **SLURM**).

## Backend Developer and System Administrator
### University of Isfahan (September 2018 – September 2021)

- Built a **Django**/**PostgreSQL** social platform for **100,000+** alumni with an automated credential verification engine.
- Administered the production **Linux (Ubuntu)**, **Nginx**, and **uWSGI** stack on the university's network.
- Developed a ticketing system integrating SMS APIs and payment gateways for event registration.

## Course Instructor and Teaching Assistant
### University of Isfahan (September 2016 – June 2020)

- Instructed Python and Django courses for the ACM Student Chapter (~20 students per cohort).
- Assisted 9 courses (~30 students each) covering ML, Algorithms, Data Structures, C++, Java, and Python.
- Built an automated grading platform (Python) using sockets, with C++ and Java interfaces for project evaluation.

# EDUCATION

## PhD in Bioinformatics
### University of British Columbia (September 2021 – November 2026)

- Thesis: Computational Representations for Nanopore Basecalling and Assembly Polishing (PI: [Dr. Inanc Birol](https://www.birollab.ca/))

## M.Sc. in Computer Engineering
### University of Isfahan (September 2019 – June 2021)

- Thesis: Deep Reinforcement Learning for Training Intelligent Agents in Natural Language Environments

## B.Sc. in Computer Engineering
### University of Isfahan (September 2015 – June 2019)

- Competitions: RoboCup 2D Soccer Simulation, ACM-ICPC West Asia Regionals, Computer Engineering Olympiad

# PROJECTS AND PUBLICATIONS

## Myrid: Self-Supervised Deep Learning for Biosensor Signal Translation
### Provisional U.S. patent filed in 2026

- Built an end-to-end pipeline on TB-scale nanopore signals, reducing dependence on hardware-specific retraining.
- Trained a self-supervised model, using quantization for memory- and compute-efficient inference.
- Demonstrated proof-of-concept results and presented the architecture at RECOMB 2026 (Thessaloniki, Greece).

## AIEdit: Deep Learning for Alignment-Free Genome Assembly Correction

### GitHub: [BirolLab/AIEdit](https://github.com/BirolLab/AIEdit) - First author paper in PLOS CB: [10.1371/journal.pcbi.1014245](https://doi.org/10.1371/journal.pcbi.1014245)

- Trained PyTorch models, compiled to C++ (**libtorch**) via **TorchScript** and **pybind11** for low-latency inference.
- 58% error reduction (vs. 21% next-best), cutting runs from days to 2.7h with 3× less RAM on 160GB data.

## ntStat: Toolkit for Statistical Analysis of k-mer Frequency

### GitHub: [BirolLab/ntStat](https://github.com/BirolLab/ntStat) - First author paper in PLOS CB: [10.1371/journal.pcbi.1014158](https://doi.org/10.1371/journal.pcbi.1014158)

- Tracks k-mer/n-gram count via Bloom filters in **C++** (**pybind11**), with 99.5% accuracy at reduced memory usage.
- Applies differential evolution and BFGS optimization to accurately model k-mer count histograms.

## ntHash2: High-Throughput Rolling Hash Algorithm for Nucleotide Sequences

### GitHub: [BirolLab/ntHash](https://github.com/BirolLab/ntHash) - First author paper in Bioinformatics: [10.1093/bioinformatics/btac564](https://doi.org/10.1093/bioinformatics/btac564)

- Accelerates hashing throughput by 3.8× over conventional algorithms for pattern matching (spaced seeds).
- Architected a C++ backend and shipped high-performance Python bindings via SWIG.

## Fuzzy Word Sense Induction and Disambiguation

### First author paper in IEEE Transactions on Fuzzy Systems: [10.1109/tfuzz.2021.3133905](https://doi.org/10.1109/tfuzz.2021.3133905)

- Designed a context-aware semantic classifier utilizing fuzzy clustering algorithms on dense word embeddings.
- Validated the architecture against standard natural language processing benchmarks (SemEval 2010 and 2013).

# SELECTED TALKS

- TEDx University of Isfahan: [Not So Artificial Intelligence](https://www.ted.com/talks/parham_kazemi_not_so_artificial_intelligence)
- Vancouver Bioinformatics User Group (VanBUG): [Modelling k-mer profiles with evolutionary algorithms](https://www.vanbug.org/archive/2025/2025-02-20/)

# VOLUNTEER EXPERIENCE & EXTRACURRICULAR ACTIVITIES

**Student Mentor & Conference Adjudicator** — UBC (2024 – 2025)
- Mentored 5 students through UBC's Undergraduate Research Opportunities program.
- Adjudicated undergraduate research posters at UBC's Multidisciplinary Undergraduate Research Conference.

**Volunteer Organizer** — Vancouver Bioinformatics User Group, VanBUG (2023 – 2024)
- Coordinated community engagement for seminars by local and international bioinformatics researchers.

**Interests:** RTS games (Age of Empires II), travel photography, competitive coding, and mechanical keyboards.

</div>
