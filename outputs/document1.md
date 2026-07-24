This file is a merged representation of the entire codebase, combined into a single document by Repomix.

<file_summary>
This section contains a summary of this file.

<purpose>
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.
</purpose>

<file_format>
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  - File path as an attribute
  - Full contents of the file
</file_format>

<usage_guidelines>
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.
</usage_guidelines>

<notes>
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)
</notes>

</file_summary>

<directory_structure>
.gitignore
configs.json
configs.py
joern/graph-for-funcs.sc
LICENSE
main.py
README.md
src/data/__init__.py
src/data/datamanager.py
src/prepare/__init__.py
src/prepare/cpg_client_wrapper.py
src/prepare/cpg_generator.py
src/prepare/embeddings.py
src/prepare/README.md
src/process/__init__.py
src/process/devign.py
src/process/loader_step.py
src/process/model.py
src/process/modeling.py
src/process/step.py
src/process/stopping.py
src/utils/__init__.py
src/utils/functions/__init__.py
src/utils/functions/cpg.py
src/utils/functions/digraph.py
src/utils/functions/parse.py
src/utils/log.py
src/utils/objects/__init__.py
src/utils/objects/cpg/__init__.py
src/utils/objects/cpg/ast.py
src/utils/objects/cpg/edge.py
src/utils/objects/cpg/function.py
src/utils/objects/cpg/node.py
src/utils/objects/cpg/properties.py
src/utils/objects/input_dataset.py
src/utils/objects/metrics.py
src/utils/objects/stats.py
</directory_structure>

<files>
This section contains the contents of the repository's files.

<file path=".gitignore">
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# static files generated from Django application using `collectstatic`
media
static
</file>

<file path="configs.json">
{
    "devign": {
        "learning_rate" : 1e-4,
        "weight_decay" : 1.3e-6,
        "loss_lambda" : 1.3e-6,
        "model": {
            "gated_graph_conv_args": {"out_channels" : 200, "num_layers" : 6, "aggr" : "add", "bias": true},
            "conv_args": {
                "conv1d_1" : {"in_channels": 205, "out_channels": 50, "kernel_size": 3, "padding" : 1},
                "conv1d_2" : {"in_channels": 50, "out_channels": 20, "kernel_size": 1, "padding" : 1},
                "maxpool1d_1" : {"kernel_size" : 3, "stride" : 2},
                "maxpool1d_2" : {"kernel_size" : 2, "stride" : 2}
            },
            "emb_size" : 101
        }
    },
    "create" : {
        "filter_column_value": {"project" : "qemu"},
        "slice_size": 100,
        "joern_cli_dir": "joern/joern-cli/"
    },
    "paths" : {
        "cpg" : "data/cpg/",
        "joern" : "data/joern/",
        "raw" : "data/raw/",
        "input" : "data/input/",
        "model" : "data/model/",
        "tokens" : "data/tokens/",
        "w2v" : "data/w2v/"
    },
    "files" : {
        "raw" : "dataset.json",
        "cpg" : "cpg",
        "tokens" : "tokens.pkl",
        "w2v" : "w2v.model",
        "input" : "input.pkl",
        "model" : "checkpoint.pt"
    },
    "embed" : {
        "nodes_dim" : 205,
        "word2vec_args": {"size" : 100, "alpha" : 0.01, "window" : 5, "min_count" : 3, "sample" : 1e-5,
                "workers" : 4, "sg" : 1, "hs" : 0, "negative" : 5
            },
        "edge_type": "Ast"
    },
    "process" : {
        "epochs" : 100,
        "patience" : 10,
        "batch_size" : 8,
        "dataset_ratio" : 0.2,
        "shuffle" : false
    }
}
</file>

<file path="configs.py">
import json
import torch


class Config(object):
    def __init__(self, config, file_path="configs.json"):
        with open(file_path) as config_file:
            self._config = json.load(config_file)
            self._config = self._config.get(config)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def get_property(self, property_name):
        return self._config.get(property_name)

    def get_device(self):
        return self.device

    def all(self):
        return self._config


class Create(Config):
    def __init__(self):
        super().__init__('create')

    @property
    def filter_column_value(self):
        return self.get_property('filter_project')

    @property
    def slice_size(self):
        return self.get_property('slice_size')

    @property
    def joern_cli_dir(self):
        return self.get_property('joern_cli_dir')


class Data(Config):
    def __init__(self, config):
        super().__init__(config)

    @property
    def cpg(self):
        return self.get_property('cpg')

    @property
    def raw(self):
        return self.get_property('raw')

    @property
    def input(self):
        return self.get_property('input')

    @property
    def model(self):
        return self.get_property('model')

    @property
    def tokens(self):
        return self.get_property('tokens')

    @property
    def w2v(self):
        return self.get_property('w2v')


class Paths(Data):
    def __init__(self):
        super().__init__('paths')

    @property
    def joern(self):
        return self.get_property('joern')


class Files(Data):
    def __init__(self):
        super().__init__('files')

    @property
    def tokens(self):
        return self.get_property('tokens')

    @property
    def w2v(self):
        return self.get_property('w2v')


class Embed(Config):
    def __init__(self):
        super().__init__('embed')

    @property
    def nodes_dim(self):
        return self.get_property('nodes_dim')

    @property
    def w2v_args(self):
        return self.get_property('word2vec_args')

    @property
    def edge_type(self):
        return self.get_property('edge_type')


class Process(Config):
    def __init__(self):
        super().__init__('process')

    @property
    def epochs(self):
        return self.get_property('epochs')

    @property
    def patience(self):
        return self.get_property('patience')

    @property
    def batch_size(self):
        return self.get_property('batch_size')

    @property
    def dataset_ratio(self):
        return self.get_property('dataset_ratio')

    @property
    def shuffle(self):
        return self.get_property('shuffle')


class Devign(Config):
    def __init__(self):
        super().__init__('devign')

    @property
    def learning_rate(self):
        return self.get_property('learning_rate')

    @property
    def weight_decay(self):
        return self.get_property('weight_decay')

    @property
    def loss_lambda(self):
        return self.get_property('loss_lambda')

    @property
    def model(self):
        return self.get_property('model')
</file>

<file path="LICENSE">
MIT License

Copyright (c) 2020 Eduard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</file>

<file path="main.py">
# -*- coding: utf-8 -*-
"""
    This module is intended to join all the pipeline in separated tasks
    to be executed individually or in a flow by using command-line options

    Example:
    Dataset embedding and processing:
        $ python taskflows.py -e -pS
"""

import argparse
import gc
import shutil
from argparse import ArgumentParser

from gensim.models.word2vec import Word2Vec

import configs
import src.data as data
import src.prepare as prepare
import src.process as process
import src.utils.functions.cpg as cpg

PATHS = configs.Paths()
FILES = configs.Files()
DEVICE = FILES.get_device()


def select(dataset):
    result = dataset.loc[dataset['project'] == "FFmpeg"]
    len_filter = result.func.str.len() < 1200
    result = result.loc[len_filter]
    #print(len(result))
    #result = result.iloc[11001:]
    #print(len(result))
    result = result.head(200)

    return result


def create_task():
    context = configs.Create()
    raw = data.read(PATHS.raw, FILES.raw)
    filtered = data.apply_filter(raw, select)
    filtered = data.clean(filtered)
    data.drop(filtered, ["commit_id", "project"])
    slices = data.slice_frame(filtered, context.slice_size)
    slices = [(s, slice.apply(lambda x: x)) for s, slice in slices]

    cpg_files = []
    # Create CPG binary files
    for s, slice in slices:
        data.to_files(slice, PATHS.joern)
        cpg_file = prepare.joern_parse(context.joern_cli_dir, PATHS.joern, PATHS.cpg, f"{s}_{FILES.cpg}")
        cpg_files.append(cpg_file)
        print(f"Dataset {s} to cpg.")
        shutil.rmtree(PATHS.joern)
    # Create CPG with graphs json files
    json_files = prepare.joern_create(context.joern_cli_dir, PATHS.cpg, PATHS.cpg, cpg_files)
    for (s, slice), json_file in zip(slices, json_files):
        graphs = prepare.json_process(PATHS.cpg, json_file)
        if graphs is None:
            print(f"Dataset chunk {s} not processed.")
            continue
        dataset = data.create_with_index(graphs, ["Index", "cpg"])
        dataset = data.inner_join_by_index(slice, dataset)
        print(f"Writing cpg dataset chunk {s}.")
        data.write(dataset, PATHS.cpg, f"{s}_{FILES.cpg}.pkl")
        del dataset
        gc.collect()


def embed_task():
    context = configs.Embed()
    # Tokenize source code into tokens
    dataset_files = data.get_directory_files(PATHS.cpg)
    w2vmodel = Word2Vec(**context.w2v_args)
    w2v_init = True
    for pkl_file in dataset_files:
        file_name = pkl_file.split(".")[0]
        cpg_dataset = data.load(PATHS.cpg, pkl_file)
        tokens_dataset = data.tokenize(cpg_dataset)
        data.write(tokens_dataset, PATHS.tokens, f"{file_name}_{FILES.tokens}")
        # word2vec used to learn the initial embedding of each token
        w2vmodel.build_vocab(sentences=tokens_dataset.tokens, update=not w2v_init)
        w2vmodel.train(tokens_dataset.tokens, total_examples=w2vmodel.corpus_count, epochs=1)
        if w2v_init:
            w2v_init = False
        # Embed cpg to node representation and pass to graph data structure
        cpg_dataset["nodes"] = cpg_dataset.apply(lambda row: cpg.parse_to_nodes(row.cpg, context.nodes_dim), axis=1)
        # remove rows with no nodes
        cpg_dataset = cpg_dataset.loc[cpg_dataset.nodes.map(len) > 0]
        cpg_dataset["input"] = cpg_dataset.apply(lambda row: prepare.nodes_to_input(row.nodes, row.target, context.nodes_dim,
                                                                                    w2vmodel.wv, context.edge_type), axis=1)
        data.drop(cpg_dataset, ["nodes"])
        print(f"Saving input dataset {file_name} with size {len(cpg_dataset)}.")
        data.write(cpg_dataset[["input", "target"]], PATHS.input, f"{file_name}_{FILES.input}")
        del cpg_dataset
        gc.collect()
    print("Saving w2vmodel.")
    w2vmodel.save(f"{PATHS.w2v}/{FILES.w2v}")


