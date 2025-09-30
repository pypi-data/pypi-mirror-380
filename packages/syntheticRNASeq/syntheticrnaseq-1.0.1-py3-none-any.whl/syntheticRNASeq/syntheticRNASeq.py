#Import modules

import numpy as np
import pandas as pd
from numpy.random import default_rng

#Classes

class SingleSampleGenerator:
  """
  Generate a single gene expression sample from a Negative Binomial distribution.

  Parameters
  ----------
  number_of_genes : int
    Number of genes (rows) in the simulated dataset.
  neg_binomial_n : float
    Number of successes parameter (n) for the Negative Binomial distribution.
  neg_binomial_p : float
    Success probability parameter (p) for the Negative Binomial distribution.
  seed : int, optional
    Random seed for reproducibility.

  Methods
  -------
  generate_single_sample() -> pd.DataFrame
    Returns a (genes × 1) dataframe of simulated raw counts.
  """

  def __init__(self, number_of_genes: int, neg_binomial_n: float, neg_binomial_p: float, seed: int = 0):
    self.number_of_genes = number_of_genes
    self.n = neg_binomial_n
    self.p = neg_binomial_p
    self.rng = default_rng(seed)

  def generate_single_sample(self) -> pd.DataFrame:
    """Generate a single-sample gene expression dataframe."""

    # Generate raw counts from Negative Binomial distribution
    counts = self.rng.negative_binomial(self.n, self.p, size=self.number_of_genes)

    # Create gene names directly with list comprehension
    gene_names = [f"Gene_{i+1}" for i in range(self.number_of_genes)]

    # Build dataframe (genes × 1 sample)
    df = pd.DataFrame(counts, index=gene_names, columns=["Sample_1"])

    return df

class MultipleSampleGenerator:
  """
  Generate gene expression for multiple samples from a Negative Binomial distribution.

  Parameters
  ----------
  number_of_samples : int
    Number of samples (columns) in the simulated dataset.
  number_of_genes : int
    Number of genes (rows) in the simulated dataset.
  neg_binomial_n : float
    Number of successes parameter (n) for the Negative Binomial distribution.
  neg_binomial_p : float
    Success probability parameter (p) for the Negative Binomial distribution.
  seed : int, optional
    Random seed for reproducibility.

  Methods
  -------
  generate_multiple_sample() -> pd.DataFrame
    Returns a (genes × number_of_samples) dataframe of simulated raw counts.
  """

  def __init__(self, number_of_samples: int, number_of_genes: int, neg_binomial_n: float, neg_binomial_p: float, seed: int = 0):
    self.number_of_samples = number_of_samples
    self.number_of_genes = number_of_genes
    self.n = neg_binomial_n
    self.p = neg_binomial_p
    self.rng = default_rng(seed)

  def generate_multiple_sample(self) -> pd.DataFrame:
    """Generate a single-sample gene expression dataframe."""
    neg_binomial_size = (self.number_of_genes, self.number_of_samples)
    # Generate raw counts from Negative Binomial distribution
    counts = self.rng.negative_binomial(self.n, self.p, size=neg_binomial_size)

    # Create gene names directly with list comprehension
    gene_names = [f"Gene_{i+1}" for i in range(self.number_of_genes)]

    # Build dataframe (genes × number of samples)
    df = pd.DataFrame(counts, index=gene_names, columns=[f"Sample_{n}" for n in range(self.number_of_samples)])

    return df

class ReplicateGenerator:
  """
  Generate technical replicates for a single-sample gene expression dataframe.

  For each gene value in the input dataframe, this class generates replicates
  sampled from a normal distribution centered at the gene’s value (mu),
  with standard deviation = sigma * mu.

  Parameters
  ----------
  normal_distribution_sigma : float
    The scaling factor applied to each gene's value to determine the
    standard deviation of the normal distribution.
  df : pandas.DataFrame
    A dataframe with a single sample (1 column) and genes as rows.
  seed : int, optional
    Random seed for reproducibility.

  Methods
  -------
  get_sample_replicates(n_replicates=2) -> pd.DataFrame
    Returns the original sample with added replicate columns.
  """

  def __init__(self, normal_distribution_sigma: float, df: pd.DataFrame, n_replicates: int = 2, seed: int = 0):
    self.sigma = normal_distribution_sigma
    self.df = df.copy()
    self.rng = default_rng(seed)
    self.n_replicates = n_replicates

  def get_sample_replicates(self) -> pd.DataFrame:
    """Generate replicate samples and return dataframe with replicates attached."""
    values = self.df.iloc[:, 0].to_numpy()

    # vectorized generation of replicates
    mu = values[:, None]
    sigma = (self.sigma * values)[:, None]
    replicates = self.rng.normal(mu, sigma, size=(len(values), self.n_replicates))

    # force positive + integer
    replicates = np.abs(np.round(replicates)).astype(int)

    # build replicate dataframe
    replicate_cols = [f"Replicate_{i+2}" for i in range(self.n_replicates)]
    replicates_df = pd.DataFrame(replicates, index=self.df.index)
    replicates_df = pd.concat([self.df, replicates_df], axis=1)
    replicate_cols = ["Replicate_1"] + replicate_cols
    replicates_df.columns = replicate_cols

    return replicates_df