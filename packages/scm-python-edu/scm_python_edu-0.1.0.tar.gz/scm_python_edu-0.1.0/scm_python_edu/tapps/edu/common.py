import numbers
import yaml

# import aspose.words as aw
import sys, os, datetime, math
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext

log = tl.log


def parse_python_extension_context(questions: list[list] = []):
    generate_date = "{:%Y-%m-%d}".format(datetime.datetime.now())
    plugin_folder: str = os.path.join(
        os.environ.get("Synology_Drive_HOME"), "shared", "隐私", "上中东初中", "数学"
    )
    if not os.path.exists(plugin_folder):
        log.error(f"{plugin_folder} is not exists")
        sys.exit(1)
    context = {"GENERATED_DATE": generate_date}
    for question in questions:
        assert isinstance(question, list) and len(
            question
        ), f"question is list expected, got: {question}"
        key_word: str = question[0]
        statements: str = question[1]
        question_func: function = question[2]
        assert (
            isinstance(statements, list) and statements
        ), f"statements is list expected, got: {key_word} {statements}"
        half_st = int(len(statements) / 2)
        question_output: list[str] = []
        if len(statements) == 1:
            context[key_word] = question_func(statements[0], "")
        else:
            for index in range(0, half_st):
                question_output.append(
                    question_func(statements[2 * index], statements[2 * index + 1])
                )
            context[key_word] = "\n".join(question_output)
    return plugin_folder, context


def conver_md_to_pdf(md_file: str):
    pdf_file = md_file.replace(".md", ".pdf")
    # aw.Document(md_file).save(pdf_file)
