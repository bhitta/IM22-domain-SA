(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art11"
    "UF_FRED_paper_style"
    "xcolor"
    "lipsum"
    "booktabs"
    "caption"
    "subcaption"
    "float"
    "geometry")
   (LaTeX-add-labels
    "table:example-tweets"
    "fig:candlestick")
   (LaTeX-add-bibliographies
    "references.bib"))
 :latex)

