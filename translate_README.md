# License
 Copyright 2019
 Code by		**Simone Marini**,
 			**Francesca Vitali**,
 			**Andrea Demartini**,
    			and
			**Daniele Pala**.

 This file is part of "Matrix trifactorization for discovery of data similarity and association".

 Matrix trifactorization for discovery of data similarity and association" is free software: you
 can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 "Matrix trifactorization for discovery of data similarity and association" is distributed in
 the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with "Matrix trifactorization for discovery of data similarity and association"

If not, see <http://www.gnu.org/licenses/>.

"Matrix trifactorization for discovery of data similarity and association" is free software: you
can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

"Matrix trifactorization for discovery of data similarity and association" is distributed in
the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with "Matrix trifactorization for discovery of data similarity and association"
If not, see <http://www.gnu.org/licenses/>.

#  发现数据相似性和关联的矩阵三因子化

该算法预测关系矩阵的元素之间的新颖关联或相似性。 例如，给定本体或关系数据集，例如元组或关联元素，它推断出从数据模式中出现的隐式关系。

数据按数据类型分组，例如 患者，基因，蛋白质或途径。 矩阵用于表示不同或相同数据类型的元素之间的关系（关联），例如，关系可以是基因共表达，基因或蛋白质相互作用，疾病之间的关系等。 

该方法基于受约束的联合矩阵三因子分解，其灵感来自M.Zitnik和B.Zupan，“Data fusion by matrix factorization”，IEEE Transactions on Pattern Analysis＆Machine Intelligence 37（1），2015中描述的算法。

在其原型形式中，它被用于：“基于网络的数据集成方法，以支持三重Negativ乳腺癌中的药物再利用和多靶点治疗”，PloS one 11（9），2016。

