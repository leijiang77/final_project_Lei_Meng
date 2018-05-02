
# simulation settings
POP_SIZE = 1000     # cohort population size
SIM_LENGTH = 20    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

ADD_BACKGROUND_MORT = False  # if background mortality should be added
DELTA_T = 1       # years

PSA_ON = False      # if probabilistic sensitivity analysis is on

# transition matrix

STR_0_MATRIX = [
    [0.891684,  0,    0,    0.097, 0.011316],   # CD4_200to500
    [0,     0,    0,  0,  1],   # CD4_200
    [0,     0,      0, 0, 1],
    [0,     0,      0,      0.9879, 0.0121]# AIDS
    ]

STR_1_MATRIX = [
    [0, 0.16006, 0.731624, 0.097, 0.011316],  # CD4_200to500
    [0, 0.959882, 0, 0.02841, 0.011708],  # CD4_200
    [0, 0, 0.959196, 0.02988, 0.010924],  # AIDS
    [0, 0, 0, 0.9879, 0.0121],

]





STR_2_MATRIX = [
    [0, 0.0832, 0.647504, 0.25798, 0.011316],  # CD4_200to500
    [0, 0.959882, 0, 0.02841, 0.011708],  # CD4_200
    [0, 0, 0.959196, 0.02988, 0.010924],  # AIDS
    [0, 0, 0, 0.9879, 0.0121],

]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0,   # CD4_200to500
    600,   # CD4_200
    0,
    0
    # AIDS
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1,   # CD4_200to500
    0.7,   # CD4_200
    1,
    0.68,
    0# AIDS
    ]

# annual drug costs
Zidovudine_COST = 0
Lamivudine_COST = 0

# treatment relative risk
#TREATMENT_RR = 0.509
#TREATMENT_RR_CI = 0.365, 0.71  # lower 95% CI, upper 95% CI

# annual probability of background mortality (number per year per 1,000 population)
#ANNUAL_PROB_BACKGROUND_MORT = 8.15 / 1000

