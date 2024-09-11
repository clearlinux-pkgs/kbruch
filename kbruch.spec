#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kbruch
Version  : 24.08.0
Release  : 73
URL      : https://download.kde.org/stable/release-service/24.08.0/src/kbruch-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/kbruch-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/kbruch-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GFDL-1.2 GPL-2.0
Requires: kbruch-bin = %{version}-%{release}
Requires: kbruch-data = %{version}-%{release}
Requires: kbruch-license = %{version}-%{release}
Requires: kbruch-locales = %{version}-%{release}
Requires: kbruch-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Please see: https://edu.kde.org/kbruch/

%package bin
Summary: bin components for the kbruch package.
Group: Binaries
Requires: kbruch-data = %{version}-%{release}
Requires: kbruch-license = %{version}-%{release}

%description bin
bin components for the kbruch package.


%package data
Summary: data components for the kbruch package.
Group: Data

%description data
data components for the kbruch package.


%package doc
Summary: doc components for the kbruch package.
Group: Documentation
Requires: kbruch-man = %{version}-%{release}

%description doc
doc components for the kbruch package.


%package license
Summary: license components for the kbruch package.
Group: Default

%description license
license components for the kbruch package.


%package locales
Summary: locales components for the kbruch package.
Group: Default

%description locales
locales components for the kbruch package.


%package man
Summary: man components for the kbruch package.
Group: Default

