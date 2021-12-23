#!/usr/bin/env python

"""Nexus file format class.

Extracts phylogenetic information from a NEXUS file. Currently this
class only attempts to extract the 'tree' and 'translate' blocks, 
to pull out newick strings and a dictionary for re-mapping names
from numeric to strings. This can return multiple newick strings
and is thus used for both single and multitree nexus files.
"""

from typing import List, Tuple, Dict
# import re
# mrbayes specific odd branch length format regex
# MB_BRLEN_RE = r"\[&B (\w+) [0-9.e-]+\]"
# MATCHER = re.compile(MB_BRLEN_RE)


def get_newicks_and_translation_from_nexus(
    data: List[str],
    ) -> Tuple[List[str], Dict[int, str]]:
    """Extract newick data and translation dict from a NEXUS file.

    This can parse generic NEXUS formats, and has also been tested
    on the mrbayes format, which has a lot of non-standard formatting
    for metadata, e.g., this removes spaces from mb newicks.
    """
    # vars to be returned
    trans_dict = {}
    newicks = []

    # data SHOULD be a list of strings at this point.
    lines = iter(data)

    # skip over lines until we reach the 'trees' block
    while 1:
        try:
            line = next(lines).strip()
            if line.lower() == "begin trees;":
                break
        except StopIteration:
            break

    # iterate over lines in the tree block to get tree and translate
    while 1:
        nextline = next(lines).strip()

        # remove horrible brlen string with spaces from mb if present
        # nextline = MATCHER.sub("", nextline)

        # split into parts on remaining spaces
        sub = nextline.split()

        # skip if a blank line
        if not sub:
            continue

        # look for 'translate' block inside of 'trees' block
        if sub[0].lower() == "translate":
            while not sub[-1].endswith(";"):                        
                sub = next(lines).strip().split()
                if not sub[-1].endswith(";"):
                    trans_dict[sub[0]] = sub[-1].strip(",").strip(";")

        # parse tree blocks
        elif sub[0].lower().startswith("tree"):
            newicks.append(sub[-1])

        # end of trees block
        elif sub[0].lower() == "end;":
            break
    return newicks, trans_dict



