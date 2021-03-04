Rapid-Strain
====
Rapid estimation of microbial strains from NGS data

## Requirement python packages
pandas (Test enviroment: Python 2.7)

Set up for requirement packages
`pip install pandas`

## Requirement tools

・[MASH](https://mash.readthedocs.io/en/latest/index.html): Fast genome and metagenome distance estimation using MinHash

・[SeqKit](https://bioinf.shenwei.me/seqkit/): a cross-platform and ultrafast toolkit for FASTA/Q file manipulation

Please refer to the official site for details of the installation of these packages.

## Installation of Rapid-Strain
Clone this repository into your local machine
`git clone https://github.com/omics-tools/rapid-strain.git`

## Getting started

### Usage

`python rapid-strain.py -fa query.fa -t species/genus [-p threads ] [-tmp tmp_dir]`

**optional arguments:**

| Flag | Description | File type, Default, Example etc. |
|:-----------|:------------|:------------|
| **-fa**      | input FASTA (may be gzipped) |.fa/.fas/.fasta|
| **-fq**      | input FASTQ (may be gzipped) |.fq/.fastq|
| **-t**       | target scheme name (See the list of supported genus/species names) (**required**) | (e.g.) -t campylobacter |
| **-p**       | Multi threads process for mash  | default: 1 |
| **-tmp**     | Temporary output directory | default: The directory in the input file |
| **-v**       | Program's version number and exit  | |
| **-h**       | Help message and exit         | |

### Genus/species supported by Rapid-Strain
| Scheme (Target)      | Genus             | Species            | Marker | Sequence Types |
|----------------------|-------------------|--------------------|--------|----------------|
| abaumannii           | Acinetobacter     | baumannii          | 7      | 14609          |
| abaumannii_2         | Acinetobacter     | baumannii          | 7      | 10003          |
| achromobacter        | Achromobacter     |                    | 7      | 3339           |
| aeromonas            | Aeromonas         |                    | 6      | 3936           |
| aphagocytophilum     | Anaplasma         | aphagocytophilum   | 7      | 1288           |
| arcobacter           | Arcobacter        |                    | 7      | 5817           |
| bcc                  | Burkholderia      | cepacia            | 7      | 12089          |
| bcereus              | Bacillus          | cereus             | 7      | 17395          |
| bhampsonii           | Brachyspira       | hampsonii          | 6      | 120            |
| bhenselae            | Bartonella        | henselae           | 8      | 288            |
| bhyodysenteriae      | Brachyspira       | hyodysenteriae     | 7      | 1841           |
| bintermedia          | Brachyspira       | intermedia         | 7      | 581            |
| blicheniformis       | Bacillus          | licheniformis      | 6      | 282            |
| bordetella           | Bordetella        | pertussis          | 7      | 651            |
| borrelia             | Borrelia          |                    | 8      | 7456           |
| bpilosicoli          | Brachyspira       | pilosicoli         | 7      | 658            |
| bpseudomallei        | Burkholderia      | pseudomallei       | 7      | 12411          |
| brachyspira          | Brachyspira       |                    | 7      | 252            |
| bsubtilis            | Bacillus          | subtilis           | 7      | 1225           |
| campylobacter        | Campylobacter     | coli               | 7      | 71407          |
| campylobacter        | Campylobacter     | jejuni             | 7      | 71407          |
| cbotulinum           | Clostridium       | botulinum          | 7      | 840            |
| cconcisus            | Campylobacter     | concisus           | 7      | 910            |
| cdifficile           | Clostridium       | difficile          | 7      | 4648           |
| cdifficile           | Peptoclostridium  | difficile          | 7      | 4648           |
| cdiphtheriae         | Corynebacterium   | diphtheriae        | 7      | 4641           |
| cfetus               | Campylobacter     | fetus              | 7      | 483            |
| cfreundii            | Citrobacter       | freundii           | 7      | 3675           |
| chelveticus          | Campylobacter     | helveticus         | 7      | 63             |
| chlamydiales         | Chlamydia         |                    | 7      | 1953           |
| chyointestinalis     | Campylobacter     | hyointestinalis    | 7      | 938            |
| cinsulaenigrae       | Campylobacter     | insulaenigrae      | 7      | 301            |
| clanienae            | Campylobacter     | lanienae           | 7      | 1204           |
| clari                | Campylobacter     | lari               | 7      | 1127           |
| cmaltaromaticum      | Carnobacterium    | maltaromaticum     | 7      | 392            |
| cronobacter          | Cronobacter       |                    | 7      | 5026           |
| csepticum            | Clostridium       | septicum           | 7      | 56             |
| csputorum            | Campylobacter     | sputorum           | 7      | 112            |
| cupsaliensis         | Campylobacter     | upsaliensis        | 7      | 1428           |
| ecloacae             | Enterobacter      | cloacae            | 7      | 9338           |
| ecoli                | Escherichia       |                    | 7      | 66136          |
| ecoli                | Shigella          |                    | 7      | 66136          |
| ecoli_2              | Escherichia       |                    | 8      | 7768           |
| edwardsiella         | Edwardsiella      | tarda              | 10     | 180            |
| efaecalis            | Enterococcus      | faecalis           | 7      | 6825           |
| efaecium             | Enterococcus      | faecium            | 7      | 11739          |
| fpsychrophilum       | Flavobacterium    | psychrophilum      | 7      | 1358           |
| hcinaedi             | Helicobacter      | cinaedi            | 7      | 140            |
| hinfluenzae          | Haemophilus       | influenzae         | 7      | 15960          |
| hparasuis            | Haemophilus       | parasuis           | 7      | 2779           |
| hpylori              | Helicobacter      | pylori             | 7      | 25809          |
| hsuis                | Haematopinus      | suis               | 7      | 966            |
| kkingae              | Kingella          | kingae             | 6      | 420            |
| koxytoca             | Klebsiella        | oxytoca            | 7      | 1897           |
| kpneumoniae          | Klebsiella        | pneumoniae         | 7      | 33880          |
| leptospira           | Leptospira        |                    | 7      | 2254           |
| leptospira_2         | Leptospira        |                    | 7      | 1911           |
| leptospira_3         | Leptospira        |                    | 6      | 1134           |
| lmonocytogenes       | Listeria          | monocytogenes      | 7      | 14490          |
| lsalivarius          | Lactobacillus     | salivarius         | 5      | 125            |
| mabscessus           | Mycobacterium     | abscessus          | 7      | 182            |
| magalactiae          | Mycoplasma        | agalactiae         | 5      | 175            |
| mbovis               | Mycoplasma        | bovis              | 7      | 1295           |
| mcatarrhalis         | Moraxells         | catarrhalis        | 8      | 6184           |
| mhaemolytica         | Mannheimia        | haemolytica        | 7      | 357            |
| mhyorhinis           | Mycoplasma        | hyorhinis          | 6      | 624            |
| mmassiliense         | Mycobacterium     | massiliense        | 7      | 84             |
| mplutonius           | Melissococcus     | plutonius          | 4      | 140            |
| neisseria            | Neisseria         |                    | 7      | 106330         |
| orhinotracheale      | Ornithobacterium  | rhinotracheale     | 7      | 245            |
| otsutsugamushi       | Orientia          | tsutsugamushi      | 7      | 686            |
| pacnes               | Propionibacterium | acnes              | 8      | 1216           |
| paeruginosa          | Pseudomonas       | aeruginosa         | 7      | 23597          |
| pfluorescens         | Pseudomonas       | fluorescens        | 7      | 770            |
| pgingivalis          | Porphyromonas     | gingivalis         | 7      | 966            |
| plarvae              | Paenibacillus     | larvae             | 7      | 168            |
| pmultocida_multihost | Pasteurella       | multocida          | 7      | 868            |
| pmultocida_rirdc     | Pasteurella       | multocida          | 7      | 2611           |
| ppentosaceus         | Pediococcus       | pentosaceus        | 7      | 119            |
| ranatipestifer       | Riemerella        | anatipestifer      | 7      | 308            |
| sagalactiae          | Streptococcus     | agalactiae         | 7      | 10038          |
| saureus              | Staphylococcus    | aureus             | 7      | 40796          |
| scanis               | Streptococcus     | canis              | 7      | 378            |
| sdysgalactiae        | Streptococcus     | dysgalactiae       | 7      | 3647           |
| senterica            | Salmonella        | enterica           | 7      | 46123          |
| sepidermidis         | Staphylococcus    | epidermidis        | 7      | 6769           |
| sgallolyticus        | Streptococcus     | gallolyticus       | 7      | 763            |
| shaemolyticus        | Staphylococcus    | haemolyticus       | 7      | 483            |
| shominis             | Stapylococcus     | hominis            | 6      | 342            |
| sinorhizobium        | Sinorhizobium     |                    | 10     | 1360           |
| slugdunensis         | Staphylococcus    | lugdunensis        | 7      | 294            |
| smaltophilia         | Stenotrophomonas  | maltophilia        | 7      | 3290           |
| soralis              | Streptococcus     | oralis             | 7      | 546            |
| spneumoniae          | Streptococcus     | pneumoniae         | 7      | 106540         |
| spseudintermedius    | Staphylococcus    | pseudintermedius   | 7      | 11200          |
| spyogenes            | Streptococcus     | pyogenes           | 7      | 8232           |
| ssuis                | Streptococcus     | suis               | 7      | 9016           |
| sthermophilus        | Streptococcus     | thermophilus       | 6      | 750            |
| sthermophilus_2      | Streptococcus     | thermophilus       | 10     | 1190           |
| streptomyces         | Streptomyces      |                    | 6      | 1404           |
| suberis              | Streptococcus     | uberis             | 7      | 8162           |
| szooepidemicus       | Streptococcus     | equi               | 7      | 2779           |
| taylorella           | Taylorella        |                    | 7      | 497            |
| tenacibaculum        | Tenacibaculum     |                    | 7      | 910            |
| vcholerae            | Vibrio            | cholerae           | 7      | 6895           |
| vibrio               | Vibrio            |                    | 4      | 712            |
| vparahaemolyticus    | Vibrio            | parahaemolyticus   | 7      | 15589          |
| vtapetis             | Vibrio            | tapetis            | 10     | 100            |
| vvulnificus          | Vibrio            | vulnificus         | 10     | 5300           |
| wolbachia            | Wolbachia         |                    | 5      | 2860           |
| xfastidiosa          | Xylella           | fastidiosa         | 7      | 609            |
| yersinia             | Yersinia          |                    | 7      | 1190           |
| ypseudotuberculosis  | Yersinia          | pseudotuberculosis | 7      | 3689           |
| yruckeri             | Yersinia          | ruckeri            | 6      | 180            |

These lists are based on the scheme names in [PubMLST](https://pubmlst.org/) and [mlst](https://github.com/tseemann/mlst).

## Version

0.0.1 (beta)

## Licence

[MIT] https://github.com/omics-tools/mitoimp/blob/master/LICENSE
