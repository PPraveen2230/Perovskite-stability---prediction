This project work is about predicting perovskite stability  using tolerance factor which can be learned from machine learning models
# Perovskites and the Goldschmidt tolerance factor

Perovskites constitute a class of materials having the basic formula $ABX_3$ and displaying a common structure in which a smaller metal cation $B$ (e.g. a transition metal) resides in corner-sharing octahedra of $X$ anions (e.g. $O^{2-}$, $Cl^-$, $Br^-$) and a larger $A$ metal cation (e.g. alkali, alkaline earth or lanthanide) has a 12-fold coordination with the $X$ anions. This class of compounds has a remarkable variety of electronic, magnetic, optical, mechanical, and transport properties. Such variety is derived from the possibility of tuning the materials propertites by the composition. About 90% of the metallic chemical elements of the periodic table can be stabilized in a perovskite structure. Therefore, perovskites are versatile materials suitable for a number of applications including photovoltaics, thermoelectrics and catalysis. 

The first step to design new perovskites is to assess their stability. For this purpose, the Goldschmidt tolerance factor, $t$, has been extensively used to predict the stability of a material in the perovskite structure based on the (Shannon) ionic radii,$r_i$, of each ion $(A,B,X)$ in the chemical formula $ABX_3$: 

$$ t=\frac{r_A+r_X}{\sqrt2(r_B+r_X)} $$

$t$ measures how much the $A$-site cation fits into the corner-sharing octahedral network in a cubic crystal structure. It indicates the compatibilty of a given set of ions with the ideal, cubic perovskite structure ($t\approx1$). Distortions from the cubic structure arise from size mismatch between cations and anions, which results in perovskite structures other than cubic (e.g. orthorhombic, rhombohedral). However, when these distortions are too large, the perovskite structure may be unstable and non-perovskites structures are rather formed.

The accuracy of the Goldschmidt factor is, however, often insufficient to screen for new potential materials and several modification have been proposed to overcome this issue. In this tutorial, we show how data can be used to derive tolerance factors for perovskite stability. 

This dataset is collected based on the following publication:

<div style="padding: 1ex; margin-top: 1ex; margin-bottom: 1ex; border-style: dotted; border-width: 1pt; border-color: blue; border-radius: 3px;">
C. Bartel, C. Sutton, B. R. Goldsmith, R. Ouyang, C. B. Musgrave, Luca M. Ghiringhelli, M. Scheffler: <span style="font-style: italic;">New tolerance factor to predict the stability of perovskite oxides and halides</span>, Sci. Adv.  5, eaav0693 (2019) <a href="https://advances.sciencemag.org/content/advances/5/2/eaav0693.full.pdf" target="_blank">[PDF]</a> .
</div>

Some scripts and data tables for this notebook have been adapted from the content of: 
<div style="padding: 1ex; margin-top: 1ex; margin-bottom: 1ex; border-style: dotted; border-width: 1pt; border-color: blue; border-radius: 3px;">
<a href="https://github.com/CJBartel/perovskite-stability" target="_blank">https://github.com/CJBartel/perovskite-stability</a> 
</div>

