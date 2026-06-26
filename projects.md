---
layout: work
title: Projects
slug: /projects
items:
  - title: AIEdit
    link: https://github.com/BirolLab/AIEdit
    image:
      src: https://github.com/BirolLab/AIEdit/blob/main/logo.png?raw=true
      alt: AIEdit Logo
    description: Think of genome assembly polishing as a spell-check for DNA. I built AIEdit, a neural network-based tool that spots and fixes "spelling" errors in genome assemblies. Older tools usually force you to choose between speed, memory efficiency, or accuracy. They either take days to run, occupy all your system's RAM, or use heuristics that scale but sacrifice accuracy. To fix this, I trained a neural network to detect error patterns using spaced seeds (from ntHash2) and their counts (from ntStat, both below). It produces highly accurate results in a fraction of the time compared to other deep learning-based tools, and it uses up to 3x less memory.

  - title: ntStat
    link: https://github.com/BirolLab/ntStat
    image:
      src: https://placehold.co/600x600?text=ntStat
      alt: ntStat Logo
    description: Analyzing a genome often involves counting billions of short substrings of a fixed length (k-mers), which can easily max out a standard computer's memory. ntStat is a high-performance C++ tool we built to count k-mers efficiently using a cascade of Bloom filters. To characterize these k-mers directly from their counts, ntStat uses differential evolution to fit a mixture model to the count histogram. This approach keeps accuracy high (over 99.5%) and completely removes the need to store huge data structures on disk, making the whole process much faster and memory-efficient.

  - title: ntHash2
    link: https://github.com/BirolLab/ntHash
    image:
      src: https://raw.githubusercontent.com/BirolLab/ntHash/refs/heads/master/nthash-logo.png
      alt: ntHash Logo
    description: ntHash is a very popular hash function in the bioinformatics field that was released long before I joined the lab. For the second version, my main job was to design an algorithm for hashing "spaced seeds". You can think of these as text search queries with wildcards. Spaced seeds are great for analyzing noisy sequences (like long reads), but they are normally slow to index and query. I wrote a new approach that cuts down on hash collisions and runs almost 4x faster than standard methods, which helps speed up all the downstream software that relies on it.
---
