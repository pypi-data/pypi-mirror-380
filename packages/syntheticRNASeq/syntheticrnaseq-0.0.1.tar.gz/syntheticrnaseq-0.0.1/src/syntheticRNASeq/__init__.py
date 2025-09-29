# __init__.py

from syntheticRNASeq import SingleSampleGenerator, MultipleSampleGenerator, ReplicateGenerator


single_sample = SingleSampleGenerator(number_of_genes = 60_000,
									  neg_binomial_n = 0.5,
									  neg_binomial_p = 0.05,
									  seed = 0)
single_sample = single_sample.generate_single_sample()
