# Changelog

## 1.6.0 (09.07.2025)

- Adapted and bumped requirements to decopler-py \>=2.0.0 \| PR #178 by
  \@robinfallegger addresses [#179](https://github.com/saezlab/liana-py/issues/179)
- Removed upper Python version requirement [#172](https://github.com/saezlab/liana-py/issues/172) [#170](https://github.com/saezlab/liana-py/issues/170)
- Minor adjustment to SpatialDM Global Moran\'s R description [#176](https://github.com/saezlab/liana-py/issues/176)
- Fix feature name warning logic [#169](https://github.com/saezlab/liana-py/issues/169)
- Use scverse cookiecutter [#180](https://github.com/saezlab/liana-py/issues/180)
- Address count issue with circle plot [#185](https://github.com/saezlab/liana-py/issues/185)

## 1.5.1 (13.02.2025)

- liana will now require Python \>= 3.10
- Removed AnnData upper version restrictions
- Merged PR #161 for numpy2.0 compatibility
- Minor documentation improvements for circle_plot.

## 1.5.0 (17.01.2025)

- New `circle_plot` is now available (Merged #139). Thanks to
  \@WeipengMO.
- Update bivariate metrics to no longer save in place but rather return
  the AnnData
- Issue related to .A for a csr_matrix after a certain scipy version
  #155, #135
- Removed inplace paramter from `li.mt.bivariate` Related to #147. It
  will now by default return an AnnData object.

## 1.4.0 (02.09.2024)

- Now published at Nat Cell Bio.
- Correctly referred to PK tutorial for orthology conversion

\- Added `batch_key` and `min_var_nbatches` to control te way batches
are selected in `li.multi.lrs_to_views`. This might result in minor
differences of how many interactions are considered per view, as I also
changed the order of filtering.

- Changed `max_neighbours` in `li.ut.spatial_neighbors` to be a fixed
  number (default=100), rather than a fraction of the spots as this was
  making RAM explode for large spatial formats.

## 1.3.0 (12.07.2024)

- Minor improvements to documentation, specifically changed to the furo
  theme. Resolved issues with latex not being rendered and plot sizes
  being off.
- An exception will now be reaised if `nz_prop` is too high in
  `li.mt.bivariate`. #121
- Updated MetalinksDB to v0.4.5 (the latest version of the MetalinksDB
  paper), extended to also include production-degradation information.
- Fixed some edgecases where an external `resource` or `interactions`
  can have duplicated entries, also resolving a pandas name index issue
  (#120)
- Added simple tutorial how to process multi-omics and multi-modal (e.g.
  metabolite inference) data with LIANA+. #41 #124

## 1.2.1 (11.06.2024)

- Added +1 to the max_neighbours to account for the spot itself in the
  spatial connectivities.
- Replaced Squidpy\'s neighbourhood graph with liana\'s radial basis
  kernel, but with a fixed number of neighbours for each spot. This does
  not account for edges, but differences are minimal does not require
  squidpy as a dependency. One can easily replace it on demand. (#
  <https://github.com/saezlab/liana-py/issues/112>)
- Fixed Python version range between 3.8 and 3.12 (Merged #112)
- Improved the Differential Expression Vignette be more explicit about
  the causal subnetwork search results (related to #66)

## 1.2.0 (24.05.2024)

\- Added inbuilt orthology conversion functions to convert between
species in the ligand-receptor resources (addressing #76) These include:
`li.rs.get_hcop_orthology` to obtain a dataframe of orthologs from
\[HCOP\](<https://www.genenames.org/tools/hcop/>),
`li.rs.translate_column` to translate a single column in a dataframe,
and `li.rs.translate_resource` as a simple wrapper from the latter
function to be applied on dataframes.

- Merged #109 to address a backward compatibility issue with plotnine\'s
  facets.
- Updated MOFAcell & MOFAtalk tutorials, by making some parameters a bit
  more explicit (#102), and using decoupler\'s association plot to do
  ANOVA + plot metadata associations.
- The mean rank returned by `rank_aggregate` when `aggregate_metod` =
  \'mean\' is now normalized by the total number of interactions.
- Fixed a minor logic issue when calculating analytical p-values for
  Moran\'s R

## 1.1.0 (12.04.2024)

- Added a check for the subset of cell types in li.multi.dea_to_lr.
  Related to #92.
- Split Local and Global Bivariate metrics. Specifically, I reworked
  completely the underlying code, though the API should remain
  relatively unchanged. With the exceptions of: 1) `lr_bivar` is now
  removed and `bivar` has been renamed to `bivariate`. This allowed me
  to remove a lot of redundancies between the two functions. 2)
  `nz_threshold` has been renamed to `nz_prop` for consistency with
  `expr_prop` in the remainder of the package. Related to #44.
- `li.mt.bivariate` parameter `mod_added` has been renamed to
  `key_added` due to this now refer to both `.obsm` and `.mod` -
  depedening whether an AnnData or MuData object is passed.
- Added Global \[Lee\'s
  statistic\](<https://onlinelibrary.wiley.com/doi/abs/10.1111/gean.12106>),
  along with a note on weighted product that upon z-scaling it is
  equivalent to Lee\'s local statistic.
- The Global \[L
  statistic\](<https://onlinelibrary.wiley.com/doi/abs/10.1111/gean.12106>)
  and Global \[Moran\'s
  R\](<https://www.nature.com/articles/s41467-023-39608-w>) are
  themselves basically identical. See Eq.22 from Lee and Eq.1 in Supps
  of SpatialDM.
- Changed the `li.mt.bivar` parameter `function_name` to `local_name`
  for consistency and to avoid ambiguity with the newly-added
  `global_name` parameter.
- Added `bumpversion` to manage versioning. Related to #73.
- Added `max_runs` and `stable_runs` parameters to enable the inference
  of robust causal networks with CORNETO. Related to #82.
- Optimized MISTy such that the matrix multiplication by weights is done
  only once, rather than for each target. Users can now obtain the
  weighted matrix via the `misty.get_weighted_matrix` function.
- MISTy models are now passed externally, rather than being hardcoded.
  This allows for more flexibility in the models used. As an example, I
  also added a RobustLinearModel from statsmodels. Related to #74.
- Removed forced conversion to sparse csr_matrix matrices in MISTy.
  Related to #57.

## 1.0.5 (25.02.2024)

- Added ScSeqComm Method, implemented by \@BaldanMatt (#68)

\- Added functions to query a metabolite-receptor interactions database
(\[MetalinksDB\](<https://github.com/biocypher/metalinks>)), including:
=\> `li.rs.get_metalinks` to get the database =\>
`li.rs.get_metalinks_values` to get the distinct annotation values of
the database =\> `describe_metalinks` to get a description of the
database

- Added a metabolite-mediated CCC tutorial in spatially-resolved
  multi-omics data (#45).
- Changed hardcoded constants to be defined in
  [constants.py]{#constants.py}
- Excluded CellChat from the default `rank_aggregate` method
- Fixed return logic of SpatialBivariate
- `li.mt.process_scores` is now exported to `li.mt`
- Changed the default `max_neighbours` in `li.ut.spatial_neighbors` to
  1/10 of the number of spots.

## 1.0.4 (17.01.2024)

- Moved the Global score summaries of `SpatialBivariate` from .uns to
  .var
- `df_to_lr` will now also return the expression and proportion of
  expression for the interactions
- `li.multi.nfm` will now also accept a DataFrame as input
- Filtered putative interactions in the Consensus resource, mostly such
  coming from CellTalkDB.
- Changed `filter_lambda` parameter to `filter_fun` for consistency and
  now any function can be passed to be applied as a row-wise filter.
- Global results of `SpatialBivariate` will now be saved to `.var`
- Added `li.ut.interpolate_adata` utility function to interpolate the
  data to a common space.
- MISTy will also work with directly non-aligned data with spatial
  connectivities from one modality to the other being passed via `obsm`
  rather than `obsp`. Making use of `li.ut.spatial_neighbors` by passing
  reference coordinates.
- Fixed a bug where `li.ut.obsm_to_adata` would assign var as a method
  rather than DataFrame
- Fixed a bug where p-values for Global Moran\'s were not calculated
  correctly.
- Enabled `cell_pairs` of interest to be passed to single-cell methods.
- Enabled Parallelization of Permutation-based methods.
- Local categories will now be only calculated for positive interactions
  (not non-ambigous as before).
- Names of source and target panels can now be passed to
  `li.pl.tileplot`.
- `li.rs.explode_complexes` is now consistently exported to `li.rs` (as
  previous versions)
- `li.mt.find_causalnet`: changed the noise assigned to nodes to be
  proportional to the minimum penalty of the model. Also, added noise to
  the edges to avoid multiple solutions to the same problem.

## 1.0.3 (06.11.2023)

- Added `filterby` and `filter_lambda` parameters to
  `li.pl.interactions` and `li.pl.target_metrics` to allow filtering of
  interactions and metrics, respectively.
- Removed unnecessary `stat` parameter from `li.pl.contributions`
- Added tests to ensure both `lr_bivar` and single-cell methods throw an
  exception when the resource is not covered by the data.
- `estimate_elbow` will add the errors and the number of patterns to
  `.uns` when inplace is True.
- When `groupby` or `sample_key` are not categorical liana will now
  print a warning before converting them to categorical. Related to #28
- Various documentation improvements, including using `docrep` to ensure
  consistency.
- `__version__` will now correctly reflect the version in pyproject.toml
- Exported repeated value definitions to `_constants.py`
- Renamed some `*_separator` columns to `*_sep` for consistency.
- Added `li.ut.query_bandwidth` to query the bandwidth of the spatial
  connectivities (used in spatial bivariate tutorial)
- Added **pre-commit** hooks adapted from scverse\'s cookiecutter.

## 1.0.2 (13.10.2023)

- Added as `seed` param to `find_causalnet`, used to a small amount of
  noise to the nodes in to avoid obtaining multiple solutions to the
  same problem when multiple equal solutions are possible.
- Updated `installation.rst` to refer to `pip install liana[common]` and
  `liana[full]` for extended installations.
- Fixed a bug which would cause `bivar` to crash when an AnnData object
  was passed

Merged #61 including the following:

- Added `standardize` parameter to spatial_neighbors, used to
  standardize the spatial connectivities such that each spot\'s
  proximity weights to 1. Required for non-standardized metrics (such as
  `product`)
- Fixed edge case in `assert_covered` to handle interactions not present
  in `adata` nor the resource.

\- Added simple product (scores ranging from -inf, +inf) and
norm_product (scores ranging from -1, +1). The former is a simple
product of x and y, while the latter standardized each variable to be
between 0 and 1, following weighing by spatial proximity, and then
multiplies them. Essentially, it diminishes the effect of spatial
proximity on the score, while still taking it into account. We observed
that this is useful for e.g. border zones.

## 1.0.1 Stable Release (30.09.2023)

- Bumped CORNETO version and it\'s now installed via PyPI.

## 1.0.0a2 (19.09.2023)

- Interactions names in `tileplot` and `dotplot` will now be sorted
  according to `orderby` when used; related to #55
- Added `filter_view_markers` function to filter view markers considered
  background in MOFAcellular tutorial
- Added `keep_stats` parameter to `adata_to_views` to enable pseudobulk
  stats to be kept.
- Replace `intra_groupby` and `extra_groupby` with `maskby` in misty.
  The spots will now only be filtered according to `maskby`, such that
  both intra and extra both contain the same spots. The extra views are
  multiplied by the spatial connectivities prior to masking and the
  model being fit
- Merge MOFAcell improvements; related to #42 and #29
- Targets with zero variance will no longer be modeled by misty.
- Resolve #46 - refactored misty\'s pipeline
- Resolved logging and package import verbosity issues related to #43
- Iternal .obs\[\'label\'\] placeholder renamed to the less generic
  .obs\[\'@label\'\]; related to #53
- Minor Readme & tutorial text improvements.

## 1.0.0a1 Biorxiv (30.07.2023)

- `positive_only` in bivariate metrics was renamed to `mask_negatives`
  will now mask only negative-negative/low-low interactions, and not
  negative-positive interactions.
- Replaced MSigDB with transcription factor activities in MISTy\'s
  tutorial
- Enable sorting according to ascending order in misty-related plots
- Enable `cmap` to be passed to tileplot & dotplots
- Minor Readme & tutorial improvements.

## 1.0.0a0 (27.07.2023)

LIANA becomes LIANA+.

Major changes have been made to the repository, however the API visible
to the user should be largely consistent with previous versions, except
minor exceptions: - `li.fun.generate_lr_geneset` is now called via
`li.rs.generate_lr_geneset`

- the old \'li.funcomics\' model is now renamed to something more
  general: `li.utils`
- `get_factor_scores` and `get_variable_loadings` were moved to
  `li.utils`

LIANA+ includes the following new features:

### Spatial

- A sklearn-based implementation to learn spatially-informed multi-view
  models, i.e.
  \[MISTy\](<https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02663-5>)
  models.
- A new tutorial that shows how to use LIANA+ to build and run MISTy
  models.
- Five vectorized local spatially-informed bivariate clustering and
  similarity metrics, such as \[Moran\'s
  R\](<https://www.biorxiv.org/content/10.1101/2022.08.19.504616v1.full>),
  Cosine, Jaccard, Pearson, Spearman. As well as a numba-compiled
  \[Masked
  Spearman\](<https://www.nature.com/articles/s41592-020-0885-x>) local
  score.

\- A new tutorial that shows how to use LIANA+ to compute
spatially-informed bivariate metrics, permutations-based p-values,
interaction categoriez, as well as how to summarize those into patterns
using NMF.

\- A radial basis kernel is implemented to calculate spot/cell
connectivities (spatial connectivities); this is used by the
spatially-informed bivariate metrics and MISTy. It mirrors
\[squidpy\'s\](<https://squidpy.readthedocs.io/en/stable/>)
`sq.gr.spatial_neighbors` function, and is hence interchangeable with
it.

### Handling multiple modalities

\- LIANA+ will now work with multi-modal data, i.e. it additionally
support MuData objects as well as AnnData objects. The API visible to
the user is the same, but the underlying implementation is different.

- These come with a new tutorial that shows how to use LIANA+ with
  multi-modal (CITE-Seq) data, along with inbuilt transformations.
- The same API is also adapted by the local bivariate metrics, i.e. they
  can also be used with multi-modal data.

### Multi-conditions

\- A utility function has been added that will take any dataframe with
various statistics and append it to information from AnnData objects;
thus creating a multi-condition dataframe in the format of LIANA.

- A new tutorial that shows how to use PyDESeq2 together with this
  utility function has been added, essentially a tutorial on
  \"Hypothesis-driven CCC\".

### Visualizations

- A tileplot (`li.pl.tileplot`) has been added to better visualize
  ligands and receptors independently.
- MISTy-related visualizations have been added to vislualize view
  contributions and performance, and interaction
  coefficients/importances.
- A simple plot `li.pl.connectivity` is added to show spatial
  connectivities

### Others

- A Causal Network inference function has been added to infer downstream
  signalling networks. This is currently placed in the tutorial with
  PyDESeq2.
- An elbow approximation approach has been added to the NMF module, to
  help with the selection of the number of patterns.
- Various utility functions to simplify AnnData extraction/conversion,
  Matrix transformations, etc (added to `li.ut`)

Note: this is just an overview of the new features, for details please
refer to the tutorials, API, and documentation.

## 0.1.9 (06.06.2023)

- Fixed issues with deprecated params of pandas.DataFrame.to_csv &
  .assert_frame_equal in tests
- `multi.get_variable_loadings` will now return all factors
- Added source & target params to `fun.generate_lr_geneset`

\- Refactored `sc._Method._get_means_perms` & related scoring functions to be more efficient.

:   `None` can now be passed to n_perms to avoid permutations - these
    are only relevant if specificity is assumed to be relevant.

- LIANA\'s aggregate method can now be customized to include any method
  of choice (added an example to basic_usage).
- Removed \'Steady\' aggregation from rank_aggregate
- Changed deprecated np.float to np.float32 in `liana_pipe`, relevant
  for CellChat `mat_max`.
- Method results will now be ordered by magnitude, if available, if not
  specificity is used.
- Added `ligand_complex` and `receptor_complex` filtering to liana\'s
  dotplot
- MOFAcellular will now work only with decoupler\>=1.4.0 which
  implements edgeR-like filtering for the views.

## 0.1.8 (24.03.2023)

- Removed walrus operator to support Python 3.7
- Added a tutorial that shows the repurposed use of MOFA with liana to
  obtain intercellular communication programmes, inspired by
  Tensor-cell2cell
- Added a tutorial that shows the repurposed use of MOFA to the analysis
  of multicellular programmes as in Ramirez et al., 2023
- Added `key_added` parameter to save liana results to any
  `adata.uns``slot, and`uns_key`to use liana results from any`adata.uns\`\`
  slot
- `inplace` now works as intended (i.e. only writes to `adata.uns` if
  `inplace` is True).

## 0.1.7 (08.02.2023)

- Fixed an edge case where subunits within the same complex with
  identical values resulted in duplicates. These are now arbitrarily
  removed according to random order.
- All methods\' complexes will now be re-assembled according to the
  closest stat to expression that each method uses, e.g. `cellchat` will
  use `trimeans` and the rest `means`.
- Added a basic liana to Tensor-cell2cell tutorial as a solution to
  liana issue #5
- Updated the basic tutorial
- Referred to CCC chapter from Theis\' best-practices book

## 0.1.6 (23.01.2023)

- Fixed issue with duplicate subunits for non-expressed LRs when
  `return_all_lrs` is True
- `min_prop` when working with `return_all_lrs` is now filled with 0s
- Added `by_sample` function to class Method that returns a long-format
  dataframe of ligand-receptors, for each sample
- Added `dotplot_by_sample` function to visualize ligand-receptor
  interactions across samples
- Refractored preprocessing of `dotplot` and `dotplot_by_sample` to a
  separate function
- Changed \"pvals\" of geometric_mean method to \"gmean_pvals\" for
  consistency
- `to_tensor_c2c` utility function to convert a long-format dataframe of
  ligand-receptor interactions by sample to Tensor-cell2cell tensor.
- Added a list to track the instances of `MethodMeta` class
- Added `generate_lr_geneset` function to generate a geneset of
  ligand-receptors for different prior knowledge databases

## 0.1.5 (11.01.2023)

- Hotfix `return_all_lrs` specificity_rank being assigned to NaN
- Add test to check that `specificity_rank` of `lrs_to_keep` is equal to
  min(specificity_rank)

## 0.1.4 (11.01.2023)

- `rank_aggregate` will now sort interactions according to
  `magnitude_rank`.
- Fixed `SettingWithCopyWarning` warning when `return_all_lrs` is True
- Minor text improvements to the basic tutorial notebook
- Removed \'Print\' from a verbose print message in `_choose_mtx_rep`

## 0.1.3 (07.12.2022)

- Added `supp_columns` parameter to allow any column from liana to be
  returned.
- Added `return_all_lrs` parameter to allow all interactions to be
  returned with a `lrs_to_filter` flag for the interaction that do not
  pass the `expr_prop`, and each of those interactions is assigned to
  the worst **present** score from the ones that do pass the threshold.
- Fixed a bug where an exception was not thrown by `assert_covered`
- Raise explicit exceptions as text in multiple places.
- Changed cellphonedb p-values column name from \"pvals\" to
  \"cellphone_pvals\".

## 0.1.2

- Added CellChat and GeometricMean methods

## 0.1.1

- Add progress bar to permutations
- Deal with adata copies to optimize RAM
- change copy to inplace, and assign to uns, rather than return adata
- remove unnecessary filtering in [pre]{#pre} + extend units tests

## 0.1.0

- Restructure API further
- Submit to PIP

## 0.0.3

- Added a filter according to `min_cells` per cell identity
- prep_check_adata will now assert that `groupby` exists
- extended test_pre.py tests
- restructured the API to be more scverse-like

## 0.0.2

- Added `dotplot` as a visualization option
- Added `basic_usage` tutorial

## 0.0.1

First release alpha version of **liana-py**

-

  Re-implementations of:

  :   - CellPhoneDB
      - NATMI
      - SingleCellSignalR
      - Connectome
      - logFC
      - Robust aggregate rank

- Ligand-receptor resources as generated via OmniPathR.
