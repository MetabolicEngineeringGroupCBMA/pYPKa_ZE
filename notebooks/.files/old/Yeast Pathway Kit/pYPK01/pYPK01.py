# coding: utf-8
'''
ScTEF1-XK-ScTPI1-XDH-ScPDC1-XR-ScFBA1-TAL1-ScTDH3

pYPK0
tef1-ScXK-tpi1
          tpi1-XDH-pdc1
                   pdc1-XR-fba1
                           fba1-TAL1-tdh3
pYPK1
tef1-EcXK-tpi1
          tpi1-XDH-pdc1
                   pdc1-XR-fba1
                           fba1-TAL1-tdh3
'''

from pydna import *
from pydna_helper.load_my_primers import primer
from pydna_helper import gb, ape
from Bio.SeqUtils.CheckSum import seguid

# load pCAPs and pCAPs-pSU0 as dsdna objects
pCAPs      = read("/home/bjorn/Dropbox/wikidata/pCAPs.wiki")
pCAPs_pSU0 = read("/home/bjorn/Dropbox/wikidata/pCAPs-pSU0.wiki")

from pyeast import saccharomyces_cerevisiae_genome as sc

sgd = sc.saccharomyces_cerevisiae_genome()

ScTEF1tp = pcr(primer[417],primer[455], sgd.promoter("TEF1"))
ScTPI1tp = pcr([primer[456],primer[419]], sgd.promoter("TPI1"))
ScPDC1tp = pcr([primer[453],primer[413]], sgd.promoter("PDC1"))
ScFBA1tp = pcr([primer[409],primer[451]], sgd.promoter("FBA1"))
ScTDH3tp = pcr([primer[454],primer[415]], sgd.promoter("TDH3"))

from Bio.Restriction import EcoRV, ZraI
pCAPs_ZraI = pCAPs.cut(ZraI).pop()
pCAPs_EcoRV = pCAPs.cut(EcoRV).pop()
pCAPs_pSU0_E_Z, stuffer = pCAPs_pSU0.cut((EcoRV,ZraI))

pCAPs_ZraI_ScTEF1tp  = (pCAPs_ZraI  + ScTEF1tp).looped()
pCAPs_EcoRV_ScTPI1tp = (pCAPs_EcoRV + ScTPI1tp).looped()
pCAPs_ZraI_ScTPI1tp  = (pCAPs_ZraI  + ScTPI1tp).looped()
pCAPs_ZraI_ScPDC1tp  = (pCAPs_ZraI  + ScPDC1tp).looped()
pCAPs_EcoRV_ScPDC1tp = (pCAPs_EcoRV + ScPDC1tp).looped()
pCAPs_ZraI_ScFBA1tp  = (pCAPs_ZraI  + ScFBA1tp).looped()
pCAPs_EcoRV_ScFBA1tp = (pCAPs_EcoRV + ScFBA1tp).looped()
pCAPs_EcoRV_ScTDH3tp = (pCAPs_EcoRV + ScTDH3tp).looped()

ypk_primer = parse("/home/bjorn/Dropbox/wikidata/ypk_primers.wiki")

XYL1=gb("X59465")
XYL2=gb("A16166")

EcoliXK = read("/home/bjorn/Dropbox/wikidata/EcXK.wiki")

# ScTEF1tp-E.coliXK-ScTPI1tp
A_ScTEF1tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScTEF1tp)
EcXK         = pcr( ypk_primer[12], ypk_primer[13], EcoliXK)
C_ScTPI1tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScTPI1tp)

sequences, circular = circular_assembly((  A_ScTEF1tp_b,
                                           EcXK,
                                           C_ScTPI1tp_d,
                                           pCAPs_pSU0_E_Z), limit=28)
pYPK0_ScTEF1tp_EcXK_ScTPI1tp = circular[0]

# ScTEF1tp-ScXK-ScTPI1tp
A_ScTEF1tp_b = pcr( primer[167], primer[567], pCAPs_ZraI_ScTEF1tp)
ScXK         = pcr( ypk_primer[4], ypk_primer[5], sgd.cds("XKS1"))
C_ScTPI1tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScTPI1tp)
sequences, circular = circular_assembly((  A_ScTEF1tp_b,
                                           ScXK,
                                           C_ScTPI1tp_d,
                                           pCAPs_pSU0_E_Z), limit=28)
pYPK0_ScTEF1tp_XK_ScTPI1tp = circular[0]


# ScTPI1tp-XDH-ScPDC1tp
A_ScTPI1tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScTPI1tp)
PsXDH        = pcr( ypk_primer[2], ypk_primer[3], XYL2)
C_ScPDC1tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScPDC1tp)
sequences, circular = circular_assembly((  A_ScTPI1tp_b,
                                                                    PsXDH,
                                                                    C_ScPDC1tp_d,
                                                                    pCAPs_pSU0_E_Z
                                                                  ), limit=28)
