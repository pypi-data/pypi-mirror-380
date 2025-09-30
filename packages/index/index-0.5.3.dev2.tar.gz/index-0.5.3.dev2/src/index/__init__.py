#!/usr/bin/env python
# coding=utf-8
# Stan 2024-12-25

import os
import tempfile
from importlib import import_module
from zipfile import ZipFile

from .timer import Timer
from .db import Db
from .print_once import print_once


def main(filename, config={}, parser_options={}, **kargs):
    """
    Main file processing function.

    Initializes the required tools using the supplied `config`,
    then iterates over each file and invokes the handler,
    passing along the `parser_options` for each call.
    """

    verbose = config.get('verbose')
    debug   = config.get('debug')

    # Db object
    db = Db(**config)
    if debug:
        print(db, end="\n\n")

    if os.path.isfile(filename):
        if verbose:
            print(f"=== Filename: {filename} ===")

        # Resolve variant
        variant = parser_options.get('variant', 1)
        parser = import_module(f".index_{variant:03}", __package__)

        # Reg task
        saved, t_id = db.reg_task(parser, parser_options)

        filename = os.path.abspath(filename)
        main_file(filename, db, config, parser, parser_options)

    else:
        if verbose:
            print(f"=== Dirname: {filename} ===")

        filename = os.path.abspath(filename)
        main_dir(filename, db, config, parser_options)


def main_file(filename, db, config, parser, parser_options):
    cname       = config.get('cname', 'dump')
    verbose     = config.get('verbose')
    debug       = config.get('debug')

    file_keys   = parser_options.get('file_keys', {})
    record_keys = parser_options.get('record_keys', {})
    raise_after_exception = parser_options.get('raise_after_exception')

    collection = db[cname]
    dirname = os.path.dirname(filename)

    # iter if archive
    for filename, localname, source in yield_file(filename):
        # Regular file
        if not source:
            name = os.path.basename(filename)

        # Archive item
        else:
            name = filename

        saved, f_id = db.reg_file(name,
            dirname = dirname,
            source = source,
            ** file_keys
        )

        exception_occurred = False
        with Timer(f"[ main_file({f_id}) ] finished", verbose) as t:
            try:
                total = None
                for records, extra in parser.main(localname, db, parser_options):
                    if total is None:
                        total = 0

                    if records:
                        db.insert_many(
                            collection,
                            records,
                            _fid = f_id,
                            ** extra,
                            ** record_keys
                        )
                        if debug and not total:     # First iteration
                            print("Cumulative:", end=' ')

                        total += len(records)

                        if debug:
                            print(total, end=' ')

                    else:
                        if verbose:
                            print("<No records>")

                if debug and total:     # New line after Cumulative message
                    print()

                if verbose and total:
                    print(f"Total: {total}; Grand total: { collection.estimated_document_count() }")

            except Exception as ex:
                print_once(f"Exception occurred in '{filename}': {ex}", key=str(ex))

                db.push_file_record(
                    "exception",
                    type = type(ex).__name__,
                    msg  = ex.msg,
                    __dev = dict(
                        name = str(ex),
                        filename = ex.filename,
                        lineno = ex.lineno,
                        offset = ex.offset,
                        text = ex.text
                    )
                )
                exception_occurred = True

                if raise_after_exception:
                    raise

        if verbose:     # New line after Timer message
            print()

        if not exception_occurred:
            db.push_file_record(
                'skipped' if total is None else 'completed',
                total = total,
                elapsed = t.elapsed
            )


def yield_file(filename, extra_info={}):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    localname = extra_info.get('localname', filename)
    source    = extra_info.get('source', [])

    if ext == '.zip':
        with tempfile.TemporaryDirectory(dir=tempfile.gettempdir()) as temp_dir:
            with ZipFile(localname) as zipf:
                for info in zipf.infolist():
                    if info.file_size:
                        # Store relative path for an archive item
                        # and basename for a regular file
                        filepath = filename if source else os.path.basename(filename)

                        for filename1, localname1, source1 in yield_file(info.filename, {
                            'localname': zipf.extract(info.filename, path=temp_dir, pwd=None),
                            'source': source + [filepath]
                        }):
                            yield filename1, localname1, source1

    else:
        yield filename, localname, source


def main_dir(dirname, db, config, parser_options):
    verbose = config.get('verbose')
#   debug   = config.get('debug')

    # Resolve variant
    variant = parser_options.get('variant', 1)
    parser = import_module(f".index_{variant:03}", __package__)

    # Reg task
    saved, t_id = db.reg_task(parser, parser_options)

    with Timer("[ main_dir ] finished", verbose) as t:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filename = os.path.join(root, name)
                if verbose:
                    print(f"Filename: {filename}")

                main_file(filename, db, config, parser, parser_options)
