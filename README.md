All .py files on the main folder of the repository, as well as hyperparameter files in hparams, are taken/modified from [recipes/VoxCeleb](https://github.com/speechbrain/speechbrain/tree/develop/recipes/VoxCeleb).

The veritest folder contains the official VoxCeleb verification list (veri_test2.txt), as well as new verification lists (gender_pairs) containing verification pairs by gender, taken from veri_test2.txt

An EER of 6.10% was obtained training xvectors with a reduced subset of VoxCeleb1, and verifying with PLDA trained with VoxCeleb1.