%description man
man components for the kbruch package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kbruch-24.08.0
cd %{_builddir}/kbruch-24.08.0
pushd ..
cp -a kbruch-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724641440
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724641440
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kbruch
cp %{_builddir}/kbruch-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kbruch/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kbruch-%{version}/LICENSES/GFDL-1.2-only.txt %{buildroot}/usr/share/package-licenses/kbruch/7b300def279cc0c38b84d3351f68d558cc01ad61 || :
cp %{_builddir}/kbruch-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kbruch/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kbruch
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kbruch
/usr/bin/kbruch

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kbruch.desktop
/usr/share/config.kcfg/kbruch.kcfg
/usr/share/icons/hicolor/128x128/apps/kbruch.png
/usr/share/icons/hicolor/16x16/apps/kbruch.png
/usr/share/icons/hicolor/22x22/apps/kbruch.png
/usr/share/icons/hicolor/32x32/apps/kbruch.png
/usr/share/icons/hicolor/48x48/apps/kbruch.png
/usr/share/icons/hicolor/64x64/apps/kbruch.png
/usr/share/icons/hicolor/scalable/apps/kbruch.svgz
/usr/share/kbruch/pics/exercise_arithmetics.png
/usr/share/kbruch/pics/exercise_compare.png
/usr/share/kbruch/pics/exercise_conversion.png
/usr/share/kbruch/pics/exercise_factorization.png
/usr/share/kbruch/pics/exercise_mixed.png
/usr/share/kbruch/pics/exercise_percentage.png
/usr/share/kbruch/pics/icon_back_arrow.png
/usr/share/kbruch/pics/icon_freestyle.png
/usr/share/kbruch/pics/icon_freestyle_1.png
/usr/share/kbruch/pics/icon_learning.png
/usr/share/kbruch/pics/icon_learning_1.png
/usr/share/kbruch/pics/icon_test_case.png
/usr/share/kbruch/pics/icon_test_case_1.png
/usr/share/metainfo/org.kde.kbruch.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kbruch/index.cache.bz2
/usr/share/doc/HTML/ca/kbruch/index.docbook
/usr/share/doc/HTML/de/kbruch/checked.png
/usr/share/doc/HTML/de/kbruch/compare.png
/usr/share/doc/HTML/de/kbruch/convert.png
/usr/share/doc/HTML/de/kbruch/factorize.png
/usr/share/doc/HTML/de/kbruch/gui_main.png
/usr/share/doc/HTML/de/kbruch/gui_mode.png
/usr/share/doc/HTML/de/kbruch/index.cache.bz2
/usr/share/doc/HTML/de/kbruch/index.docbook
/usr/share/doc/HTML/de/kbruch/learning.png
/usr/share/doc/HTML/de/kbruch/percentage.png
/usr/share/doc/HTML/de/kbruch/reduced.png
/usr/share/doc/HTML/de/kbruch/settings.png
/usr/share/doc/HTML/de/kbruch/statistics.png
/usr/share/doc/HTML/en/kbruch/checked.png
/usr/share/doc/HTML/en/kbruch/compare.png
/usr/share/doc/HTML/en/kbruch/convert.png
/usr/share/doc/HTML/en/kbruch/factorize.png
/usr/share/doc/HTML/en/kbruch/gui_main.png
/usr/share/doc/HTML/en/kbruch/gui_mode.png
/usr/share/doc/HTML/en/kbruch/index.cache.bz2
/usr/share/doc/HTML/en/kbruch/index.docbook
/usr/share/doc/HTML/en/kbruch/learning.png
/usr/share/doc/HTML/en/kbruch/mixed.png
/usr/share/doc/HTML/en/kbruch/percentage.png
/usr/share/doc/HTML/en/kbruch/reduced.png
/usr/share/doc/HTML/en/kbruch/settings.png
/usr/share/doc/HTML/en/kbruch/statistics.png
/usr/share/doc/HTML/es/kbruch/checked.png
/usr/share/doc/HTML/es/kbruch/compare.png
/usr/share/doc/HTML/es/kbruch/convert.png
/usr/share/doc/HTML/es/kbruch/factorize.png
/usr/share/doc/HTML/es/kbruch/gui_main.png
/usr/share/doc/HTML/es/kbruch/gui_mode.png
/usr/share/doc/HTML/es/kbruch/index.cache.bz2
/usr/share/doc/HTML/es/kbruch/index.docbook
/usr/share/doc/HTML/es/kbruch/learning.png
/usr/share/doc/HTML/es/kbruch/percentage.png
/usr/share/doc/HTML/es/kbruch/reduced.png
/usr/share/doc/HTML/es/kbruch/settings.png
/usr/share/doc/HTML/es/kbruch/statistics.png
/usr/share/doc/HTML/et/kbruch/index.cache.bz2
/usr/share/doc/HTML/et/kbruch/index.docbook
/usr/share/doc/HTML/fr/kbruch/checked.png
/usr/share/doc/HTML/fr/kbruch/compare.png
/usr/share/doc/HTML/fr/kbruch/convert.png
/usr/share/doc/HTML/fr/kbruch/factorize.png
/usr/share/doc/HTML/fr/kbruch/gui_main.png
/usr/share/doc/HTML/fr/kbruch/gui_mode.png
/usr/share/doc/HTML/fr/kbruch/index.cache.bz2
/usr/share/doc/HTML/fr/kbruch/index.docbook
/usr/share/doc/HTML/fr/kbruch/learning.png
/usr/share/doc/HTML/fr/kbruch/mixed.png
/usr/share/doc/HTML/fr/kbruch/percentage.png
/usr/share/doc/HTML/fr/kbruch/reduced.png
/usr/share/doc/HTML/fr/kbruch/settings.png
/usr/share/doc/HTML/fr/kbruch/statistics.png
/usr/share/doc/HTML/it/kbruch/index.cache.bz2
/usr/share/doc/HTML/it/kbruch/index.docbook
/usr/share/doc/HTML/nl/kbruch/checked.png
/usr/share/doc/HTML/nl/kbruch/compare.png
/usr/share/doc/HTML/nl/kbruch/convert.png
/usr/share/doc/HTML/nl/kbruch/factorize.png
/usr/share/doc/HTML/nl/kbruch/gui_main.png
/usr/share/doc/HTML/nl/kbruch/gui_mode.png
/usr/share/doc/HTML/nl/kbruch/index.cache.bz2
/usr/share/doc/HTML/nl/kbruch/index.docbook
/usr/share/doc/HTML/nl/kbruch/learning.png
/usr/share/doc/HTML/nl/kbruch/mixed.png
/usr/share/doc/HTML/nl/kbruch/percentage.png
/usr/share/doc/HTML/nl/kbruch/reduced.png
/usr/share/doc/HTML/nl/kbruch/settings.png
/usr/share/doc/HTML/nl/kbruch/statistics.png
/usr/share/doc/HTML/pt/kbruch/index.cache.bz2
/usr/share/doc/HTML/pt/kbruch/index.docbook
/usr/share/doc/HTML/pt_BR/kbruch/checked.png
/usr/share/doc/HTML/pt_BR/kbruch/compare.png
/usr/share/doc/HTML/pt_BR/kbruch/convert.png
/usr/share/doc/HTML/pt_BR/kbruch/factorize.png
/usr/share/doc/HTML/pt_BR/kbruch/gui_main.png
/usr/share/doc/HTML/pt_BR/kbruch/gui_mode.png
/usr/share/doc/HTML/pt_BR/kbruch/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kbruch/index.docbook
/usr/share/doc/HTML/pt_BR/kbruch/learning.png
/usr/share/doc/HTML/pt_BR/kbruch/percentage.png
/usr/share/doc/HTML/pt_BR/kbruch/reduced.png
/usr/share/doc/HTML/pt_BR/kbruch/settings.png
/usr/share/doc/HTML/pt_BR/kbruch/statistics.png
/usr/share/doc/HTML/ru/kbruch/checked.png
/usr/share/doc/HTML/ru/kbruch/compare.png
/usr/share/doc/HTML/ru/kbruch/convert.png
/usr/share/doc/HTML/ru/kbruch/factorize.png
/usr/share/doc/HTML/ru/kbruch/gui_main.png
/usr/share/doc/HTML/ru/kbruch/gui_mode.png
/usr/share/doc/HTML/ru/kbruch/index.cache.bz2
/usr/share/doc/HTML/ru/kbruch/index.docbook
/usr/share/doc/HTML/ru/kbruch/learning.png
/usr/share/doc/HTML/ru/kbruch/percentage.png
/usr/share/doc/HTML/ru/kbruch/reduced.png
/usr/share/doc/HTML/ru/kbruch/settings.png
/usr/share/doc/HTML/ru/kbruch/statistics.png
/usr/share/doc/HTML/sv/kbruch/checked.png
/usr/share/doc/HTML/sv/kbruch/compare.png
/usr/share/doc/HTML/sv/kbruch/convert.png
/usr/share/doc/HTML/sv/kbruch/factorize.png
/usr/share/doc/HTML/sv/kbruch/gui_main.png
/usr/share/doc/HTML/sv/kbruch/index.cache.bz2
/usr/share/doc/HTML/sv/kbruch/index.docbook
/usr/share/doc/HTML/sv/kbruch/reduced.png
/usr/share/doc/HTML/sv/kbruch/settings.png
/usr/share/doc/HTML/uk/kbruch/checked.png
/usr/share/doc/HTML/uk/kbruch/compare.png
/usr/share/doc/HTML/uk/kbruch/convert.png
/usr/share/doc/HTML/uk/kbruch/factorize.png
/usr/share/doc/HTML/uk/kbruch/gui_main.png
/usr/share/doc/HTML/uk/kbruch/gui_mode.png
/usr/share/doc/HTML/uk/kbruch/index.cache.bz2
/usr/share/doc/HTML/uk/kbruch/index.docbook
/usr/share/doc/HTML/uk/kbruch/learning.png
/usr/share/doc/HTML/uk/kbruch/mixed.png
/usr/share/doc/HTML/uk/kbruch/percentage.png
/usr/share/doc/HTML/uk/kbruch/reduced.png
/usr/share/doc/HTML/uk/kbruch/settings.png
/usr/share/doc/HTML/uk/kbruch/statistics.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kbruch/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kbruch/7b300def279cc0c38b84d3351f68d558cc01ad61
/usr/share/package-licenses/kbruch/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kbruch.1
/usr/share/man/de/man1/kbruch.1
/usr/share/man/es/man1/kbruch.1
/usr/share/man/et/man1/kbruch.1
/usr/share/man/fr/man1/kbruch.1
/usr/share/man/it/man1/kbruch.1
/usr/share/man/man1/kbruch.1
/usr/share/man/nl/man1/kbruch.1
/usr/share/man/pt/man1/kbruch.1
/usr/share/man/pt_BR/man1/kbruch.1
/usr/share/man/ru/man1/kbruch.1
/usr/share/man/sv/man1/kbruch.1
/usr/share/man/uk/man1/kbruch.1

%files locales -f kbruch.lang
%defattr(-,root,root,-)

