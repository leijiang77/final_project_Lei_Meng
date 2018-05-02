import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov


# simulating mono therapy
# create a cohort
cohort_none = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_none = cohort_none.simulate()

# simulating combination therapy
# create a cohort
cohort_mono = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.MONO)
simOutputs_mono = cohort_mono.simulate()
cohort_combo = MarkovCls.Cohort(
    id=2,
    therapy=P.Therapies.COMBO)
# simulate the cohort
simOutputs_combo = cohort_combo.simulate()

# draw survival curves and histograms
#SupportMarkov.draw_survival_curves_and_histograms(simOutputs_mono, simOutputs_combo)

# print the estimates for the mean survival time and mean time to AIDS
SupportMarkov.print_outcomes(simOutputs_none, "STRATEGY 0:")
SupportMarkov.print_outcomes(simOutputs_mono, "STRATEGY 1:")
SupportMarkov.print_outcomes(simOutputs_combo, "STRATEGY 2:")

# print comparative outcomes
#SupportMarkov.print_comparative_outcomes(simOutputs_mono, simOutputs_combo)

# report the CEA results
#SupportMarkov.report_CEA_CBA(simOutputs_mono, simOutputs_combo)



cost_ratio1 = (simOutputs_mono.get_sumStat_discounted_cost().get_mean())/((simOutputs_mono.get_sumStat_discounted_utility().get_mean()-simOutputs_none.get_sumStat_discounted_utility().get_mean()))
cost_ratio2 = (simOutputs_combo.get_sumStat_discounted_cost().get_mean())/((simOutputs_combo.get_sumStat_discounted_utility().get_mean()-simOutputs_none.get_sumStat_discounted_utility().get_mean()))

print("Strategy1:",cost_ratio1)
print("Strategy2:",cost_ratio2)

