SHELL = /bin/bash

project_dependencies ?= $(addprefix $(project_root)/, cltl-combot cltl-emissor-data)

git_remote ?= https://github.com/leolani

include util/make/makefile.base.mk
include util/make/makefile.component.mk
include util/make/makefile.py.base.mk
include util/make/makefile.git.mk