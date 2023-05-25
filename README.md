# Leiden Language Database (LeiLanD) at Leiden University
# https://leiland.lucdh.nl

This Django app is a port of the previous Java version of LeiLanD.
That previous version had an unfortunate memory leak that caused the
application to crash unexpectedly. This new version appears to work
properly, and is a complete rewrite in Python/Django. In some cases,
HTML templates have been imported from the earlier project in order
to retain consistency of user interfaces. Those templates still contain
some remnants of the old project, which we are now removing as we
continue revising the code for readability and add new features.

