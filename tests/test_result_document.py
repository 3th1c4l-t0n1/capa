# Copyright (C) 2020 Mandiant, Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
# You may obtain a copy of the License at: [package root]/LICENSE.txt
# Unless required by applicable law or agreed to in writing, software distributed under the License
#  is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

from typing import Dict, Tuple
import textwrap
import fixtures
from fixtures import *

import capa
import capa.engine as ceng
import capa.render.result_document as rdoc
import capa.features.freeze.features as frzf


def test_optional_node_from_capa():
    node = rdoc.node_from_capa(
        ceng.Some(
            0,
            [],
        )
    )
    assert isinstance(node, rdoc.StatementNode)
    assert isinstance(node.statement, rdoc.CompoundStatement)
    assert node.statement.type == rdoc.CompoundStatementType.OPTIONAL


def test_some_node_from_capa():
    node = rdoc.node_from_capa(
        ceng.Some(
            1,
            [
                capa.features.insn.Number(0),
            ],
        )
    )
    assert isinstance(node, rdoc.StatementNode)
    assert isinstance(node.statement, rdoc.SomeStatement)


def test_range_node_from_capa():
    node = rdoc.node_from_capa(
        ceng.Range(
            capa.features.insn.Number(0),
        )
    )
    assert isinstance(node, rdoc.StatementNode)
    assert isinstance(node.statement, rdoc.RangeStatement)


def test_subscope_node_from_capa():
    node = rdoc.node_from_capa(
        ceng.Subscope(
            capa.rules.Scope.BASIC_BLOCK,
            capa.features.insn.Number(0),
        )
    )
    assert isinstance(node, rdoc.StatementNode)
    assert isinstance(node.statement, rdoc.SubscopeStatement)


def test_and_node_from_capa():
    node = rdoc.node_from_capa(
        ceng.And(
            [
                capa.features.insn.Number(0),
            ],
        )
    )
    assert isinstance(node, rdoc.StatementNode)
    assert isinstance(node.statement, rdoc.CompoundStatement)
    assert node.statement.type == rdoc.CompoundStatementType.AND


def test_or_node_from_capa():
    node = rdoc.node_from_capa(
        ceng.Or(
            [
                capa.features.insn.Number(0),
            ],
        )
    )
    assert isinstance(node, rdoc.StatementNode)
    assert isinstance(node.statement, rdoc.CompoundStatement)
    assert node.statement.type == rdoc.CompoundStatementType.OR


def test_not_node_from_capa():
    node = rdoc.node_from_capa(
        ceng.Not(
            [
                capa.features.insn.Number(0),
            ],
        )
    )
    assert isinstance(node, rdoc.StatementNode)
    assert isinstance(node.statement, rdoc.CompoundStatement)
    assert node.statement.type == rdoc.CompoundStatementType.NOT


def test_os_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.OS(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.OSFeature)


def test_arch_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.Arch(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.ArchFeature)


def test_format_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.Format(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.FormatFeature)


def test_match_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.MatchedRule(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.MatchFeature)


def test_characteristic_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.Characteristic(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.CharacteristicFeature)


def test_substring_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.Substring(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.SubstringFeature)


def test_regex_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.Regex(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.RegexFeature)


def test_class_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.Class(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.ClassFeature)


def test_namespace_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.Namespace(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.NamespaceFeature)


def test_bytes_node_from_capa():
    node = rdoc.node_from_capa(capa.features.common.Bytes(b""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.BytesFeature)


def test_export_node_from_capa():
    node = rdoc.node_from_capa(capa.features.file.Export(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.ExportFeature)


def test_import_node_from_capa():
    node = rdoc.node_from_capa(capa.features.file.Import(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.ImportFeature)


def test_section_node_from_capa():
    node = rdoc.node_from_capa(capa.features.file.Section(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.SectionFeature)


def test_function_name_node_from_capa():
    node = rdoc.node_from_capa(capa.features.file.FunctionName(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.FunctionNameFeature)


def test_api_node_from_capa():
    node = rdoc.node_from_capa(capa.features.insn.API(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.APIFeature)


def test_property_node_from_capa():
    node = rdoc.node_from_capa(capa.features.insn.Property(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.PropertyFeature)


def test_number_node_from_capa():
    node = rdoc.node_from_capa(capa.features.insn.Number(0))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.NumberFeature)


def test_offset_node_from_capa():
    node = rdoc.node_from_capa(capa.features.insn.Offset(0))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.OffsetFeature)


def test_mnemonic_node_from_capa():
    node = rdoc.node_from_capa(capa.features.insn.Mnemonic(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.MnemonicFeature)


def test_operand_number_node_from_capa():
    node = rdoc.node_from_capa(capa.features.insn.OperandNumber(0, 0))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.OperandNumberFeature)


def test_operand_offset_node_from_capa():
    node = rdoc.node_from_capa(capa.features.insn.OperandOffset(0, 0))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.OperandOffsetFeature)


def test_basic_block_node_from_capa():
    node = rdoc.node_from_capa(capa.features.basicblock.BasicBlock(""))
    assert isinstance(node, rdoc.FeatureNode)
    assert isinstance(node.feature, frzf.BasicBlockFeature)

def test_json_to_rdoc (capsys, tmpdir):
    path = fixtures.get_data_path_by_name("pma01-01")
    assert capa.main.main([path, "-j"]) == 0
    temp_file = tmpdir.join("capa.json")
    temp_file.write(capsys.readouterr().out)
    assert isinstance(rdoc.ResultDocument.parse_raw(temp_file),rdoc.ResultDocument)