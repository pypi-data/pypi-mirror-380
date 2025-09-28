# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_polly import type_defs as bs_td


class POLLYCaster:

    def describe_voices(
        self,
        res: "bs_td.DescribeVoicesOutputTypeDef",
    ) -> "dc_td.DescribeVoicesOutput":
        return dc_td.DescribeVoicesOutput.make_one(res)

    def get_lexicon(
        self,
        res: "bs_td.GetLexiconOutputTypeDef",
    ) -> "dc_td.GetLexiconOutput":
        return dc_td.GetLexiconOutput.make_one(res)

    def get_speech_synthesis_task(
        self,
        res: "bs_td.GetSpeechSynthesisTaskOutputTypeDef",
    ) -> "dc_td.GetSpeechSynthesisTaskOutput":
        return dc_td.GetSpeechSynthesisTaskOutput.make_one(res)

    def list_lexicons(
        self,
        res: "bs_td.ListLexiconsOutputTypeDef",
    ) -> "dc_td.ListLexiconsOutput":
        return dc_td.ListLexiconsOutput.make_one(res)

    def list_speech_synthesis_tasks(
        self,
        res: "bs_td.ListSpeechSynthesisTasksOutputTypeDef",
    ) -> "dc_td.ListSpeechSynthesisTasksOutput":
        return dc_td.ListSpeechSynthesisTasksOutput.make_one(res)

    def start_speech_synthesis_task(
        self,
        res: "bs_td.StartSpeechSynthesisTaskOutputTypeDef",
    ) -> "dc_td.StartSpeechSynthesisTaskOutput":
        return dc_td.StartSpeechSynthesisTaskOutput.make_one(res)

    def synthesize_speech(
        self,
        res: "bs_td.SynthesizeSpeechOutputTypeDef",
    ) -> "dc_td.SynthesizeSpeechOutput":
        return dc_td.SynthesizeSpeechOutput.make_one(res)


polly_caster = POLLYCaster()
