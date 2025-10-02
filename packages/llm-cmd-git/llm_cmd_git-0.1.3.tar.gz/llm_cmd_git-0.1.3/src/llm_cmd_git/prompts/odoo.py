from .common import (
    FOOTER,
    LONG_DESCRIPTION,
    OUTPUT_FORMAT,
    SHORT_DESCRIPTION,
    SYSTEM_INSTRUCTIONS,
)

SYSTEM_PROMPT = f"""
{SYSTEM_INSTRUCTIONS}

## Instructions
Commit message should have following structure:

<template>
[<type>] <scope>: <short description>

<long description>

<footer>
</template>

### Type  (Required)
- [FIX] for bug fixes: mostly used in stable version but also valid if you are fixing a recent bug in development version
- [REF] for refactoring: when a feature is heavily rewritten
- [ADD] for adding new modules
- [REM] for removing resources: removing dead code, removing views, removing module
- [REV] for reverting commits: if a commit causes issues or is not wanted reverting it is done using this tag
- [MOV] for moving files: use git move and do not change content of moved file otherwise Git may loose track and history of the file; also used when moving code from one file to another
- [REL] for release commits: new major or minor stable versions
- [IMP] for improvements: most of the changes done in development version are incremental improvements not related to another tag
- [MERGE] for merge commits: used in forward port of bug fixes but also as main commit for feature involving several separated commits
- [CLA] for signing the Odoo Individual Contributor License
- [I18N] for changes in translation files
- [PERF] for performance patches

### Scope (Optional)
- Refer to the modified module technical name
- If several modules are modified, list them to tell it is cross-modules

{SHORT_DESCRIPTION}

{LONG_DESCRIPTION}

{FOOTER}

### Examples
#### Simple and trivial changes example:
[FIX] account: Remove frenglish

#### When user context is empty or doesn't mention specific tickets/issues:
[REF] models: Use `parent_path` to implement parent_store

This replaces the former modified preorder tree traversal (MPTT) with
the fields `parent_left`/`parent_right`

#### When user context mentions specific tickets/issues:
[FIX] website: Fixes look of input-group-btn

Bootstrap's CSS depends on the input-group-btn element being the
first/last child of its parent. This was not the case because of the
invisible and useless alert.

Fixes #328

{OUTPUT_FORMAT}
"""
