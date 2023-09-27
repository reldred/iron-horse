# Various needed programs
GIT = git
PYTHON3 = python3
SED = sed
ZIP = zip

NMLC = nmlc
GRFCODEC = grfcodec
GRFID = grfid

GIT_INFO = $(PYTHON3) src/polar_fox/git_info.py
FILL_TEMPLATE = bin/fill-template
FIND_FILES = bin/find-files
MK_ARCHIVE = bin/mk-archive


# Project details
PROJECT_NAME = iron-horse

-include Makefile.local

EXPORTED = no
ifeq ($(strip $(EXPORTED)),no)
  # Not exported source, therefore regular checkout
  REPO_INFO = $(shell $(GIT_INFO))
  REPO_REVISION = $(word 1,$(REPO_INFO))
  # we pick the 5th item from git info for Horse, as Horse uses a monorepo strategy and tags/versions need special handling
  REPO_TAG_OR_VERSION = $(word 5,$(REPO_INFO))
else
  # Exported version, lines below should get modified in 'bundle_src' target
  REPO_REVISION = ${exported_revision}
  REPO_TAG_OR_VERSION = ${exported_version}
endif

REPO_TITLE = "$(PROJECT_NAME) $(REPO_TAG_OR_VERSION)"
PROJECT_VERSIONED_NAME = $(PROJECT_NAME)
# optional make args that will be passed through to python
ifdef GRF
  GRF_NAMES = iron-$(GRF)
else
  GRF_NAMES = iron-horse iron-ibex iron-moose
  GRF = 'ALL'
endif
ifdef PW
    pool-workers = --pool_workers=$(PW)
endif
ifeq ($(SC), True)
  suppress-cargo-sprites = --suppress-cargo-sprites
endif
ifeq ($(SD), True)
  suppress-docs = --suppress-docs
endif
# --grf-name needs to be handled differently depending on the python script, so is not included in PY_GLOBAL_ARGS
PY_GLOBAL_ARGS = $(pool-workers) $(suppress-cargo-sprites) $(suppress-docs)

# GRF_FILES include the full path to generated dir and .grf suffixes
GRF_FILES = $(GRF_NAMES:%=generated/%.grf)
NFO_FILES = $(GRF_FILES:.grf=.nfo)
NML_FILES = $(GRF_FILES:.grf=.nml)
LANG_FILES = $(GRF_NAMES:%=generated/lang/%/english.lng)
TAR_FILES = $(GRF_NAMES:%=%-$(REPO_TAG_OR_VERSION).tar)
ZIP_FILE = $(PROJECT_VERSIONED_NAME).zip
MD5_FILE = $(PROJECT_NAME).check.md5
HTML_DOCS = $(GRF_NAMES:%=docs/%/index.html)
# we don't currently bother detecting graphics directly as deps, we rely on python spitting them all out in the compile
# instead we create proxy target (via make) after the python step has completed
GRAPHICS_TARGETS = $(GRF_NAMES:%=generated/graphics/%/make_target)

SOURCE_NAME = $(PROJECT_VERSIONED_NAME)-source
BUNDLE_DIR = bundle_dir

# Build rules
.PHONY: default graphics lang nml grf tar bundle_tar bundle_zip bundle_src clean copy_docs_to_grf_farm release
default: html_docs grf
bundle_tar: tar
bundle_zip: $(ZIP_FILE)
graphics: $(GRAPHICS_TARGETS)
lang: $(LANG_FILES)
nml: $(NML_FILES)
nfo: $(NFO_FILES)
grf: $(GRF_FILES)
tar: $(TAR_FILES)

# default num. pool workers for python compile,
# default is 0 to disable multiprocessing (also avoids multiprocessing pickle failures masking genuine python errors)
PW = 0
# option to suppress cargo sprites, makes minor difference to compile time
SC = 'False'
# remove the @ for more verbose output (@ suppresses command output)
_V ?= @

$(GRAPHICS_TARGETS): $(shell $(FIND_FILES) --ext=.py --ext=.png src)
# we depend on a single proxy target per grf rather than having a list of all the graphics pre-requisites
# a pre-requisites list could actually be generated by python, but it's not proven necessary so far
	$(_V) $(PYTHON3) src/render_graphics.py $(PY_GLOBAL_ARGS) --grf-name=$(subst generated/graphics/,,$(subst /make_target,,$@))
	$(_V) touch $@

$(LANG_FILES): $(shell $(FIND_FILES) --ext=.py --ext=.pynml --ext=.pylng --ext=.toml src)
	$(_V) $(PYTHON3) src/render_lang.py $(PY_GLOBAL_ARGS) --grf-name=$(subst /english.lng,,$(subst generated/lang/,,$@))

$(HTML_DOCS): $(GRAPHICS_TARGETS) $(shell $(FIND_FILES) --ext=.py --ext=.pynml --ext=.pt --ext=.toml --ext=.png src)
	$(_V) $(PYTHON3) src/render_docs.py $(PY_GLOBAL_ARGS) --grf-name=$(subst /index.html,,$(subst docs/,,$@))

html_docs: $(HTML_DOCS)
	$(_V) $(PYTHON3) src/id_report.py -gn=id-report-only

$(NML_FILES): $(shell $(FIND_FILES) --ext=.py --ext=.pynml src)
	$(_V) $(PYTHON3) src/render_nml.py $(PY_GLOBAL_ARGS) --grf-name=$(subst .nml,,$(subst generated/,,$@))

