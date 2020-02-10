---
layout: compute
meet_date: 2020-02-19
topic: "GATK's Variant Quality Score Recalibration (VQSR) and exploring VCF files with scikit-allel to identify VCF filtering criteria"
leaders: "Group Discussion"
---

Please read the following documentation prior to the discussion:

1. [How to filter variants either with VQSR or by hard-filtering](https://software.broadinstitute.org/gatk/documentation/article?id=23216)
2. [Variant Quality Score Recalibration (VQSR)](https://gatkforums.broadinstitute.org/gatk/discussion/39/variant-quality-score-recalibration-vqsr/p1)
3. [The variant calling section of Samtools workflows documentation](http://www.htslib.org/workflow/#mapping_to_variant)

If you are unfamiliar with scikit-allel, please spend a few minutes familiarizing yourself with the tool. Documentation is available here: https://scikit-allel.readthedocs.io/en/stable/. Specifically, the following tutorials are relevant:
- Tutorial on filtering variants: http://alimanfoo.github.io/2018/04/09/selecting-variants.html
- Tutorial on exploratory analyses for VCF files: http://alimanfoo.github.io/2016/06/10/scikit-allel-tour.html

NOTE: During the discussion we will be looking at some Jupyter notebooks from the Morrell Lab that uses scikit-allel to explore VCF files to identify a set of VCF filtering criteria. We will also take a brief look at plots of `bcftools stats`.
