#! /usr/bin/env python
# encoding: utf-8

import os
from waflib import Task, TaskGen

APPNAME = 'function_ref'
VERSION = '1.0.0'

def build(bld):
    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_FUNCTION_REF_VERSION="{}"'.format(VERSION))

    # Path to the function_ref repo
    sources = bld.dependency_node("function_ref-source")

    # Export own includes
    bld(name='function_ref',
        export_includes=[sources])

    if bld.is_toplevel():

        # The actual sources are stored outside this repo - so we manually
        # add them for the solution generator
        bld.solution_name = 'foo.sln'
        bld.msvs_extend_sources = [sources]

        # Only build tests when executed from the top-level wscript,
        # i.e. not when included as a dependency

        bld.program(
            features='cxx test',
            source=sources.ant_glob('tests/*.cpp'),
            target='function_ref_tests',
            use=['function_ref'])
