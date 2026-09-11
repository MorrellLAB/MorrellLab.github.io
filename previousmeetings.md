---
layout: hidden_page
hidden_title: Previous Meetings
permalink: /previous/
---

{% assign site_year = site.time | date: "%Y" %}
{% assign site_day = site.time | date: "%j" %}

<div class="home">
    <ul class="posts">
        {% for post in site.meetings reversed%}
            {% assign post_year = post.meet_date | date: "%Y" %}
            {% assign post_day = post.meet_date | date: "%j" %}
            {% if post_year < site_year %}
                <li>
                    <span class="post-date">{{ post.meet_date | date: "%b %-d, %Y" }} - Lead by {{ post.leader }}</span>
                    <a class="post-link" href="{{ post.paper_url }}">{{ post.paper_title }}</a> <br />
                    <span class="post-content">{{ post.paper_author }} ({{ post.paper_year }}). {{post.paper_journal }}.</span>
                </li>     
            {% endif %}
            {% if post_year == site_year %}
                {% if post_day < site_day %}
                    <li>
                        <span class="post-date">{{ post.meet_date | date: "%b %-d, %Y" }} - Lead by {{ post.leader }}</span>
                        <a class="post-link" href="{{ post.paper_url }}">{{ post.paper_title }}</a> <br />
                        <span class="post-content">{{ post.paper_author }} ({{ post.paper_year }}). {{post.paper_journal }}.</span>
                    </li>
                {% endif %}
            {% endif %}
        {% endfor %}
    </ul>
</div>
        
