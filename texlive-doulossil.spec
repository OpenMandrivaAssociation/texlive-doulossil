Name:		texlive-doulossil
Version:	63255
Release:	2
Summary:	A font for typesetting the International Phonetic Alphabet (IPA)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/doulossil
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doulossil.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/doulossil.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the IPA font Doulos SIL in TrueType
format.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/doulossil
%doc %{_texmfdistdir}/doc/fonts/doulossil

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