# nmlc is used to compile a nfo file only, which is then used by grfcodec
# this means that the (relatively slow) nmlc stage can be skipped if the nml file is unchanged (only graphics changed)
$(NFO_FILES): %.nfo : %.nml $(LANG_FILES) | $(GRAPHICS_TARGETS)
	$(NMLC) -l generated/lang/$(*F) --verbosity=4 --palette=DEFAULT  --no-optimisation-warning --nfo=$@ $<

# N.B grf codec can't compile into a specific target dir, so after compiling, move the compiled grf to appropriate dir
# grfcodec -n was tried, but was slower and produced a large grf file
$(GRF_FILES): %.grf : %.nfo $(GRAPHICS_TARGETS)
# we use notdir and dir to get the correct paths from the list of target filenames (which include generated dir)
# result is e.g. grfcodec -s -e -c -g 2 iron-horse.grf generated/
	time $(GRFCODEC) -s -e -c -g 2 $(notdir $@) $(dir $<)
	$(_V) mv $(notdir $@) $@

$(TAR_FILES): $(GRF_FILES) $(HTML_DOCS)
# the goal here is a sparse tar for distribution
# path for docs, specific to current prerequisite
# create an intermediate dir, and copy in what we need
# delete the intermediate dir
# this could have been done with a list of targets, and maybe should be, but it was convenient to copy a shell loop from the install target
	echo $(subst .tar,,$@)
	mkdir $(subst .tar,,$@)
	cp $< $(subst .tar,,$@)
	$(_V) for DOC_NAME in readme.txt changelog.txt license.txt ; do \
		cp docs/$(subst generated/,,$(subst .grf,,$<))/$$DOC_NAME $(subst .tar,,$@) ; \
	done
	$(MK_ARCHIVE) --tar --output=$@ $(subst .tar,,$@)
	rm -r $(subst .tar,,$@)

$(ZIP_FILE): $(TAR_FILES)
	$(ZIP) -9rq $(ZIP_FILE) $($@) >/dev/null

$(MD5_FILE): $(GRF_FILES)
	$(GRFID) -m $(GRF_FILES) > $(MD5_FILE)

bundle_src: $(MD5_FILE)
	if test -d $(BUNDLE_DIR); then rm -r $(BUNDLE_DIR); fi
	mkdir $(BUNDLE_DIR)
	$(GIT) archive -t files $(BUNDLE_DIR)/src
	$(FILL_TEMPLATE) --template=Makefile \
		--output=$(BUNDLE_DIR)/src/Makefile \
		"exported_revision=$(REPO_REVISION)" \
		"exported_version=$(REPO_TAG_OR_VERSION)"
	$(SED) -i -e 's/^EXPORTED = no/EXPORTED = yes/' $(BUNDLE_DIR)/src/Makefile
	$(MK_ARCHIVE) --tar --output=$(SOURCE_NAME).tar --base=$(SOURCE_NAME) \
		`$(FIND_FILES) $(BUNDLE_DIR)/src` $(MD5_FILE)

# this expects to find a '../../grf.farm' path relative to the project, and will fail otherwise
copy_docs_to_grf_farm: $(HTML_DOCS)
	$(_V) echo "[COPYING DOCS TO GRF.FARM]"
	$(_V) for GRF_NAME in $(GRF_NAMES) ; do \
		echo .. $$GRF_NAME ; \
    	$(PYTHON3) src/polar_fox/grf_farm.py $$GRF_NAME --nested-docs-by-grf ; \
	done
	$(_V) echo "[DONE]"

# need to clean when releasing, as git version info won't otherwise be regenerated (nml, docs etc) when the only change is git tag (no deps changed)
# we do this by recursive make calls, sequentially, to avoid clean conflicting with other targets by running simultaneously when make -j is invoked for parallel compile
# this is crude and could be done by actually checking git version, but eh, it seems to work
release:
	$(_V) $(MAKE) clean
	$(_V) $(MAKE) bundle_tar
	$(_V) $(MAKE) copy_docs_to_grf_farm

# this is a macOS-specifc install location; the pre-2017 Makefile handled multiple platforms, that could be restored if needed
# remove first, OpenTTD does not like having the _contents_ of the current file change under it, but will handle a removed-and-replaced file correctly
install: default
# note the switch to shell syntax for vars in the for loop, rather than make syntax;
	$(_V) echo "[INSTALLING]"
	$(_V) for GRF_NAME in $(GRF_NAMES) ; do \
		echo .. $$GRF_NAME ; \
		rm ~/Documents/OpenTTD/newgrf/$${GRF_NAME}.grf ; \
		cp generated/$$GRF_NAME.grf ~/Documents/OpenTTD/newgrf/ ; \
	done
	$(_V) echo "[DONE]"


clean:
	$(_V) echo "[CLEANING]"
	$(_V) for f in .chameleon_cache .nmlcache src/__pycache__ src/*/__pycache__ docs generated \
	$(GRF_FILES) $(TAR_FILES) $(ZIP_FILE) $(MD5_FILE) $(BUNDLE_DIR) $(SOURCE_NAME).tar;\
	do if test -e $$f;\
	   then rm -r $$f;\
	   fi;\
	done
	$(_V) echo "[DONE]"