def process_task(stopping):
    context = configs.Process()
    devign = configs.Devign()
    model_path = PATHS.model + FILES.model
    model = process.Devign(path=model_path, device=DEVICE, model=devign.model, learning_rate=devign.learning_rate,
                           weight_decay=devign.weight_decay,
                           loss_lambda=devign.loss_lambda)
    train = process.Train(model, context.epochs)
    input_dataset = data.loads(PATHS.input)
    # split the dataset and pass to DataLoader with batch size
    train_loader, val_loader, test_loader = list(
        map(lambda x: x.get_loader(context.batch_size, shuffle=context.shuffle),
            data.train_val_test_split(input_dataset, shuffle=context.shuffle)))
    train_loader_step = process.LoaderStep("Train", train_loader, DEVICE)
    val_loader_step = process.LoaderStep("Validation", val_loader, DEVICE)
    test_loader_step = process.LoaderStep("Test", test_loader, DEVICE)

    if stopping:
        early_stopping = process.EarlyStopping(model, patience=context.patience)
        train(train_loader_step, val_loader_step, early_stopping)
        model.load()
    else:
        train(train_loader_step, val_loader_step)
        model.save()

    process.predict(model, test_loader_step)


def main():
    """
    main function that executes tasks based on command-line options
    """
    parser: ArgumentParser = argparse.ArgumentParser()
    # parser.add_argument('-p', '--prepare', help='Prepare task', required=False)
    parser.add_argument('-c', '--create', action='store_true')
    parser.add_argument('-e', '--embed', action='store_true')
    parser.add_argument('-p', '--process', action='store_true')
    parser.add_argument('-pS', '--process_stopping', action='store_true')

    args = parser.parse_args()

    if args.create:
        create_task()
    if args.embed:
        embed_task()
    if args.process:
        process_task(False)
    if args.process_stopping:
        process_task(True)



if __name__ == "__main__":
    main()
</file>

<file path="src/data/__init__.py">
from .datamanager import *
</file>

<file path="src/data/datamanager.py">
import glob

import pandas as pd
import numpy as np
import os
import src.utils.functions.parse as parse

from os import listdir
from os.path import isfile, join
from src.utils.objects.input_dataset import InputDataset
from sklearn.model_selection import train_test_split


def read(path, json_file):
    """
    :param path: str
    :param json_file: str
    :return DataFrame
    """
    return pd.read_json(path + json_file)


def get_ratio(dataset, ratio):
    approx_size = int(len(dataset) * ratio)
    return dataset[:approx_size]


def load(path, pickle_file, ratio=1):
    dataset = pd.read_pickle(path + pickle_file)
    dataset.info(memory_usage='deep')
    if ratio < 1:
        dataset = get_ratio(dataset, ratio)

    return dataset


def write(data_frame: pd.DataFrame, path, file_name):
    data_frame.to_pickle(path + file_name)


def apply_filter(data_frame: pd.DataFrame, filter_func):
    return filter_func(data_frame)


def rename(data_frame: pd.DataFrame, old, new):
    return data_frame.rename(columns={old: new})


def tokenize(data_frame: pd.DataFrame):
    data_frame.func = data_frame.func.apply(parse.tokenizer)
    # Change column name
    data_frame = rename(data_frame, 'func', 'tokens')
    # Keep just the tokens
    return data_frame[["tokens"]]


def to_files(data_frame: pd.DataFrame, out_path):
    # path = f"{self.out_path}/{self.dataset_name}/"
    os.makedirs(out_path)

    for idx, row in data_frame.iterrows():
        file_name = f"{idx}.c"
        with open(out_path + file_name, 'w') as f:
            f.write(row.func)


def create_with_index(data, columns):
    data_frame = pd.DataFrame(data, columns=columns)
    data_frame.index = list(data_frame["Index"])

    return data_frame


def inner_join_by_index(df1, df2):
    return pd.merge(df1, df2, left_index=True, right_index=True)


def train_val_test_split(data_frame: pd.DataFrame, shuffle=True):
    print("Splitting Dataset")

    false = data_frame[data_frame.target == 0]
    true = data_frame[data_frame.target == 1]

    train_false, test_false = train_test_split(false, test_size=0.2, shuffle=shuffle)
    test_false, val_false = train_test_split(test_false, test_size=0.5, shuffle=shuffle)
    train_true, test_true = train_test_split(true, test_size=0.2, shuffle=shuffle)
    test_true, val_true = train_test_split(test_true, test_size=0.5, shuffle=shuffle)

    train = train_false.append(train_true)
    val = val_false.append(val_true)
    test = test_false.append(test_true)

    train = train.reset_index(drop=True)
    val = val.reset_index(drop=True)
    test = test.reset_index(drop=True)

    return InputDataset(train), InputDataset(test), InputDataset(val)


def get_directory_files(directory):
    return [os.path.basename(file) for file in glob.glob(f"{directory}/*.pkl")]


def loads(data_sets_dir, ratio=1):
    data_sets_files = sorted([f for f in listdir(data_sets_dir) if isfile(join(data_sets_dir, f))])

    if ratio < 1:
        data_sets_files = get_ratio(data_sets_files, ratio)

    dataset = load(data_sets_dir, data_sets_files[0])
    data_sets_files.remove(data_sets_files[0])

    for ds_file in data_sets_files:
        dataset = dataset.append(load(data_sets_dir, ds_file))

    return dataset


def clean(data_frame: pd.DataFrame):
    return data_frame.drop_duplicates(subset="func", keep=False)


def drop(data_frame: pd.DataFrame, keys):
    for key in keys:
        del data_frame[key]