if __name__ == "__main__":

    NEX = """
#NEXUS
[ID: 8147504813]
begin taxa;
    dimensions ntax=30;
    taxlabels
        r0_0
        r10_0
        r11_0
        r12_0
        r13_0
        r14_0
        r15_0
        r16_0
        r17_0
        r18_0
        r19_0
        r1_0
        r20_0
        r21_0
        r22_0
        r23_0
        r24_0
        r25_0
        r26_0
        r27_0
        r28_0
        r29_0
        r2_0
        r3_0
        r4_0
        r5_0
        r6_0
        r7_0
        r8_0
        r9_0
        ;
end;
begin trees;
    translate
        1   r0_0,
        2   r10_0,
        3   r11_0,
        4   r12_0,
        5   r13_0,
        6   r14_0,
        7   r15_0,
        8   r16_0,
        9   r17_0,
        10  r18_0,
        11  r19_0,
        12  r1_0,
        13  r20_0,
        14  r21_0,
        15  r22_0,
        16  r23_0,
        17  r24_0,
        18  r25_0,
        19  r26_0,
        20  r27_0,
        21  r28_0,
        22  r29_0,
        23  r2_0,
        24  r3_0,
        25  r4_0,
        26  r5_0,
        27  r6_0,
        28  r7_0,
        29  r8_0,
        30  r9_0
        ;
   tree con_all_compat = [&R] ((((((((11[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67836987e-06,height_median=7.94000066e-08,height_95%HPD={0.00000000e+00,6.80510000e-06},age_mean=1.67836987e-06,age_median=7.94000066e-08,age_95%HPD={0.00000000e+00,6.80510000e-06}]:3.577141e-03[&length_mean=3.57593349e-03,length_median=3.57586400e-03,length_95%HPD={3.52370300e-03,3.62749200e-03}],13[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67836987e-06,height_median=7.94000066e-08,height_95%HPD={0.00000000e+00,6.80510000e-06},age_mean=1.67836987e-06,age_median=7.94000066e-08,age_95%HPD={0.00000000e+00,6.80510000e-06}]:3.577141e-03[&length_mean=3.57593349e-03,length_median=3.57586400e-03,length_95%HPD={3.52370300e-03,3.62749200e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=3.57761186e-03,height_median=3.57722000e-03,height_95%HPD={3.52717960e-03,3.62989190e-03},age_mean=3.57761186e-03,age_median=3.57722000e-03,age_95%HPD={3.52717960e-03,3.62989190e-03}]:2.553669e-03[&length_mean=2.55232393e-03,length_median=2.55284600e-03,length_95%HPD={2.49653400e-03,2.60812400e-03}],14[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67838318e-06,height_median=7.94000030e-08,height_95%HPD={0.00000000e+00,6.80510000e-06},age_mean=1.67838318e-06,age_median=7.94000030e-08,age_95%HPD={0.00000000e+00,6.80510000e-06}]:6.130810e-03[&length_mean=6.12825741e-03,length_median=6.12852500e-03,length_95%HPD={6.07356400e-03,6.18458900e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=6.12993579e-03,height_median=6.13088900e-03,height_95%HPD={6.07356800e-03,6.18437600e-03},age_mean=6.12993579e-03,age_median=6.13088900e-03,age_95%HPD={6.07356800e-03,6.18437600e-03}]:1.713222e-03[&length_mean=1.71312181e-03,length_median=1.71207800e-03,length_95%HPD={1.66543100e-03,1.77036500e-03}],15[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67838888e-06,height_median=7.94000030e-08,height_95%HPD={0.00000000e+00,6.80410000e-06},age_mean=1.67838888e-06,age_median=7.94000030e-08,age_95%HPD={0.00000000e+00,6.80410000e-06}]:7.844032e-03[&length_mean=7.84137921e-03,length_median=7.84220600e-03,length_95%HPD={7.78507100e-03,7.90093900e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=7.84305760e-03,height_median=7.84411140e-03,height_95%HPD={7.78128800e-03,7.89894100e-03},age_mean=7.84305760e-03,age_median=7.84411140e-03,age_95%HPD={7.78128800e-03,7.89894100e-03}]:1.254925e-03[&length_mean=1.25609338e-03,length_median=1.25602800e-03,length_95%HPD={1.21184200e-03,1.30434300e-03}],(16[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67837082e-06,height_median=7.94000030e-08,height_95%HPD={0.00000000e+00,6.80410000e-06},age_mean=1.67837082e-06,age_median=7.94000030e-08,age_95%HPD={0.00000000e+00,6.80410000e-06}]:5.586956e-03[&length_mean=5.58497121e-03,length_median=5.58582000e-03,length_95%HPD={5.52789900e-03,5.65289000e-03}],17[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67837082e-06,height_median=7.94000030e-08,height_95%HPD={0.00000000e+00,6.80410000e-06},age_mean=1.67837082e-06,age_median=7.94000030e-08,age_95%HPD={0.00000000e+00,6.80410000e-06}]:5.586956e-03[&length_mean=5.58497121e-03,length_median=5.58582000e-03,length_95%HPD={5.52789900e-03,5.65289000e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=5.58664958e-03,height_median=5.58703520e-03,height_95%HPD={5.52368290e-03,5.64809900e-03},age_mean=5.58664958e-03,age_median=5.58703520e-03,age_95%HPD={5.52368290e-03,5.64809900e-03}]:3.512001e-03[&length_mean=3.51250140e-03,length_median=3.51403300e-03,length_95%HPD={3.44846900e-03,3.57752800e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=9.09915098e-03,height_median=9.09903600e-03,height_95%HPD={9.04231400e-03,9.16062900e-03},age_mean=9.09915098e-03,age_median=9.09903600e-03,age_95%HPD={9.04231400e-03,9.16062900e-03}]:3.321345e-03[&length_mean=3.32115212e-03,length_median=3.32170400e-03,length_95%HPD={3.25479100e-03,3.39292900e-03}],(18[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67854572e-06,height_median=8.23999997e-08,height_95%HPD={0.00000000e+00,6.80410000e-06},age_mean=1.67854572e-06,age_median=8.23999997e-08,age_95%HPD={0.00000000e+00,6.80410000e-06}]:1.025155e-02[&length_mean=1.02483493e-02,length_median=1.02498600e-02,length_95%HPD={1.01741900e-02,1.03222200e-02}],19[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67854572e-06,height_median=8.23999997e-08,height_95%HPD={0.00000000e+00,6.80410000e-06},age_mean=1.67854572e-06,age_median=8.23999997e-08,age_95%HPD={0.00000000e+00,6.80410000e-06}]:1.025155e-02[&length_mean=1.02483493e-02,length_median=1.02498600e-02,length_95%HPD={1.01741900e-02,1.03222200e-02}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.02500278e-02,height_median=1.02516371e-02,height_95%HPD={1.01713120e-02,1.03217410e-02},age_mean=1.02500278e-02,age_median=1.02516371e-02,age_95%HPD={1.01713120e-02,1.03217410e-02}]:2.168743e-03[&length_mean=2.17027526e-03,length_median=2.17013200e-03,length_95%HPD={2.11825700e-03,2.23148400e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.24203031e-02,height_median=1.24203805e-02,height_95%HPD={1.23461670e-02,1.24913982e-02},age_mean=1.24203031e-02,age_median=1.24203805e-02,age_95%HPD={1.23461670e-02,1.24913982e-02}]:9.594353e-03[&length_mean=9.59600240e-03,length_median=9.59631600e-03,length_95%HPD={9.47029400e-03,9.69796500e-03}],(20[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67841169e-06,height_median=7.73999993e-08,height_95%HPD={0.00000000e+00,6.81010000e-06},age_mean=1.67841169e-06,age_median=7.73999993e-08,age_95%HPD={0.00000000e+00,6.81010000e-06}]:3.397693e-03[&length_mean=3.39738563e-03,length_median=3.39649200e-03,length_95%HPD={3.34411600e-03,3.45538700e-03}],21[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67841169e-06,height_median=7.73999993e-08,height_95%HPD={0.00000000e+00,6.81010000e-06},age_mean=1.67841169e-06,age_median=7.73999993e-08,age_95%HPD={0.00000000e+00,6.81010000e-06}]:3.397693e-03[&length_mean=3.39738563e-03,length_median=3.39649200e-03,length_95%HPD={3.34411600e-03,3.45538700e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=3.39906404e-03,height_median=3.39777070e-03,height_95%HPD={3.34592500e-03,3.45704400e-03},age_mean=3.39906404e-03,age_median=3.39777070e-03,age_95%HPD={3.34592500e-03,3.45704400e-03}]:1.861696e-02[&length_mean=1.86172415e-02,length_median=1.86172600e-02,length_95%HPD={1.84914500e-02,1.87477000e-02}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=2.20163055e-02,height_median=2.20147332e-02,height_95%HPD={2.19006110e-02,2.21383511e-02},age_mean=2.20163055e-02,age_median=2.20147332e-02,age_95%HPD={2.19006110e-02,2.21383511e-02}]:4.349388e-04[&length_mean=4.31812213e-04,length_median=4.32655900e-04,length_95%HPD={3.07930000e-04,5.49171200e-04}],22[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.67839620e-06,height_median=8.10000031e-08,height_95%HPD={0.00000000e+00,6.80500000e-06},age_mean=1.67839620e-06,age_median=8.10000031e-08,age_95%HPD={0.00000000e+00,6.80500000e-06}]:2.244959e-02[&length_mean=2.24464393e-02,length_median=2.24474900e-02,length_95%HPD={2.23263200e-02,2.25636700e-02}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=2.24481177e-02,height_median=2.24496720e-02,height_95%HPD={2.23273132e-02,2.25687230e-02},age_mean=2.24481177e-02,age_median=2.24496720e-02,age_95%HPD={2.23273132e-02,2.25687230e-02}]:2.338998e+01[&length_mean=2.35408532e+01,length_median=2.33900900e+01,length_95%HPD={2.24790200e+01,2.49217400e+01}],((((((((1[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70284724e-06,height_median=5.79999337e-09,height_95%HPD={0.00000000e+00,6.95510001e-06},age_mean=1.70284724e-06,age_median=5.79999337e-09,age_95%HPD={0.00000000e+00,6.95510001e-06}]:4.620996e-04[&length_mean=4.60380482e-04,length_median=4.60422600e-04,length_95%HPD={4.39606700e-04,4.80731200e-04}],12[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70284724e-06,height_median=5.79999337e-09,height_95%HPD={0.00000000e+00,6.95510001e-06},age_mean=1.70284724e-06,age_median=5.79999337e-09,age_95%HPD={0.00000000e+00,6.95510001e-06}]:4.620996e-04[&length_mean=4.60380482e-04,length_median=4.60422600e-04,length_95%HPD={4.39606700e-04,4.80731200e-04}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=4.62083329e-04,height_median=4.62105400e-04,height_95%HPD={4.40647200e-04,4.82502100e-04},age_mean=4.62083329e-04,age_median=4.62105400e-04,age_95%HPD={4.40647200e-04,4.82502100e-04}]:4.179187e-04[&length_mean=4.17983278e-04,length_median=4.17938500e-04,length_95%HPD={3.90855000e-04,4.46944400e-04}],23[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70284753e-06,height_median=5.70000580e-09,height_95%HPD={0.00000000e+00,6.95510001e-06},age_mean=1.70284753e-06,age_median=5.70000580e-09,age_95%HPD={0.00000000e+00,6.95510001e-06}]:8.800184e-04[&length_mean=8.78363760e-04,length_median=8.78583100e-04,length_95%HPD={8.51509300e-04,9.05177600e-04}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=8.80066607e-04,height_median=8.80024100e-04,height_95%HPD={8.53135000e-04,9.06225200e-04},age_mean=8.80066607e-04,age_median=8.80024100e-04,age_95%HPD={8.53135000e-04,9.06225200e-04}]:1.392625e-03[&length_mean=1.39346313e-03,length_median=1.39355800e-03,length_95%HPD={1.35676900e-03,1.43105800e-03}],24[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70282376e-06,height_median=5.69999870e-09,height_95%HPD={0.00000000e+00,6.95590000e-06},age_mean=1.70282376e-06,age_median=5.69999870e-09,age_95%HPD={0.00000000e+00,6.95590000e-06}]:2.272644e-03[&length_mean=2.27182691e-03,length_median=2.27124900e-03,length_95%HPD={2.23325400e-03,2.30756800e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=2.27352974e-03,height_median=2.27264940e-03,height_95%HPD={2.23540180e-03,2.31111490e-03},age_mean=2.27352974e-03,age_median=2.27264940e-03,age_95%HPD={2.23540180e-03,2.31111490e-03}]:4.620250e-04[&length_mean=4.61125654e-04,length_median=4.61310400e-04,length_95%HPD={4.28894400e-04,4.86921100e-04}],25[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70283631e-06,height_median=6.00000050e-09,height_95%HPD={0.00000000e+00,6.95520000e-06},age_mean=1.70283631e-06,age_median=6.00000050e-09,age_95%HPD={0.00000000e+00,6.95520000e-06}]:2.734668e-03[&length_mean=2.73295255e-03,length_median=2.73287100e-03,length_95%HPD={2.69160200e-03,2.77164000e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=2.73465539e-03,height_median=2.73467440e-03,height_95%HPD={2.69664300e-03,2.77759500e-03},age_mean=2.73465539e-03,age_median=2.73467440e-03,age_95%HPD={2.69664300e-03,2.77759500e-03}]:5.817687e-03[&length_mean=5.81846305e-03,length_median=5.81889000e-03,length_95%HPD={5.75317700e-03,5.88387900e-03}],((26[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70284335e-06,height_median=5.89999871e-09,height_95%HPD={0.00000000e+00,6.95520000e-06},age_mean=1.70284335e-06,age_median=5.89999871e-09,age_95%HPD={0.00000000e+00,6.95520000e-06}]:7.719512e-03[&length_mean=7.71721378e-03,length_median=7.71778300e-03,length_95%HPD={7.66217500e-03,7.77517400e-03}],27[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70284335e-06,height_median=5.89999871e-09,height_95%HPD={0.00000000e+00,6.95520000e-06},age_mean=1.70284335e-06,age_median=5.89999871e-09,age_95%HPD={0.00000000e+00,6.95520000e-06}]:7.719512e-03[&length_mean=7.71721378e-03,length_median=7.71778300e-03,length_95%HPD={7.66217500e-03,7.77517400e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=7.71891662e-03,height_median=7.71951770e-03,height_95%HPD={7.65515150e-03,7.77125090e-03},age_mean=7.71891662e-03,age_median=7.71951770e-03,age_95%HPD={7.65515150e-03,7.77125090e-03}]:4.299567e-04[&length_mean=4.30276403e-04,length_median=4.29855400e-04,length_95%HPD={4.02774800e-04,4.61291900e-04}],28[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70284411e-06,height_median=5.59999691e-09,height_95%HPD={0.00000000e+00,6.95560000e-06},age_mean=1.70284411e-06,age_median=5.59999691e-09,age_95%HPD={0.00000000e+00,6.95560000e-06}]:8.149469e-03[&length_mean=8.14749018e-03,length_median=8.14714500e-03,length_95%HPD={8.09223300e-03,8.20216300e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=8.14919303e-03,height_median=8.14947440e-03,height_95%HPD={8.09217340e-03,8.20265650e-03},age_mean=8.14919303e-03,age_median=8.14947440e-03,age_95%HPD={8.09217340e-03,8.20265650e-03}]:4.028866e-04[&length_mean=4.03925410e-04,length_median=4.03845700e-04,length_95%HPD={3.76679200e-04,4.33503400e-04}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=8.55311844e-03,height_median=8.55236100e-03,height_95%HPD={8.49573800e-03,8.60737600e-03},age_mean=8.55311844e-03,age_median=8.55236100e-03,age_95%HPD={8.49573800e-03,8.60737600e-03}]:1.958388e-03[&length_mean=1.95720740e-03,length_median=1.95791200e-03,length_95%HPD={1.90538400e-03,2.01104300e-03}],29[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70276502e-06,height_median=9.00000074e-09,height_95%HPD={0.00000000e+00,6.95420000e-06},age_mean=1.70276502e-06,age_median=9.00000074e-09,age_95%HPD={0.00000000e+00,6.95420000e-06}]:1.051074e-02[&length_mean=1.05086231e-02,length_median=1.05084500e-02,length_95%HPD={1.04477100e-02,1.05723400e-02}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.05103258e-02,height_median=1.05107490e-02,height_95%HPD={1.04469763e-02,1.05730360e-02},age_mean=1.05103258e-02,age_median=1.05107490e-02,age_95%HPD={1.04469763e-02,1.05730360e-02}]:4.049242e-03[&length_mean=4.05006826e-03,length_median=4.04855200e-03,length_95%HPD={3.97651700e-03,4.12568900e-03}],((((2[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70288308e-06,height_median=5.89999871e-09,height_95%HPD={0.00000000e+00,6.95400000e-06},age_mean=1.70288308e-06,age_median=5.89999871e-09,age_95%HPD={0.00000000e+00,6.95400000e-06}]:1.036496e-03[&length_mean=1.03496615e-03,length_median=1.03515100e-03,length_95%HPD={1.00712600e-03,1.06433900e-03}],30[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70288308e-06,height_median=5.89999871e-09,height_95%HPD={0.00000000e+00,6.95400000e-06},age_mean=1.70288308e-06,age_median=5.89999871e-09,age_95%HPD={0.00000000e+00,6.95400000e-06}]:1.036496e-03[&length_mean=1.03496615e-03,length_median=1.03515100e-03,length_95%HPD={1.00712600e-03,1.06433900e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.03666903e-03,height_median=1.03650210e-03,height_95%HPD={1.00858830e-03,1.06596040e-03},age_mean=1.03666903e-03,age_median=1.03650210e-03,age_95%HPD={1.00858830e-03,1.06596040e-03}]:3.538341e-04[&length_mean=3.53747389e-04,length_median=3.54099000e-04,length_95%HPD={3.29079000e-04,3.78897300e-04}],3[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70285818e-06,height_median=6.00000050e-09,height_95%HPD={0.00000000e+00,6.95420000e-06},age_mean=1.70285818e-06,age_median=6.00000050e-09,age_95%HPD={0.00000000e+00,6.95420000e-06}]:1.390330e-03[&length_mean=1.38871356e-03,length_median=1.38864800e-03,length_95%HPD={1.35890500e-03,1.42138700e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.39041642e-03,height_median=1.39033620e-03,height_95%HPD={1.35921200e-03,1.42227100e-03},age_mean=1.39041642e-03,age_median=1.39033620e-03,age_95%HPD={1.35921200e-03,1.42227100e-03}]:7.895243e-03[&length_mean=7.89591006e-03,length_median=7.89407700e-03,length_95%HPD={7.81753700e-03,7.96743500e-03}],4[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70288859e-06,height_median=6.00000050e-09,height_95%HPD={0.00000000e+00,6.95420000e-06},age_mean=1.70288859e-06,age_median=6.00000050e-09,age_95%HPD={0.00000000e+00,6.95420000e-06}]:9.285573e-03[&length_mean=9.28462360e-03,length_median=9.28391800e-03,length_95%HPD={9.21091200e-03,9.35704500e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=9.28632648e-03,height_median=9.28557900e-03,height_95%HPD={9.21159730e-03,9.35801390e-03},age_mean=9.28632648e-03,age_median=9.28557900e-03,age_95%HPD={9.21159730e-03,9.35801390e-03}]:4.007984e-03[&length_mean=4.00724325e-03,length_median=4.00643400e-03,length_95%HPD={3.94184700e-03,4.08318700e-03}],((5[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70283441e-06,height_median=6.00000050e-09,height_95%HPD={0.00000000e+00,6.95520000e-06},age_mean=1.70283441e-06,age_median=6.00000050e-09,age_95%HPD={0.00000000e+00,6.95520000e-06}]:2.874904e-03[&length_mean=2.87298082e-03,length_median=2.87286800e-03,length_95%HPD={2.82157300e-03,2.92271900e-03}],6[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70283441e-06,height_median=6.00000050e-09,height_95%HPD={0.00000000e+00,6.95520000e-06},age_mean=1.70283441e-06,age_median=6.00000050e-09,age_95%HPD={0.00000000e+00,6.95520000e-06}]:2.874904e-03[&length_mean=2.87298082e-03,length_median=2.87286800e-03,length_95%HPD={2.82157300e-03,2.92271900e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=2.87468365e-03,height_median=2.87491000e-03,height_95%HPD={2.82227700e-03,2.92272400e-03},age_mean=2.87468365e-03,age_median=2.87491000e-03,age_95%HPD={2.82227700e-03,2.92272400e-03}]:9.158060e-03[&length_mean=9.15707397e-03,length_median=9.15662600e-03,length_95%HPD={9.07745100e-03,9.23724400e-03}],7[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70284392e-06,height_median=9.00000430e-09,height_95%HPD={0.00000000e+00,6.95420000e-06},age_mean=1.70284392e-06,age_median=9.00000430e-09,age_95%HPD={0.00000000e+00,6.95420000e-06}]:1.203296e-02[&length_mean=1.20300548e-02,length_median=1.20309700e-02,length_95%HPD={1.19514200e-02,1.21014600e-02}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.20317576e-02,height_median=1.20329700e-02,height_95%HPD={1.19521610e-02,1.21026910e-02},age_mean=1.20317576e-02,age_median=1.20329700e-02,age_95%HPD={1.19521610e-02,1.21026910e-02}]:1.260593e-03[&length_mean=1.26181212e-03,length_median=1.26184100e-03,length_95%HPD={1.21337200e-03,1.31227900e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.32935697e-02,height_median=1.32935630e-02,height_95%HPD={1.32177375e-02,1.33682924e-02},age_mean=1.32935697e-02,age_median=1.32935630e-02,age_95%HPD={1.32177375e-02,1.33682924e-02}]:1.266428e-03[&length_mean=1.26682436e-03,length_median=1.26698800e-03,length_95%HPD={1.21864600e-03,1.31670700e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.45603941e-02,height_median=1.45599910e-02,height_95%HPD={1.44863080e-02,1.46380590e-02},age_mean=1.45603941e-02,age_median=1.45599910e-02,age_95%HPD={1.44863080e-02,1.46380590e-02}]:6.722690e-03[&length_mean=6.72311336e-03,length_median=6.72225000e-03,length_95%HPD={6.61512700e-03,6.82896800e-03}],((8[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70291806e-06,height_median=9.00000074e-09,height_95%HPD={0.00000000e+00,6.95620000e-06},age_mean=1.70291806e-06,age_median=9.00000074e-09,age_95%HPD={0.00000000e+00,6.95620000e-06}]:2.232348e-03[&length_mean=2.23125230e-03,length_median=2.23046000e-03,length_95%HPD={2.18717800e-03,2.27569900e-03}],9[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70291806e-06,height_median=9.00000074e-09,height_95%HPD={0.00000000e+00,6.95620000e-06},age_mean=1.70291806e-06,age_median=9.00000074e-09,age_95%HPD={0.00000000e+00,6.95620000e-06}]:2.232348e-03[&length_mean=2.23125230e-03,length_median=2.23046000e-03,length_95%HPD={2.18717800e-03,2.27569900e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=2.23295522e-03,height_median=2.23235700e-03,height_95%HPD={2.18782000e-03,2.27550700e-03},age_mean=2.23295522e-03,age_median=2.23235700e-03,age_95%HPD={2.18782000e-03,2.27550700e-03}]:6.872550e-03[&length_mean=6.87195982e-03,length_median=6.87307500e-03,length_95%HPD={6.77763100e-03,6.95546500e-03}],10[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=1.70291616e-06,height_median=9.00000074e-09,height_95%HPD={0.00000000e+00,6.95720000e-06},age_mean=1.70291616e-06,age_median=9.00000074e-09,age_95%HPD={0.00000000e+00,6.95720000e-06}]:9.104898e-03[&length_mean=9.10321212e-03,length_median=9.10369100e-03,length_95%HPD={9.01900200e-03,9.20399500e-03}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=9.10491504e-03,height_median=9.10490700e-03,height_95%HPD={9.01120530e-03,9.19671300e-03},age_mean=9.10491504e-03,age_median=9.10490700e-03,age_95%HPD={9.01120530e-03,9.19671300e-03}]:1.217777e-02[&length_mean=1.21785924e-02,length_median=1.21786500e-02,length_95%HPD={1.20719000e-02,1.22809200e-02}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=2.12835075e-02,height_median=2.12826809e-02,height_95%HPD={2.11662870e-02,2.13854000e-02},age_mean=2.12835075e-02,age_median=2.12826809e-02,age_95%HPD={2.11662870e-02,2.13854000e-02}]:2.339115e+01[&length_mean=2.35420178e+01,length_median=2.33911500e+01,length_95%HPD={2.24802100e+01,2.49229100e+01}])[&prob=1.00000000e+00,prob_stddev=0.00000000e+00,prob_range={1.00000000e+00,1.00000000e+00},prob(percent)="100",prob+-sd="100+-0",height_mean=2.35633013e+01,height_median=2.34124308e+01,height_95%HPD={2.25014492e+01,2.49441691e+01},age_mean=2.35633013e+01,age_median=2.34124308e+01,age_95%HPD={2.25014492e+01,2.49441691e+01}][&length_mean=0.00000000e+00,length_median=0.00000000e+00,length_95%HPD={0.00000000e+00,0.00000000e+00}];
end;
"""
    # the TreeParser class would split the string into lines
    DATA = NEX.split("\n")
    print(get_newick_and_translation_from_nexus(DATA))
    