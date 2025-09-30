"""Comparison of multiple clustering results."""

from clustools.pairwise.agreement import coassociation_matrix, pairwise_ari_matrix
from clustools.pairwise.distances import overlap_distance_matrix
from clustools.pairwise.summary import ari_summary

__all__ = ["ari_summary", "coassociation_matrix", "overlap_distance_matrix", "pairwise_ari_matrix"]
