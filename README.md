# gepard-site
Sources for the gepard.phy.hr site


These are sources for the [gepard.phy.hr](https://gepard.phy.hr) site.
Note that most of this site presently is documentation for
Gepard software, which is provided by sources from `docs/sources`
subdirectory of `gepard` github repository, and not this gepard-site
repository.

So, to create the whole site, you should clone both repositories,
copy (or, better, link) `gepard/doc/sources  --> gepard-site/sources`
and then do
```
make html
```
in `gepard-site`.