def slice_frame(data_frame: pd.DataFrame, size: int):
    data_frame_size = len(data_frame)
    return data_frame.groupby(np.arange(data_frame_size) // size)
</file>

<file path="src/prepare/__init__.py">
from .cpg_generator import *
from .embeddings import *
</file>

<file path="src/prepare/cpg_client_wrapper.py">
import os
import requests
import time

from cpgclient.CpgClient import CpgClient


class CPGClientWrapper(CpgClient):
    def __init__(self, address='127.0.0.1', port=8080):
        super(CPGClientWrapper, self).__init__(address, port)
        self.abs_path = os.path.dirname(os.path.abspath(os.getcwd()))
        self.query_script = f"cpg.runScript(\"{self.abs_path}/joern/graph-for-funcs.sc\")"

    def __call__(self, out_path):
        self.create_cpg(self.abs_path + out_path)
        return self.query(self.query_script)

    def _wait_until_cpg_is_created(self):
        while not self.is_cpg_loaded():
            time.sleep(1)

    def _poll_for_query_result(self):
        while True:
            response = requests.get("{}/v1/query/{}".format(self.handlerAndUrl, self.currentQueryId))
            json_body = response.json()
            if json_body["ready"]:
                return json_body["result"] or json_body["error"]
            time.sleep(.1)
</file>

<file path="src/prepare/embeddings.py">
import numpy as np
import torch
from torch_geometric.data import Data
from src.utils.functions.parse import tokenizer
from src.utils import log as logger
from gensim.models.keyedvectors import Word2VecKeyedVectors


class NodesEmbedding:
    def __init__(self, nodes_dim: int, w2v_keyed_vectors: Word2VecKeyedVectors):
        self.w2v_keyed_vectors = w2v_keyed_vectors
        self.kv_size = w2v_keyed_vectors.vector_size
        self.nodes_dim = nodes_dim

        assert self.nodes_dim >= 0

        # Buffer for embeddings with padding
        self.target = torch.zeros(self.nodes_dim, self.kv_size + 1).float()

    def __call__(self, nodes):
        embedded_nodes = self.embed_nodes(nodes)
        nodes_tensor = torch.from_numpy(embedded_nodes).float()

        self.target[:nodes_tensor.size(0), :] = nodes_tensor

        return self.target

    def embed_nodes(self, nodes):
        embeddings = []

        for n_id, node in nodes.items():
            # Get node's code
            node_code = node.get_code()
            # Tokenize the code
            tokenized_code = tokenizer(node_code, True)
            if not tokenized_code:
                # print(f"Dropped node {node}: tokenized code is empty.")
                msg = f"Empty TOKENIZED from node CODE {node_code}"
                logger.log_warning('embeddings', msg)
                continue
            # Get each token's learned embedding vector
            vectorized_code = np.array(self.get_vectors(tokenized_code, node))
            # The node's source embedding is the average of it's embedded tokens
            source_embedding = np.mean(vectorized_code, 0)
            # The node representation is the concatenation of label and source embeddings
            embedding = np.concatenate((np.array([node.type]), source_embedding), axis=0)
            embeddings.append(embedding)
        # print(node.label, node.properties.properties.get("METHOD_FULL_NAME"))

        return np.array(embeddings)

    # fromTokenToVectors
    def get_vectors(self, tokenized_code, node):
        vectors = []

        for token in tokenized_code:
            if token in self.w2v_keyed_vectors.vocab:
                vectors.append(self.w2v_keyed_vectors[token])
            else:
                # print(node.label, token, node.get_code(), tokenized_code)
                vectors.append(np.zeros(self.kv_size))
                if node.label not in ["Identifier", "Literal", "MethodParameterIn", "MethodParameterOut"]:
                    msg = f"No vector for TOKEN {token} in {node.get_code()}."
                    logger.log_warning('embeddings', msg)

        return vectors


class GraphsEmbedding:
    def __init__(self, edge_type):
        self.edge_type = edge_type

    def __call__(self, nodes):
        connections = self.nodes_connectivity(nodes)

        return torch.tensor(connections).long()

    # nodesToGraphConnectivity
    def nodes_connectivity(self, nodes):
        # nodes are ordered by line and column
        coo = [[], []]

        for node_idx, (node_id, node) in enumerate(nodes.items()):
            if node_idx != node.order:
                raise Exception("Something wrong with the order")

            for e_id, edge in node.edges.items():
                if edge.type != self.edge_type:
                    continue

                if edge.node_in in nodes and edge.node_in != node_id:
                    coo[0].append(nodes[edge.node_in].order)
                    coo[1].append(node_idx)

                if edge.node_out in nodes and edge.node_out != node_id:
                    coo[0].append(node_idx)
                    coo[1].append(nodes[edge.node_out].order)

        return coo


def nodes_to_input(nodes, target, nodes_dim, keyed_vectors, edge_type):
    nodes_embedding = NodesEmbedding(nodes_dim, keyed_vectors)
    graphs_embedding = GraphsEmbedding(edge_type)
    label = torch.tensor([target]).float()

    return Data(x=nodes_embedding(nodes), edge_index=graphs_embedding(nodes), y=label)
</file>

<file path="src/prepare/README.md">
# Description

This module contains scripts used for transforming the raw code from the dataset into Code Property Graphs.

## cpg_generator.py
This script launches and queries the Joern server that deals with the conversion of the code.
It takes as input a Pandas Dataframe containing code functions which are written to a folder.
The Joern is queried to create the CPG from the functions in the folder and returns the result into json format.

## The JSON generated has the following keys:
"functions": Array of all methods contained in the currently loaded CPG
 - |_ "function": Method name as String
 - |_ "id": Method id as String (String representation of the underlying Method node)
 - |_ "AST": Array of all nodes connected via AST edges
 - |_ "CFG": Array of all nodes connected via CFG edges
 - |_ "PDG": Array of all nodes that are reachable by data-flow or control-flow from the current method locals
  
 - Nodes have the following keys:
     - |_ "id": Node id as String (String representation of the underlying AST node)
     - |_ "properties": Array of properties of the current node as key-value pair
     - |_ "edges": Array of all AST edges where the current node is referenced as inVertex or outVertex
         - |_ "id": Edge id as String (String representation of the AST edge)
         - |_ "in": Node id as String of the inVertex node (String representation of the inVertex node)
         - |_ "out": Node id as String of the outVertex node (String representation of the outVertex node)
</file>

<file path="src/process/__init__.py">
from .loader_step import *
from .devign import *
from .modeling import *
from .stopping import *
from .devign import *
</file>

<file path="src/process/devign.py">
import torch.optim as optim
import torch.nn.functional as F

from ..utils import log
from .step import Step
from .model import Net


class Devign(Step):
    def __init__(self,
                 path: str,
                 device: str,
                 model: dict,
                 learning_rate: float,
                 weight_decay: float,
                 loss_lambda: float):
        self.path = path
        self.lr = learning_rate
        self.wd = weight_decay
        self.ll = loss_lambda
        log.log_info('devign', f"LR: {self.lr}; WD: {self.wd}; LL: {self.ll};")
        _model = Net(**model, device=device)
        super().__init__(model=_model,
                         loss_function=lambda o, t: F.binary_cross_entropy(o, t) + F.l1_loss(o, t) * self.ll,
                         optimizer=optim.Adam(_model.parameters(), lr=self.lr, weight_decay=self.wd),
                         )

        self.count_parameters()

    def load(self):
        self.model.load(self.path)

    def save(self):
        self.model.save(self.path)

    def count_parameters(self):
        count = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        print(f"The model has {count:,} trainable parameters")
</file>

<file path="src/process/loader_step.py">
from ..utils.objects import stats


class LoaderStep:
    def __init__(self, name, data_loader, device):
        self.name = name
        self.loader = data_loader
        self.size = len(data_loader)
        self.device = device

    def __call__(self, step):
        self.stats = stats.Stats(self.name)

        for i, batch in enumerate(self.loader):
            batch.to(self.device)
            stat: stats.Stat = step(i, batch, batch.y)
            self.stats(stat)

        return self.stats
</file>

<file path="src/process/model.py">
import torch
import torch.nn as nn
import torch.nn.functional as F

from torch_geometric.nn.conv import GatedGraphConv

torch.manual_seed(2020)


def get_conv_mp_out_size(in_size, last_layer, mps):
    size = in_size

    for mp in mps:
        size = round((size - mp["kernel_size"]) / mp["stride"] + 1)

    size = size + 1 if size % 2 != 0 else size

    return int(size * last_layer["out_channels"])


def init_weights(m):
    if type(m) == nn.Linear or type(m) == nn.Conv1d:
        torch.nn.init.xavier_uniform_(m.weight)


class Conv(nn.Module):

    def __init__(self, conv1d_1, conv1d_2, maxpool1d_1, maxpool1d_2, fc_1_size, fc_2_size):
        super(Conv, self).__init__()
        self.conv1d_1_args = conv1d_1
        self.conv1d_1 = nn.Conv1d(**conv1d_1)
        self.conv1d_2 = nn.Conv1d(**conv1d_2)

        fc1_size = get_conv_mp_out_size(fc_1_size, conv1d_2, [maxpool1d_1, maxpool1d_2])
        fc2_size = get_conv_mp_out_size(fc_2_size, conv1d_2, [maxpool1d_1, maxpool1d_2])

        # Dense layers
        self.fc1 = nn.Linear(fc1_size, 1)
        self.fc2 = nn.Linear(fc2_size, 1)

        # Dropout
        self.drop = nn.Dropout(p=0.2)

        self.mp_1 = nn.MaxPool1d(**maxpool1d_1)
        self.mp_2 = nn.MaxPool1d(**maxpool1d_2)

    def forward(self, hidden, x):
        concat = torch.cat([hidden, x], 1)
        concat_size = hidden.shape[1] + x.shape[1]
        concat = concat.view(-1, self.conv1d_1_args["in_channels"], concat_size)

        Z = self.mp_1(F.relu(self.conv1d_1(concat)))
        Z = self.mp_2(self.conv1d_2(Z))

        hidden = hidden.view(-1, self.conv1d_1_args["in_channels"], hidden.shape[1])

        Y = self.mp_1(F.relu(self.conv1d_1(hidden)))
        Y = self.mp_2(self.conv1d_2(Y))

        Z_flatten_size = int(Z.shape[1] * Z.shape[-1])
        Y_flatten_size = int(Y.shape[1] * Y.shape[-1])

        Z = Z.view(-1, Z_flatten_size)
        Y = Y.view(-1, Y_flatten_size)
        res = self.fc1(Z) * self.fc2(Y)
        res = self.drop(res)
        # res = res.mean(1)
        # print(res, mean)
        sig = torch.sigmoid(torch.flatten(res))
        return sig


class Net(nn.Module):

    def __init__(self, gated_graph_conv_args, conv_args, emb_size, device):
        super(Net, self).__init__()
        self.ggc = GatedGraphConv(**gated_graph_conv_args).to(device)
        self.conv = Conv(**conv_args,
                         fc_1_size=gated_graph_conv_args["out_channels"] + emb_size,
                         fc_2_size=gated_graph_conv_args["out_channels"]).to(device)
        # self.conv.apply(init_weights)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.ggc(x, edge_index)
        x = self.conv(x, data.x)

        return x

    def save(self, path):
        torch.save(self.state_dict(), path)

    def load(self, path):
        self.load_state_dict(torch.load(path))
</file>

<file path="src/process/modeling.py">
from ..utils.objects.metrics import Metrics
import torch
import time
from ..utils import log as logger


class Train(object):
    def __init__(self, step, epochs, verbose=True):
        self.epochs = epochs
        self.step = step
        self.history = History()
        self.verbose = verbose

    def __call__(self, train_loader_step, val_loader_step=None, early_stopping=None):
        for epoch in range(self.epochs):
            self.step.train()
            train_stats = train_loader_step(self.step)
            self.history(train_stats, epoch + 1)

            if val_loader_step is not None:
                with torch.no_grad():
                    self.step.eval()
                    val_stats = val_loader_step(self.step)
                    self.history(val_stats, epoch + 1)

                print(self.history)

                if early_stopping is not None:
                    valid_loss = val_stats.loss()
                    # early_stopping needs the validation loss to check if it has decreased,
                    # and if it has, it will make a checkpoint of the current model
                    if early_stopping(valid_loss):
                        self.history.log()
                        return
            else:
                print(self.history)
        self.history.log()


def predict(step, test_loader_step):
    print(f"Testing")
    with torch.no_grad():
        step.eval()
        stats = test_loader_step(step)
        metrics = Metrics(stats.outs(), stats.labels())
        print(metrics)
        metrics.log()
    return metrics()["Accuracy"]


class History:
    def __init__(self):
        self.history = {}
        self.epoch = 0
        self.timer = time.time()

    def __call__(self, stats, epoch):
        self.epoch = epoch

        if epoch in self.history:
            self.history[epoch].append(stats)
        else:
            self.history[epoch] = [stats]

    def __str__(self):
        epoch = f"\nEpoch {self.epoch};"
        stats = ' - '.join([f"{res}" for res in self.current()])
        timer = f"Time: {(time.time() - self.timer)}"

        return f"{epoch} - {stats} - {timer}"

    def current(self):
        return self.history[self.epoch]

    def log(self):
        msg = f"(Epoch: {self.epoch}) {' - '.join([f'({res})' for res in self.current()])}"
        logger.log_info("history", msg)
</file>

<file path="src/process/step.py">
import torch
from ..utils.objects import stats


def softmax_accuracy(probs, all_labels):
    acc = (torch.argmax(probs) == all_labels).sum()
    acc = torch.div(acc, len(all_labels) + 0.0)
    return acc


class Step:
    # Performs a step on the loader and returns the result
    def __init__(self, model, loss_function, optimizer):
        self.model = model
        self.criterion = loss_function
        self.optimizer = optimizer

    def __call__(self, i, x, y):
        out = self.model(x)
        loss = self.criterion(out, y.float())
        acc = softmax_accuracy(out, y.float())

        if self.model.training:
            # calculates the gradient
            loss.backward()
            # and performs a parameter update based on it
            self.optimizer.step()
            # clears old gradients from the last step
            self.optimizer.zero_grad()

        # print(f"\tBatch: {i}; Loss: {round(loss.item(), 4)}", end="")
        return stats.Stat(out.tolist(), loss.item(), acc.item(), y.tolist())

    def train(self):
        self.model.train()

    def eval(self):
        self.model.eval()
</file>

<file path="src/process/stopping.py">
import numpy as np


# Author: https://github.com/Bjarten/early-stopping-pytorch
class EarlyStopping:
    """Early stops the training if validation loss doesn't improve after a given patience."""

    def __init__(self, model, patience=7, verbose=False, delta=0):
        """
        Args:
            patience (int): How long to wait after last time validation loss improved.
                            Default: 7
            verbose (bool): If True, prints a message for each validation loss improvement. 
                            Default: False
            delta (float): Minimum change in the monitored quantity to qualify as an improvement.
                            Default: 0
        """
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.delta = delta
        self.model = model

    def __call__(self, val_loss):

        score = -val_loss

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss)
        elif score < self.best_score + self.delta:
            self.counter += 1
            print(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
                print("Early stopping")
        else:
            self.best_score = score
            self.save_checkpoint(val_loss)
            self.counter = 0

        return self.early_stop

    def save_checkpoint(self, val_loss):
        """
            Saves model when validation loss decrease.
        """
        if self.verbose:
            print(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        self.model.save()
        self.val_loss_min = val_loss
</file>

<file path="src/utils/__init__.py">
from .functions import *
from .objects import *
</file>

<file path="src/utils/functions/__init__.py">
from .cpg import *
from .parse import *
from .digraph import *
</file>

<file path="src/utils/functions/cpg.py">
from collections import OrderedDict
from ..objects.cpg.function import Function


def order_nodes(nodes, max_nodes):
    # sorts nodes by line and column

    nodes_by_column = sorted(nodes.items(), key=lambda n: n[1].get_column_number())
    nodes_by_line = sorted(nodes_by_column, key=lambda n: n[1].get_line_number())

    for i, node in enumerate(nodes_by_line):
        node[1].order = i

    if len(nodes) > max_nodes:
        print(f"CPG cut - original nodes: {len(nodes)} to max: {max_nodes}")
        return OrderedDict(nodes_by_line[:max_nodes])

    return OrderedDict(nodes_by_line)


def filter_nodes(nodes):
    return {n_id: node for n_id, node in nodes.items() if node.has_code() and
            node.has_line_number() and
            node.label not in ["Comment", "Unknown"]}


def parse_to_nodes(cpg, max_nodes=500):
    nodes = {}
    for function in cpg["functions"]:
        func = Function(function)
        # Only nodes with code and line number are selected
        filtered_nodes = filter_nodes(func.get_nodes())
        nodes.update(filtered_nodes)

    return order_nodes(nodes, max_nodes)
</file>

<file path="src/utils/functions/digraph.py">
import subprocess


def create_digraph(name, nodes):
    with open('digraph.gv', 'w') as f:
        f.write("digraph {\n")
        digraph = ''

        for n_id, node in nodes.items():
            label = node.get_code() + "\n" + node.label
            f.write(f"\"{node.get_code()}\" [label=\"{label}\"]\n")
            for e_id, edge in node.edges.items():
                if edge.type != "Ast": continue

                if edge.node_in in nodes and edge.node_in != node.id:
                    n_in = nodes.get(edge.node_in)
                    label = "\"" + n_in.label + "\""
                    digraph += f"\"{node.get_code()}\" -> \"{n_in.get_code()}\" [label={label}]\n"
                '''
				if edge.node_out in nodes and edge.node_out != node.id:
					n_out = nodes.get(edge.node_out)
					label = "\"" + n_out.label + "\""
					digraph += f"\"{n_out.get_code()}\" -> \"{node.get_code()}\" [label={label}]\n"		
				'''
        f.write(digraph)
        f.write("}\n")
    subprocess.run(["dot", "-Tps", "digraph.gv", "-o", f"{name}.ps"], shell=False)


'''
def to_digraph(name, nodes):
    k_nodes = nodes.keys()
    code = {}
    connections = { "in" : dict.fromkeys(k_nodes), "out" : dict.fromkeys(k_nodes) }

	for n_id, node in nodes.items():
		#print(n_id, node.properties)
		connections = node.connections(connections, "Ast")
		code.update({n_id : node.get_code()})

	create_digraph(name, code, k_nodes, connections)
'''
</file>

<file path="src/utils/functions/parse.py">
import re
import codecs

# Clean Gadget
# Author https://github.com/johnb110/VDPython:
# For each gadget, replaces all user variables with "VAR#" and user functions with "FUN#"
# Removes content from string and character literals keywords up to C11 and C++17; immutable set
from typing import List

keywords = frozenset({'__asm', '__builtin', '__cdecl', '__declspec', '__except', '__export', '__far16', '__far32',
                      '__fastcall', '__finally', '__import', '__inline', '__int16', '__int32', '__int64', '__int8',
                      '__leave', '__optlink', '__packed', '__pascal', '__stdcall', '__system', '__thread', '__try',
                      '__unaligned', '_asm', '_Builtin', '_Cdecl', '_declspec', '_except', '_Export', '_Far16',
                      '_Far32', '_Fastcall', '_finally', '_Import', '_inline', '_int16', '_int32', '_int64',
                      '_int8', '_leave', '_Optlink', '_Packed', '_Pascal', '_stdcall', '_System', '_try', 'alignas',
                      'alignof', 'and', 'and_eq', 'asm', 'auto', 'bitand', 'bitor', 'bool', 'break', 'case',
                      'catch', 'char', 'char16_t', 'char32_t', 'class', 'compl', 'const', 'const_cast', 'constexpr',
                      'continue', 'decltype', 'default', 'delete', 'do', 'double', 'dynamic_cast', 'else', 'enum',
                      'explicit', 'export', 'extern', 'false', 'final', 'float', 'for', 'friend', 'goto', 'if',
                      'inline', 'int', 'long', 'mutable', 'namespace', 'new', 'noexcept', 'not', 'not_eq', 'nullptr',
                      'operator', 'or', 'or_eq', 'override', 'private', 'protected', 'public', 'register',
                      'reinterpret_cast', 'return', 'short', 'signed', 'sizeof', 'static', 'static_assert',
                      'static_cast', 'struct', 'switch', 'template', 'this', 'thread_local', 'throw', 'true', 'try',
                      'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using', 'virtual', 'void', 'volatile',
                      'wchar_t', 'while', 'xor', 'xor_eq', 'NULL'})
# holds known non-user-defined functions; immutable set
main_set = frozenset({'main'})
# arguments in main function; immutable set
main_args = frozenset({'argc', 'argv'})

operators3 = {'<<=', '>>='}
operators2 = {
    '->', '++', '--', '**',
    '!~', '<<', '>>', '<=', '>=',
    '==', '!=', '&&', '||', '+=',
    '-=', '*=', '/=', '%=', '&=', '^=', '|='
}
operators1 = {
    '(', ')', '[', ']', '.',
    '+', '&',
    '%', '<', '>', '^', '|',
    '=', ',', '?', ':',
    '{', '}', '!', '~'
}


def to_regex(lst):
    return r'|'.join([f"({re.escape(el)})" for el in lst])


regex_split_operators = to_regex(operators3) + to_regex(operators2) + to_regex(operators1)


# input is a list of string lines
def clean_gadget(gadget):
    # dictionary; map function name to symbol name + number
    fun_symbols = {}
    # dictionary; map variable name to symbol name + number
    var_symbols = {}

    fun_count = 1
    var_count = 1

    # regular expression to find function name candidates
    rx_fun = re.compile(r'\b([_A-Za-z]\w*)\b(?=\s*\()')
    # regular expression to find variable name candidates
    # rx_var = re.compile(r'\b([_A-Za-z]\w*)\b(?!\s*\()')
    rx_var = re.compile(r'\b([_A-Za-z]\w*)\b((?!\s*\**\w+))(?!\s*\()')

    # final cleaned gadget output to return to interface
    cleaned_gadget = []

    for line in gadget:
        # replace any non-ASCII characters with empty string
        ascii_line = re.sub(r'[^\x00-\x7f]', r'', line)
        # remove all hexadecimal literals
        hex_line = re.sub(r'0[xX][0-9a-fA-F]+', "HEX", ascii_line)
        # return, in order, all regex matches at string list; preserves order for semantics
        user_fun = rx_fun.findall(hex_line)
        user_var = rx_var.findall(hex_line)

        # Could easily make a "clean gadget" type class to prevent duplicate functionality
        # of creating/comparing symbol names for functions and variables in much the same way.
        # The comparison frozenset, symbol dictionaries, and counters would be class scope.
        # So would only need to pass a string list and a string literal for symbol names to
        # another function.
        for fun_name in user_fun:
            if len({fun_name}.difference(main_set)) != 0 and len({fun_name}.difference(keywords)) != 0:
                # check to see if function name already in dictionary
                if fun_name not in fun_symbols.keys():
                    fun_symbols[fun_name] = 'FUN' + str(fun_count)
                    fun_count += 1
                # ensure that only function name gets replaced (no variable name with same
                # identifier); uses positive lookforward
                hex_line = re.sub(r'\b(' + fun_name + r')\b(?=\s*\()', fun_symbols[fun_name], hex_line)

        for var_name in user_var:
            # next line is the nuanced difference between fun_name and var_name
            if len({var_name[0]}.difference(keywords)) != 0 and len({var_name[0]}.difference(main_args)) != 0:
                # check to see if variable name already in dictionary
                if var_name[0] not in var_symbols.keys():
                    var_symbols[var_name[0]] = 'VAR' + str(var_count)
                    var_count += 1
                # ensure that only variable name gets replaced (no function name with same
                # identifier); uses negative lookforward
                # print(var_name, gadget, user_var)
                hex_line = re.sub(r'\b(' + var_name[0] + r')\b(?:(?=\s*\w+\()|(?!\s*\w+))(?!\s*\()',
                                  var_symbols[var_name[0]], hex_line)

        cleaned_gadget.append(hex_line)
    # return the list of cleaned lines
    return cleaned_gadget


# Cleaner & Tokenizer
# Author https://github.com/hazimhanif/svd-transformer/blob/master/transformer_svd.ipynb

def tokenizer(code, flag=False):
    gadget: List[str] = []
    tokenized: List[str] = []
    # remove all string literals
    no_str_lit_line = re.sub(r'["]([^"\\\n]|\\.|\\\n)*["]', '', code)
    # remove all character literals
    no_char_lit_line = re.sub(r"'.*?'", "", no_str_lit_line)
    code = no_char_lit_line

    if flag:
        code = codecs.getdecoder("unicode_escape")(no_char_lit_line)[0]

    for line in code.splitlines():
        if line == '':
            continue
        stripped = line.strip()
        # if "\\n\\n" in stripped: print(stripped)
        gadget.append(stripped)

    clean = clean_gadget(gadget)

    for cg in clean:
        if cg == '':
            continue

        # Remove code comments
        pat = re.compile(r'(/\*([^*]|(\*+[^*\/]))*\*+\/)|(\/\/.*)')
        cg = re.sub(pat, '', cg)

        # Remove newlines & tabs
        cg = re.sub('(\n)|(\\\\n)|(\\\\)|(\\t)|(\\r)', '', cg)
        # Mix split (characters and words)
        splitter = r' +|' + regex_split_operators + r'|(\/)|(\;)|(\-)|(\*)'
        cg = re.split(splitter, cg)

        # Remove None type
        cg = list(filter(None, cg))
        cg = list(filter(str.strip, cg))
        # code = " ".join(code)
        # Return list of tokens
        tokenized.extend(cg)

    return tokenized

#test = "((uint32_t *)(&s->boncop))[addr/sizeof(uint32_t)]"
#test2 = "(type_code[hw_breakpoint[n].type] << (16 + n*4)) |\n\n                ((uint32_t)len_code[hw_breakpoint[n].len] << (18 + n*4))"
#asd = re.split(regex_split_operators + r'|(\/)', test)
#print(list(filter(None,asd)))
#print(tokenizer(test2))
</file>

<file path="src/utils/log.py">
import logging.config

FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'

logging.basicConfig(filename="logs.log",
                    filemode='a',
                    format=FORMAT,
                    datefmt='%d/%m/%Y %I:%M:%S')


def log_info(logger_name, msg):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.info(msg)

def log_warning(logger_name, msg):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.WARNING)
    logger.warning(msg)
</file>

<file path="src/utils/objects/__init__.py">
from .cpg import *
from .stats import *
from .input_dataset import *
from .metrics import *
</file>

<file path="src/utils/objects/cpg/__init__.py">
from .edge import *
from .properties import *
from .node import *
from .ast import *
from .function import *
</file>

<file path="src/utils/objects/cpg/ast.py">
from .node import Node


class AST:
    def __init__(self, nodes, indentation):
        self.size = len(nodes)
        self.indentation = indentation + 1
        self.nodes = {node["id"].split(".")[-1]: Node(node, self.indentation) for node in nodes}

    def __str__(self):
        indentation = self.indentation * "\t"
        nodes_str = ""

        for node in self.nodes:
            nodes_str += f"{indentation}{self.nodes[node]}"

        return f"\n{indentation}Size: {self.size}\n{indentation}Nodes:{nodes_str}"

    def get_nodes_type(self):
        return {n_id: node.type for n_id, node in self.nodes.items()}
</file>

<file path="src/utils/objects/cpg/edge.py">
class Edge:
	def __init__(self, edge, indentation):
		self.id = edge["id"].split(".")[-1]
		self.type = self.id.split("@")[0]
		self.node_in = edge["in"].split(".")[-1]
		self.node_out = edge["out"].split(".")[-1]
		self.indentation = indentation + 1

	def __str__(self):
		indentation = self.indentation * "\t"
		return f"\n{indentation}Edge id: {self.id}\n{indentation}Node in: {self.node_in}\n{indentation}Node out: {self.node_out}\n"
</file>

<file path="src/utils/objects/cpg/function.py">
from .ast import AST


class Function:
    def __init__(self, function):
        self.name = function["function"]
        self.id = function["id"].split(".")[-1]
        self.indentation = 1
        self.ast = AST(function["AST"], self.indentation)

    def __str__(self):
        indentation = self.indentation * "\t"
        return f"{indentation}Function Name: {self.name}\n{indentation}Id: {self.id}\n{indentation}AST:{self.ast}"

    def get_nodes(self):
        return self.ast.nodes

    def get_nodes_types(self):
        return self.ast.get_nodes_type()
</file>

<file path="src/utils/objects/cpg/node.py">
from .properties import Properties
from .edge import Edge
from ... import log as logger

node_labels = ["Block", "Call", "Comment", "ControlStructure", "File", "Identifier", "FieldIdentifier", "Literal",
               "Local", "Member", "MetaData", "Method", "MethodInst", "MethodParameterIn", "MethodParameterOut",
               "MethodReturn", "Namespace", "NamespaceBlock", "Return", "Type", "TypeDecl", "Unknown"]

operators = ['addition', 'addressOf', 'and', 'arithmeticShiftRight', 'assignment',
             'assignmentAnd', 'assignmentArithmeticShiftRight', 'assignmentDivision',
             'assignmentMinus', 'assignmentMultiplication', 'assignmentOr', 'assignmentPlus',
             'assignmentShiftLeft', 'assignmentXor', 'cast', 'conditionalExpression',
             'division', 'equals', 'fieldAccess', 'greaterEqualsThan', 'greaterThan',
             'indirectFieldAccess', 'indirectIndexAccess', 'indirection', 'lessEqualsThan',
             'lessThan', 'logicalAnd', 'logicalNot', 'logicalOr', 'minus', 'modulo', 'multiplication',
             'not', 'notEquals', 'or', 'postDecrement', 'plus', 'postIncrement', 'preDecrement',
             'preIncrement', 'shiftLeft', 'sizeOf', 'subtraction']

node_labels += operators

node_labels = {label: i for i, label in enumerate(node_labels)}

PRINT_PROPS = True


class Node:
    def __init__(self, node, indentation):
        self.id = node["id"].split(".")[-1]
        self.label = self.id.split("@")[0]
        self.indentation = indentation + 1
        self.properties = Properties(node["properties"], self.indentation)
        self.edges = {edge["id"].split(".")[-1]: Edge(edge, self.indentation) for edge in node["edges"]}
        self.order = None
        operator = self.properties.get_operator()
        self.label = operator if operator is not None else self.label
        self._set_type()

    def __str__(self):
        indentation = self.indentation * "\t"
        properties = f"{indentation}Properties: {self.properties}\n"
        edges_str = ""

        for edge in self.edges:
            edges_str += f"{self.edges[edge]}"

        return f"\n{indentation}Node id: {self.id}\n{properties if PRINT_PROPS else ''}{indentation}Edges: {edges_str}"

    def connections(self, connections, e_type):
        for e_id, edge in self.edges.items():
            if edge.type != e_type: continue

            if edge.node_in in connections["in"] and edge.node_in != self.id:
                connections["in"][self.id] = edge.node_in

            if edge.node_out in connections["out"] and edge.node_out != self.id:
                connections["out"][self.id] = edge.node_out

        return connections

    def has_code(self):
        return self.properties.has_code()

    def has_line_number(self):
        return self.properties.has_line_number()

    def get_code(self):
        return self.properties.code()

    def get_line_number(self):
        return self.properties.line_number()

    def get_column_number(self):
        return self.properties.column_number()

    def _set_type(self):
        # label = self.label if self.operator is None else self.operator
        self.type = node_labels.get(self.label)  # Label embedding

        if self.type is None:
            logger.log_warning("node", f"LABEL {self.label} not in labels!")
            self.type = len(node_labels) + 1
</file>

<file path="src/utils/objects/cpg/properties.py">
class Properties:
	def __init__(self, props, indentation):
		self.size = len(props)
		self.indentation = indentation + 1
		self.pairs = {prop["key"]: prop["value"] for prop in props}
	
	def __str__(self):
		indentation = self.indentation * "\t"
		string = ""

		for prop in self.pairs:
			string += f"\n{indentation}Property - {prop} : {self.pairs[prop]}"

		return f"{indentation}{string}\n"

	def code(self):
		if self.has_code():
			code = self.pairs["CODE"]
			if self.has_type() and self.get_type() != "ANY" and self.get_type() not in code:
				code = f"{self.get_type()} {code}"
			return code
		return None

	def get_type(self):
		return self.pairs.get("TYPE_FULL_NAME")

	def has_type(self):
		return "TYPE_FULL_NAME" in self.pairs

	def has_code(self):
		return "CODE" in self.pairs

	def line_number(self):
		return self.pairs["LINE_NUMBER"] if self.has_line_number() else None

	def has_line_number(self):
		return "LINE_NUMBER" in self.pairs

	def column_number(self):
		return self.pairs["COLUMN_NUMBER"] if self.has_column_number() else None

	def has_column_number(self):
		return "COLUMN_NUMBER" in self.pairs

	def get(self):
		return self.pairs

	def get_operator(self):
		value = self.pairs.get("METHOD_FULL_NAME")
		if value is None:
			return value
		if ("<operator>" in value) or ("<operators>" in value):
			return value.split(".")[-1] 
		return None
</file>

<file path="src/utils/objects/input_dataset.py">
from torch.utils.data import Dataset as TorchDataset
from torch_geometric.data import DataLoader


class InputDataset(TorchDataset):
    def __init__(self, dataset):
        self.dataset = dataset

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        return self.dataset.iloc[index].input

    def get_loader(self, batch_size, shuffle=True):
        return DataLoader(dataset=self, batch_size=batch_size, shuffle=shuffle)
</file>

<file path="src/utils/objects/metrics.py">
import pandas as pd

from .. import log as logger
from sklearn.metrics import confusion_matrix
from sklearn import metrics


class Metrics:
    def __init__(self, outs, labels):
        self.scores = outs
        self.labels = labels
        self.transform()
        print(self.predicts)

    def transform(self):
        self.series = pd.Series(self.scores)
        self.predicts = self.series.apply(lambda x: 1 if x >= 0.5 else 0)
        self.predicts.reset_index(drop=True, inplace=True)

    def __str__(self):
        confusion = confusion_matrix(y_true=self.labels, y_pred=self.predicts)
        tn, fp, fn, tp = confusion.ravel()
        string = f"\nConfusion matrix: \n"
        string += f"{confusion}\n"
        string += f"TP: {tp}, FP: {fp}, TN: {tn}, FN: {fn}\n"
        string += '\n'.join([name + ": " + str(metric) for name, metric in self().items()])
        return string

    def __call__(self):
        _metrics = {"Accuracy": metrics.accuracy_score(y_true=self.labels, y_pred=self.predicts),
                    "Precision": metrics.precision_score(y_true=self.labels, y_pred=self.predicts),
                    "Recall": metrics.recall_score(y_true=self.labels, y_pred=self.predicts),
                    "F-measure": metrics.f1_score(y_true=self.labels, y_pred=self.predicts),
                    "Precision-Recall AUC": metrics.average_precision_score(y_true=self.labels, y_score=self.scores),
                    "AUC": metrics.roc_auc_score(y_true=self.labels, y_score=self.scores),
                    "MCC": metrics.matthews_corrcoef(y_true=self.labels, y_pred=self.predicts),
                    "Error": self.error()}

        return _metrics

    def log(self):
        excluded = ["Precision-Recall AUC", "AUC"]
        _metrics = self()
        msg = ' - '.join(
            [f"({name[:3]} {round(metric, 3)})" for name, metric in _metrics.items() if name not in excluded])

        logger.log_info('metrics', msg)

    def error(self):
        errors = [(abs(score - (1 if score >= 0.5 else 0))/score)*100 for score, label in zip(self.scores, self.labels)]

        return sum(errors)/len(errors)
</file>

<file path="src/utils/objects/stats.py">
import dataclasses
from dataclasses import dataclass
from typing import List


class Stat:
    def __init__(self, outs=None, loss=0.0, acc=0.0, labels=None):
        if labels is None:
            labels = []
        if outs is None:
            outs = []
        self.outs = outs
        self.labels = labels
        self.loss = loss
        self.acc = acc

    def __add__(self, other):
        return Stat(self.outs + other.outs, self.loss + other.loss, self.acc + other.acc, self.labels + other.labels)

    def __str__(self):
        return f"Loss: {round(self.loss, 4)}; Acc: {round(self.acc, 4)};"


@dataclass
class Stats:
    name: str
    results: List[Stat] = dataclasses.field(default_factory=list)
    total: Stat = Stat()

    def __call__(self, stat):
        self.total += stat
        self.results.append(stat)

    def __str__(self):
        return f"{self.name} {self.mean()}"

    def __len__(self):
        return len(self.results)

    def mean(self):
        res = Stat()
        res += self.total
        res.loss /= len(self)
        res.acc /= len(self)

        return res

    def loss(self):
        return self.mean().loss

    def acc(self):
        return self.mean().acc

    def outs(self):
        return self.total.outs

    def labels(self):
        return self.total.labels
</file>

<file path="joern/graph-for-funcs.sc">
/* graph-for-funcs.scala

   This script returns a Json representation of the graph resulting in combining the
   AST, CGF, and PDG for each method contained in the currently loaded CPG.

   Input: A valid CPG
   Output: Json

   Running the Script
   ------------------
   see: README.md

   The JSON generated has the following keys:

   "functions": Array of all methods contained in the currently loaded CPG
     |_ "function": Method name as String
     |_ "id": Method id as String (String representation of the underlying Method node)
     |_ "AST": see ast-for-funcs script
     |_ "CFG": see cfg-for-funcs script
     |_ "PDG": see pdg-for-funcs script
 */

import scala.jdk.CollectionConverters._

import io.circe.syntax._
import io.circe.generic.semiauto._
import io.circe.{Encoder, Json}

import io.shiftleft.semanticcpg.language.types.expressions.generalizations.CfgNode
import io.shiftleft.codepropertygraph.generated.EdgeTypes
import io.shiftleft.codepropertygraph.generated.NodeTypes
import io.shiftleft.codepropertygraph.generated.nodes
import io.shiftleft.dataflowengineoss.language._
import io.shiftleft.semanticcpg.language._
import io.shiftleft.semanticcpg.language.types.expressions.Call
import io.shiftleft.semanticcpg.language.types.structure.Local
import io.shiftleft.codepropertygraph.generated.nodes.MethodParameterIn

import overflowdb._
import overflowdb.traversal._

final case class GraphForFuncsFunction(function: String,
                                       file: String,
                                       id: String,
                                       AST: List[nodes.AstNode],
                                       CFG: List[nodes.AstNode],
                                       PDG: List[nodes.AstNode])
final case class GraphForFuncsResult(functions: List[GraphForFuncsFunction])

implicit val encodeEdge: Encoder[OdbEdge] =
  (edge: OdbEdge) =>
    Json.obj(
      ("id", Json.fromString(edge.toString)),
      ("in", Json.fromString(edge.inNode.toString)),
      ("out", Json.fromString(edge.outNode.toString))
    )

implicit val encodeNode: Encoder[nodes.AstNode] =
  (node: nodes.AstNode) =>
    Json.obj(
      ("id", Json.fromString(node.toString)),
      ("edges",
        Json.fromValues((node.inE("AST", "CFG").l ++ node.outE("AST", "CFG").l).map(_.asJson))),
      ("properties", Json.fromValues(node.propertyMap.asScala.toList.map { case (key, value) =>
        Json.obj(
          ("key", Json.fromString(key)),
          ("value", Json.fromString(value.toString))
        )
      }))
    )

implicit val encodeFuncFunction: Encoder[GraphForFuncsFunction] = deriveEncoder
implicit val encodeFuncResult: Encoder[GraphForFuncsResult] = deriveEncoder

@main def main(): Json = {
  GraphForFuncsResult(
    cpg.method.map { method =>
      val methodName = method.fullName
      val methodId = method.toString
      val methodFile = method.location.filename
      val methodVertex: Vertex = method //TODO MP drop as soon as we have the remainder of the below in ODB graph api

      val astChildren = method.astMinusRoot.l
      val cfgChildren = method.out(EdgeTypes.CONTAINS).asScala.collect { case node: nodes.CfgNode => node }.toList

      val local = new NodeSteps(
        methodVertex
          .out(EdgeTypes.CONTAINS)
          .hasLabel(NodeTypes.BLOCK)
          .out(EdgeTypes.AST)
          .hasLabel(NodeTypes.LOCAL)
          .cast[nodes.Local])
      val sink = local.evalType(".*").referencingIdentifiers.dedup
      val source = new NodeSteps(methodVertex.out(EdgeTypes.CONTAINS).hasLabel(NodeTypes.CALL).cast[nodes.Call]).nameNot("<operator>.*").dedup

      val pdgChildren = sink
        .reachableByFlows(source)
        .l
        .flatMap { path =>
          path.elements
            .map {
              case trackingPoint @ (_: MethodParameterIn) => trackingPoint.start.method.head
              case trackingPoint                          => trackingPoint.cfgNode
            }
        }
        .filter(_.toString != methodId)

      GraphForFuncsFunction(methodName, methodFile, methodId, astChildren, cfgChildren, pdgChildren.distinct)
    }.l
  ).asJson
}
</file>

<file path="src/prepare/cpg_generator.py">
import json
import re
import subprocess
import os.path
import os
import time
from .cpg_client_wrapper import CPGClientWrapper
#from ..data import datamanager as data


def funcs_to_graphs(funcs_path):
    client = CPGClientWrapper()
    # query the cpg for the dataset
    print(f"Creating CPG.")
    graphs_string = client(funcs_path)
    # removes unnecessary namespace for object references
    graphs_string = re.sub(r"io\.shiftleft\.codepropertygraph\.generated\.", '', graphs_string)
    graphs_json = json.loads(graphs_string)

    return graphs_json["functions"]


def graph_indexing(graph):
    idx = int(graph["file"].split(".c")[0].split("/")[-1])
    del graph["file"]
    return idx, {"functions": [graph]}


def joern_parse(joern_path, input_path, output_path, file_name):
    out_file = file_name + ".bin"
    joern_parse_call = subprocess.run(["./" + joern_path + "joern-parse", input_path, "--output", output_path + out_file],
                                      stdout=subprocess.PIPE, text=True, check=True)
    print(str(joern_parse_call))
    return out_file


def joern_create(joern_path, in_path, out_path, cpg_files):
    joern_process = subprocess.Popen(["./" + joern_path + "joern"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    json_files = []
    for cpg_file in cpg_files:
        json_file_name = f"{cpg_file.split('.')[0]}.json"
        json_files.append(json_file_name)

        print(in_path+cpg_file)
        if os.path.exists(in_path+cpg_file):
            json_out = f"{os.path.abspath(out_path)}/{json_file_name}"
            import_cpg_cmd = f"importCpg(\"{os.path.abspath(in_path)}/{cpg_file}\")\r".encode()
            script_path = f"{os.path.dirname(os.path.abspath(joern_path))}/graph-for-funcs.sc"
            run_script_cmd = f"cpg.runScript(\"{script_path}\").toString() |> \"{json_out}\"\r".encode()
            joern_process.stdin.write(import_cpg_cmd)
            print(joern_process.stdout.readline().decode())
            joern_process.stdin.write(run_script_cmd)
            print(joern_process.stdout.readline().decode())
            joern_process.stdin.write("delete\r".encode())
            print(joern_process.stdout.readline().decode())
    try:
        outs, errs = joern_process.communicate(timeout=60)
    except subprocess.TimeoutExpired:
        joern_process.kill()
        outs, errs = joern_process.communicate()
    if outs is not None:
        print(f"Outs: {outs.decode()}")
    if errs is not None:
        print(f"Errs: {errs.decode()}")
    return json_files


def json_process(in_path, json_file):
    if os.path.exists(in_path+json_file):
        with open(in_path+json_file) as jf:
            cpg_string = jf.read()
            cpg_string = re.sub(r"io\.shiftleft\.codepropertygraph\.generated\.", '', cpg_string)
            cpg_json = json.loads(cpg_string)
            container = [graph_indexing(graph) for graph in cpg_json["functions"] if graph["file"] != "N/A"]
            return container
    return None

'''
def generate(dataset, funcs_path):
    dataset_size = len(dataset)
    print("Size: ", dataset_size)
    graphs = funcs_to_graphs(funcs_path[2:])
    print(f"Processing CPG.")
    container = [graph_indexing(graph) for graph in graphs["functions"] if graph["file"] != "N/A"]
    graph_dataset = data.create_with_index(container, ["Index", "cpg"])
    print(f"Dataset processed.")

    return data.inner_join_by_index(dataset, graph_dataset)
'''

# client = CPGClientWrapper()
# client.create_cpg("../../data/joern/")
# joern_parse("../../joern/joern-cli/", "../../data/joern/", "../../joern/joern-cli/", "gen_test")
# print(funcs_to_graphs("/data/joern/"))
"""
while True:
    raw = input("query: ")
    response = client.query(raw)
    print(response)
"""
</file>

<file path="README.md">
# Devign

Implementation of Devign Model in Python with code for processing the dataset and generation of Code Property Graphs.
###### This project is under development. For now, just the Abstract Syntax Tree is considered for the graph embedding of code and model training.

## Table of Contents

* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
     * [Software](#software)
     * [Python Libraries](#python-libraries)
  * [Setup](#setup)
* [Structure](#structure)
* [Usage](#usage)
    * [Dataset](#dataset)
	* [Fields](#fields)
    * [Baseline "main.py"](#baseline-mainpy)
        * [Create Task](#create-task)
        * [Embed Task](#embed-task)
        * [Process Task](#process-task)
* [Results](#results)
* [Roadmap](#roadmap)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Install the necessary dependencies before running the project:
<br/>
##### Software:
* [Joern](https://joern.io/docs/)
* [Python (=>3.6)](https://www.python.org/)
##### Python Libraries:
* [Pandas (>=1.0.1)](https://pandas.pydata.org/)
* [scikit-learn (>=0.22.2)](https://scikit-learn.org/stable/)
* [PyTorch (>=1.4.0)](https://pytorch.org/)
* [PyTorch Geometric (>=1.4.2)](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html)
* [Gensim (>=3.8.1)](https://radimrehurek.com/gensim/)
* [cpgclientlib (>=0.11.111)](https://pypi.org/project/cpgclientlib/)

### Notes

---
These notes might save you some time:

* Changes to the ```configs.json``` structure need to be reflected in the ```configs.py``` script.
* **PyTorch Geometric** has several dependencies that need to match, including **PyTorch**. 
Follow the installation steps on their website.
* Joern processing might be slow and even freeze your OS, that depends on your system's specifications.
Choose a smaller size for the chunks that are processed when splitting the dataset during the **Create** task.
That can be done by changing the ```"slice_size"``` value under ```"create"``` in the configurations file ```configs.json``` 
* In the ```"slice_size"``` file, the nodes are filtered and discarded if the size is greater than the limit configured.
* When changing the number of nodes considered for processing, ```"nodes_dim"``` under ```"embed"``` 
needs to match ```"in_channels"```, under ```"devign" -> "model" -> "conv_args" -> "conv1d_1"```.
* The embedding size is equal to Word2Vec vector size plus 1.
* When executing the **Create** task, a directory named ```joern``` is created and deleted automatically under ```'project'\data\```.
* The dataset split for modeling during **Process** task is done under ```src/data/datamanger.py```. The sets are balanced and the train/val/test ratio are 0.8/0.1/0.1 respectively.
* The script **graph-for-funcs.sc** queries the CPG graphs from Joern. That script has a minor change to make it possible to track the files to the CPGs generated. The last time was failing because dependencies in Joern changed and needed the updated version. I assume you can find it in their latest version. I suggested you look at issue **#3**. Those CPGs are saved in a JSON file, check function "joern_create" line 48, it prints the CPG created in Joern to a JSON file **... .toString() |> \"{json_out}\"**,  and that file is processed by the function "json_process". Both those functions are in the file **devign/src/prepare/cpg_generator.py**. If you have troubles creating the CPG JSON file with Joern, I advise you to do what you are trying manually in Joern. Create a new project pointing to the dataset folder containing all the files and query the CPG with the  **graph-for-funcs.sc** script that's built-in, then export it to a file with .toString() |>. Joern commands are quite easy to understand and they have good support on Gitter. As well, follow the [commit](https://github.com/epicosy/devign/commit/87d11378eabaeea3a3c6f2bc5748a6eaf0e32b3c) to understand the changes I've previously made.
* Tested on Ubuntu 18.04/19.04

### Setup

---
###### __For now this project is not pip installable. With the proper use cases will be implemented.__

This section gives the steps, explanations and examples for getting the project running.
#### 1) Clone this repo

``` console
$ git clone https://github.com/epicosy/devign/devign.git
```

#### 2) Install Prerequisites

#### 3) Configure the project
Verify you have the correct directory structure by matching with the ```"paths"``` in the configurations file ```configs.json```.
The dataset related files that are generated are saved under those paths. 
#### 4) Joern
This step is only necessary for the **Create** task.
Follow the instructions on [Joern's documentation page](https://joern.io/docs/) and install Joern's command line tools
under ```'project'\joern\joern-cli\ ```.
<br/>

## Structure

---
``` 
├── LICENSE
├── README.md                       <- The top-level README for developers using this project.
├── data
│   ├── cpg                         <- Dataset with CPGs.
│   ├── input                       <- Cannonical dataset for modeling.
│   ├── model                       <- Trained models.
│   ├── raw                         <- The original, immutable data dump.
│   ├── tokens                      <- Tokens dataset files generated from the raw data functions.
│   └── w2v                         <- Word2Vec model files for initial embeddings.
│
├── joern
│   ├── joern-cli                   <- Joern command line tools for creating and analyzing code property graphs.
│   └── graphs-for-funcs.sc         <- Script that returns in Json format the AST, CGF, and PDG for each method 
│                                       contained in the loaded CPG.
│
├── src                             <- Source code for use in this project.
│   ├── __init__.py                 <- Makes src a Python package.
│   │
│   ├── data                        <- Data handling scripts.
│   │   ├── __init__.py             <- Makes data a Python package.
│   │   └── datamanger.py           <- Module for the most essential operations on the dataset.
│   │
│   ├── prepare                     <- Package for CPG generation and representation.
│   │   ├── __init__.py             <- Makes prepare a Python package.
│   │   ├── cpg_client_wrapper.py   <- Simple class wrapper for the CpgClient that interacts with the Joern REST server 
│   │   ├── cpg_generator.py        <- Ad-hoc script for creating CPGs with Joern and processing the results.
│   │   └── embeddings.py           <- Module that embeds the graph nodes into node features.
│   │
│   ├── process                     <- Scripts for modeling and predictions.
│   │   ├── __init__.py             <- Makes process a Python package.
│   │   ├── devign.py               <- Module that implements the devign model.
│   │   ├── loader_step.py          <- Module for one epoch iteration over dataset
│   │   ├── model.py                <- Module that implements the devign neural network.
│   │   ├── modeling.py             <- Module for training and prediction the model.
│   │   ├── step.py                 <- Module that performs a forward step on a batch for train/val/test loop.
│   │   └── stopping.py             <- Module that performs early stopping.
│   │
│   │
│   └── utils                       <- Package with helper components like functions and classes, used across 
│       │                              the project.
│       ├── __init__.py             <- Makes utils a Python package.
│       ├── log.py                  <- Module for logging modules messages.
│       ├── functions               <- Auxiliar functions for processing.
│       │   ├── __init__.py         <- Makes functions a Python package
│       │   ├── cpg.py              <- Module with auxiliar functions for CPGs.
│       │   ├── digraph.py          <- Module for creating digraphs from nodes.
│       │   └── parase.py           <- Module for parsing source code into tokens.
│       │ 
│       └── objects                 <- Auxiliar data classes with basic methods.
│           ├── __init__.py         <- Makes objects a Python package.
│           ├── cpg                 <- Auxiliar data classes for representing and handling the Json graphs.
│           │   ├── __init__.py     
│           │   ├── ast.py
│           │   ├── edge.py
│           │   ├── function.py
│           │   ├── node.py
│           │   └── properties.py
│           │
│           ├── input_dataset.py    <- Custom wrapper for Torch Dataset.
│           ├── metrics.py          <- Module for evaluating the results.
│           └── stats.py            <- Module for handling raw results.
│       
│
├── configs.py                      <- Configuration management script.
├── configs.json                    <- Project configurations used by main.py. 
└── main.py                         <- Main script file that joins the modules into executable tasks. 
```

##Usage

### Dataset

---
The dataset used is the [partial dataset](https://sites.google.com/view/devign) released by the authors.
The dataset is handled with Pandas and the file ```src/data/datamanger.py``` contains wrapper functions for the most essential operations. 
<br/>
<br/>
A small sample of 994 entries from the original dataset is available for testing purposes. 
The sample dataset contains functions from the **FFmpeg** project with a maximum of 287 nodes per function.
For each task, the necessary dataset files are available under the respective folders.
<br/>
<br/>
For example, under ```data/cpg``` are available the datasets with the graphs constituting the CPG for the functions.

#### Fields

|project|               commit_id                  | target |                           func                    |
|------:|:----------------------------------------:| ------:| -------------------------------------------------:|
|FFmpeg | 973b1a6b9070e2bf17d17568cbaf4043ce931f51 |    0   | static av_cold int vdadec_init(AVCodecContext ... |
|FFmpeg | 321b2a9ded0468670b7678b7c098886930ae16b2 |    0   | static int transcode(AVFormatContext **output_... |
|FFmpeg | 5d5de3eba4c7890c2e8077f5b4ae569671d11cf8 |    0   | static void v4l2_free_buffer(void *opaque, uin... |
|FFmpeg | 32bf6550cb9cc9f487a6722fe2bfc272a93c1065 |    0   | int ff_get_wav_header(AVFormatContext *s, AVIO... |
|FFmpeg | 57d77b3963ce1023eaf5ada8cba58b9379405cc8 |    0   | int av_opencl_buffer_write(cl_mem dst_cl_buf, ... |
|       |   ...                                    |   ...  |  ...                                          ... |
|qemu   | 1ea879e5580f63414693655fcf0328559cdce138 |    0   | static int no_init_in (HWVoiceIn *hw, audsetti... |
|qemu   | f74990a5d019751c545e9800a3376b6336e77d38 |    0   | uint32_t HELPER(stfle)(CPUS390XState *env, uin... |
|qemu   | a89f364ae8740dfc31b321eed9ee454e996dc3c1 |    0   | static void pxa2xx_fir_write(void *opaque, hwa... |
|qemu   | 39fb730aed8c5f7b0058845cb9feac0d4b177985 |    0   | static void disas_thumb_insn(CPUARMState *env,... |
|FFmpeg | 7104c23bd1a1dcb8a7d9e2c8838c7ce55c30a331 |    0   | static void rv34_pred_mv(RV34DecContext *r, in... |


### Baseline "main.py"

---
The script ```main.py``` contains functions that put together the modules into executable tasks for the baseline approach.
It can be used as example to elaborate custom functionalities.
<br/>
<br/>
The basic baseline transforms the dataset to the input for the model, proceeding with it's training and evaluation. 
The tasks that compose it are Create, Embed and Process.
``` console
$ python main.py -c -e -p.
```

For each task, verify that the correct files are in the respective folders.
For example, executing the **Process** task requires the input datasets that contain 
the embedded graphs with the associated labels.

#### Create Task
This is the first task where the dataset is filtered (optionally) and augmented with a column that 
contains the respective Code Property Graph (CPG).
<br/>
<br/>
Functions in the dataset are written to files into a target directory which Joern is queried with for creating the CPG. 
After the CPG creation, Joern is queried with the script "graph-for-funcs.sc" which creates the graphs from the CPG.
Those are returned in JSON format, containing all the functions with the respective AST, CFG and PDG graphs.

Execute with:

``` console
$ python main.py -c
```
Filtering the dataset can be done with ```data.apply_filter(raw: pandas.Dataframe, select: callable)``` 
under ```create_task``` function.

#### Embed Task
This task transforms the source code functions into tokens which are used to generate and train the word2vec model 
for the initial embeddings. The nodes embeddings are done as explained in the paper, for now just for the AST: 
![Node Representation](https://lh6.googleusercontent.com/DcfjhgnCH23Zsw7FZ5_WFr2M-4Tzn9uO8U32QpbaUBiBOjfi3-yRE0mDT7SEIEe4OorV8-BvDppk3CGxY8AfPxCAdeZEkkf47K9X_W-mfc5QSCB8VIU=w1175)

Execute with:
``` console
$ python main.py -e

```

##### Tokenization example
Source code:
```
'static void v4l2_free_buffer(void *opaque, uint8_t *unused)
{

    V4L2Buffer* avbuf = opaque;

    V4L2m2mContext *s = buf_to_m2mctx(avbuf);



    if (atomic_fetch_sub(&avbuf->context_refcount, 1) == 1) {

        atomic_fetch_sub_explicit(&s->refcount, 1, memory_order_acq_rel);



        if (s->reinit) {

            if (!atomic_load(&s->refcount))

              sem_post(&s->refsync);

        } else if (avbuf->context->streamon)

            ff_v4l2_buffer_enqueue(avbuf);



        av_buffer_unref(&avbuf->context_ref);

    }

}
'
```
Tokens:
['static', 'void', 'FUN1', '(', 'void', '*', 'VAR1', ',', 'uint8_t', '*', 'VAR2)', '{', 'VAR3', '*', 'VAR4', '=', 'VAR1', ';', 'V4L2m2mContext', '*', 'VAR5', '=', 'FUN2', '(', 'VAR4)', ';', 'if', '(', 'FUN3', '(', '&', 'VAR4', '-', '>', 'VAR6', ',', '1)', '==', '1)', '{', 'FUN4', '(', '&', 'VAR5', '-', '>', 'VAR7', ',', '1', ',', 'VAR8)', ';', 'if', '(', 'VAR5', '-', '>', 'VAR9)', '{', 'if', '(', '!', 'FUN5', '(', '&', 'VAR5', '-', '>', 'VAR7))', 'FUN6', '(', '&', 'VAR5', '-', '>', 'VAR10)', ';', '}', 'else', 'if', '(', 'VAR4', '-', '>', 'VAR11', '-', '>', 'VAR12)', 'FUN7', '(', 'VAR4)', ';', 'FUN8', '(', '&', 'VAR4', '-', '>', 'VAR13)', ';', '}', '}']

 
#### Process Task
In this task the previous transformed dataset is split into train, validation and test sets which are
 used to train an evaluate the model. The accuracy from training output is **softmax accuracy**.

Execute with:
``` console
$ python main.py -p
```

Enable EarlyStopping for training with:

``` console
$ python main.py -pS
``` 

## Results
Train/Val/Test ratios - 0.8/0.1/0.1
Example results of training with early stopping on the sample dataset.
Last Model checkpoint at 5 epochs.
 
Parameters used:
 - "learning_rate" : 1e-4
 - "weight_decay" : 1.3e-6
 - "loss_lambda" : 1.3e-6
 - "epochs" : 100
 - "patience" : 10
 - "batch_size" : 8
 - "dataset_ratio" : 1 (Total entries)
 - "shuffle" : false

True Pos.: 37, False Pos.: 27, True Neg.: 22, False Neg.: 15
Accuracy: 0.5841584158415841
Precision: 0.578125
Recall: 0.7115384615384616
F-measure: 0.6379310344827586
Precision-Recall AUC: 0.5388430220841324
AUC: 0.5569073783359497
MCC: 0.166507096257419

Example results of training without early stopping on the sample dataset.
 
Parameters used:
 - "learning_rate" : 1e-4
 - "weight_decay" : 1.3e-6
 - "loss_lambda" : 1.3e-6
 - "epochs" : 30
 - "patience" : 10
 - "batch_size" : 8
 - "dataset_ratio" : 1 (Total entries)
 - "shuffle" : false

True Pos.: 38, False Pos.: 34, True Neg.: 15, False Neg.: 14
Accuracy: 0.5247524752475248
Precision: 0.5277777777777778
Recall: 0.7307692307692307
F-measure: 0.6129032258064515
Precision-Recall AUC: 0.5592493611149129
AUC: 0.5429748822605965
MCC: 0.04075331061223071
Error: 53.56002758457897


## Roadmap

See the [open issues](https://github.com/epicosy/devign/issues) for a list of proposed features (and known issues).

## Authors
* **Yaqin Zhou**, **Shangqing Liu**, **Jingkai Siow**, **Xiaoning Du**, **Yang Liu**
* *Initial work* - [Devign Paper](https://arxiv.org/pdf/1909.03496v1.pdf), [Node Representation and Datasets](https://sites.google.com/view/devign/home)

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact

Eduard Pinconschi - eduard.pinconschi@tecnico.ulisboa.pt

## Acknowledgments
Guidance and ideas for some parts from:

* [Transformer for Software Vulnerability Detection](https://github.com/hazimhanif/svd-transformer)
* [SySeVR: A Framework for Using Deep Learning to Detect Vulnerabilities](https://github.com/SySeVR/SySeVR)
* [VulDeePecker algorithm implemented in Python](https://github.com/johnb110/VDPython)
</file>

</files>
