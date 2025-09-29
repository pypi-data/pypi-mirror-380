# **syntheticRNASeq**

## **Introduction**
syntheticRNASeq is a python package that allows generation of synthetic RNA-Sequencing data by sampling a negative binomial distribution.
The output of the generators are pandas data frames with genes in rows and samples in columns.

## **Usage**

Install and import the module:

```
!pip install syntheticRNASeq 
import syntheticRNASeq as synRNA
from synRNA import SingleSampleGenerator, ReplicateGenerator, MultipleSampleGenerator
```

### **Generation of a single sample**

To create a single sample we will use the *SingleSampleGenerator* class and call the *generate_single_sample* function:

```
single_sample = SingleSampleGenerator(number_of_genes = 60_000,
									  neg_binomial_n = 0.5,
									  neg_binomial_p = 0.05,
									  seed = 0)
single_sample = single_sample.generate_single_sample()
```

### **Generation of a replicates from a single sample**

To create triplicates from a single sample created from the above function we will use the *ReplicateGenerator* class and call the *get_sample_replicates* function:

```
replicates = ReplicateGenerator(normal_distribution_sigma = 1,
								df = single,
								seed = 0)
replicates = replicates.get_sample_replicates()
```

### **Generation of multiple samples**

To create multiple sample we will use the *MultipleSampleGenerator* class and call the *generate_multiple_sample* function:

```
multiple_samples = MultipleSampleGenerator(number_of_samples = 3,
										   number_of_genes = 60_000,
										   neg_binomial_n = 0.5,
										   neg_binomial_p = 0.05,
										   seed = 0)
multiple_samples = multiple_samples.generate_multiple_sample()
```


### **GitHub**

https://github.com/ttkaralis/syntheticRNASeq

