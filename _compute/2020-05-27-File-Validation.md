---
layout: compute
meet_date: 2020-05-27
topic: "Validating files at each step in a sequence processing pipeline using sequence_handling as an example"
leaders: "Chaochih Liu"
---

This discussion will focus on commands/tools we can use to check and validate our output files at each step in a sequence processing pipeline and make sure they don't have any obvious problems. Given how broad in scope this topic is, we will use the Morrell lab's [`sequence_handling`](https://github.com/MorrellLAB/sequence_handling) pipeline to guide the discussion. This pipeline is intended to process sequence data from raw FASTQ files all the way up through GATK's SNP calling best practices workflow and returns a VCF file ready for downstream analysis.

Please read the following prior to the discussion:

- If you are not familiar with our pipeline, please skim through the main README page: [`sequence_handling`](https://github.com/MorrellLAB/sequence_handling).

Slides from this discussion are available on the DoesNaughtCompute Github page [here](https://github.com/MorrellLAB/DoesNaughtCompute/blob/master/Past_sessions/DNC_Validating_Files.pdf).
