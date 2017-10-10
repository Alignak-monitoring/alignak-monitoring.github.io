---
layout: page
title: Download
permalink: /download/
menu: true
order: 4
---

## Stable versions

### DEB

Add in your `/etc/apt/sources.list`:

```
deb https://dl.bintray.com/ddurieux/alignak_deb-stable {distribution} main
```
where `{distribution}` is your distribution name, work only for one in the list:

* jessie
* Stretch
* Trusty 
* xenial
* Yakkety
* Zesty
* Artful


### RPM

See the page [https://copr.fedorainfracloud.org/coprs/hvad/Alignak/](https://copr.fedorainfracloud.org/coprs/hvad/Alignak/)

### PIP

It's possible to install with pip with the command:

```
pip install {package_name}
```

## Development versions

### DEB

The DEB packages are generated each time a Pull Request is merged in the `develop` branch.

Add in your `/etc/apt/sources.list`:

```
deb https://dl.bintray.com/ddurieux/alignak_deb-testing {distribution} main
```
where `{distribution}` is your distribution name, work only for one in the list:

* jessie
* Stretch
* Trusty 
* xenial
* Yakkety
* Zesty
* Artful


### RPM

It is not possible currently to have the develop branch version with RPM packages.

### Source

Get the github repository and install with the command:

```
pip install .
```