pYPK0_ScTPI1tp_XDH_ScPDC1tp = circular[0]
# ScPDC1tp-XR-ScFBA1tp
A_ScPDC1tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScPDC1tp)
PsXR   = pcr( ypk_primer[0], ypk_primer[1], XYL1)
C_ScFBA1tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScFBA1tp)
sequences, circular = circular_assembly((  A_ScPDC1tp_b,
                                                                    PsXR,
                                                                    C_ScFBA1tp_d,
                                                                    pCAPs_pSU0_E_Z
                                                                  ), limit=28)
pYPK0_ScPDC1tp_XR_ScFBA1tp = circular[0]
# ScFBA1tp-TAL1-ScTDH3tp
A_ScFBA1tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScFBA1tp)
ScTAL1 = pcr( ypk_primer[6], ypk_primer[7], sgd.cds("TAL1"))
C_ScTDH3tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScTDH3tp)
sequences, circular = circular_assembly((  A_ScFBA1tp_b,
                                                                    ScTAL1,
                                                                    C_ScTDH3tp_d,
                                                                    pCAPs_pSU0_E_Z
                                                                  ), limit=28)
pYPK0_ScFBA1tp_TAL1_ScTDH3tp = circular[0]




#ScTEF1-XK-ScTPI1-XDH-ScPDC1-XR-ScFBA1-TAL1-ScTDH3

ScTEF1tp_EcXK_ScTPI1tp_2  = pcr([primer[167],primer[166]], pYPK0_ScTEF1tp_EcXK_ScTPI1tp)
ScTEF1tp_XK_ScTPI1tp_2    = pcr([primer[167],primer[166]], pYPK0_ScTEF1tp_XK_ScTPI1tp)
ScTPI1tp_XDH_ScPDC1tp_2   = pcr([primer[167],primer[166]], pYPK0_ScTPI1tp_XDH_ScPDC1tp)
ScPDC1tp_XR_ScFBA1tp_2    = pcr([primer[167],primer[166]], pYPK0_ScPDC1tp_XR_ScFBA1tp)
ScFBA1tp_TAL1_ScTDH3tp_2  = pcr([primer[167],primer[166]], pYPK0_ScFBA1tp_TAL1_ScTDH3tp)

sequences, linear = linear_assembly((ScTEF1tp_XK_ScTPI1tp_2,
                                     ScTPI1tp_XDH_ScPDC1tp_2,
                                     ScPDC1tp_XR_ScFBA1tp_2,
                                     ScFBA1tp_TAL1_ScTDH3tp_2), limit=550)

print sequences

sequences, circular = circular_assembly(( linear[0],
                                          pCAPs_pSU0_E_Z),limit=61)

pYPK0 = sync(circular[0], "tcgcgcgtttcggtgatgacggtgaaaacc")

sequences, linear = linear_assembly((ScTEF1tp_EcXK_ScTPI1tp_2,
                                     ScTPI1tp_XDH_ScPDC1tp_2,
                                     ScPDC1tp_XR_ScFBA1tp_2,
                                     ScFBA1tp_TAL1_ScTDH3tp_2), limit=550)

sequences, circular = circular_assembly(( linear[0],
                                          pCAPs_pSU0_E_Z),limit=61)

pYPK1 = sync(circular[0], "tcgcgcgtttcggtgatgacggtgaaaacc")

assert len(pYPK0)        == 14343
assert seguid(pYPK0.seq) == "y7qYLw8mUOrJNcgOh8JIsbYezzE"
assert len(pYPK1)        == 13995
assert seguid(pYPK1.seq) == "lOUiO1MzO3lT2deakf0Gm+pR79E"

from Bio import SeqIO


import random

for feature in pYPK0.features:
    if not "ApEinfo_fwdcolor" in feature.qualifiers.keys():
        color = '#%02x%02x%02x' % (random.uniform(150,255),
                                   random.uniform(150,255),
                                   random.uniform(150,255),)
        feature.qualifiers.update({"ApEinfo_fwdcolor":color})
        color = '#%02x%02x%02x' % (random.uniform(150,255),
                                   random.uniform(150,255),
                                   random.uniform(150,255),)
        feature.qualifiers.update({"ApEinfo_revcolor":color})



SeqIO.write(pYPK0,"pYPK01.gb","gb")

print "done!"

'''
LOCUS       New_DNA                    6 bp ds-DNA     linear       12-DEC-2012
DEFINITION  .
ACCESSION
VERSION
SOURCE      .
  ORGANISM  .
COMMENT
COMMENT     ApEinfo:methylated:1
FEATURES             Location/Qualifiers
     misc_feature    2..5
                     /label=New Feature
                     /ApEinfo_fwdcolor=#acffff
                     /ApEinfo_revcolor=#00ffa8
                     /ApEinfo_graphicformat=arrow_data {{0 1 2 0 0 -1} {} 0}
                     width 5 offset 0
ORIGIN
        1 aaaaaa
//
'''