#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import shutil
from os import path, devnull, mkdir
from subprocess import check_call, STDOUT, PIPE, Popen
import subprocess,shlex
import pandas as pd
import time
import re
from collections import Counter

FNULL = open(devnull, 'w')

parser = argparse.ArgumentParser(description='Rapid-Strain\n Version : 0.0.1')
parser.add_argument('-fa',action='store',dest='fa',help='input FASTA (may be gzipped)',default='')
parser.add_argument('-fq',action='store',dest='fq',help='input FASTQ (may be gzipped)',default='')
parser.add_argument('-t',action='store',dest='target',help='target genus/species (See the list of supported genus/species names)',default='')
parser.add_argument('-p',action='store',dest='threads',help='Multi threads process for mash (Default:1)',default=1)
parser.add_argument('-m',action='store',dest='target',help='Minimum rate of shared-hashes with markers (default:0.9)',default=0.9)
parser.add_argument('-tmp',action='store',dest='tmp_dir',help='Temporary output directory (output directory for intermediate files) defaul:The same directory as the input file',default='')
parser.add_argument('-v',action='version',version='Version : 0.0.1')

print "============================================================================"
print "                              Rapid-strain                                  "
print "           - Rapid estimation of microbial strains from NGS data -          "
print "                                                                            "
print "                          > Version : 0.0.1                                 "
print "                          > Written by K.I.                                 "
print "                                                                            "
print "============================================================================"

sttime = time.time()

args = parser.parse_args()

if len(args.target) == 0 :
     print ('INPUT ERROR.\nPlease set a target genus/species name.')
     sys.exit()


print "Loading input sequences..."

if len(args.fa) == 0  and len(args.fq) == 0:
     print ('INPUT ERROR.\nPlease input FASTA (-fa input.fa) or FASTQ (-fq input.fq) as the input file.')
     sys.exit()

if len(args.fa) == 0 and len(args.fq) >0 :
    if len(args.tmp_dir) == 0:
        tmp_dir_path = path.dirname(path.abspath(args.fq))+"/tmp"
        if path.exists(tmp_dir_path):
            shutil.rmtree(tmp_dir_path)
            mkdir(tmp_dir_path)
        else:
            shutil.rmtree(tmp_dir_path)
            mkdir(tmp_dir_path)
    else:
        tmp_dir_path = path.abspath(args.tmp_dir)
        if path.exists(tmp_dir_path):
            shutil.rmtree(tmp_dir_path)
            mkdir(tmp_dir_path)
        else:
            mkdir(tmp_dir_path)
    cmd_fq2fa = "seqkit fq2fa {input} > {tmp_dir}/tmp1.fa".format(input=path.abspath(args.fq),tmp_dir=tmp_dir_path)
    check_call(cmd_fq2fa,shell=True, stdout=FNULL, stderr=STDOUT)
    input_seq=path.abspath("{tmp_dir}/tmp1.fa".format(tmp_dir=tmp_dir_path))

elif len(args.fq) == 0 and len(args.fa) > 0:
    if len(args.tmp_dir) == 0:
        tmp_dir_path = path.dirname(path.abspath(args.fa))+"/tmp"
        if path.exists(tmp_dir_path):
            shutil.rmtree(tmp_dir_path)
            mkdir(tmp_dir_path)
        else:
            mkdir(tmp_dir_path)
    else:
        tmp_dir_path = path.abspath(args.tmp_dir)
        if path.exists(tmp_dir_path):
            shutil.rmtree(tmp_dir_path)
            mkdir(tmp_dir_path)
        else:
            mkdir(tmp_dir_path)
    input_seq = path.abspath(args.fa)

cmd_run_screen1="""mash screen -p {threads} {target}.msh {input_seq} > {tmp_dir}/tmp1.out""".format(threads=args.threads,target=args.target,input_seq=input_seq,tmp_dir=tmp_dir_path)
check_call(cmd_run_screen1,shell=True, stdout=FNULL, stderr=STDOUT)

print "Searching for candidate strains in {target}".format(target=args.target)

df = pd.read_csv("{tmp_dir}/tmp1.out".format(tmp_dir=tmp_dir_path),sep="\t",header=None)
df_marker = pd.read_csv("{target}.txt".format(target=args.target),sep="\t")

candidates_list=[]
for i in df[df[0] == df[0].max()][4].to_list():
    for j in re.split("ST|_|.fa|\.|/",i):
        if str.isdigit(j):
            candidates_list.append(int(j))
df_top=df_marker[df_marker['ST'].isin(candidates_list)]


df_comp = pd.DataFrame()

for i in df_top.columns[1:][::-1][1:][::-1]:
    if len(df_top[['ST',i]][~df_top.duplicated(subset=[i],keep=False)]) != 0:
        if len(df_comp) == 0:
            df_comp = df_top[['ST',i]][~df_top.duplicated(subset=[i],keep=False)].copy()
        else:
            df_comp = pd.merge(df_comp,df_top[['ST',i]],on="ST")

print "Found candidates that have the most shared hash with markers..."

for i in df_comp.columns:
    grep_fasta = []
    grep_fasta_out = []
    if i != 'ST':
        for j in df_comp[i]:
            cmd_gen_fasta = "seqkit grep -p {marker}_{num} {marker}.tfa > {tmp_dir}/{marker}_{num}.fa".format(marker=i,num=j,tmp_dir=tmp_dir_path)
            check_call(cmd_gen_fasta,shell=True, stdout=FNULL, stderr=STDOUT)
        cmd_sketch = "mash sketch -p {threads} -o {tmp_dir}/{marker}.msh {tmp_dir}/{marker}_*.fa".format(threads=args.threads,tmp_dir=tmp_dir_path,marker=i)
        check_call(cmd_sketch,shell=True, stdout=FNULL, stderr=STDOUT)
        cmd_run_screen2 ="mash screen -p {threads} -i 1 -w {tmp_dir}/{marker}.msh {input}".format(threads=args.threads,tmp_dir=tmp_dir_path,marker=i,input=input_seq)
        proc = subprocess.Popen(shlex.split(cmd_run_screen2), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_stdout = proc.stdout.read()
        l_num=len(output_stdout.split("\n"))-1
        best_hit_strain = []
        for l in range(l_num):
            best_hit_strain.append(df_comp[df_comp[re.split('\t|\s+',output_stdout.split('\n')[l])[5].split('_')[0]] == int(re.split('\t|\s+',output_stdout.split('\n')[l])[5].split('_')[1])]['ST'].to_list()[0])
freq = lambda x: float(x)/sum(Counter(best_hit_strain).values())
df_best_hit=pd.DataFrame(Counter(best_hit_strain).items(),columns=['Strain','Freq'])
df_best_hit['Freq'] = df_best_hit['Freq'].map(freq)

print "Estimated Strain:"
print (df_marker[df_marker['ST'] == int(df_best_hit.iloc[df_best_hit['Freq'].idxmax()]['Strain'])]).to_string(index=False)
print "Run time:",round((time.time() - sttime),3)
print "----------------------------------------------------------------"