04/29/2014<br>
Kono TJY, Fu F, Mohammadi M et al. (in preparation) Bad mutations. <br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
04/24/2014<br>
Joint Meeting [Brandvain](http://yanivbrandvain.wordpress.com), [Goldberg](http://www.cbs.umn.edu/explore/departments/eeb/faculty-research/directory/emma-goldberg), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), [Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Mimura M, Ono K, Goka K, Hara T (2013) [Standing variation boosted by multiple sources of introduction contributes to the success of the introduced species, _Lotus corniculatus_](http://link.springer.com/article/10.1007%2Fs10530-013-0488-x#). Biol Invasions 15: 2743-2754.<br>
Discussion Leader: Derek Nedveck<br>
<br>
04/22/2014<br>
Baldwin-Brown JG, Long AD, Thornton KR (2014) [The power to detect quantitative trait loci using resequenced, experimentally evolved populations of diploid, sexual organisms.](http://mbe.oxfordjournals.org/content/31/4/1040.abstract) Mol Biol Evol <br>
Discussion Leader: Diana Trujillo<br>
<br>
04/15/2014<br>
Ralph P, Coop G (2013) [The geography of recent genetic ancestry across Europe.](http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001555) PLoS Biol 11: e1001555.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
04/08/2014<br>
Crisci JL, Poh YP, Bean A, Simkin A, Jensen JD (2012) [Recent progress in polymorphism-based population genetic inference.](http://jhered.oxfordjournals.org/content/103/2/287.abstract) J Hered 103: 287-296.<br>
Discussion Leader: Allison Haaning<br>
<br>
04/01/2014<br>
Xu S, Jia Z (2007) [Genomewide analysis of epistatic effects for quantitative traits in barley.](http://www.genetics.org/content/175/4/1955) Genetics 175: 1955-1963.<br>
Discussion Leader: Justin Anderson<br>
<br>
03/28/2014<br>
Joint Meeting [Brandvain](http://yanivbrandvain.wordpress.com), [Goldberg](http://www.cbs.umn.edu/explore/departments/eeb/faculty-research/directory/emma-goldberg), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), [Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Chantha SC, Herman AC, Platts AE, Vekemans X, Schoen DJ (2013) [Secondary evolution of a self-incompatibility locus in the Brassicaceae genus Leavenworthia.](http://www.plosbiology.org/article/info:doi/10.1371/journal.pbio.1001560) PLoS Biol 11: e1001560.<br>
Discussion Leader: [Emma Goldberg](http://www.cbs.umn.edu/explore/departments/eeb/faculty-research/directory/emma-goldberg)<br>
<br>
03/25/2014<br>
Reading the Classics<br>
Lander ES, Botstein D (1989) [Mapping mendelian factors underlying quantitative traits using RFLP linkage maps.](http://www.genetics.org/content/121/1/185.abstract) Genetics 121: 185-199.<br>
Discussion Leader: Derek Nedveck<br>
<br>
03/18/2014<br>
Li H, Durbin R (2011) [Inference of human population history from individual whole-genome sequences.](http://www.nature.com/nature/journal/v475/n7357/full/nature10231.html) Nature 475: 493-496.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
03/11/2014<br>
Freedman AH, Gronau I, Schweizer RM, Ortega-Del V, Diego, Han E et al. (2014) [Genome sequencing highlights the dynamic early history of dogs.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1004016;jsessionid=74FB84F5F2972AB43BDA3677EFA17580) PLoS Genet 10: e1004016.<br>
Discussion Leader: [Chaochih Liu](http://faculty.agronomy.cfans.umn.edu/pmorrell/people/people.htm) & [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
03/04/2014<br>
Hollister JD, Ross-Ibarra J, Gaut BS (2010) [Indel-associated mutation rate varies with mating system in flowering plants.](http://mbe.oxfordjournals.org/content/27/2/409.short) Mol Biol Evol 27: 409-416.<br>
Discussion Leader: Diana Trujillo<br>
<br>
02/28/2014<br>
Joint Meeting [Brandvain](http://yanivbrandvain.wordpress.com), [Goldberg](http://www.cbs.umn.edu/explore/departments/eeb/faculty-research/directory/emma-goldberg), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), [Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Rasmussen M, Anzick SL, Waters MR, Skoglund P, DeGiorgio M et al. (2014) [The genome of a Late Pleistocene human from a Clovis burial site in western Montana.](http://www.nature.com/nature/journal/v506/n7487/full/nature13025.html) Nature 506: 225-229.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
02/25/2014<br>
Hartfield M, Glemin S (2014) [Hitchhiking of deleterious alleles and the cost of adaptation in partially selfing species.](http://www.genetics.org/content/196/1/281.abstract) Genetics 196: 281-293.<br>
Discussion Leader: Ron Okagaki<br>
<br>
02/18/2014<br>
Arbiza L, Gronau I, Aksoy BA, Hubisz MJ, Gulko B et al. (2013) [Genome-wide inference of natural selection on human transcription factor binding sites.](http://www.nature.com/ng/journal/v45/n7/abs/ng.2658.html) Nat Genet 45: 723-729.<br>
Discussion Leader: Allison Haaning<br>
<br>
02/11/2014<br>
Nielsen R, Korneliussen T, Albrechtsen A, Li Y, Wang J (2012) [SNP calling, genotype calling, and sample allele frequency estimation from New-Generation Sequencing data.](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0037558#pone-0037558-g004) PLoS One 7: e37558.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
02/04/2014 - 2:30 pm - Note Special Time<br>
Reading the Classics<br>
Lewontin RC, Krakauer J (1973) [Distribution of gene frequency as a test of the theory of the selective neutrality of polymorphisms](http://www.genetics.org/content/74/1/175.abstract). Genetics 74: 175-195.<br>
Discussion Leader: Derek Nedveck<br>
<br>
01/28/2014<br>
Han E, Sinsheimer JS, Novembre J (2013) [Characterizing bias in population genetic inferences from low coverage sequencing data.](http://mbe.oxfordjournals.org/content/early/2013/11/27/molbev.mst229.abstract) Mol Biol Eval <br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
01/24/2014<br>
Joint Meeting [Brandvain](http://yanivbrandvain.wordpress.com), [Goldberg](http://www.cbs.umn.edu/explore/departments/eeb/faculty-research/directory/emma-goldberg), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), [Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Skoglund P, Malmstrom H, Raghavan M, Stora J, Hall P et al. (2012) [Origins and genetic legacy of Neolithic farmers and hunter-gatherers in Europe.](http://www.sciencemag.org/content/336/6080/466) Science 336: 466-469.<br>
Discussion Leader: [Yaniv Brandvain](http://yanivbrandvain.wordpress.com)<br>
<br>
01/21/2014<br>
Slatkin M (2009) [Epigenetic inheritance and the missing heritability problem.](http://www.genetics.org/content/182/3/845.abstract) Genetics 182: 845-850.<br>
Discussion Leader: [Justin Anderson](http://stuparlab.cfans.umn.edu/personnel/)<br>
<br>
01/14/2014<br>
[International Plant and Animal Genome Meeting](http://www.intlpag.org/)<br>
<br>
01/07/2014<br>
Fay JC, Wyckoff GJ, Wu CI (2001) [Positive and negative selection on the human genome.](http://www.genetics.org/content/158/3/1227.abstract) Genetics 158: 1227-1234.<br>
Discussion Leader: Kiran Seth<br>
<br>
12/31/2013<br>
Christmas Holiday<br>
<br>
12/24/2013<br>
Christmas Holiday<br>
<br>
12/17/2013<br>
Gonzales AM, Fang Z, Clegg MT, Morrell PL (in prep) Barley landraces - SNP Analysis.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
12/12/2013 - Note Special Date<br>
Guo M, Rupe MA, Wei J, Winkler C, Goncalves-Butruille M et al. (2013) [Maize ARGOS1 (ZAR1) transgenic alleles increase hybrid maize yield.](http://jxb.oxfordjournals.org/content/early/2013/11/10/jxb.ert370.abstract) J Exp Bot <br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
12/13/2013 - 10:30 am - Note Special Date & Time<br>
Joint Meeting [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), [Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Moreno-Estrada A, Gravel S, Zakharia F, McCauley JL, Byrnes JK et al. (2013) [Reconstructing the population genetic history of the Caribbean.](http://www.plosgenetics.org/article/info:doi/10.1371/journal.pgen.1003925;jsessionid=245CD99EA4F3B1CCD093F5A459783F92) PLoS Genet 9: e1003925.<br>
Discussion Leader: [Dave Moeller](http://www.cbs.umn.edu/lab/moeller)<br>
<br>
12/03/2013<br>
Nicholson G, Smith AV, Jónsson F, Gústafsson Ó, Stefánsson K et al. (2002) [Assessing population differentiation and isolation from single-nucleotide polymorphism data.](http://onlinelibrary.wiley.com/doi/10.1111/1467-9868.00357/abstract) J R Stat Soc Ser B Stat Methodol 64: 695-715.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
11/26/2013<br>
Epperson B.K., 1999. [Gustave Malecot, 1911-1998. Population genetics founding father.](http://www.genetics.org/content/152/2/477.long) Genetics 152: 477-484.<br>
Discussion Leader: Ron Okagaki<br>
<br>
11/19/2013<br>
Berg J.J., Coop G., 2013. [The population genetic signature of polygenic local adaptation.](http://arxiv.org/abs/1307.7759) J arXiv preprint arXiv:1307.7759<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
11/15/2013 - 2:30 pm - Note Special Date & Time<br>
Joint Meeting with [Blekham](http://blekhmanlab.org), [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Brandvain Y., Slotte T., Hazzouri K.M., Wright S.I., Coop G., 2013. [Genomic identification of founding haplotypes reveals the history of the selfing species _Capsella rubella_.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1003754) PLoS Genet 9: e1003754.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
11/12/2013<br>
Reading the Classics<br>
Hill WG, Robertson A (1966) [The effect of linkage on limits to artificial selection.](http://journals.cambridge.org/action/displayAbstract;jsessionid=E2B69B0826FF500514879DC498BD7D40.journals?fromPage=online&aid=1747272) Genet Res 8: 269-294.<br>
Discussion Leader: Ron Okagaki<br>
<br>
11/05/2013<br>
van Heerwaarden J, Hufford MB, Ross-Ibarra J (2012) [Historical genomics of North American maize.](http://www.pnas.org/content/early/2012/07/12/1209275109.abstract) Proc Natl Acad Sci U S A <br>
Discussion Leader: Xin Li<br>
<br>
10/29/2013<br>
Rosenberg NA, Li LM, Ward R, Pritchard JK (2003) [Informativeness of genetic markers for inference of ancestry.](http://www.cell.com/AJHG/retrieve/pii/S0002929707639901) Am J Hum Genet 73: 1402-1422.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
10/22/2013<br>
Loh PR, Lipson M, Patterson N, Moorjani P, Pickrell JK et al. (2013) [Inferring admixture histories of human populations using linkage disequilibrium.](http://www.genetics.org/content/193/4/1233.abstract) Genetics 193: 1233-1254.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
10/15/2013<br>
Rosenberg NA, Mahajan S, Ramachandran S, Zhao C, Pritchard JK et al. (2005) [Clines, clusters, and the effect of study design on the inference of human population structure.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.0010070) PLoS Genetics 1: e70.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
10/08/2013<br>
Fang Z, Gonzales AM, Clegg MT, Muehlbauer GJ, et al. (in preparation) Two genomic regions contribute disproportionately to population structure in wild barley.<br>
Discussion Leader: Allison Haaning<br>
<br>
10/04/2013 - 2:30 pm - Note Special Date & Time<br>
Joint Meeting with [Blekham](http://blekhmanlab.org), [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Long Q, Rabanal FA, Meng D, Huber CD, Farlow A et al. (2013) [Massive genomic variation and strong selection in _Arabidopsis thaliana_ lines from Sweden.](http://www.nature.com/ng/journal/v45/n8/full/ng.2678.html) Nat Genet 45: 884-890.<br>
Discussion Leader: [Peter Tiffin](http://www.cbs.umn.edu/lab/tiffin)<br>
<br>
09/24/2013<br>
King EG, Macdonald SJ, Long AD (2012) [Properties and power of the _Drosophila_ synthetic population resource for the routine dissection of complex traits.](http://www.genetics.org/content/191/3/935.abstract) Genetics 191: 935-949.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
09/17/2013<br>
Richman AD, Uyenoyama MK, Kohn JR (1996) [Allelic diversity and gene genealogy at the self-incompatibility locus in the Solanaceae.](http://www.sciencemag.org/content/273/5279/1212.abstract?sid=ac5565b3-a1b4-44f7-9956-125128af70e4) Science 273: 1212-1216.<br>
Discussion Leader: [Kelly Tweito](http://faculty.agronomy.cfans.umn.edu/pmorrell/people/people.htm)<br>
<br>
09/10/2013<br>
Flowers JM, Molina J, Rubinstein S, Huang P, Schaal BA, Purugganan MD (2012) [Natural selection in gene-dense regions shapes the genomic pattern of polymorphism in wild and domesticated rice.](http://mbe.oxfordjournals.org/content/early/2011/09/13/molbev.msr225) Mol Biol Evol 29: 675-687.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
08/29/2013<br>
King EG, Merkes CM, McNeil CL, Hoofer SR, Sen S et al. (2012) [Genetic dissection of a model complex trait using the Drosophila Synthetic Population Resource.](http://genome.cshlp.org/content/22/8/1558.abstract) Genome Res <br>
Discussion Leader: Vikram Vikus<br>
<br>
08/22/2013<br>
Beleza S, Johnson NA, Candille SI, Absher DM, Coram MA et al. (2013) [Genetic architecture of skin and eye color in an African-European admixed population.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1003372?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+plosgenetics%2FNewArticles+%28Ambra+-+Genetics+New+Articles%29) PLoS Genet 9: e1003372.<br>
Discussion Leader: Allison Haaning<br>
<br>
08/14/2013 - 10:00 am - Note Special Date & Time<br>
Hudson RR, Bailey K, Skarecky D, Kwiatowski J, Ayala FJ (1994) [Evidence for positive selection in the superoxide dismutase (_Sod_) region of _Drosophila melanogaster_.](http://www.genetics.org/content/136/4/1329) Genetics 136: 1329-1340.<br>
Discussion Leader: [Justin Anderson](http://stuparlab.cfans.umn.edu/personnel/)<br>
<br>
08/08/2013<br>
Morrell, P.L., Rieseberg, L.H. 1998. [Molecular tests of the proposed diploid hybrid origin of _Gilia achilleifolia_ (Polemoniaceae)](http://www.amjbot.org/content/85/10/1439.abstract). Am J Bot 85:1439–1453.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
08/01/2013<br>
Cutter AD, Payseur BA (2013) [Genomic signatures of selection at linked sites: unifying the disparity among species.](http://www.nature.com/nrg/journal/v14/n4/full/nrg3425.html) Nat Rev Genet 14: 262-274.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
07/26/2013 - Note Special Date<br>
McVean G (2009) [A genealogical interpretation of principal components analysis.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1000686) PLoS Genet 5: e1000686.<br>
Discussion Leader: Vikram Vikus<br>
<br>
07/18/2013<br>
Deleterious Mutations Jigsaw<br>
Lopes AM, Aston KI, Thompson E, Carvalho F, Goncalves J et al. (2013) [Human spermatogenic failure purges deleterious mutation load from the autosomes and both sex chromosomes, including the gene DMRT1.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1003349) PLoS Genet 9: e1003349.<br>
Discussion Leaders: Allison Haaning, [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
Peischl S, Dupanloup I, Kirkpatrick M, Excoffier L (2013) [On the accumulation of deleterious mutations during range expansions.](http://arxiv.org/abs/1306.1652) J arXiv preprint arXiv:13061652 <br>
Discussion Leaders: [Kelly Tweito](http://faculty.agronomy.cfans.umn.edu/pmorrell/people/people.htm), [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
Simons YB, Turchin MC, Pritchard JK, Sella G (2013) [The deleterious mutation load is insensitive to recent population history.](http://arxiv.org/abs/1305.2061) J arXiv preprint arXiv:13052061 <br>
Discussion Leaders: [Margie Stringfield](http://faculty.agronomy.cfans.umn.edu/pmorrell/people/people.htm), [Justin Anderson](http://stuparlab.cfans.umn.edu/personnel/)<br>
<br>
Szpiech ZA, Xu J, Pemberton TJ, Peng W, Zollner S et al. (2013) [Long runs of homozygosity are enriched for deleterious variation.](http://www.cell.com/AJHG/abstract/S0002-9297(13)00216-4) Am J Hum Genet <br>
Discussion Leaders: Mikey Kantar, Diana Trujillo<br>
<br>
07/11/2013<br>
[Society for Molecular Biology & Evolution (SMBE) Meeting 2013](http://smbe2013.org/2013/Home.aspx) - Chicago<br>
<br>
07/04/2013<br>
Independence Day<br>
<br>
06/27/2013<br>
Sousa V, Hey J (2013) [Understanding the origin of species with genome-scale data: modelling gene flow.](http://www.nature.com/nrg/journal/v14/n6/abs/nrg3446.html) Nat Rev Genet 14: 404-414.<br>
Discussion Leader: Diana Trujillo<br>
<br>
06/20/2013<br>
Petersen JL, Mickelson JR, Rendahl AK, Valberg SJ, Andersson LS et al. (2013) [Genome-wide analysis reveals selection for important traits in domestic horse breeds.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1003211) PLoS Genet 9: e1003211.<br>
Discussion Leaders: [Justin Anderson](http://stuparlab.cfans.umn.edu/personnel/)<br>
<br>
06/13/2013<br>
Reading the Classics<br>
Smith JM, Haigh J (1974) [The hitchhiking effect of a favorable gene.](http://journals.cambridge.org/action/displayAbstract;jsessionid=A111A3DD5F299AE05714CB9810A47782.journals?fromPage=online&aid=1754360) Genet Res 23: 23-35.<br>
Discussion Leader: Mikey Kantar<br>
<br>
06/06/2013<br>
Charlesworth B 2012. [The effects of deleterious mutations on evolution at linked sites.](http://www.genetics.org/content/190/1/5.abstract) Genetics 190: 5–22.<br>
Charlesworth B 2013. [Background selection 20 years on: The Wilhelmine E. Key 2012 Invitational Lecture.](http://jhered.oxfordjournals.org/content/104/2/161.abstract) J Hered 104: 161–171.<br>
Discussion Leaders: Fengli Fu & Mohsen Mohammadi<br>
<br>
05/30/2013<br>
Lin Z, Li X, Shannon LM, Yeh CT, Wang ML et al. (2012) [Parallel domestication of the _Shattering1_ genes in cereals.](http://www.nature.com/ng/journal/v44/n6/abs/ng.2281.html) Nat Genet 44: 720-724.<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
05/23/2013<br>
Guerrero RF, Rousset F, Kirkpatrick M (2012) [Coalescent patterns for chromosomal inversions in divergent populations.](http://rstb.royalsocietypublishing.org/content/367/1587/430.abstract) Philos Trans R Soc Lond B Biol Sci 367: 430-438.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
05/17/2013<br>
Fuller DQ, Willcox G, Allaby RG (2012) [Early agricultural pathways: moving outside the ‘core area’ hypothesis in Southwest Asia.](http://jxb.oxfordjournals.org/content/early/2011/11/02/jxb.err307.abstract) J Exp Bot 63: 617-633.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
05/10/2013<br>
Takebayashi N, Morrell PL (2001) [Is self-fertilization an evolutionary dead end? Revisiting an old hypothesis with genetic theories and a macroevolutionary approach.](http://www.amjbot.org/content/88/7/1143.abstract) Am J Bot 88: 1143-1150.<br>
Igic B, Busch JW (2013) [Is self-fertilization an evolutionary dead end?](http://onlinelibrary.wiley.com/doi/10.1111/nph.12182/abstract) New Phytol 198: 386-397.<br>
Discussion Leaders: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/) & [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
05/03/2013<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Ober U, Ayroles JF, Stone EA, Richards S, Zhu D, Gibbs RA, Stricker C, Gianola D, Schlather M, Mackay TF, Simianer H (2012) [Using whole-genome sequence data to predict quantitative trait phenotypes in _Drosophila melanogaster_.](http://www.plosgenetics.org/article/info:doi/10.1371/journal.pgen.1002685) PLoS Genet 8: e1002685.<br>
Discussion Leader: Vikram Vikus<br>
<br>
04/26/2013<br>
Fuller DQ, Willcox G, Allaby RG (2011) [Cultivation and domestication had multiple origins: arguments against the core area hypothesis for the origins of agriculture in the Near East.](http://www.tandfonline.com/doi/abs/10.1080/00438243.2011.624747) World Archaeology 43: 628-652.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
04/19/2013<br>
Reading the Classics<br>
Felsenstein J (1974) [The evolutionary advantage of recombination.](http://www.genetics.org/content/78/2/737.abstract) Genetics 78: 737-756.<br>
Discussion Leader: Mikey Kantar<br>
<br>
04/12/2013<br>
Parker GA, Smith JM (1990) [Optimality theory in evolutionary biology.](http://www.nature.com/nature/journal/v348/n6296/abs/348027a0.html) Nature 348: 27-33.<br>
Shoval O, Sheftel H, Shinar G, Hart Y, Ramote O et al. (2012) [Evolutionary trade-offs, Pareto optimality, and the geometry of phenotype space.](https://www.sciencemag.org/content/336/6085/1157) Science 336: 1157-1160.<br>
Discussion Leader: Ron Okagaki<br>
<br>
04/05/2013<br>
Fu W, O’Connor TD, Jun G, Kang HM, Abecasis G, Leal SM, Gabriel S, Altshuler D, Shendure J, Nickerson DA, Bamshad MJ, Akey JM (2013) [Analysis of 6,515 exomes reveals the recent origin of most human protein-coding variants.](http://www.nature.com/nature/journal/v493/n7431/full/nature11690.html) Nature 493: 216-220.v
Karakoc E, Alkan C, O’Roak BJ, Dennis MY, Vives L et al. (2012) [Detection of structural variants and indels within exome data.](http://www.nature.com/nmeth/journal/v9/n2/full/nmeth.1810.html) Nat Methods 9: 176-178.<br>
Discussion Leader: Ahmad Sallam<br>
<br>
03/29/2013<br>
Gan X, Stegle O, Behr J, Steffen JG, Drewe P et al. (2011) [Multiple reference genomes and transcriptomes for _Arabidopsis thaliana_.](http://www.nature.com/nature/journal/v477/n7365/full/nature10414.html) Nature 477: 419-423.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/%7Ekonox006/)<br>
<br>
03/22/2013<br>
Spring Break<br>
<br>
03/15/2013<br>
Yang S, Yuan Y, Wang L, Li J, Wang W et al. (2012) [Great majority of recombination events in _Arabidopsis_ are gene conversion events.](http://www.pnas.org/content/early/2012/11/30/1211827110.abstract.html) Proc Natl Acad Sci USA<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
03/08/2013<br>
Reading the Classics<br>
Watterson GA (1975) [On the number of segregating sites in genetical models without recombination.](http://www.sciencedirect.com/science/article/pii/0040580975900209) Theor Popul Biol 7: 256-276.<br>
Discussion Leader: Mikey Kantar<br>
<br>
03/01/2013<br>
Morrell PL, Gonzales AM, Meyer KKT, Clegg MT (in prep) Resequencing data indicate a modest effect of domestication on diversity in barley: a cultigen with multiple origins. <br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/%7Ezhou/)<br>
<br>
02/22/2013<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Rockman MV (2012) [The QTN program and the alleles that matter for evolution: all that’s gold does not glitter.](http://onlinelibrary.wiley.com/doi/10.1111/j.1558-5646.2011.01486.x/abstract) Evolution 66: 1-17.<br>
Discussion Leader: Peter Tiffin<br>
<br>
02/15/2013<br>
Lu J, Tang T, Tang H, Huang J, Shi S, Wu CI (2006) [The accumulation of deleterious mutations in rice genomes: a hypothesis on the cost of domestication.](http://www.cell.com/trends/genetics/abstract/S0168-9525(06)00022-9) Trends Genet 22: 126-131.<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
02/08/2013<br>
Reading the Classics<br>
Gould SJ, Lewontin RC (1979) [The spandrels of San Marco and the Panglossian paradigm: a critique of the adaptationist programme.](http://rspb.royalsocietypublishing.org/content/205/1161/581.abstract) Proceedings of the Royal Society B: Biological Sciences 205: 581-598.<br>
Discussion Leader: Mikey Kantar<br>
<br>
02/01/2013<br>
Comeron JM, Ratnappan R, Bailin S (2012) [The many landscapes of recombination in _Drosophila_ _melanogaster_.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1002905) PLoS Genet 8: e1002905.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
01/24/2013<br>
Turchin MC, Chiang CW, Palmer CD, Sankararaman S, Reich D et al. (2012) [Evidence of widespread selection on standing variation in Europe at height-associated SNPs.](http://www.nature.com/ng/journal/v44/n9/abs/ng.2368.html) Nat Genet 44: 1015-1019.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
01/17/2013<br>
Pickrell JK, Pritchard JK (2012) [Inference of population splits and mixtures from genome-wide allele frequency data.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1002967) PLoS Genet 8: e1002967.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
01/10/2013<br>
[International Plant and Animal Genome Meeting](http://www.intlpag.org/)<br>
<br>
01/03/2013<br>
Christmas Holiday<br>
<br>
12/27/2013<br>
Christmas Holiday<br>
<br>
12/20/2012<br>
Swanson-Wagner R, Briskine R, Schaefer R, Hufford MB, Ross-Ibarra J, Myers CL, Tiffin P, Springer NM (2012) [Reshaping of the maize transcriptome by domestication.](http://www.pnas.org/content/109/29/11878.abstract) Proc Natl Acad Sci U S A 109: 11878-11883.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/%7Ezhou/)<br>
<br>
12/13/2012<br>
Leffler EM, Bullaughey K, Matute DR, Meyer WK, Segurel L et al. (2012) [Revisiting an old riddle: what determines genetic diversity levels within species?](http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001388) PLoS Biol 10: e1001388.<br>
Sella G, Petrov DA, Przeworski M, Andolfatto P (2009) [Pervasive natural selection in the _Drosophila_ genome?](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1000495) Plos Genet 5: ARTN e1000495.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/) & [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/) <br>
<br>
12/06/2012<br>
van Heerwaarden J, Hufford MB, Ross-Ibarra J (2012) [Historical genomics of North American maize.](http://www.pnas.org/content/early/2012/07/12/1209275109.abstract) Proc Natl Acad Sci USA<br>
Discussion Leader: Emily Combs<br>
<br>
11/28/2012<br>
Kono TY, Seth K, Stupar RM, Morrell PL (in prep) SNP annotation and SNP metadata collection without a reference genome.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
11/22/2012<br>
Thanksgiving Holiday<br>
<br>
11/16/2012<br>
Hahn MW (2008) [Toward a selection theory of molecular evolution](http://onlinelibrary.wiley.com/doi/10.1111/j.1558-5646.2007.00308.x/abstract). Evolution 62: 255-265.<br>
Discussion Leader: Ron Okagaki<br>
<br>
11/08/2012 <br>
Reading the Classics<br>
Tajima F (1983) [Evolutionary relationship of DNA sequences in finite populations.](http://www.genetics.org/content/105/2/437.abstract) Genetics 105: 437-460.<br>
Discussion Leader: Mikey Kantar<br>
<br>
11/01/2012<br>
Ralph P, Coop G (2012) [The geography of recent genetic ancestry across Europe.](http://arxiv.org/abs/1207.3815) J Arxiv preprint arXiv:12073815<br>
Discussion Leader: Ron Okagaki<br>
<br>
10/25/2012<br>
Mayer KF, Waugh R, Langridge P, Close TJ, Wise RP et al. (2012) [A physical, genetic and functional sequence assembly of the barley genome.](http://www.nature.com/nature/journal/vaop/ncurrent/full/nature11543.html) Nature<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
10/19/2012<br>
Joint Meeting with the [Smith](http://agronomy.cfans.umn.edu/People/FacultyDirectory/SmithKevinP/index.htm) Lab<br>
Fang Z, Eule-Nashoba A, Powers C, Kono TY, Morrell PL et al. (in prep) Multiple genomic regions indicate a response to selection for Fusarium head blight resistance in a barley experimental breeding population. <br>
Discussion Leader: Vikram Vikus<br>
<br>
10/11/2012<br>
Fang Z, Gonzales AM, Durbin ML, Meyer KKT, Miller BH, Volz KM, Clegg MT, Morrell PL (in prep) Tracing the geographic origin of weedy _Ipomoea purpurea_ in the Southeastern United States.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
10/04/2012<br>
Lee CR, Mitchell-Olds T (2011) [Quantifying effects of environmental and geographical factors on patterns of genetic differentiation.](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-294X.2011.05310.x/abstract) Mol Ecol 20: 4631-4642.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
09/27/2012<br>
Gonzales AM, Fang Z, Durbin ML, Meyer KKT, Clegg MT et al. (in press) [Nucleotide sequence diversity of floral pigment genes in Mexican populations of _Ipomoea purpurea_ (morning glory) accord with a neutral model of evolution.](http://f1000.com/posters/browse/summary/1092010) J of Heredity<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
09/21/2012<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Labs<br>
Wang C, Zollner S, Rosenberg NA (2012) [A quantitative comparison of the similarity between genes and geography in worldwide human populations.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1002886) PLoS Genet 8: e1002886.<br>
Discussion Leader: Jeremy Yoder<br>
<br>
09/13/2012<br>
Whittington HR, Deede L, Powers JS (2012) [Growth responses, biomass partitioning, and nitrogen isotopes of prairie legumes in response to elevated temperature and varying nitrogen source in a growth chamber experiment.](http://www.amjbot.org/content/99/5/838) Am J Bot 99: 838-846.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
09/06/2012<br>
Morrell PL, Buckler ES, Ross-Ibarra J (2012) [Crop genomics: advances and applications.](http://www.nature.com/nrg/journal/vaop/ncurrent/abs/nrg3097.html) Nat Rev Genet 13: 85-96.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
08/30/2012<br>
[Microbial and Plant Genomics Institute](http://www.mpgi.umn.edu/index.htm)<br>
[3rd Annual Fall Symposium](http://www.mpgi.umn.edu/NewsandEvents/Events/FallSymposium/index.htm)<br>
<br>
08/23/2012<br>
Eichten SR, Swanson-Wagner RA, Schnable JC, Waters AJ, Hermanson PJ, Liu S, Yeh CT, Jia Y, Gendler K, Freeling M, Schnable PS, Vaughn MW, Springer NM (2011) [Heritable epigenetic variation among maize inbreds.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1002372) PLoS Genet 7: e1002372.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
08/16/2012<br>
Warmuth V, Eriksson A, Bower MA, Canon J, Cothran G et al. (2011) [European domestic horses originated in two holocene refugia.](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0018194)PLoS One 6: e18194.<br>
Warmuth V, Eriksson A, Bower MA, Barker G, Barrett E et al. (2012) [Reconstructing the origin and spread of horse domestication in the Eurasian steppe.](http://www.pnas.org/content/early/2012/05/02/1111122109.short) Proc Natl Acad Sci U S A 109: 8202-8206.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
08/09/2012<br>
Zhong SQ, Dekkers JCM, Fernando RL, Jannink JL (2009) [Factors affecting accuracy from genomic selection in populations derived from multiple inbred lines: A barley case study.](http://www.genetics.org/content/182/1/355.abstract) Genetics 182: 355-364.<br>
Discussion Leader: Vikram Vikus<br>
<br>
08/02/2012<br>
Hoban S, Bertorelle G, Gaggiotti OE (2011) [Computer simulations: tools for population and evolutionary genetics.](http://www.nature.com/nrg/journal/v13/n2/abs/nrg3130.html) Nat Rev Genet 13: 110-122.<br>
Discussion Leader: Emily Combs<br>
<br>
07/26/2012<br>
Reading the Classics<br>
Kreitman M (1983) [Nucleotide polymorphism at the alcohol dehydrogenase locus of _Drosophila melanogaster_.](http://www.nature.com/nature/journal/v304/n5925/pdf/304412a0.pdf) Nature 304: 412-417.<br>
Discussion Leader: Mikey Kantar<br>
<br>
07/19/2012<br>
Mackay TF, Richards S, Stone EA, Barbadilla A, Ayroles JF et al. (2012) [The _Drosophila melanogaster_ Genetic Reference Panel.](http://www.nature.com/nature/journal/v482/n7384/full/nature10811.html) Nature 482: 173-178.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
07/12/2012<br>
Novembre J, Ramachandran S (2011) [Perspectives on human population structure at the cusp of the sequencing era.](http://www.annualreviews.org/doi/abs/10.1146/annurev-genom-090810-183123) Annu Rev Genomics Hum Genet 12: 245-274.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
07/05/2012<br>
Wegmann D, Kessner DE, Veeramah KR, Mathias RA, Nicolae DL et al. (2011) [Recombination rates in admixed individuals identified by ancestry-based inference.](http://www.nature.com/ng/journal/v43/n9/abs/ng.894.html) Nat Genet 43: 847-853.<br>
Discussion Leader: Ron Okagaki<br>
<br>
06/28/2012<br>
Horton MW, Hancock AM, Huang YS, Toomajian C, Atwell S et al. (2012) [Genome-wide patterns of genetic variation in worldwide _Arabidopsis thaliana_ accessions from the RegMap panel.](http://www.nature.com/ng/journal/vaop/ncurrent/full/ng.1042.html) Nat Genet 44: 212-216.<br>
Gaut BS (2012) _[Arabidopsis thaliana_ as a model for the genetics of local adaptation.](http://www.nature.com/ng/journal/v44/n2/full/ng.1079.html) Nat Genet 44: 115-116.<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
06/21/2012<br>
Engelhardt BE, Stephens M (2010) [Analysis of population structure: a unifying framework and novel methods based on sparse factor analysis.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1001117) PLoS Genet 6:<br>
Yang WY, Novembre J, Eskin E, Halperin E (2012) [A model-based approach for analysis of spatial structure in genetic data.](http://www.nature.com/ng/journal/v44/n6/full/ng.2285.html) Nat Genet 44: 725-731.<br>
Discussion Leader: Vikram Vikus & [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/) <br>
<br>
06/14/2012<br>
Moeller DA, Geber MA, Tiffin P (2011) [Population genetics and the evolution of geographic range limits in an annual plant.](http://www.jstor.org/stable/info/10.1086/661783) Am Nat 178 Suppl 1: S44-57.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
06/07/2012<br>
Hufford MB, Xun X, van Heerwaarden J, Pyhäjärvi T, Chia J-M, Cartwright RA, Elshire RJ, Glaubitz JC, Guill KE, Kaeppler SM, Lai J, Morrell PL, Shannon LM, Song C, Springer NM, Swanson-Wagner RA, Tiffin P, Wang J, Zhang G, Doebley J, McMullen MD, Ware D, Buckler ES, Yang S, Ross-Ibarra J (in press) [Population genomics of domestication and improvement in maize.](http://www.nature.com/ng/journal/vaop/ncurrent/abs/ng.2309.html) Nature Genetics<br>
Discussion Leader: Mikey Kantar<br>
<br>
05/31/2012<br>
Otto SP, Whitlock MC (1997) [The probability of fixation in populations of changing size.](http://www.genetics.org/content/146/2/723.abstract) Genetics 146: 723-733.<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
05/24/2012<br>
Tang H, Choudhry S, Mei R, Morgan M, Rodriguez-Cintron W et al. (2007) [Recent genetic selection in the ancestral admixture of Puerto Ricans.](http://www.sciencedirect.com/science/article/pii/S0002929707613597) Am J Hum Genet 81: 626-633.<br>
Discussion Leader:  [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/) <br>
<br>
05/17/2012<br>
Ng PC, Henikoff S (2003) [SIFT: Predicting amino acid changes that affect protein function.](http://nar.oxfordjournals.org/content/31/13/3812.abstract) Nucleic Acids Res 31: 3812-3814.<br>
Ng PC, Nickerson DA, Bamshad MJ, Shendure J (2010) [Massively parallel sequencing and rare disease.](http://hmg.oxfordjournals.org/content/early/2010/09/21/hmg.ddq390) Hum Mol Genet 19: R119-24.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
05/10/2012<br>
Lawson DJ, Hellenthal G, Myers S, Falush D (2012) [Inference of population structure using dense haplotype data.](http://www.plosgenetics.org/article/info:doi/10.1371/journal.pgen.1002453) PLoS Genet 8: e1002453.<br>
Gattepaille LM, Jakobsson M (2012) [Combining markers into haplotypes can improve population structure inference.](http://www.genetics.org/content/early/2011/08/24/genetics.111.131136.short?rss=1) Genetics 190: 159-174.<br>
Discussion Leaders:  [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/) & [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
05/03/2012<br>
Haun WJ, Hyten DL, Xu WW, Gerhardt DJ, Albert TJ et al. (2011) [The composition and origins of genomic variation among individuals of the soybean reference cultivar Williams 82.](http://www.plantphysiol.org/content/155/2/645.abstract) Plant Physiol 155: 645-655.<br>
Discussion Leader: Mikey Kantar<br>
<br>
04/26/2012<br>
Fournier-Level A, Korte A, Cooper MD, Nordborg M, Schmitt J et al. (2011) [A map of local adaptation in _Arabidopsis thaliana_.](http://www.sciencemag.org/content/334/6052/86.abstract) Science 334: 86-89.<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
04/19/2012<br>
Marth GT, Yu F, Indap AR, Garimella K, Gravel S et al. (2011) [The functional spectrum of low-frequency coding variation](http://genomebiology.com/2011/12/9/R84/abstract). Genome Biol 12: R84.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
04/12/2012<br>
Pyhäjärvi T, Kujala ST, Savolainen O (2011) [Revisiting protein heterozygosity in plants—nucleotide diversity in allozyme coding genes of conifer _Pinus sylvestris_.](http://www.springerlink.com/content/m19412061520u247/) Tree Genetics & Genomes 7: 385-397.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
04/05/2012<br>
Dumont BL, Payseur BA (2011) [Genetic analysis of genome-scale recombination rate evolution in house mice.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1002116) PLoS Genet 7: e1002116.<br>
Discussion Leader: Mikey Kantar<br>
<br>
03/29/2012<br>
Tenaillon O, Rodriguez-Verdugo A, Gaut RL, McDonald P, Bennett AF et al. (2012) [The molecular diversity of adaptive convergence.](http://www.sciencemag.org/content/335/6067/457.abstract?sid=7ecf696d-9c04-4884-91e5-670bc43ee1f3) Science 335: 457-461.<br>
Discussion Leader: Ron Okagaki<br>
<br>
03/22/2012<br>
Blackman BK, Rasmussen DA, Strasburg JL, Raduski AR, Burke JM et al. (2011) [Contributions of flowering time genes to sunflower domestication and improvement.](http://www.genetics.org/content/187/1/271.abstract) Genetics 187: 271-287.<br>
Discussion Leader: Mikey Kantar<br>
<br>
03/15/2012<br>
Spring Break<br>
<br>
03/08/2012 (location - 138 Cargill)<br>
Joint Meeting with the [Smith](http://agronomy.cfans.umn.edu/People/FacultyDirectory/SmithKevinP/index.htm) Lab<br>
Illumina Genotyping - [GenomeStudio](http://www.illumina.com/gsp/genomestudio_software.ilmn) and [Alchemy](http://alchemy.sourceforge.net/)<br>
Wright MH, Tung CW, Zhao K, Reynolds A, McCouch SR et al. (2010) [ALCHEMY: a reliable method for automated SNP genotype calling for small batch sizes and highly homozygous populations.](http://bioinformatics.oxfordjournals.org/content/26/23/2952.abstract) Bioinformatics 26: 2952-2960.<br>
Discussion Leaders: Karen Beaubien, [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/), and Maria Munoz<br>
__If you need an Minnesota Supercomputing Institute ([MSI](https://www.msi.umn.edu/)) account to participate, register here:__
[https://www.msi.umn.edu/tutorial/802](https://www.msi.umn.edu/tutorial/802)<br>
<br>
03/01/2012<br>
Zhao K, Tung CW, Eizenga GC, Wright MH, Ali ML et al. (2011) [Genome-wide association mapping reveals a rich genetic architecture of complex traits in _Oryza sativa_.](http://www.nature.com/ncomms/journal/v2/n9/full/ncomms1467.html) Nat Commun 2: 467.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
02/23/2012<br>
Macdonald SJ, Long AD (2007) [Joint estimates of quantitative trait locus effect and frequency using synthetic recombinant populations of _Drosophila melanogaster_.](http://www.genetics.org/cgi/content/abstract/176/2/1261) Genetics 176: 1261-1281.<br>
Discussion Leader: Vikram Vikus<br>
<br>
02/16/2012<br>
Albrechtsen A, Nielsen FC, Nielsen R (2010) [Ascertainment biases in SNP chips affect measures of population divergence.](http://mbe.oxfordjournals.org/content/27/11/2534.abstract) Mol Biol Evol 27: 2534-2547.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
02/09/2012<br>
Reading the Classics<br>
Lewontin RC, Hubby JL (1966) [A molecular approach to the study of genic heterozygosity in natural populations. II. Amount of variation and degree of heterozygosity in natural populations of _Drosophila pseudoobscura_.](http://www.genetics.org/content/54/2/595.full.pdf+html) Genetics 54: 595-609.<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
02/02/2012<br>
Saintenac C, Jiang D, Akhunov ED (2011) [Targeted analysis of nucleotide and copy number variation by exon capture in allotetraploid wheat genome.](http://genomebiology.com/2011/12/9/R88) Genome Biol 12: R88.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
01/26/2012<br>
Reading the Classics<br>
Lewontin RC, Krakauer J (1973) [Distribution of gene frequency as a test of the theory of the selective neutrality of polymorphisms](http://www.genetics.org/content/74/1/175.abstract). Genetics 74: 175-195.<br>
Discussion Leader: Mikey Kantar<br>
<br>
01/19/2012<br>
[International Plant and Animal Genome Meeting](http://www.intlpag.org/web/)<br>
<br>
01/13/2012<br>
[International Plant and Animal Genome Meeting](http://www.intlpag.org/web/)<br>
<br>
01/06/2012<br>
Christmas Holiday<br>
<br>
12/29/2011<br>
Christmas Holiday<br>
<br>
12/22/2011<br>
Nair, S.K., Wang, N., Turuspekov, Y., Pourkheirandish, M., Sinsuwongwat, S., Chen, G., Sameri, M., Tagiri, A., Honda, I., Watanabe, Y., Kanamori, H., Wicker, T., Stein, N., Nagamura, Y., Matsumoto, T., Komatsuda, T. 2010. [Cleistogamous flowering in barley arises from the suppression of microRNA-guided HvAP2 mRNA cleavage.](Cleistogamous%20flowering%20in%20barley%20arises%20from%20the%20suppression%20of%20microRNA-guided%20HvAP2%20mRNA%20cleavage.) Proc Natl Acad Sci U S A 107:490–495.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
12/15/2011<br>
Wakeley J (2005) [The limits of theoretical population genetics.](http://www.genetics.org/content/169/1/1.full) Genetics 169: 1-7.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
12/08/2011 (location - 138 Cargill)<br>
Joint Meeting with the [Smith](http://agronomy.cfans.umn.edu/People/FacultyDirectory/SmithKevinP/index.htm) Lab<br>
UNIX Shell Scripting and Job Queueing on Linux Clusters<br>
[http://manuals.bioinformatics.ucr.edu/home/linux-basics](http://manuals.bioinformatics.ucr.edu/home/linux-basics)<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/) and Erin Treiber<br>
__If you need an Minnesota Supercomputing Institute ([MSI](https://www.msi.umn.edu/)) account to participate, register here:__
[https://www.msi.umn.edu/tutorial/786](https://www.msi.umn.edu/tutorial/786)<br>
<br>
11/30/2011<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Labs<br>
Studer A, Zhao Q, Ross-Ibarra J, Doebley J (2011) [Identification of a functional transposon insertion in the maize domestication gene _tb1_.](http://www.nature.com/ng/journal/v43/n11/abs/ng.942.html) Nat Genet 43: 1160-1163.<br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
11/24/2010<br>
Thanksgiving Holiday<br>
<br>
11/17/2011<br>
Fay JC (2011) [Weighing the evidence for adaptation at the molecular level.](http://www.cell.com/trends/genetics/abstract/S0168-9525(11)00094-1) Trends Genet <br>
Discussion Leader: Raffa Teixera<br>
<br>
11/10/2011<br>
Macdonald SJ, Long AD (2007) [Joint estimates of quantitative trait locus effect and frequency using synthetic recombinant populations of _Drosophila melanogaster_.](http://www.genetics.org/content/176/2/1261.abstract) Genetics 176: 1261-1281.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
11/03/2011<br>
Ju YS, Kim JI, Kim S, Hong D, Park H et al. (2011) [Extensive genomic and transcriptional diversity identified through massively parallel DNA and RNA sequencing of eighteen Korean individuals.](http://www.nature.com/ng/journal/v43/n8/full/ng.872.html) Nat Genet 43: 745-752.<br>
Discussion Leader: Mikey Kantar<br>
<br>
10/26/2011 (note date, time, and location 371 Bioscience - 12:30 pm)<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Cao, J., Schneeberger, K., Ossowski, S., Gunther, T., Bender, S., Fitz, J., Koenig, D., Lanz, C., Stegle, O., Lippert, C., Wang, X., Ott, F., Muller, J., Alonso-Blanco, C., Borgwardt, K., Schmid, K.J., Weigel, D. 2011. [Whole-genome sequencing of multiple _Arabidopsis thaliana_ populations.](http://www.nature.com/ng/journal/v43/n10/full/ng.911.html) Nat Genet <br>
Discussion Leader: [John Stanton-Geddes](http://www.tc.umn.edu/~stant067/)<br>
<br>
10/20/2011<br>
[Emasculation and pollination of barley](http://www.youtube.com/watch?v=8E8RuHb9cRE)<br>
Discussion Leader: [Kevin Smith](http://agronomy.cfans.umn.edu/People/FacultyDirectory/SmithKevinP/index.htm)<br>
<br>
10/13/2011<br>
McHale LK, Huan WJ, Xu WW, Bhaskar PB, Hyten DL et al. (in review) Structural variation hotspots in the soybean genome localize to clusters of biotic stress response genes. __- see email for weblink__ <br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
10/06/2011<br>
Kover PX, Valdar W, Trakalo J, Scarcelli N, Ehrenreich IM et al. (2009) [A multiparent advanced generation inter-cross to fine-map quantitative traits in _Arabidopsis thaliana_.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1000551) Plos Genet 5: ARTN e1000551.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
09/28/2011 (note date)<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Vonholdt BM, Pollinger JP, Earl DA, Knowles JC, Boyko AR et al. (2011) [A genome-wide perspective on the evolutionary history of enigmatic wolf-like canids.](http://genome.cshlp.org/content/21/8/1294.abstract) Genome Res 21: 1294-1305.<br>
Discussion Leader: Tim Paape<br>
<br>
09/22/2011<br>
McHale LK, Huan WJ, Xu WW, Bhaskar PB, Hyten DL et al. (in review) Stuctural variation hotspots in the soybean genome localize to clusters of biotic stress response genes. __- see email for weblink__ <br>
Discussion Leader: [Tom Kono](http://www.tc.umn.edu/~konox006/)<br>
<br>
09/15/2011<br>
Coop G, Pickrell JK, Novembre J, Kudaravalli S, Li J et al. (2009) [The role of geography in human adaptation.](http://www.plosgenetics.org/article/info:doi/10.1371/journal.pgen.1000500) PLoS Genet 5: e1000500.<br>
Discussion Leader: Mikey Kantar<br>
<br>
09/08/2011<br>
Ossowski S, Schneeberger K, Lucas-Lledo JI, Warthmann N, Clark RM et al. (2010) [The rate and molecular spectrum of spontaneous mutations in _Arabidopsis thaliana_.](http://www.sciencemag.org/content/327/5961/92.abstract) Science 327: 92-94.<br>
Discussion Leader: Emily Combs<br>
<br>
09/01/2011<br>
Microbial and Plant Genomics Institute<br>
[2nd Annual Fall Symposium](http://www.mpgi.umn.edu/)<br>
<br>
08/25/2011<br>
Coop G, Witonsky D, Di Rienzo A, Pritchard JK (2010) [Using environmental correlations to identify loci underlying local adaptation.](http://www.genetics.org/content/185/4/1411.abstract) Genetics 185: 1411-1423.<br>
Discussion Leader: Hongyun Wang<br>
<br>
08/18/2011<br>
Sakai AK, Lane MJ (1996) [National Science Foundation funding patterns of women and minorities in biology.](http://www.jstor.org/stable/1312991) BioScience 46: 621-625.<br>
Discussion Leader: Kiran Seth<br>
<br>
08/11/2011<br>
Moyle LC, Nakazato T (2010) [Hybrid incompatibility “snowballs” between _Solanum_ species.](http://www.sciencemag.org/content/329/5998/1521.abstract) Science 329: 1521-1523.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
08/04/2011<br>
Rothberg JM, Hinz W, Rearick TM, Schultz J, Mileski W et al. (2011) [An integrated semiconductor device enabling non-optical genome sequencing.](http://www.nature.com/nature/journal/v475/n7356/full/nature10242.html) Nature 475: 348-352.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
07/28/2011<br>
Altshuler DL, Durbin RM, Abecasis GR, Bentley DR, Chakravarti A et al. (2010) [A map of human genome variation from population-scale sequencing.](http://www.nature.com/nature/journal/v467/n7319/abs/nature09534.html) Nature 467: 1061-1073.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
07/21/2011<br>
Li H, Ruan J, Durbin R (2008) [Mapping short DNA sequencing reads and calling variants using mapping quality scores.](http://genome.cshlp.org/content/18/11/1851.abstract) Genome Res 18: 1851-1858.<br>
Discussion Leader: Robert Schaefer<br>
<br>
07/14/2011<br>
Haasl RJ, Payseur BA (2011) [Multi-locus inference of population structure: a comparison between single nucleotide polymorphisms and microsatellites.](http://www.nature.com/hdy/journal/v106/n1/abs/hdy201021a.html) Heredity 106: 158-171.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
07/07/2011<br>
Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S et al. (2009) [Genome sequence, comparative analysis, and population genetics of the domestic horse.](http://www.sciencemag.org/content/326/5954/865) Science 326: 865-867.<br>
Discussion Leader: Ron Okagaki<br>
<br>
06/30/2011<br>
Yang Z, Rannala B (2010) [Bayesian species delimitation using multilocus sequence data.](http://www.pnas.org/content/107/20/9264.abstract) Proc Natl Acad Sci U S A 107: 9264-9269.<br>
Discussion Leader: Beau Miller<br>
<br>
06/23/2011<br>
Molina J, Sikora M, Garud N, Flowers JM, Rubinstein S et al. (2011) [Molecular evidence for a single evolutionary origin of domesticated rice.](http://www.pnas.org/content/early/2011/04/27/1104686108.abstract) Proc Natl Acad Sci U S A 108: 8351-8356.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
06/16/2011<br>
[Evolution Meeting 2011](http://www.evolution2011.ou.edu/)<br>
<br>
06/09/2011<br>
Mackay TF, Stone EA, Ayroles JF (2009) [The genetics of quantitative traits: challenges and prospects.](http://www.nature.com/nrg/journal/v10/n8/abs/nrg2612.html) Nat Rev Genet 10: 565-577.<br>
Discussion Leader: Kiran Seth<br>
<br>
06/02/2011<br>
Nielsen R, Paul JS, Albrechtsen A, Song YS (2011) [Genotype and SNP calling from next-generation sequencing data.](http://www.nature.com/nrg/journal/v12/n6/abs/nrg2986.html) Nat Rev Genet 12: 443-451.<br>
Discussion Leader: Jessica Petersen<br>
<br>
05/26/2011<br>
Morrell PL, Toleno DM, Lundy KE, Clegg MT (2006) [Estimating the contribution of mutation, recombination and gene conversion in the generation of haplotypic diversity.](http://www.genetics.org/content/173/3/1705.short) Genetics 173: 1705-1723.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
05/19/2011<br>
Guo F, Dey DK, Holsinger KE (2009) [A Bayesian hierarchical model for analysis of SNP diversity in multilocus, multipopulation samples.](http://pubs.amstat.org/doi/abs/10.1198/jasa.2009.0010) J Am Stat Assoc 104: 142-154.<br>
Discussion Leader: Amber Eule-Nashoba<br>
<br>
05/12/2011<br>
Reading the Classics<br>
Cavalli-Sforza LL (1966) [Population structure and human evolution.](http://rspb.royalsocietypublishing.org/content/164/995/362.full.pdf+html) Proc R Soc Lond B Biol Sci 164: 362-379.<br>
Discussion Leader: Ron Okagaki<br>
<br>
05/05/2011<br>
Huynh LY, Maney DL, Thomas JW (2010) [Chromosome-wide linkage disequilibrium caused by an inversion polymorphism in the white-throated sparrow (_Zonotrichia albicollis_)](http://www.nature.com/hdy/journal/v106/n4/full/hdy201085a.html?WT.ec_id=HDY-201104). Heredity 106: 537-546.<br>
Discussion Leader: Zhou Fang<br>
<br>
04/28/2011<br>
Macdonald SJ, Long AD (2007) [Joint estimates of quantitative trait locus effect and frequency using synthetic recombinant populations of _Drosophila melanogaster_](http://www.genetics.org/cgi/content/abstract/176/2/1261). Genetics 176: 1261-1281.<br>
Discussion Leader: Nichol Schultz<br>
<br>
04/21/2011<br>
Ralph P, Coop G (2010) [Parallel adaptation: one or many waves of advance of an advantageous allele?](http://www.genetics.org/cgi/content/abstract/186/2/647) Genetics 186: 647-668.<br>
Discussion Leader: Jessica Petersen<br>
<br>
04/14/2011<br>
Burke MK, Dunham JP, Shahrestani P, Thornton KR, Rose MR et al. (2010) [Genome-wide analysis of a long-term evolution experiment with _Drosophila_.](http://www.nature.com/nature/journal/v467/n7315/full/nature09352.html) Nature 467: 587-590.<br>
Discussion Leader: Margaret Taylor<br>
<br>
04/07/2011<br>
Joint Meeting with McCue, Moeller, & Tiffin Lab Groups<br>
Tenaillon MI, Hufford MB, Gaut BS, Ross-Ibarra J (2011) [Genome size and transposable element content as determined by high-throughput sequencing in maize and _Zea luxurians_.](http://gbe.oxfordjournals.org/content/early/2011/02/04/gbe.evr008.abstract) Genome Biol Evol<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
03/31/2011<br>
Cuesta-Marcos A, Szucs P, Close TJ, Filichkin T, Muehlbauer GJ, Smith KP, Hayes PM (2010) [Genome-wide SNPs and re-sequencing of growth habit and inflorescence genes in barley: implications for association mapping in germplasm arrays varying in size and structure.](http://www.biomedcentral.com/1471-2164/11/707) BMC Genomics 11: ARTN 707<br>
Discussion Leader: Emily Combs<br>
<br>
03/24/2011<br>
Barley diversity manuscript - see email for weblink<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
03/17/2011<br>
Spring Break<br>
<br>
03/10/2011<br>
Li Y, Vinckenbosch N, Tian G, Huerta-Sanchez E, Jiang T et al. (2010) [Resequencing of 200 human exomes identifies an excess of low-frequency non-synonymous coding variants.](http://www.nature.com/ng/journal/v42/n11/full/ng.680.html) Nat Genet 42: 969-972.<br>
Discussion Leader: Krista Fritz<br>
<br>
03/03/2011<br>
Lohmueller KE, Indap AR, Schmidt S, Boyko AR, Hernandez RD et al. (2008) [Proportionally more deleterious genetic variation in European than in African populations.](http://www.nature.com/nature/journal/v451/n7181/full/nature06611.html) Nature 451: 994-997.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
02/24/2011<br>
Chun S, Fay JC (2009) [Identification of deleterious mutations within three human genomes.](http://genome.cshlp.org/content/19/9/1553) Genome Res 19: 1553-1561.<br>
Discussion Leader: [Beau Miller](http://www.linkedin.com/profile/view?id=110578462&authType=NAME_SEARCH&authToken=Xyg5&locale=en_US&srchid=0fdf6188-2ca4-48f4-848b-4f0f7a78235f-0&srchindex=1&srchtotal=27&goback=%2Efps_PBCK_*1_Beau_Miller_*1_*1_*1_*1_*2_*1_Y_*1_*1_*1_false_1_R_*1_*51_*1_*51_true_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2_*2&pvs=ps&trk=pp_profile_name_link)<br>
<br>
02/17/2011<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Casto AM, Feldman MW__ __(2011) [Genome-wide association study SNPs in the Human Genome Diversity Project populations: does selection affect unlinked SNPs with shared trait associations?](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1001266) PLoS Genet 7__:__ e1001266<br>
Discussion Leader: Tim Paape<br>
<br>
02/10/2011<br>
Sabeti PC, Walsh E, Schaffner SF, Varilly P, Fry B et al. (2005) [The case for selection at CCR5-Delta 32.](http://www.plosbiology.org/article/info:doi/10.1371/journal.pbio.0030378) Plos Biol 3: 1963-1969-ARTN e378.<br>
Discussion Leader: Annette McCoy<br>
<br>
02/03/2011<br>
To Be Determined (Maize LD manuscript)<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
01/27/2011<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Lam HM, Xu X, Liu X, Chen W, Yang G et al. (2010) [Resequencing of 31 wild and cultivated soybean genomes identifies patterns of genetic diversity and selection.](http://www.nature.com/ng/journal/v42/n12/full/ng.715.html) Nat Genet 42: 1053-1059.<br>
Discussion Leader: Emily Combs<br>
<br>
01/20/2011<br>
Albrechtsen A, Moltke I, Nielsen R (2010) [Natural selection and the distribution of identity-by-descent in the human genome](http://www.genetics.org/cgi/content/abstract/186/1/295). Genetics 186: 295-308.<br>
Discussion Leader: Amber Eule-Nashoba/Ron Okagaki<br>
<br>
01/13/2011<br>
Kirkpatrick M, Barton N (2006) [Chromosome inversions, local adaptation and speciation.](http://www.genetics.org/cgi/content/short/173/1/419) Genetics 173: 419-434.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
01/06/2011<br>
Pluzhnikov A, Donnelly P (1996) [Optimal sequencing strategies for surveying molecular genetic diversity.](http://www.genetics.org/cgi/content/abstract/144/3/1247) Genetics 144: 1247-1262.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
12/30/2010<br>
Christmas Holiday<br>
<br>
12/23/2010<br>
Christmas Holiday<br>
<br>
12/16/2010<br>
Coalescent Simulation<br>
[http://home.uchicago.edu/~rhudson1/source/mksamples.html](http://home.uchicago.edu/~rhudson1/source/mksamples.html)<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
12/09/2010<br>
Padhukasahasram B, Marjoram P, Wall JD, Bustamante CD, Nordborg M (2008) [Exploring population genetic models with recombination using efficient forward-time simulations.](http://www.genetics.org/cgi/content/abstract/178/4/2417) Genetics 178: 2417-2427.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
12/02/2010<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups<br>
Dickson SP, Wang K, Krantz I, Hakonarson H, Goldstein DB (2010) [Rare variants create synthetic genome-wide associations.](http://www.plosbiology.org/article/info:doi/10.1371/journal.pbio.1000294) PLoS Biol 8: e1000294.<br>
Discussion Leader: [Peter Tiffin](http://www.cbs.umn.edu/tiffin/)<br>
<br>
11/25/2010<br>
Thanksgiving Holiday<br>
<br>
11/18/2010<br>
Komatsuda T, Pourkheirandish M, He C, Azhaguvel P, Kanamori H et al. (2007) [Six-rowed barley originated from a mutation in a homeodomain-leucine zipper I-class homeobox gene.](http://www.pnas.org/content/104/4/1424.abstract) Proc Natl Acad Sci USA 104: 1424-1429. <br>
Discussion Leader: Ron Okagaki<br>
<br>
11/11/2010<br>
Hancock AM, Witonsky DB, Gordon AS, Eshel G, Pritchard JK et al. (2008) [Adaptations to climate in candidate genes for common metabolic disorders.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.0040032) Plos Genet 4: ARTN e32.<br>
Discussion Leader: Jessica Petersen<br>
<br>
11/04/2010<br>
Li H, Homer N (2010) [A survey of sequence alignment algorithms for next-generation sequencing.](http://bib.oxfordjournals.org/content/11/5/473.abstract) Brief Bioinform 11: 473-483.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
10/29/2010<br>
Clark RM, Linton E, Messing J, Doebley JF (2004) [Pattern of diversity in the genomic region near the maize domestication gene tb1.](http://www.pnas.org/content/101/3/700.abstract) Proc Natl Acad Sci U S A 101: 700-707.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
10/21/2010<br>
Joint Meeting with [McCue](http://www.cvm.umn.edu/equinegenetics/home.html), [Moeller](http://www.cbs.umn.edu/labs/moeller/Home.html), & [Tiffin](http://www.cbs.umn.edu/tiffin/) Lab Groups
Gossmann TI, Song BH, Windsor AJ, Mitchell-Olds T, Dixon CJ et al. (2010) [Genome wide analyses reveal little evidence for adaptive evolution in many plant species.](http://mbe.oxfordjournals.org/content/27/8/1822.abstract) Mol Biol Evol 27: 1822-1832.<br>
Discussion Leader: Tim Paape<br>
<br>
10/14/2010<br>
Haddrill PR, Thornton KR, Charlesworth B, Andolfatto P (2005) [Multilocus patterns of nucleotide variability and the demographic and selection history of _Drosophila melanogaster_ populations.](http://genome.cshlp.org/content/15/6/790.abstract) Genome Res 15: 790-799.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
10/07/2010<br>
Hudson RR (1990) [Gene genealogies and the coalescent process.](http://home.uchicago.edu/~rhudson1/popgen356/OxfordSurveysEvolBiol7_1-44.pdf) Oxford Surveys in Evolutionary Biology 7: 1-42.
Second half of the chapter.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
09/30/2010<br>
Durand E, Tenaillon MI, Ridel C, Coubriche D, Jamin P et al. (2010) [Standing variation and new mutations both contribute to a fast response to selection for flowering time in maize inbreds.](http://www.biomedcentral.com/1471-2148/10/2/abstract/) Bmc Evol Biol 10: ARTN 2.<br>
Discussion Leader: Vikram Vikus<br>
<br>
09/23/2010<br>
Andolfatto P, Nordborg M (1998) [The effect of gene conversion on intralocus associations.](http://www.genetics.org/cgi/content/full/148/3/1397) Genetics 148: 1397-1399.<br>
Jeffreys AJ, May CA (2004) [Intense and highly localized gene conversion activity in human meiotic crossover hot spots.](http://www.nature.com/ng/journal/v36/n2/full/ng1287.html) Nat Genet 36: 151-156.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
09/16/2010<br>
Atwell S, Huang YS, Vilhjalmsson BJ, Willems G, Horton M et al. (2010) [Genome-wide association study of 107 phenotypes in _Arabidopsis thaliana_ inbred lines.](http://www.nature.com/nature/journal/v465/n7298/full/nature08800.html) Nature 465: 627-631.<br>
Discussion Leader: Nichol Schultz<br>
<br>
09/09/2010<br>
Zhai W, Nielsen R, Slatkin M (2009) [An investigation of the statistical power of neutrality tests based on comparative and population genetic data.](http://mbe.oxfordjournals.org/content/26/2/273.abstract) Mol Biol Evol 26: 273-283.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
09/03/2010<br>
Lockton S, Ross-Ibarra J, Gaut BS (2008) [Demography and weak selection drive patterns of transposable element diversity in natural populations of _Arabidopsis lyrata_.](http://www.pnas.org/content/105/37/13965) P Natl Acad Sci Usa 105: 13965–13970<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
08/27/2010<br>
Albrechtsen A, Nielsen FC, Nielsen R (2010) [Ascertainment biases in SNP chips affect measures of population divergence.](http://mbe.oxfordjournals.org/content/27/11/2534) Mol Biol Evol 27: 2534-2547.<br>
Discussion Leaders: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
08/20/2010<br>
Karasov T, Messer PW, Petrov DA (2010) [Evidence that adaptation in _Drosophila_ is not limited by mutation at single sites.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1000924) Plos Genet 6: ARTN e1000924.<br>
Discussion Leader: Krista Fritz<br>
<br>
08/13/2010<br>
Baudat F, Buard J, Grey C, Fledel-Alon A, Ober C et al. (2010) [PRDM9 is a major determinant of meiotic recombination hotspots in humans and mice.](http://www.sciencemag.org/cgi/content/abstract/327/5967/836) Science 327: 836-840.<br>
Discussion Leader:  [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
08/06/2010<br>
No Meeting<br>
<br>
07/30/2010<br>
No Meeting<br>
<br>
07/23/2010<br>
Yang J, Benyamin B, McEvoy BP, Gordon S, Henders AK et al. (2010) [Common SNPs explain a large proportion of the heritability for human height.](http://www.nature.com/ng/journal/v42/n7/full/ng.608.html) Nat Genet 42: 565-569.<br>
Discussion Leader: [Molly McCue](http://www.cvm.umn.edu/equinegenetics/home.html)<br>
<br>
07/16/2010<br>
Hudson RR (1990) [Gene genealogies and the coalescent process.](http://home.uchicago.edu/~rhudson1/popgen356/OxfordSurveysEvolBiol7_1-44.pdf) Oxford Surveys in Evolutionary Biology 7: 1-42.<br>
Discussion Leader: Diego Coelho<br>
<br>
07/09/2010<br>
An introduction to libsequence & phred/phrap/consed/polyphred<br>
Thornton K (2003) [Libsequence: a C++ class library for evolutionary genetic analysis.](http://bioinformatics.oxfordjournals.org/content/19/17/2325.abstract) Bioinformatics 19: 2325-2327.<br>
Discussion Leaders: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/) / [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
07/02/2010<br>
Fay JC, Wu CI (2000) [Hitchhiking under positive Darwinian selection.](http://www.genetics.org/cgi/content/abstract/155/3/1405) Genetics 155: 1405-1413.<br>
Discussion Leader: Jessica Petersen<br>
<br>
06/25/2010<br>
Morrell PL, Clegg MT (2007) [Genetic evidence for a second domestication of barley (_Hordeum vulgare_) east of the Fertile Crescent.](http://www.pnas.org/content/104/9/3289.abstract) Proc Natl Acad Sci USA 104: 3289-3294.<br>
Discussion Leader: Godwin Macharia<br>
<br>
06/18/2010<br>
Eckert AJ, van Heerwaarden J, Wegrzyn JL, Nelson CD, Ross-Ibarra J et al. (2010) [Patterns of population structure and environmental associations to aridity across the range of loblolly pine (_Pinus taeda_ L., Pinaceae).](http://www.genetics.org/cgi/content/abstract/185/3/969) Genetics 185: 969-982.<br>
Discussion Leaders: Diego Coelho / Kevin Volz<br>
<br>
06/11/2010<br>
Ross-Ibarra J, Tenaillon M, Gaut BS (2009) [Historical divergence and gene flow in the genus _Zea_.](http://www.genetics.org/cgi/content/abstract/181/4/1399) Genetics 181: 1399-1413.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
06/04/2010<br>
Plagnol V, Padhukasahasram B, Wall JD, Marjoram P, Nordborg M (2006) [Relative influences of crossing over and gene conversion on the pattern of linkage disequilibrium in _Arabidopsis thaliana_.](http://www.genetics.org/cgi/content/abstract/172/4/2441) Genetics 172: 2441-2448.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
05/28/2010<br>
Price AL, Tandon A, Patterson N, Barnes KC, Rafaels N et al. (2009) [Sensitive detection of chromosomal segments of distinct ancestry in admixed populations.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1000519) PLoS Genet 5: e1000519.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
05/21/2010<br>
Gaut BS, Long AD (2003) [The lowdown on linkage disequilibrium.](http://www.plantcell.org/cgi/content/full/15/7/1502) Plant Cell 15: 1502-1506.<br>
Discussion Leaders: Peter Morrell<br>
<br>
05/14/2010<br>
Green RE, Krause J, Briggs AW, Maricic T, Stenzel U et al. (2010) [A draft sequence of the Neandertal genome.](http://www.sciencemag.org/cgi/content/abstract/328/5979/710) Science 328: 710-722.<br>
Discussion Leaders: Ana Gonzales / Diego Coelho<br>
<br>
05/07/2010<br>
Linux Basics<br>
[http://manuals.bioinformatics.ucr.edu/home/linux-basics](http://manuals.bioinformatics.ucr.edu/home/linux-basics)<br>
Discussion Leaders: Ana Gonzales / [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
04/30/2010<br>
Feng L, Sebastian S, Smith S, Cooper M (2006) [Temporal trends in SSR allele frequencies associated with long-term selection for yield of maize.](http://www.maiscoltura.it/maydica/articles/51_293.pdf) Maydica 51: 293-300.<br>
Discussion Leader: Godwin Macharia<br>
<br>
04/23/2010<br>
Charlesworth D, Willis JH (2009) [FUNDAMENTAL CONCEPTS IN GENETICS The genetics of inbreeding depression.](http://www.nature.com/nrg/journal/v10/n11/full/nrg2664.html) Nat Rev Genet 10: 783-796.<br>
Discussion Leader: Hao Zhou<br>
<br>
04/16/2010<br>
Pickrell JK, Coop G, Novembre J, Kudaravalli S, Li JZ et al. (2009) [Signals of recent positive selection in a worldwide sample of human populations.](http://genome.cshlp.org/content/19/5/826) Genome Res 19: 826-837.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
04/09/2010<br>
Metzker ML (2010) [APPLICATIONS OF NEXT-GENERATION SEQUENCING Sequencing technologies - the next generation.](http://www.nature.com/nrg/journal/v11/n1/full/nrg2626.html) Nat Rev Genet 11: 31-46.<br>
Discussion Leader: Vikram Vikus<br>
<br>
04/02/2010<br>
Vonholdt BM, Pollinger JP, Lohmueller KE, Han E, Parker HG et al. (2010) [Genome-wide SNP and haplotype analyses reveal a rich history underlying dog domestication.](http://www.nature.com/nature/journal/v464/n7290/full/nature08837.html) Nature 464: 898-902. - Supplemental Information & analytical methods<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
03/26/2010<br>
Vonholdt BM, Pollinger JP, Lohmueller KE, Han E, Parker HG et al. (2010) [Genome-wide SNP and haplotype analyses reveal a rich history underlying dog domestication.](http://www.nature.com/nature/journal/v464/n7290/full/nature08837.html) Nature 464: 898-902.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
03/19/2010<br>
Spring Break<br>
<br>
03/12/2010<br>
Chen H, Morrell PL, Ashworth VE, de la Cruz M, Clegg MT (2009) [Tracing the geographic origins of major avocado cultivars.](http://jhered.oxfordjournals.org/content/100/1/56.abstract) J Hered 100: 56-65.<br>
Discussion Leader: Ana Gonzales<br>
<br>
03/05/2010<br>
Chen H, Morrell PL, de la Cruz M, Clegg MT (2008) [Nucleotide diversity and linkage disequilibrium in wild avocado (_Persea americana_ Mill.).](http://jhered.oxfordjournals.org/content/99/4/382.abstract) J Hered 99: 382-389.<br>
Discussion Leader: Ana Gonzales<br>
<br>
02/26/2010<br>
Long AD, Langley CH (1999) [The power of association studies to detect the contribution of candidate genetic loci to variation in complex traits.](http://genome.cshlp.org/content/9/8/720.abstract) Genome Res 9: 720-731.<br>
Discussion Leader: Liana Nice<br>
<br>
02/19/2010<br>
Rockman MV, Kruglyak L (2008) [Breeding designs for recombinant inbred advanced intercross lines.](http://www.genetics.org/cgi/content/abstract/179/2/1069) Genetics 179: 1069-1078.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
02/12/2010<br>
Buckler ES, Holland JB, Bradbury PJ, Acharya CB, Brown PJ et al. (2009) [The genetic architecture of maize flowering time.](http://www.sciencemag.org/cgi/content/abstract/325/5941/714) Science 325: 714-718.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
02/05/2010<br>
Zhao KY, Aranzana MJ, Kim S, Lister C, Shindo C et al. (2007) [An _Arabidopsis_ example of association mapping in structured samples.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.0030004) Plos Genet 3: ARTN e4.<br>
Discussion Leaders: Vikram Vikus / Stephanie Nevara<br>
<br>
01/29/2010<br>
Nordborg M, Hu TT, Ishino Y, Jhaveri J, Toomajian C et al. (2005) [The pattern of polymorphism in _Arabidopsis thaliana_.](http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.0030196) PLos Biol 3: e196.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
01/22/2010<br>
Wright SI, Bi IV, Schroeder SG, Yamasaki M, Doebley JF et al. (2005) [The effects of artificial selection on the maize genome.](http://www.sciencemag.org/cgi/content/abstract/308/5726/1310) Science 308: 1310-1314.<br>
Discussion Leader: Chris Taylor<br>
<br>
01/12/2010<br>
[Plant & Animal Genome Meeting](http://www.intlpag.org/web/)<br>
<br>
01/05/2010<br>
Rosenberg NA, Pritchard JK, Weber JL, Cann HM, Kidd KK et al. (2002) [Genetic structure of human populations.](http://www.sciencemag.org/cgi/content/abstract/298/5602/2381) Science 298: 2381-2385.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
12/23/2009<br>
Rosenberg NA, Nordborg M (2002) [Genealogical trees, coalescent theory and the analysis of genetic polymorphisms.](http://www.nature.com/nrg/journal/v3/n5/full/nrg795.html) Nat Rev Genet 3: 380-390.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
12/17/2009<br>
Voelkerding KV, Dames SA, Durtschi JD (2009) [Next-generation sequencing: from basic research to diagnostics.](http://www.clinchem.org/cgi/content/abstract/55/4/641) Clin Chem 55: 641-658.<br>
Discussion Leader: [Zhou Fang](http://users.stat.umn.edu/~zhou/)<br>
<br>
12/10/2009<br>
Gore MA, Chia JM, Elshire RJ, Sun Q, Ersoz ES et al. (2009) [A first-generation haplotype map of maize.](http://www.sciencemag.org/cgi/content/abstract/326/5956/1115) Science 326: 1115-1117.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>
12/03/2009<br>
Wakeley J (2008) [Coalescent Theory: An Introduction.](http://www.roberts-publishers.com/index.php?page=shop.product_details&flypage=flypage.tpl&product_id=46&option=com_virtuemart&Itemid=64&vmcchk=1&Itemid=64) Roberts & Company Publishers. Chapter 1 (continued).<br>
Discussion Leader: Chris Taylor<br>
<br>
11/26/2009<br>
Thanksgiving Holiday<br>
<br>
11/19/2009<br>
Wakeley J (2008) [Coalescent Theory: An Introduction.](http://www.roberts-publishers.com/index.php?page=shop.product_details&flypage=flypage.tpl&product_id=46&option=com_virtuemart&Itemid=64&vmcchk=1&Itemid=64) Roberts & Company Publishers. Chapter 1.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
11/12/2009<br>
Tenaillon MI, Sawkins MC, Long AD, Gaut RL, Doebley JF et al. (2001) [Patterns of DNA sequence polymorphism along chromosome 1 of maize (_Zea mays_ ssp. _mays_ L.)](http://www.pnas.org/content/98/16/9161.abstract). Proc Natl Acad Sci USA 98: 9161-9166.<br>
Discussion Leader: [Ana Gonzales](https://sites.google.com/site/anamariagonzalesb/)<br>
<br>
11/05/2009<br>
Stumpf MP, McVean GA (2003) [Estimating recombination rates from population-genetic data.](http://www.nature.com/nrg/journal/v4/n12/full/nrg1227.html) Nat Rev Genet 4: 959-968.<br>
Discussion Leader: [Peter Morrell](http://faculty.agronomy.cfans.umn.edu/pmorrell/)<br>
<br>

<!-- Start Google Analytics -->
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-19694768-1']);
_gaq.push(['_trackPageview']);
(function() {
var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
<!-- End Google Analytics -->