#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : complete
Version  : 0.0.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/4e/f4/c3bd2443dd19e6dd2b283b9edd1153a2255ed839471f2a80b1f9c9380818/complete-0.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/f4/c3bd2443dd19e6dd2b283b9edd1153a2255ed839471f2a80b1f9c9380818/complete-0.0.1.tar.gz
Summary  : A Python library to autocomplete questions using search engines
Group    : Development/Tools
License  : MIT
Requires: complete-python = %{version}-%{release}
Requires: complete-python3 = %{version}-%{release}
Requires: aiohttp
Requires: lxml
Requires: requests
BuildRequires : aiohttp
BuildRequires : buildreq-distutils3
BuildRequires : lxml
BuildRequires : requests

%description
Complete is a Python library to autocomplete questions using search engines
        
        ## Installation

%package python
Summary: python components for the complete package.
Group: Default
Requires: complete-python3 = %{version}-%{release}

%description python
python components for the complete package.


%package python3
Summary: python3 components for the complete package.
Group: Default
Requires: python3-core
Provides: pypi(complete)
Requires: pypi(aiohttp)
Requires: pypi(lxml)
Requires: pypi(requests)

%description python3
python3 components for the complete package.


%prep
%setup -q -n complete-0.0.1
cd %{_builddir}/complete-0.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618248294
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