# Cite
If you use this code in your research work, please cite:
1. [Marini, S., et al. "Protease target prediction via matrix factorization." Bioinformatics (2018).](https://doi.org/10.1093/bioinformatics/bty746)
2. [Vitali, F., et al. "Patient similarity by joint matrix trifactorization to identify subgroups in acute myeloid leukemia." JAMIA Open (2018).](https://doi.org/10.1093/jamiaopen/ooy008)

# Applications

#### 蛋白质-蛋白酶靶标的研究

该项目旨在发现人类蛋白酶的新蛋白质靶标。It leverages on [BioGRID](https://thebiogrid.org/), [KEGG](http://www.genome.jp/kegg/pathway.html), [STRING](https://string-db.org/), [3did](https://3did.irbbarcelona.org/), [Domine](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2238965/), [MEROPS](https://www.ebi.ac.uk/merops/), [UniProt](http://www.uniprot.org/), and [Interpro](https://www.ebi.ac.uk/interpro/).

[数据和参数](protease_target).

More here: [Marini, S., et al. "Protease target prediction via matrix factorization." Bioinformatics (2018).](https://doi.org/10.1093/bioinformatics/bty746).

#### 应用：患者在精确肿瘤学中的相似性。
该项目是基于TCGA AML计算患者相似度，与公共工具/存储库集成，namely [DisGeNET](http://www.disgenet.org/web/DisGeNET/menu), [BioGRID](https://thebiogrid.org/), [KEGG](http://www.genome.jp/kegg/pathway.html), [Disease Ontology](http://disease-ontology.org/), and [PaPI](http://papi.unipv.it/).

[数据和参数](Patient_similarity_TCGA).

More here: [Vitali, F., et al. "Patient similarity by joint matrix trifactorization to identify subgroups in acute myeloid leukemia." JAMIA Open (2018).](https://doi.org/10.1093/jamiaopen/ooy008)


# Quick start

## 在玩具示例上运行算法
1. 在命令行上运行`main`
2. 输入项目目录名称“Test_example”
3. 利润

## 对您的数据运行算法

1. 准备（pair，value）格式的数据为`csv`文件（详见下文，[运行算法]（＃running-the-algorithm））
2. 在`parameters.m`文件中设置参数
3. 运行`get_mats_from_PV.m`
3. 运行`main.m`
4. 利润

# User manual 贡献者
Manual by **Simone Marini**.

Contributions by **Daniele Pala** and **Giovanna Nicora**.

## 目标Goal

该软件预测元素之间的新颖关联或相似性，即，给定本体或关系数据集，例如元组或相关元素，它推断出从数据模式中出现的隐式关系。 数据按对象类型分组，例如 患者，基因，蛋白质或途径。 矩阵用于表示不同或相同对象类型的元素之间的关系（关联）。 例如，关系可以是基因共表达，基因或蛋白质相互作用，疾病之间的关系等。 该算法基于约束联合矩阵三因子分解，其灵感来自M.Zitnik和B.Zupan所描述的算法，“Data fusion by matrix factorization”，IEEE Transactions on Pattern Analysis＆Machine Intelligence 37（1），2015; 和F.维塔利等人。 “基于网络的数据集成方法，支持三阴性乳腺癌中的药物再利用和多靶点治疗”，PloS one 11（9），2016。

## _D_ and _S_ mode

该算法的目标是揭示

+  __different(D)__数据类型之间的关系，例如患者和疾病（诊断）患者和生存率（预测）

+ __same(S)__数据类型之间的关系，如蛋白质（相互作用发现）或患者（患者相似度计算）

这两种模式将产生不同的输出，如第7节所述。

本手册的目的是描述代码的工作原理。 在上述文献中解释了该算法背后的概念

## Language
This software is developed in Matlab 2018a.

## Folder organization

### Main Folder

主文件夹包含算法主脚本以及附加文档，包括本手册。 其他文件夹是项目特定的，即它们托管涉及该算法应用的项目的数据和参数。 在“Test_example”文件夹中提供了一个现成的玩具示例。

+ `main.m` 运行算法
+ `find_new_relations.m` 计算一致性矩阵
+ `get_list.m`写入并保存找到的关系列表
+ `get_mat_from_PV.m`计算读取`pair_value`文件夹中的csv文件的_R_和_Theta_矩阵
+ `get_R.m`计算_R_矩阵
+ `get_teta.m`计算约束矩阵Theta
+ `getNeg.m`和`getPos.m`计算矩阵中的正负元素
+ `load_dump.m`从最后一个可用备份（`parsave.m`）加载在算法意外中断的情况下保存的Matlab工作空间
+ `parsave.m`每100次迭代保存Matlab环境
+ `random_mats.m`计算随机矩阵_R_和_Theta_以制作玩具示例
+ `read_mats.m`读取矩阵以创建块矩阵_R_
+ `trifact_core.m`包含算法主要计算

### Project folders
Each project folder is structured in the followed way:

+ `parameters.m`, Matlab file specifying the algorithm parameters
+ `pair_value`, folder containing the associations in the (pair, value) format, e.g., `data_x,data_y,0.2`
+ `matrices,` folder containing the matrices representing the (pair, value) data
+ `objects`, folder with the list of unique elements of the object types
+ `output`, folder with the algorithm results

### Matrix construction

构建块矩阵R的初始矩阵由`pair_value`文件夹中的`csv`文件构成。 每个文件包含两种特定类型的对象对之间的关联，例如patient-gene; 基因 - 基因; 或基因通路; 单个对值文件用于构建关系矩阵_r_。 然后组装所有_rs_矩阵（即，每个_r_是块）以组成_R_。 配对值文件中的每一行包含以特定顺序编写的两个对象，并用逗号分隔，以及[0,1]权重量化它们之间的关系，如图1所示。

![Figure1](https://github.com/smarini/MaDDA/blob/master/Figures/Figure1.png "Figure1")

__Figure 1__: 对象及其关系，逗号分隔。 这些名称是随机的，因为它们是在玩具示例项目中自行生成的。

The constraints for the filenames are:
+ `<Data type 1>_<Data type 2>.csv` 用于包含不同类型的数据类型（关系矩阵）之间关系的那些;
+ `<Data type 1>_<Data type 1>_<n>.csv` 如果它们包含相同类型的对象之间的关系。 `n`表示多重性，对于约束矩阵可以> 1，即由相同类型对象之间的关系构成的矩阵。 换句话说，可以有多个矩阵表示数据类型A和B之间的关系。

矩阵自动构建运行脚本`get_mat_from_PV.m`。 图2中提供了一个图形示例。关系矩阵R中的值必须以[0,1]间隔为界，而在约束矩阵中，它们以[-1,1]间隔为界。 注意-1表示最强的关系，1表示最强的多样性。

![Figure2](https://github.com/smarini/MaDDA/blob/master/Figures/Figure2.png "Figure2")

__Figure 2__: example of how matrices are extracted from the pair-value files.

组装两种对象类型的关系矩阵，在该示例中为患者和基因。
csv文件必须保存在名为pair_value的文件夹中。
并非所有关系矩阵都存在，而如果缺少一个或多个约束矩阵，则会出现错误消息。 如果相同类型的对象之间的关系未知，则将costraint矩阵构造为对角矩阵，其中对角线的每个元素等于-1。

#### Matrix file naming convention
+ 关系矩阵命名为`R <n> - <m> .mat`，其中`n`和`m`分别表示第n和第m类型的对象，遵循它们保存在 文件夹对象（例如，如果文件夹`objects`中的第三类数据是_gene_而第四类是_mutation_，则`R3-4`.mat是_gene-mutatio_n矩阵）;

+ 成本矩阵被命名为“T<t>-<n >”矩阵，其中“t”表示第t类对象，“n”是它的多重性。例如，如果_gene_是第三种对象类型，并且我们同时具有_gene-gene_交互矩阵和_gene-gene_共表达矩阵，那么‘T3-1 . mat’和‘T3-2 . mat’是第一和第二基因-基因约束矩阵。它们分别基于交互和共表达。

所有`R <n> - <m> .mat`文件都包含一个稀疏矩阵，`R_matr`。 它是由文件名指定的对象类型的特定关系矩阵。 另一方面，每个`T <n> - <t> .mat`文件包含一个名为`teta_matr`的稀疏矩阵。

`objects`文件夹中的每个`mat`文件都包含一个名为`vett`的单元数组，其中包含文件名中指定类型的唯一对象。 在运行算法之前，可以检查特定类型的对象的数量和名称是否与期望相对应。


### Running the algorithm

#### Running the Toy example

The folder named `Test_example`, located in the main folder, contains a toy example that can be
run to test the algorithm. To use it is sufficient to run the script `main.m` and type
the name of the folder when requested on the Matlab command window.

###### Generating a random toy example

要更好地理解矩阵构造的工作原理，可以使用名为`random_mats.m`的脚本。 数组`dim`表示对象类型的数量（`dim`的元素数），以及每种类型的对象数。 当使用随机矩阵探索算法时，为了避免过多的计算时间，建议使用少量100个元素的少量对象类型（3-4）。 但是，我们还建议避免使用太少的对象元素。 例如，可以为每个对象使用50到100之间的多个元素。 当脚本启动时，消息将请求您希望保存随机矩阵的项目文件夹的名称。

在使用玩具示例之前，确保项目文件夹中的目录`objects`，`pair_value`和`matrices`为空，否则它们将被重写。

一旦“dim”和文件夹的名称被定义，就会在文件夹`pair_value`中生成一个`csv`文件列表。 这些对象是随机创建的字符串，用于模拟病例，蛋白质或基因ID等实例（参见图1中的示例）。 数据类型被命名为“ObjectA”，“ObjectB”，“ObjectC”等。 建立这种关系的方式产生的稀疏程度约为90％。

创建`csv`文件后，您应该运行脚本`get_mats_from_PV.m`。 之后，随机数据就可以处理了。

#### Running the algorithm on your data

##### Data preparation

+ 要运行算法，您需要以正确的格式存储数据。 文件命名约定和数据格式在[Matrix Construction]（＃matrix-construction）中描述。 例如，假设您有三种数据类型，基因，途径和患者。
  然后你可以得到以下文件：`gene_pathway.csv`，`patient_gene.csv`，`patient_patient_1.csv`，`gene_gene_1.csv`，`gene_gene_2.csv`和`gene_gene_3.csv`。

+ 确保您的数据对（例如`gene_pathway.csv`或`patient_disease.csv`）位于文件夹`pair_values`中。

+ 确保`parameters.m`中的参数正确, see [Parameters](#parameters))

##### Matrix calculation

运行`get_mats_from_PV.m`来计算初始矩阵。 矩阵保存在`matrices`文件夹中，数据类型保存在`objects`中。

##### Run the algorithm

Run `main.m`.

#### Parameters

In the script named `parameters.m` it’s possible to set the following parameters:

+ `num_rep`, 算法的所需运行次数（重复次数）。 默认值：10。
+ `Targ` and `cTarg`, 分别是我们用作目标的块矩阵_R_的行和列, i.e. 目标矩阵“R<n>-<m >”的“n”和“m”索引值 where 新的关系将被揭开. ( 用于同一对象和不同对象搜索).
+ `T`,  停止阈值，如果目标矩阵重建误差的绝对差值低于此值，则算法停止（每10次迭代验证）. Default: 10 −4 .
+ `epsilon`, 一个任意的小参数，可以避免可能发生的除零。 默认值：10 -16。 我们建议不要更改此参数。
+ `index_target`, 表示我们感兴趣的对象的对象类型。 （仅用于同一对象搜索），_R_中的行列坐标
+ `max_iter`,  每次重复的最大迭代次数，默认值：1000。
+ `directoryMAT`: 要使用的矩阵所在的文件夹的名称。 我们建议不要更改此参数。
+ `lambda`, 包含排名缩放因子的数组，每个对象类型一个。
+ `select`, 一个字符，表明该算法是否将用于计算相同类型（`s`）或不同类型（`d`）的对象之间的关系。

启动`main.m`脚本时，Matlab命令窗口中会显示一条请求项目文件夹名称的消息。 输入文件夹的名称，算法将启动。 有两种不同的运行trifactorization算法的方法，取决于目标是找到相同类型的对象之间的关系。

### Output
可以在名为output的文件夹中找到该过程的结果。 结果取决于算法运行的模式（D或S）。

#### _S_ mode
+ 对于相同类型的对象找到共识共识矩阵。
+ `R_original`, 最初组装的块关系矩阵（稀疏）
+ `R_reconstructed`, 推断块关系矩阵（完整）
+ `New_found_relations`, 对于相同类型的对象的新推断的关联

#### _D_ mode

+ `Consensus_row`, 根据行规则为不同类型的对象找到共识矩阵。
+ `Consensus_col`, 根据列规则为不同类型的对象找到共识矩阵。
+ `R_original`, 最初组装的块关系矩阵（稀疏）
+ `R_reconstructed`, 推断块关系矩阵（完整）
+ `New_found_relations_row`, 根据行规则新推断的不同类型对象的关联。
+ `New_found_relations_col`, 根据列规则新推断的不同类型对象的关联。

 一旦三分解终止，带有所有找到的关系列表的`csv`文件将保存在输出文件夹中。 此文件名为`new_found_relations.csv`，并在每行包含两个对象的名称及其找到的关系的权重，以逗号分隔。 如果算法已被用于计算相同类型的对象之间的关联，则文件的每一行将包含两个对象，并且分别包含基于行和基于列的规则找到的关联值; 如果算法已用于查找相同类型的对象之间的关联，则文件的每一行将包含两个对象以及可在共识矩阵中找到的关联值。 在这种情况下，关联以关联强度的降序报告。

### Rank selection
The input ranks can be computed in different ways, including:

+ 对比例因子进行排名，例如矩阵的非零元素的数量除以诸如50,100或200之类的任意数量。然后选择矩阵的等级作为列数除以等级比例因子。
+ 在给定所选等级（较高系数ρ，更好）的情况下，提供性能估计的色散系数ρ∈[0,1]。 注意，此处分散系数ρ在每次算法运行时默认计算。
+ 交叉验证可以优化排名选择。

## Additional information

+ 在执行脚本期间，Matlab命令窗口会出现一些更新，每10次迭代显示目标函数的Frobenius范数的每次重复;

+ 如果由于外部原因导致脚本意外中断，则无需从头开始重新启动该过程。 在执行期间，Matlab工作区定期保存在名为`dump.mat`的`mat`文件中。 您可以使用名为`load_dump.m`的脚本重新加载工作空间变量并继续该过程。

# MaddA
