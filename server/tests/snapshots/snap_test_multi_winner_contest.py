# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_multi_winner_sample_size 1"] = [
    {"key": "asn", "prob": None, "size": 48}
]

snapshots[
    "test_multi_winner_two_rounds 1"
] = """######## ELECTION INFO ########\r
Organization,Election Name,State\r
Test Org test_multi_winner_two_rounds,Test Election,CA\r
\r
######## CONTESTS ########\r
Contest Name,Targeted?,Number of Winners,Votes Allowed,Total Ballots Cast,Tabulated Votes\r
Contest 1,Targeted,2,1,1000,candidate 1: 600; candidate 2: 300; candidate 3: 100\r
\r
######## AUDIT SETTINGS ########\r
Audit Name,Audit Type,Audit Math Type,Risk Limit,Random Seed,Online Data Entry?\r
Test Audit test_multi_winner_two_rounds,BALLOT_POLLING,BRAVO,10%,1234567890,Yes\r
\r
######## AUDIT BOARDS ########\r
Jurisdiction Name,Audit Board Name,Member 1 Name,Member 1 Affiliation,Member 2 Name,Member 2 Affiliation\r
\r
######## ROUNDS ########\r
Round Number,Contest Name,Targeted?,Sample Size,Risk Limit Met?,P-Value,Start Time,End Time,Audited Votes\r
1,Contest 1,Targeted,48,No,1.0,DATETIME,DATETIME,candidate 1: 24; candidate 2: 14; candidate 3: 10\r
2,Contest 1,Targeted,72,Yes,0.0014064875,DATETIME,DATETIME,candidate 1: 50; candidate 2: 21; candidate 3: 1\r
\r
######## SAMPLED BALLOTS ########\r
Jurisdiction Name,Batch Name,Ballot Position,Ticket Numbers: Contest 1,Audited?,Audit Result: Contest 1\r
J1,1,23,Round 1: 0.026709936196363079,AUDITED,candidate 1\r
J1,1,54,Round 1: 0.048061589358911498,AUDITED,candidate 1\r
J1,1,107,Round 1: 0.003802451161239746,AUDITED,candidate 1\r
J1,2,6,Round 1: 0.028662515227396225,AUDITED,candidate 1\r
J1,2,25,Round 1: 0.023369462249873393,AUDITED,candidate 1\r
J1,2,30,Round 1: 0.028807763145463000,AUDITED,candidate 1\r
J1,2,70,Round 1: 0.032079033020155699,AUDITED,candidate 1\r
J1,2,75,Round 1: 0.035640239666365080,AUDITED,candidate 1\r
J1,3,38,Round 1: 0.018230756390081779,AUDITED,candidate 2\r
J1,3,40,Round 1: 0.014739823561707141,AUDITED,candidate 2\r
J1,3,50,Round 1: 0.001315804865633048,AUDITED,candidate 2\r
J1,3,82,Round 1: 0.046244912686705392,AUDITED,candidate 2\r
J1,3,97,Round 1: 0.000454186428506763,AUDITED,candidate 2\r
J1,3,100,Round 1: 0.000619826143680938,AUDITED,candidate 2\r
J1,3,117,Round 1: 0.026152774099611906,AUDITED,candidate 2\r
J1,3,124,Round 1: 0.048188248088779317,AUDITED,candidate 3\r
J1,4,3,Round 1: 0.010306372247476217,AUDITED,candidate 3\r
J1,4,7,Round 1: 0.042092437205341423,AUDITED,candidate 3\r
J1,4,44,Round 1: 0.042228065622768503,AUDITED,candidate 3\r
J1,4,61,Round 1: 0.054099586219482054,AUDITED,candidate 3\r
J1,4,63,Round 1: 0.003836186945975918,AUDITED,candidate 3\r
J1,4,90,Round 1: 0.032834360453541187,AUDITED,candidate 3\r
J1,4,105,Round 1: 0.023112222444256629,AUDITED,candidate 3\r
J2,1,3,Round 1: 0.026974562209906179,AUDITED,candidate 1\r
J2,1,18,Round 1: 0.014104975821697965,AUDITED,candidate 1\r
J2,1,92,Round 1: 0.052806674901110402,AUDITED,candidate 1\r
J2,1,95,Round 1: 0.016973643141289284,AUDITED,candidate 1\r
J2,1,119,Round 1: 0.049912981083657973,AUDITED,candidate 1\r
J2,1,120,Round 1: 0.047080232298202492,AUDITED,candidate 1\r
J2,2,4,Round 1: 0.044147335849878093,AUDITED,candidate 1\r
J2,2,6,Round 1: 0.011988982664080463,AUDITED,candidate 1\r
J2,2,10,Round 1: 0.045351581516619860,AUDITED,candidate 1\r
J2,2,21,Round 1: 0.033623351422977819,AUDITED,candidate 1\r
J2,2,47,Round 1: 0.027498964298693411,AUDITED,candidate 1\r
J2,2,54,Round 1: 0.045371165761538274,AUDITED,candidate 1\r
J2,2,55,Round 1: 0.050963497467456710,AUDITED,candidate 1\r
J2,2,57,Round 1: 0.041385359143715479,AUDITED,candidate 1\r
J2,2,76,Round 1: 0.008194396580254860,AUDITED,candidate 1\r
J2,2,90,Round 1: 0.044466188247895144,AUDITED,candidate 1\r
J2,2,100,Round 1: 0.010690201994334043,AUDITED,candidate 2\r
J2,3,30,Round 1: 0.042672901163402832,AUDITED,candidate 2\r
J2,3,47,Round 1: 0.040062098731520309,AUDITED,candidate 2\r
J2,3,58,Round 1: 0.045253125083783178,AUDITED,candidate 2\r
J2,3,101,"Round 1: 0.014786076170605607, 0.033699457455768933",AUDITED,candidate 2\r
J2,3,106,Round 1: 0.045266995759010649,AUDITED,candidate 2\r
J2,4,53,Round 1: 0.025265343975139206,AUDITED,candidate 3\r
J2,4,118,Round 1: 0.032998237452482243,AUDITED,candidate 3\r
J1,1,3,Round 2: 0.088404500051420169,AUDITED,candidate 1\r
J1,1,4,Round 2: 0.056455363529765325,AUDITED,candidate 1\r
J1,1,6,Round 2: 0.063938772948313277,AUDITED,candidate 1\r
J1,1,30,Round 2: 0.095685779866665180,AUDITED,candidate 1\r
J1,1,39,Round 2: 0.106266582840628214,AUDITED,candidate 1\r
J1,1,49,Round 2: 0.111726627292736698,AUDITED,candidate 1\r
J1,1,57,Round 2: 0.098173030719660224,AUDITED,candidate 1\r
J1,1,88,Round 2: 0.076055887409616811,AUDITED,candidate 1\r
J1,1,94,Round 2: 0.082214499319451481,AUDITED,candidate 1\r
J1,1,102,Round 2: 0.111156528532090532,AUDITED,candidate 1\r
J1,1,117,Round 2: 0.056348996792332103,AUDITED,candidate 1\r
J1,1,124,Round 2: 0.075774081324570325,AUDITED,candidate 1\r
J1,2,2,Round 2: 0.091912034655946169,AUDITED,candidate 1\r
J1,2,29,Round 2: 0.071025445549972134,AUDITED,candidate 1\r
J1,2,73,Round 2: 0.108526924051470744,AUDITED,candidate 1\r
J1,2,77,Round 2: 0.061243853397465359,AUDITED,candidate 1\r
J1,2,84,Round 2: 0.095975333017344763,AUDITED,candidate 1\r
J1,2,88,Round 2: 0.071804966402309250,AUDITED,candidate 1\r
J1,2,89,Round 2: 0.054646592241035729,AUDITED,candidate 1\r
J1,2,100,Round 2: 0.101396216379465808,AUDITED,candidate 1\r
J1,2,104,Round 2: 0.103436445326700926,AUDITED,candidate 1\r
J1,2,115,Round 2: 0.058845725605483224,AUDITED,candidate 1\r
J1,2,118,"Round 2: 0.091540862184618771, 0.092163080690315387",AUDITED,candidate 1\r
J1,2,119,Round 2: 0.086135177372894679,AUDITED,candidate 1\r
J1,2,120,Round 2: 0.096522009786288950,AUDITED,candidate 1\r
J1,3,2,Round 2: 0.096258425102788892,AUDITED,candidate 1\r
J1,3,11,Round 2: 0.093515621534103985,AUDITED,candidate 1\r
J1,3,84,Round 2: 0.101133216050746816,AUDITED,candidate 1\r
J1,3,106,Round 2: 0.061350998660180108,AUDITED,candidate 2\r
J1,3,121,Round 2: 0.068048811291378543,AUDITED,candidate 2\r
J1,4,5,"Round 2: 0.080704071573746128, 0.099341639942774926",AUDITED,candidate 2\r
J1,4,6,Round 2: 0.104029943609805403,AUDITED,candidate 2\r
J1,4,26,Round 2: 0.074248137323249137,AUDITED,candidate 2\r
J1,4,66,Round 2: 0.096975818551066342,AUDITED,candidate 2\r
J1,4,67,Round 2: 0.091470963043987134,AUDITED,candidate 2\r
J1,4,117,Round 2: 0.082550146523358971,AUDITED,candidate 2\r
J1,4,120,Round 2: 0.075775152592425405,AUDITED,candidate 2\r
J2,1,32,Round 2: 0.093250691492184987,AUDITED,candidate 1\r
J2,1,36,Round 2: 0.100566100382829742,AUDITED,candidate 1\r
J2,1,44,Round 2: 0.089536880024228724,AUDITED,candidate 1\r
J2,1,88,Round 2: 0.061988769962685236,AUDITED,candidate 1\r
J2,1,104,Round 2: 0.073179653163604751,AUDITED,candidate 1\r
J2,2,11,Round 2: 0.076534644403810603,AUDITED,candidate 1\r
J2,2,27,Round 2: 0.103016966040980465,AUDITED,candidate 1\r
J2,2,33,Round 2: 0.092640015650788899,AUDITED,candidate 1\r
J2,2,34,Round 2: 0.065713671814989107,AUDITED,candidate 1\r
J2,2,82,Round 2: 0.067178292177545946,AUDITED,candidate 1\r
J2,2,107,Round 2: 0.062728594392484951,AUDITED,candidate 1\r
J2,3,18,Round 2: 0.069668342793075274,AUDITED,candidate 1\r
J2,3,32,Round 2: 0.089615926764951869,AUDITED,candidate 1\r
J2,3,50,Round 2: 0.108342102764767955,AUDITED,candidate 1\r
J2,3,51,Round 2: 0.096120553260524803,AUDITED,candidate 1\r
J2,3,56,"Round 2: 0.091048982285661053, 0.101378875314002018",AUDITED,candidate 1\r
J2,3,61,Round 2: 0.096604572871094987,AUDITED,candidate 1\r
J2,3,71,Round 2: 0.088124330140694101,AUDITED,candidate 1\r
J2,3,76,Round 2: 0.077988294597998248,AUDITED,candidate 1\r
J2,3,88,Round 2: 0.109322394754273640,AUDITED,candidate 1\r
J2,3,97,Round 2: 0.096444576053280526,AUDITED,candidate 2\r
J2,3,110,Round 2: 0.072858131275512064,AUDITED,candidate 2\r
J2,3,122,Round 2: 0.073465505074563528,AUDITED,candidate 2\r
J2,4,34,Round 2: 0.060816634473886193,AUDITED,candidate 2\r
J2,4,37,Round 2: 0.092786549356518562,AUDITED,candidate 2\r
J2,4,62,Round 2: 0.081027631242719463,AUDITED,candidate 2\r
J2,4,88,Round 2: 0.074151674671897012,AUDITED,candidate 2\r
J2,4,91,Round 2: 0.085323108240190809,AUDITED,candidate 2\r
J2,4,95,Round 2: 0.060503357563847771,AUDITED,candidate 2\r
J2,4,97,Round 2: 0.077496313705379178,AUDITED,candidate 2\r
J2,4,105,Round 2: 0.057001269882451539,AUDITED,candidate 2\r
J2,4,123,Round 2: 0.087663943701822178,AUDITED,candidate 3\r
"""
