# flake8-deprecation

Flake8-deprecation is a flake8 plugin to detect when functions that you import call `warnings.warn(..., DeprecationWarning)`

This exists because some libraries do not use `@deprecation`, and (as far as I could find) there are no tools out there that give you a linter/lsp warning when `warnings.warn` is used.

flake8-warnings heavily inspired this work, but... it seems to just not work at all for me and it's a small enough thing that I thought it would just be easier to rewrite.

I only care about unconditional calls to warnings.warn


# i have made mistakes

I need this working tomorrow, Astroid was a mistake, I should borrow the ast parsing crate from ruff... Maybe one day

# contributing
Feel free to open a PR but I don't promise to look at it
