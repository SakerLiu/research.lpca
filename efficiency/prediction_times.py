from datasets import YAGO3_10, WN18RR, WN18, FB15K_237, FB15K
from models import *

# TIMES ARE IN SECONDS

PREDICTION_TIMES_FB15K = {
                ANYBURL: 0.0356,  # obtained a posteriori
                DISTMULT: 0.0033069978311893265,
                COMPLEX: 0.0003304681825877434,
                ANALOGY: 0.00000118555,
                SIMPLE: 0.001187020242214203,
                HOLE: 0.005470062694248303,
                TUCKER: 0.0003905716793244656,
                TRANSE: 0.003278677359396873,
                STRANSE: 0.062753,
                CROSSE: 0.0013039112091064453,
                TORUSE: 0.02541720164078423,
                ROTATE: 0.05567470349763569,
                CONVE: 0.0012242592723164338,
                CONVKB: 0.04948139190673828,
                CONVR: 0.0013225809236367544,
                CAPSE: 0.20796704292297363,
                RSN: 0.0026609593670246963,
                }

PREDICTION_TIMES_WN18 = {
                ANYBURL: 0.006,  # obtained a posteriori
                DISTMULT: 0.003943323230743408,
                COMPLEX: 0.0003445267677307129,
                ANALOGY: 0.00000244094,
                SIMPLE: 0.002852851152420044,
                HOLE: 0.010833172178268433,
                TUCKER: 0.0004132308765333526,
                TRANSE: 0.0035955833435058595,
                STRANSE: 0.050761,
                CROSSE: 0.0016238689422607422,
                TORUSE: 0.049019145506569654,
                ROTATE: 0.038623298917497904,
                CONVE: 0.0015852397897330318,
                CONVKB: 0.1681804656982422,
                CONVR: 0.0014776821931203206,
                CAPSE: 0.17118620872497559,
                RSN: 0.003178550089248503
}

PREDICTION_TIMES_FB15K_237 = {
                ANYBURL: 1.4072119613,
                DISTMULT: 0.003669004184134215,
                COMPLEX: 0.00034103280805014623,
                ANALOGY: 0.000000384398496,
                SIMPLE: 0.0012009495496749878,
                HOLE: 0.0077382882335015925,
                TUCKER: 0.000384125107643651,
                TRANSE: 0.004248693365210341,
                STRANSE: 0.063991,
                CROSSE: 0.0013866424560546875,
                TORUSE: 0.017823028802739324,
                ROTATE: 0.054145270586013795,
                CONVE: 0.0013413627778609135,
                CONVKB: 0.01569080352783203,
                CONVR: 0.0015630913234892345,
                CAPSE: 0.18288111686706543,
                RSN: 0.0025339838803983203
}

PREDICTION_TIMES_WN18RR = {
                ANYBURL: 0.09572431397,
                DISTMULT: 0.005455575465503698,
                COMPLEX: 0.0003307632605234782,
                ANALOGY: 0.00000184057,
                SIMPLE: 0.0028388551870981854,
                HOLE: 0.010864286514052614,
                TUCKER: 0.0005271967121812164,
                TRANSE: 0.005915231238311684,
                STRANSE: 0.050474,
                CROSSE: 0.002019166946411133,
                TORUSE: 0.04940585372990665,
                ROTATE: 0.03787659669851328,
                CONVE: 0.001313240981540797,
                CONVKB: 0.25911450386047363,
                CONVR: 0.0016291208267211915,
                CAPSE: 0.4239077568054199,
                RSN: 0.0023369689456752087
}

PREDICTION_TIMES_YAGO3_10 = {
                ANYBURL: 12.96,
                DISTMULT: 0.021822674405570012,
                COMPLEX: 0.0003343490759531657,
                ANALOGY: 0.00000146525,
                SIMPLE: 0.008047932982444763,
                HOLE: 0.06092171848944898,
                TUCKER: 0.0005583797425639873,
                TRANSE: 0.02363071863740288,
                STRANSE: 7.620921,
                CROSSE: 0.0047855377197265625,
                TORUSE: 5.51,
                ROTATE: 0.056850203564572134,
                CONVE: 0.0013776865220607672,
                CONVKB: 0.3650972843170166,
                CONVR: 0.0015148500601450603,
                CAPSE: 6.081542253494263,
                RSN: 0.003697187515220257
}

PREDICTION_TIMES = dict()
PREDICTION_TIMES[FB15K] = PREDICTION_TIMES_FB15K
PREDICTION_TIMES[FB15K_237] = PREDICTION_TIMES_FB15K_237
PREDICTION_TIMES[WN18] = PREDICTION_TIMES_WN18
PREDICTION_TIMES[WN18RR] = PREDICTION_TIMES_WN18RR
PREDICTION_TIMES[YAGO3_10] = PREDICTION_TIMES_YAGO3_10