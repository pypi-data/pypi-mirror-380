import click
import os
import base64
import mimetypes
from enum import Enum
from accqsure.cli import cli, pass_config


class FILE_FORMATS(str, Enum):
    DOCX = "docx"
    TEXT = "text"
    XLSX = "xlsx"
    CSV = "csv"
    PDF = "pdf"


DOCUMENT_TYPES = {
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": FILE_FORMATS.DOCX,
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": FILE_FORMATS.XLSX,
    "text/plain": FILE_FORMATS.TEXT,
    "application/json": FILE_FORMATS.TEXT,
    "text/csv": FILE_FORMATS.CSV,
    "text/markdown": FILE_FORMATS.TEXT,
    "application/pdf": FILE_FORMATS.PDF,
}


@cli.group()
@pass_config
def plot(config):
    """AccQsure plot commands."""
    pass


@plot.command()
@pass_config
def list(
    config,
):
    """List plots."""
    data = [
        ["ID", "NAME", "STATUS"],
        [
            "-" * 80,
            "-" * 80,
            "-" * 80,
        ],
    ]
    # TODO: implement cursor function
    plots, _ = config.accqsure.run(config.accqsure.client.plots.list())
    for doc in plots:
        data.append(
            [
                doc.id,
                doc.name,
                doc.status,
            ]
        )
    for row in data:
        click.echo(
            "{: >26.24} {: >40.38} {: >14.12} " "".format(*row),
            file=config.stdout,
        )


# @inspection.command()
# @click.option("--type", "-t", type=click.STRING, required=True)
# @click.option(
#     "--file",
#     "-f",
#     type=click.Path(
#         exists=True, file_okay=True, dir_okay=False, resolve_path=True
#     ),
#     required=True,
# )
# @click.argument("name", type=click.STRING, required=True)
# @click.argument("doc-id", type=click.STRING, required=True)
# @pass_config
# def create(config, name, doc_id, type, file):
#     """
#     Create an inspection

#     """

#     mime_type, _ = mimetypes.guess_type(file)

#     if mime_type not in DOCUMENT_TYPES:
#         raise ValueError(
#             f"Invalid file type. Detected MIME type '{mime_type}' not in allowed types: {', '.join(DOCUMENT_TYPES.values())}"
#         )

#     file_type = DOCUMENT_TYPES[mime_type]

#     with open(os.path.expanduser(file), "rb") as f:
#         value = f.read()
#         base64_contents = base64.b64encode(value).decode("utf-8")

#     title = os.path.splitext(os.path.basename(file))[0]
#     result = config.accqsure.run(
#         config.accqsure.client.documents.create(
#             document_type_id=document_type_id,
#             name=name,
#             doc_id=doc_id,
#             contents=dict(
#                 title=title, type=file_type, base64_contents=base64_contents
#             ),
#         )
#     )
#     click.echo(result)
